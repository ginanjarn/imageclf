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


class DrawObject:
	def __init__(self):
		self.name = ""
		self.point1: wx.Point = None
		self.point2: wx.Point = None
		self.radius:int = 0
		self.size:wx.Size = None
		self.bitmap:wx.Bitmap = None

	def add_bitmap(self,p1,bitmap):
		self.name="bitmap"
		self.point1 = p1
		self.bitmap = bitmap

	def add_line(self,p1,p2):
		self.name = "line"
		self.point1 = p1
		self.point2 = p2

	def add_rect(self,p1,p2):
		self.name = "rect"
		self.point1 = p1
		self.size = calculate_size(p1,p2)

	def render(self,dc):
		if self.name == "bitmap":
			dc.DrawBitmap(self.bitmap,self.point1.x,self.point1.y)
		elif self.name == "line":
			dc.DrawLine(self.point1,self.point2)


class Main(MainFrame):
	def __init__(self, parent):
		super().__init__(parent)
		self.init_dirbrowser()
		self.init_imagehandler()
		self.init_editing()

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

		self.object_list = []
		self.temp_object_list = []

	def UpdateMemoryDC(self):
		imw,imh = self.image.GetSize()

		bitmap = wx.Bitmap(imw,imh)
		self.memoryDc = wx.MemoryDC(bitmap)
		# self.memoryDc.Clear()
		count = 0
		for obj in self.object_list:
			obj.render(self.memoryDc)
			print("draw obj %s"%count)
			count+=1

		self.m_scrolledWindow_image.Refresh(eraseBackground=False)		

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

		if self.Draw:
			# def draw():
			# 	self.memoryDc.SetBrush(wx.Brush(wx.Colour(0,0,0),style=wx.BRUSHSTYLE_TRANSPARENT))
			# 	self.memoryDc.SetPen(wx.Pen(wx.Colour(255,288,20),width=4))
			# 	self.memoryDc.DrawLine(self.logical_point1,self.logical_point2)
			# draw()
			# self.object_list.append(draw)
			do = DrawObject()
			do.add_line(self.logical_point1,self.logical_point2)
			self.object_list.append(do)
			self.UpdateMemoryDC()


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
			# print("on draw")
			dc.SetBrush(wx.Brush(wx.Colour(0,0,0),style=wx.BRUSHSTYLE_TRANSPARENT))
			# dc.SetPen(wx.Pen(wx.Colour(255,288,20),width=4))
			dc.DrawLine(self.logical_point1,self.logical_point2)
			# dc.DrawRectangle(calculate_rect(self.logical_point1,self.logical_point2))
			# dc.DrawCircle(self.logical_point1,calculate_radius(self.logical_point1,self.logical_point2))


	def open_file(self,path):
		if not os.path.isfile(path):
			return
		if not self.image.CanRead(path):
			return
		self.image.LoadFile(path)
		imw,imh = self.image.GetSize()
		self.object_list.clear()

		# bitmap = wx.Bitmap(imw,imh)
		# self.memoryDc = wx.MemoryDC(bitmap)

		# self.memoryDc.DrawBitmap(self.image.ConvertToBitmap(),0,0)
		# self.object_list.append(self.memoryDc.DrawBitmap(self.image.ConvertToBitmap(),0,0))
		do = DrawObject()
		do.add_bitmap(wx.Point(0,0),self.image.ConvertToBitmap())
		self.object_list.append(do)

		self.UpdateMemoryDC()

		self.m_scrolledWindow_image.SetVirtualSize(imw,imh)
		# self.m_scrolledWindow_image.Refresh()

	def init_dirbrowser(self):
		self.m_genericDirCtrl_filebrowser.SetPath(str(os.path.expanduser("~")))
		self.Bind(wx.EVT_DIRCTRL_SELECTIONCHANGED,lambda e: self.open_file(self.m_genericDirCtrl_filebrowser.GetPath()),self.m_genericDirCtrl_filebrowser)

	def init_editing(self):
		self.Bind(wx.EVT_TOOL, self.on_undo, self.m_tool_undo)
		self.Bind(wx.EVT_TOOL, self.on_redo, self.m_tool_redo)

	def on_undo(self,event):
		print("undo")
		try:
			self.temp_object_list.append(self.object_list.pop())
			self.UpdateMemoryDC()
		except IndexError:
			# disabel undo
			pass

	def on_redo(self,event):
		print("redo")
		try:
			self.object_list.append(self.temp_object_list.pop())
			self.UpdateMemoryDC()
		except IndexError:
			# disable undo
			pass


if __name__ == '__main__':
	app = wx.App()
	frame = Main(None)
	frame.Show()
	app.MainLoop()