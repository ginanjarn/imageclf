from generated.wxui import MainFrame
import wx
import os
import math
from pathlib import Path

"""Drawing object"""
DRAW_POINT = wx.ID_ANY
DRAW_BITMAP = wx.ID_ANY
DRAW_LINE = wx.ID_ANY
DRAW_RECTANGLE = wx.ID_ANY
DRAW_CIRCLE = wx.ID_ANY
DRAW_ELLIPSE = wx.ID_ANY


def calculate_size(pt1: wx.Point, pt2: wx.Point):
	return wx.Size(pt2.x-pt1.x, pt2.y-pt1.y)


def calculate_radius(pt1: wx.Point, pt2: wx.Point):
	return math.sqrt(math.pow(pt2.x-pt1.x)+math.pow(pt2.y-pt1.y))


def calculate_rect(pt1: wx.Point, pt2: wx.Point):
	return wx.Rect(pt1, calculate_size(pt1, pt2))


def calculate_ext_rect(pt1: wx.Point, pt2: wx.Point, padding=20):
	xmin, xmax = min(pt1.x, pt2.x), max(pt1.x, pt2.x)
	ymin, ymax = min(pt1.y, pt2.y), max(pt1.y, pt2.y)
	x, y = xmin-padding, ymin-padding
	w,h = xmax+padding-x,ymax+padding-y
	return wx.Rect(wx.Point(x,y),wx.Size(w,h))


class DrawingObject:
	def __init__(self):
		self.temp_object = None
		self.objects = []

	def add_point(self, point1: wx.Point, preview=False):
		obj = {"name": DRAW_LINE, "point1": point1}
		if not preview:
			self.objects.append(obj)
		else:
			self.temp_object = obj

	def add_line(self, point1: wx.Point, point2: wx.Point, preview=False):
		obj = {"name": DRAW_LINE, "point1": point1, "point2": point2}
		if not preview:
			self.objects.append(obj)
		else:
			self.temp_object = obj

	def add_bitmap(self, point1: wx.Point, bitmap: wx.Bitmap, preview=False):
		obj = {"name": DRAW_BITMAP, "point1": point1}
		if not preview:
			self.objects.append(obj)
		else:
			self.temp_object = obj

	def add_rect(self, point1: wx.Point, point2: wx.Point, preview=False):
		w = point2.x - point1.x
		h = point2.y - point1.y
		obj = {"name": DRAW_RECTANGLE, "point1": point1, "size": wx.Size(w, h)}
		if not preview:
			self.objects.append(obj)
		else:
			self.temp_object = obj

	def add_circle(self, point1: wx.Point, point2: wx.Point, preview=False):
		w = point2.x - point1.x
		h = point2.y - point1.y
		r = math.sqrt(math.pow(w)+math.pow(h))
		obj = {"name": DRAW_CIRCLE, "point1": point1, "radius": r}
		if not preview:
			self.objects.append(obj)
		else:
			self.temp_object = obj

	def add_ellipse(self, point1: wx.Point, point2: wx.Point, preview=False):
		w = point2.x - point1.x
		h = point2.y - point1.y
		obj = {"name": DRAW_ELLIPSE, "point1": point1, "size": wx.Size(w, h)}
		if not preview:
			self.objects.append(obj)
		else:
			self.temp_object = obj


class Main(MainFrame):
	def __init__(self, parent):
		super().__init__(parent)
		self.m_genericDirCtrl_filebrowser.SetDefaultPath(os.getcwd())
		self.m_genericDirCtrl_filebrowser.ReCreateTree()
		self.Bind(wx.EVT_DIRCTRL_SELECTIONCHANGED,
				  self.on_dirctrl_select_change)

		self.paint_dc = None
		self.point1: wx.Point = None
		self.point2: wx.Point = None
		self.Draw = False

		self.src_point1: wx.Point = None
		self.src_point2: wx.Point = None

		self.drawing_object = DrawingObject()

		self.image = wx.Image()
		self.image_bitmap = None
		self.mem_dc = None
		self.m_scrolledWindow_image.Bind(wx.EVT_PAINT, self.on_paint)

		self.init_menu()
		self.init_toolbar()
		self.init_drawing()

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

		self.line_stock = []
		self.line_stock.append((wx.Point(12, 10), wx.Point(70, 100)))
		self.line_stock.append((wx.Point(120, 10), wx.Point(70, 40)))

		self.paint_timer = wx.Timer(self)
		self.Bind(wx.EVT_TIMER,self.on_update_timer ,self.paint_timer)

	def on_update_timer(self,event):
		w,h = self.image.GetSize()
		# bitmap = wx.Bitmap(w,h)
		# self.mem_dc = wx.MemoryDC(bitmap)
		if self.mem_dc:
			print("mem_dc available")
		# self.mem_dc.DrawBitmap(self.image_bitmap, 0, 0)
		# for line in self.line_stock:
			# self.mem_dc.DrawLine(line[0], line[1])

		# if not self.Draw:
			# return
		# self.mem_dc.DrawLine(self.point1, self.point2)

		rect = calculate_ext_rect(self.src_point1, self.src_point2)
		self.m_scrolledWindow_image.RefreshRect(rect)

	def open_image(self, path):
		if os.path.isfile(path):
			if self.image.CanRead(path):
				self.image.LoadFile(path, wx.BITMAP_TYPE_ANY)
				self.image_bitmap = self.image.ConvertToBitmap()
				imw, imh = self.image.GetSize()
				self.mem_dc = wx.MemoryDC(self.image.ConvertToBitmap())
				self.m_scrolledWindow_image.SetVirtualSize(imw, imh)
				self.m_scrolledWindow_image.Refresh()

	def on_dirctrl_select_change(self, event):
		filepath = self.m_genericDirCtrl_filebrowser.GetPath()
		self.open_image(filepath)

	def on_paint(self, event):		
		if not self.mem_dc:
			print("no mem_dc")
			return

		dc = wx.PaintDC(self.m_scrolledWindow_image)
		if not dc.IsOk():
			return
		self.paint_dc = dc
		self.m_scrolledWindow_image.PrepareDC(dc)
		# dc.Blit(xdest, ydest, width, height, source, xsrc, ysrc)
		dc.Blit(xdest=0, ydest=0, width=self.image.Width, height=self.image.Height, source=self.mem_dc, xsrc=0, ysrc=0)
		# dc.DrawBitmap(self.image_bitmap, 0, 0)
		# dc.DrawLine(wx.Point(12,10),wx.Point(70,100))
		# dc.DrawLine(wx.Point(120,10),wx.Point(670,100))
		# for line in self.line_stock:
			# dc.DrawLine(line[0], line[1])

		if not self.Draw:
			return
		dc.DrawLine(self.point1, self.point2)

	def get_logical_position(self, event):
		if self.paint_dc:
			return event.GetLogicalPosition(self.paint_dc)
		else:
			return None

	def on_left_down(self, event):
		self.src_point1 = event.GetPosition()
		pos = self.get_logical_position(event)
		if not pos:
			return
		self.point1 = pos
		self.Draw = True
		self.paint_timer.Start(25)

	def on_left_up(self, event):
		self.src_point2 = event.GetPosition()
		pos = self.get_logical_position(event)
		if not pos:
			return
		self.point2 = pos
		rect = calculate_rect(self.src_point1, self.src_point2)
		self.line_stock.append((self.point1, self.point2))
		# self.drawing_object.add_line(point1=self.point1,point2=self.point2)
		# w, h = self.m_scrolledWindow_image.GetSize()
		# self.m_scrolledWindow_image.RefreshRect(wx.Rect(0, 0, w, h))
		# self.m_scrolledWindow_image.Refresh()
		if self.Draw:
			self.mem_dc.DrawLine(self.point1,self.point2)
		self.Draw = False
		self.paint_timer.Stop()

	def on_motion(self, event):
		self.src_point2 = event.GetPosition()
		pos = self.get_logical_position(event)
		if not pos:
			return
		self.point2 = pos
		if not self.Draw:
			return
		self.drawing_object.add_line(
			point1=self.point1, point2=self.point2, preview=True)
		if self.point1:
			rect = calculate_ext_rect(self.src_point1, self.src_point2)
			# rect = calculate_rect(self.src_point1, self.src_point2)
			# self.m_scrolledWindow_image.RefreshRect(rect)

	def on_close(self, event):
		self.Destroy()

	def on_open(self, event):
		wildcard = self.image.GetImageExtWildcard()
		fd = wx.FileDialog(self, wildcard=wildcard,
						   style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
		if fd.ShowModal() == wx.ID_OK:
			filepath = fd.GetPath()
			self.open_image(filepath)

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