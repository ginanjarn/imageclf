from generated.wxui import MainFrame
import wx
import os
import math
from pathlib import Path

class DrawingObject:
	def __init__(self, dc):
		# self.dc = wx.PaintDC(self)
		self.dc = dc
		self.objects = []

	def Realize(self):
		for obj in self.objects:
			obj

	def add_bitmap(self,point,bitmap):
		self.objects.append(self.dc.DrawBitmap(bitmap,point))

	def add_circle(self, point1: wx.Point, point2: wx.Point):
		radius = math.sqrt(math.pow(point2.x-point1.x)+math.pow(point2.y-point1.y))
		self.objects.append(self.dc.DrawCircle(point1,radius))

class Main(MainFrame):
	def __init__(self, parent):
		super().__init__(parent)
		self.m_genericDirCtrl_filebrowser.SetDefaultPath(os.getcwd())
		self.m_genericDirCtrl_filebrowser.ReCreateTree()
		self.Bind(wx.EVT_DIRCTRL_SELECTIONCHANGED,self.on_dirctrl_select_change)

# ----------------------------------------------------------------------
		self.paint_dc = None
		self.point1: wx.Point = None
		self.point2: wx.Point = None

		self.src_point1: wx.Point = None
		self.src_point2: wx.Point = None

		self.on_edit = False

		self.image = wx.Image()
		self.m_scrolledWindow_image.Bind(wx.EVT_PAINT, self.on_paint)
# ----------------------------------------------------------------------
		self.init_menu()
		self.init_toolbar()
		self.init_drawing()
# ---------------------------------------------------------------------


	def init_menu(self):
		self.Bind(wx.EVT_MENU, self.on_open, self.m_menuItem_open)
		self.Bind(wx.EVT_MENU, self.on_save, self.m_menuItem_save)
		self.Bind(wx.EVT_MENU, self.on_saveas, self.m_menuItem_saveas)
		self.Bind(wx.EVT_MENU, lambda e: self.Close(), self.m_menuItem_exit)

		self.Bind(wx.EVT_MENU, self.on_undo, self.m_menuItem_undo)
		self.Bind(wx.EVT_MENU, self.on_redo, self.m_menuItem_redo)
		self.Bind(wx.EVT_MENU, self.on_changehistory,
				  self.m_menuItem_changehistory)

		self.Bind(wx.EVT_MENU, self.on_crop, self.m_menuItem_toolcrop)
		self.Bind(wx.EVT_MENU, self.on_resize, self.m_menuItem_toolresize)
		self.Bind(wx.EVT_MENU, self.on_rotate, self.m_menuItem_toolrotate)
		self.Bind(wx.EVT_MENU, self.on_adjustcolor,
				  self.m_menuItem_tooladjustcolor)

	def init_toolbar(self):
		self.Bind(wx.EVT_TOOL, self.on_open, self.m_tool_open)

	def init_drawing(self):
		self.m_scrolledWindow_image.Bind(wx.EVT_LEFT_DOWN, self.on_left_down)
		self.m_scrolledWindow_image.Bind(wx.EVT_LEFT_UP, self.on_left_up)
		self.m_scrolledWindow_image.Bind(wx.EVT_MOTION, self.on_motion)

# ----------------------------------------------------------------------

	def on_dirctrl_select_change(self, event):
		filepath = self.m_genericDirCtrl_filebrowser.GetPath()
		if os.path.isfile(filepath):
			if self.image.CanRead(filepath):
				self.image.LoadFile(filepath, wx.BITMAP_TYPE_ANY)
				imw, imh = self.image.GetSize()
				self.m_scrolledWindow_image.SetVirtualSize(imw, imh)
				self.m_scrolledWindow_image.Refresh()
				
	def on_paint(self, event):
		if self.image.IsOk():
			dc = wx.PaintDC(self.m_scrolledWindow_image)
			self.paint_dc = dc
			self.m_scrolledWindow_image.PrepareDC(dc)
			dc.DrawBitmap(self.image.ConvertToBitmap(), 0, 0)

			if self.on_edit:
			if self.point1:
				dc.DrawLine(self.point1,self.point2)

			# self.point1 = self.point2 = None


	def get_cursor_position(self, event):
		if self.paint_dc:
			return event.GetLogicalPosition(self.paint_dc)
		else:
			return None


	def on_left_down(self, event):
		pos = self.get_cursor_position(event)
		if pos:
			# print(pos)
			self.point1 = pos
			self.src_point1 = event.GetPosition()
			self.on_edit = True

	def on_left_up(self, event):
		pos = self.get_cursor_position(event)
		if pos:
			self.point2 = pos
			self.src_point2 = event.GetPosition()
			rect = wx.Rect(self.src_point1.x,self.src_point1.y,
				self.src_point2.x-self.src_point1.x,self.src_point2.y-self.src_point1.y)
			self.on_edit = False
			self.m_scrolledWindow_image.RefreshRect(rect)	

	def on_motion(self, event):
		pos = self.get_cursor_position(event)
		if pos:
			# print(pos)
			self.point2 = pos
			if self.point1 and self.on_edit:
				self.src_point2 = event.GetPosition()
				rect = wx.Rect(self.src_point1.x,self.src_point1.y,
					self.src_point2.x-self.src_point1.x,self.src_point2.y-self.src_point1.y)
				self.m_scrolledWindow_image.RefreshRect(rect)	

	def on_close(self, event):
		self.Destroy()

	def on_open(self, event):
		# pass
		wildcard = self.image.GetImageExtWildcard()
		fd = wx.FileDialog(self, wildcard=wildcard,
						   style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
		if fd.ShowModal() == wx.ID_OK:
			filepath = fd.GetPath()
			if self.image.CanRead(filepath):
				self.image.LoadFile(filepath, wx.BITMAP_TYPE_ANY)

				imw, imh = self.image.GetSize()
				self.m_scrolledWindow_image.SetVirtualSize(imw, imh)

				self.m_scrolledWindow_image.Refresh()

	def on_save(self, event):
		pass

	def on_saveas(self, event):
		pass

	def on_undo(self, event):
		pass

	def on_redo(self, event):
		pass

	def on_changehistory(self, event):
		pass

	def on_crop(self, event):
		pass

	def on_resize(self, event):
		pass

	def on_rotate(self, event):
		pass

	def on_adjustcolor(self, event):
		pass


if __name__ == '__main__':
	app = wx.App()
	frame = Main(None)
	frame.Show()
	app.MainLoop()