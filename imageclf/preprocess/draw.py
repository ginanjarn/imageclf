import wx
import os
from generated.wxui import CanvasPanel
from pubsub import pub

"""Hover area"""
HOVER_TOP_LEFT = 0
HOVER_TOP = 1
HOVER_TOP_RIGTH = 2
HOVER_LEFT = 3
HOVER_MIDDLE = 4
HOVER_RIGTH = 5
HOVER_BOTTOM_LEFT = 6
HOVER_BOTTOM = 7
HOVER_BOTTOM_RIGHT = 8

def calculate_size(pt1: wx.Point, pt2: wx.Point) -> wx.Size:
	size = wx.Size(pt2.x-pt1.x, pt2.y-pt1.y)
	return size

class HoverArea:
	def __init__(self, x1,x2,y1,y2):
		self.x1,self.y1,self.x2,self.y2 = x1,y1,x2,y2

	def isHover(self, x:int,y:int):
		return self.x1 < x < self.x2 and self.y1 < y < self.y2

	def isHover(self, point: wx.Point):
		x,y = point.Get()
		return self.x1 < x < self.x2 and self.y1 < y < self.y2

class SelectArea:
	def __init__(self, x1:int,y1:int,x2:int,y2:int):
		w,h = x2-x1, y2-y1
		rect = wx.Rect()
		rect.SetLeft(x1)
		rect.SetRight(x2)
		rect.SetTop(y1)
		rect.SetBottom(y2)
		self.init(rect)

	def __init__(self, pt1: wx.Point, pt2: wx.Point):
		rect = wx.Rect()
		rect.SetLeft(min(pt1.x,pt2.x))
		rect.SetTop(min(pt1.y,pt2.y))
		rect.SetRight(max(pt1.x,pt2.x))
		rect.SetBottom(max(pt1.y,pt2.y))
		self.init(rect)

	def init(self,rect, rd=10):
		self.rect = rect
		self.temp_rect = None
		self.hover_areas = None
		self.select_area = -1
		self.set_hover_area(self.rect, rd)

	def GetRect(self):
		return self.rect

	def set_hover_area(self,rect: wx.Rect, rd=10):
		l, t, r, b = rect.Left, rect.Top, rect.Right, rect.Bottom

		xpa = []
		xpa.append(HoverArea(l-rd,l+rd,t-rd,t+rd))
		xpa.append(HoverArea(l+rd,r-rd,t-rd,t+rd))
		xpa.append(HoverArea(r-rd,r+rd,t-rd,t+rd))
		xpa.append(HoverArea(l-rd,l+rd,t+rd,b-rd))
		xpa.append(HoverArea(l+rd,r-rd,t+rd,b-rd))
		xpa.append(HoverArea(r-rd,r+rd,t+rd,b-rd))
		xpa.append(HoverArea(l-rd,l+rd,b-rd,b+rd))
		xpa.append(HoverArea(l+rd,r-rd,b-rd,b+rd))
		xpa.append(HoverArea(r-rd,r+rd,b-rd,b+rd))
		self.hover_areas = xpa

	def Draw(self, dc: wx.DC):
		dc.SetPen(wx.Pen(wx.Colour(0,0,255),width=2))
		dc.SetBrush(wx.Brush(wx.Colour(0,0,0),wx.BRUSHSTYLE_TRANSPARENT))
		rc = self.rect if not self.temp_rect else self.temp_rect
		dc.DrawRectangle(rc)

	def IsExpandable(self, point: wx.Point) -> bool:
		expandable = False
		x,y = point.Get()
		index = 0
		for xa in self.hover_areas:
			if xa.isHover(point):
				break
			index += 1
		self.select_area = index if index < len(self.hover_areas) else -1
		expandable = True if index < len(self.hover_areas) else False
		return expandable

	def Dragging(self, pt1: wx.Point, pt2: wx.Point):
		w,h = pt2.x-pt1.x, pt2.y-pt1.y

		if self.select_area < 0:
			return		

		rect = wx.Rect(*self.rect)
		l, t, r, b = rect.Left, rect.Top, rect.Right, rect.Bottom

		if self.select_area == HOVER_TOP_LEFT:
			rect.SetTopLeft(wx.Point(l+w,t+h))
			rect.SetBottomRight(wx.Point(r,b))
		elif self.select_area == HOVER_TOP:
			rect.SetTop(t+h)
			rect.SetBottom(b)
		elif self.select_area == HOVER_TOP_RIGTH:
			rect.SetTopRight(wx.Point(r+w,t+h))
			rect.SetBottomLeft(wx.Point(l,b))
		elif self.select_area == HOVER_LEFT:
			rect.SetLeft(l+w)
			rect.SetRight(r)
		elif self.select_area == HOVER_MIDDLE:
			rect.SetTopLeft(wx.Point(l+w,t+h))
		elif self.select_area == HOVER_RIGTH:
			rect.SetRight(r+w)
			rect.SetLeft(l)
		elif self.select_area == HOVER_BOTTOM_LEFT:			
			rect.SetBottomLeft(wx.Point(l+w,b+h))
			rect.SetTopRight(wx.Point(r,t))
		elif self.select_area == HOVER_BOTTOM:
			rect.SetBottom(b+h)
			rect.SetTop(t)
		elif self.select_area == HOVER_BOTTOM_RIGHT:
			rect.SetBottomRight(wx.Point(r+w,b+h))
			rect.SetTopLeft(wx.Point(l,t))

		self.temp_rect = rect

	def UpdateSelectArea(self):
		self.rect = wx.Rect(*self.temp_rect)
		self.temp_rect = None
		self.set_hover_area(self.rect)

class Canvas(CanvasPanel):
	def __init__(self, parent):
		super().__init__(parent)
		self.BRUSH_PIN_ACTIVE = wx.Brush(wx.Colour(255, 255, 0))
		self.BRUSH_PIN_DEFAULT = wx.Brush(wx.Colour(0, 255, 0))
		self.BRUSH_SELECTION = wx.Brush(
			wx.Colour(0, 0, 0), wx.BRUSHSTYLE_TRANSPARENT)
		self.PEN_SELECTION = wx.Pen(wx.Colour(0,0,255),width=5)

		self.buffer = None
		self.temp_buffer = None
		self.selection_buffer = None

		self.selected = False
		self.selecting = False
		self.selectArea = None
		self.expanding = False

		self.image = None
		self.canvas_size: wx.Size = None

		self.XY1 = None
		self.XY2 = None

		self.expand_selection = False

		pub.subscribe(self.OnMessage, "Canvas")

		self.m_scrolledWindow_image.Bind(wx.EVT_PAINT, self.OnPaint)
		self.m_scrolledWindow_image.Bind(wx.EVT_LEFT_DOWN, self.OnLeftEvent)
		self.m_scrolledWindow_image.Bind(wx.EVT_LEFT_UP, self.OnLeftEvent)
		self.m_scrolledWindow_image.Bind(wx.EVT_MOTION, self.OnLeftEvent)

	def OnPaint(self, event):
		if not self.buffer:
			return
		buff = self.buffer if not self.temp_buffer else self.temp_buffer
		buff = self.buffer if not self.selection_buffer else self.selection_buffer

		dc = wx.BufferedPaintDC(self.m_scrolledWindow_image,
			buff, wx.BUFFER_VIRTUAL_AREA)
		if self.selectArea:			
			self.CleanCanvas(dc,self.image.ConvertToBitmap())
			self.selectArea.Draw(dc)	

	def OpenImage(self, path):
		img = wx.Image()
		if not img.CanRead(path):
			return
		img.LoadFile(path)
		self.canvas_size = img.GetSize()
		imw, imh = img.GetSize()
		self.image = img
		self.buffer = wx.Bitmap(imw, imh)
		self.m_scrolledWindow_image.SetVirtualSize(self.canvas_size)
		dc = wx.BufferedDC(None, self.buffer)
		dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
		dc.Clear()
		dc.DrawBitmap(img.ConvertToBitmap(), 0, 0)
		self.m_scrolledWindow_image.Refresh()

	def OnMessage(self, arg1, arg2=None):
		if arg1 == "open" and arg2 is not None:
			if not os.path.isfile(arg2):
				return
			self.OpenImage(str(arg2))

	def GetLogicalPosition(self, point: wx.Point) -> (int, int):
		return self.m_scrolledWindow_image.CalcUnscrolledPosition(point.x, point.y)

	def GetScreenPosition(self, point: wx.Point) -> (int, int):
		return self.m_scrolledWindow_image.CalcScrolledPosition(point.x, point.y)

	def CleanCanvas(self, dc: wx.DC, buff: wx.Bitmap):
		dc.DrawBitmap(buff,0,0)

	def OnLeftEvent(self, event: wx.MouseEvent):
		if not self.buffer:
			return
		pos = event.GetPosition()

		if event.LeftDown():
			self.XY1 = wx.Point(self.GetLogicalPosition(pos))
			if not self.selected:
				self.temp_buffer = wx.Bitmap(self.buffer)
				self.selecting = True
			else:
				self.expanding = self.selectArea.IsExpandable(self.XY1)

		elif event.Dragging():
			self.XY2 = wx.Point(self.GetLogicalPosition(pos))
			if self.selecting:				
				self.selectArea = SelectArea(self.XY1,self.XY2)

			if self.expanding:
				self.selectArea.Dragging(self.XY1,self.XY2)

			self.m_scrolledWindow_image.Refresh(eraseBackground=False)

		elif event.LeftUp():
			self.XY2 = wx.Point(self.GetLogicalPosition(pos))
			if self.selecting:
				self.temp_buffer = None
				self.selecting = False
				if self.selectArea:
					self.selected = True

			if self.expanding:
				self.selectArea.UpdateSelectArea()
				self.expanding = False

			self.m_scrolledWindow_image.Refresh(eraseBackground=False)
		
