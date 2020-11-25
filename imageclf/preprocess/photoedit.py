from generated.wxui import MainFrame, FileBrowsePanel
from edit import CropPanel
from draw import Canvas
import wx
import wx.aui as aui
import os
from pubsub import pub


class FileBrowser(FileBrowsePanel):
	def __init__(self, parent):
		super().__init__(parent)
		self.m_genericDirCtrl_file.SetPath(str(os.path.expanduser("~")))
		self.Bind(wx.EVT_DIRCTRL_SELECTIONCHANGED,
				  self.OnSelectionChanged, self.m_genericDirCtrl_file)

	def OnSelectionChanged(self, event):
		pub.sendMessage("Canvas", arg1="open",
						arg2=self.m_genericDirCtrl_file.GetPath())


class Main(MainFrame):
	def __init__(self, parent):
		super().__init__(parent)

		self._mgr = aui.AuiManager(self)

		self.fb = FileBrowser(self)
		self.fb_pane = self._mgr.AddPane(self.fb, wx.LEFT, "Files")

		self.canvas = Canvas(self)
		self._mgr.AddPane(self.canvas, aui.AuiPaneInfo().CaptionVisible(False)
						  .Center())

		self.editPanelInfo = aui.AuiPaneInfo().DestroyOnClose(
			True).Fixed().Right().BottomDockable(False).TopDockable(False)

		self._mgr.Update()

		self.Bind(wx.EVT_CLOSE, self.OnClose)
		
		self.Bind(wx.EVT_MENU, self.ShowLeftBrowser,
				  self.m_menuItem_showfilebrowser)
		
		self.Bind(wx.EVT_MENU, self.OnCrop,
				  self.m_menuItem_toolcrop)
		self.Bind(wx.EVT_MENU, self.ShowLeftBrowser,
				  self.m_menuItem_tooladjustcolor)
		self.Bind(wx.EVT_MENU, self.ShowLeftBrowser,
				  self.m_menuItem_toolresize)
		self.Bind(wx.EVT_MENU, self.ShowLeftBrowser,
				  self.m_menuItem_toolrotate)

	def OnClose(self, event):
		self._mgr.UnInit()
		del self._mgr
		self.Destroy()

	def ShowLeftBrowser(self, event):
		pn = self._mgr.GetPane(self.fb)
		pn.Show(True)
		self._mgr.Update()

	def OnCrop(self, event):
		po = self.editPanelInfo.Caption("Crop")
		self._mgr.AddPane(CropPanel(self),po)
		self._mgr.Update()


if __name__ == '__main__':
	app = wx.App()
	frame = Main(None)
	frame.Show()
	app.MainLoop()