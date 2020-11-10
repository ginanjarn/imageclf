from cv2 import VideoCapture, cvtColor, COLOR_BGR2RGB, imwrite, resize
import wx
import os
from random import randint
from datetime import datetime
from generated.wxui import CameraDialog, SettingsDialog
import logging

logger = logging.getLogger("camera")
# logger.setLevel(logging.DEBUG)				# package logging level
chandler = logging.StreamHandler()
chandler.setFormatter(logging.Formatter(
    "%(levelname)s\t%(module)s:%(lineno)s\t%(message)s"))
chandler.setLevel(logging.DEBUG)
logger.addHandler(chandler)


class CameraInitError(Exception):
    """Failed initialize camera"""
    pass


class Settings:
    """Camera settings"""

    def __init__(self):
        self.name = "IMG$.png"
        self.refresh_time = 1
        self.max_frame = 0


class SettingsDialog(SettingsDialog):
    def __init__(self, parent, settings: Settings):
        super().__init__(parent)
        self.settings = settings

        self.m_textCtrl_imgname.Value = settings.name
        self.m_textCtrl_refreshtime.Value = str(settings.refresh_time)
        self.m_textCtrl_maxframe.Value = str(settings.max_frame)

    def get_settings(self):
        settings = self.settings
        settings.name = self.m_textCtrl_imgname.Value
        try:
            settings.refresh_time = float(self.m_textCtrl_refreshtime.Value)
            settings.max_frame = int(self.m_textCtrl_maxframe.Value)
        except Exception:
            logger.error("invalid value", exc_info=True)
            wx.MessageBox("data invalid. settings not changed", "Error",
                          wx.OK | wx.OK_DEFAULT | wx.CENTER | wx.ICON_ERROR)
        return settings


class Camera(CameraDialog):
    """Camera

    Args:
        parent: parent window
        cameraId: camera id(if multiple camera available)
        camera_refresh: refresh preview timeout(milisecond)"""

    def __init__(self, parent, cameraId=0, camera_refresh=50):
        super().__init__(parent)
        self.camera = VideoCapture(0)
        if not self.camera.isOpened():
            raise CameraInitError

        self.settings = Settings()

        self.Bind(wx.EVT_CLOSE, self.on_close)

        bitmap = wx.Bitmap()
        bitmap.LoadFile(os.path.join("generated", "res", "camera.png"))
        self.tool_capture = self.m_toolBar.AddTool(
            toolId=wx.ID_ANY, label="capture", bitmap=bitmap, shortHelp="Capture image", kind=wx.ITEM_NORMAL)
        self.m_toolBar.AddSeparator()
        bitmap.LoadFile(os.path.join("generated", "res", "videocam.png"))
        self.tool_record = self.m_toolBar.AddTool(
            toolId=wx.ID_ANY, label="record", bitmap=bitmap, shortHelp="Capture image", kind=wx.ITEM_NORMAL)
        bitmap.LoadFile(os.path.join("generated", "res", "stop.png"))
        self.tool_stop = self.m_toolBar.AddTool(
            toolId=wx.ID_ANY, label="stop", bitmap=bitmap, shortHelp="Capture image", kind=wx.ITEM_NORMAL)
        self.m_toolBar.AddSeparator()
        bitmap.LoadFile(os.path.join("generated", "res", "settings.png"))
        self.tool_settings = self.m_toolBar.AddTool(
            toolId=wx.ID_ANY, label="settings", bitmap=bitmap, shortHelp="Capture image", kind=wx.ITEM_NORMAL)
        self.m_toolBar.Realize()

        self.Bind(wx.EVT_TOOL, self.on_capture, self.tool_capture)
        self.Bind(wx.EVT_TOOL, self.on_record, self.tool_record)
        self.Bind(wx.EVT_TOOL, self.on_stop, self.tool_stop)
        self.Bind(wx.EVT_TOOL, self.on_settings, self.tool_settings)

        self.preview_timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.on_preview_timer, self.preview_timer)
        self.preview_timer.Start(camera_refresh)

        self.previewDc = wx.ClientDC(self.m_panel_preview)

        self.capture_timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.on_capture_timer, self.capture_timer)
        self.capture_limit = -1

    def on_close(self, event):
        self.preview_timer.Stop()
        self.camera.release()
        self.Destroy()

    def on_capture(self, event):
        logger.info("on_capture")
        self.capture_image()

    def on_record(self, event):
        logger.info("start record")
        self.capture_timer.Start(int(self.settings.refresh_time*1000))
        self.capture_limit = self.settings.max_frame

    def on_stop(self, event):
        logger.info("stop record")
        self.capture_timer.Stop()

    def on_settings(self, event):
        logger.info("on_settings")
        if self.capture_timer.IsRunning():
            if wx.MessageBox("Stop capture to open settings?", "Warning",
                             style=wx.OK | wx.CANCEL | wx.CANCEL_DEFAULT |
                             wx.ICON_WARNING | wx.CENTER) == wx.OK:
                self.capture_timer.Stop()
            else:
                return

        settingDlg = SettingsDialog(self, self.settings)
        if settingDlg.ShowModal() == wx.ID_OK:
            logger.debug("return settings")
            self.settings = settingDlg.get_settings()

    def on_preview_timer(self, event):
        # logger.info("refesh")
        width, height = self.m_panel_preview.GetClientSize()
        buffDc = wx.BufferedDC(self.previewDc)
        ret, frame = self.camera.read()
        frame = cvtColor(frame, COLOR_BGR2RGB)
        frame = resize(frame, (width, height))
        im_height, im_width = frame.shape[:2]

        # TODO: fix this later
        def fit_image(imw, imh, clw, clh):
            imratio = imw/imh
            clratio = clw/clh
            potrait = imw < imh
            if potrait:
                pass
            else:
                if imratio < clratio:
                    nwidth = clw
                    nheight = imh * clw / imw
                else:
                    nheight = clh
                    nwidth = imw * clh / imh
            return nwidth, nheight

        image = wx.Image()
        image.SetDataBuffer(frame, width, height)
        buffDc.DrawBitmap(image.ConvertToBitmap(), 0, 0)

    def on_capture_timer(self, event):
        logger.info("capture Timer")
        if self.capture_limit > 1:
            self.capture_limit -= 1
        elif self.capture_limit == 1:
            self.capture_timer.Stop()
        self.capture_image()

    def capture_image(self):
        logger.info("capture_image")
        ret, frame = self.camera.read()
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        uname = "%s%s" % (timestamp, randint(1000, 9999))
        filename = self.settings.name.replace("$", "%s")
        filename = filename % uname
        logger.debug("filename = %s", filename)
        imwrite(filename, frame)


if __name__ == '__main__':
    app = wx.App()
    frame = Camera(None)
    frame.Show()
    app.MainLoop()