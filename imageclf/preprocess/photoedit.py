from generated.wxui import MainFrame
import wx
import os
import math
from pathlib import Path


def calculate_size(pt1: wx.Point, pt2: wx.Point):
	return wx.Size(pt2.x-pt1.x, pt2.y-pt1.y)


def calculate_radius(pt1: wx.Point, pt2: wx.Point):
	return math.sqrt(math.pow(pt2.x-pt1.x,2)+math.pow(pt2.y-pt1.y,2))


def calculate_rect(pt1: wx.Point, pt2: wx.Point):
	return wx.Rect(pt1, calculate_size(pt1, pt2))


def calculate_ext_rect(pt1: wx.Point, pt2: wx.Point, padding=20):
	xmin, xmax = min(pt1.x, pt2.x), max(pt1.x, pt2.x)
	ymin, ymax = min(pt1.y, pt2.y), max(pt1.y, pt2.y)
	x, y = xmin-padding, ymin-padding
	w, h = xmax+padding-x, ymax+padding-y
	return wx.Rect(wx.Point(x, y), wx.Size(w, h))


class Main(MainFrame):
	def __init__(self, parent):
		super().__init__(parent)
		self.init_dirbrowser()
		self.init_imagehandler()

	def init_imagehandler(self):
		self.m_scrolledWindow_image.Bind(wx.EVT_PAINT, self.image_paint)
		self.image = wx.Image()
		self.memoryDc = None
		self.canvas = None

		self.m_scrolledWindow_image.Bind(wx.EVT_LEFT_DOWN,self.on_leftdown)
		self.m_scrolledWindow_image.Bind(wx.EVT_LEFT_UP,self.on_leftup)
		self.m_scrolledWindow_image.Bind(wx.EVT_MOTION,self.on_motion)

		self.mouse_point1 = None
		self.mouse_point2 = None

		self.logical_point1 = None
		self.logical_point2 = None

		self.Draw = False

	def get_logical_position(self,event):
		if self.canvas:
			return event.GetLogicalPosition(self.canvas)
		else:
			return None

	def on_leftdown(self,event):
		self.mouse_point1 = event.GetPosition()
		self.logical_point1 = self.get_logical_position(event)

		self.Draw = True

	def on_leftup(self,event):
		self.mouse_point2 = event.GetPosition()
		self.logical_point2 = self.get_logical_position(event)

		self.Draw = False

	def on_motion(self,event):
		self.mouse_point2 = event.GetPosition()
		self.logical_point2 = self.get_logical_position(event)
		if self.Draw:
			self.m_scrolledWindow_image.Refresh(eraseBackground=False)


	def image_paint(self,event):
		dc = wx.PaintDC(self.m_scrolledWindow_image)
		self.m_scrolledWindow_image.PrepareDC(dc)
		if not self.memoryDc:
			return
		self.canvas = dc

		BITMAP_WIDTH, BITMAP_HEIGHT = self.image.GetSize()
		dc.Blit(0, 0, BITMAP_WIDTH, BITMAP_HEIGHT, self.memoryDc, 0, 0)

		if self.Draw:
			print("on draw")
			brush = wx.Brush(wx.Colour(0,0,0),style=wx.BRUSHSTYLE_TRANSPARENT)
			dc.SetBrush(brush)
			dc.DrawLine(self.logical_point1,self.logical_point2)
			# dc.DrawRectangle(calculate_rect(self.logical_point1,self.logical_point2))
			dc.DrawCircle(self.logical_point1,calculate_radius(self.logical_point1,self.logical_point2))


	def open_file(self,path):
		if not os.path.isfile(path):
			return
		if not self.image.CanRead(path):
			return
		self.image.LoadFile(path)
		imw,imh = self.image.GetSize()

		bitmap = wx.Bitmap(imw,imh)
		self.memoryDc = wx.MemoryDC(bitmap)

		self.memoryDc.DrawBitmap(self.image.ConvertToBitmap(),0,0)

		self.m_scrolledWindow_image.SetVirtualSize(imw,imh)
		self.m_scrolledWindow_image.Refresh()

	def init_dirbrowser(self):
		self.m_genericDirCtrl_filebrowser.SetPath(str(os.path.expanduser("~")))
		self.Bind(wx.EVT_DIRCTRL_SELECTIONCHANGED,lambda e: self.open_file(self.m_genericDirCtrl_filebrowser.GetPath()),self.m_genericDirCtrl_filebrowser)


if __name__ == '__main__':
	app = wx.App()
	frame = Main(None)
	frame.Show()
	app.MainLoop()