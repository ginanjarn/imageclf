import wx

class ImageOps:
	"""ImageOps is image modify helper"""
	def __init__(self, image:wx.Image):
		self.image = image

	def get_size(self):
		return self.image.GetSize()

	def get_image(self):
		return self.image

	def to_bitmap(self):
		"""return bitmap"""
		return self.image.ConvertToBitmap()

	def to_grey(self):
		"""return grayed image"""
		return self.image.ConvertToGreyscale()

	def adjust_color(self,r,g,b,a=1):
		"""adjust color channel"""
		self.image = self.image.AdjustChannels(r, g, b, factor_alpha=1.0)
		return self

	def rotate(self,center:wx.Point,angle):
		"""rotate image"""
		self.image = self.image.Rotate(angle, center, interpolating=True, offsetAfterRotation=None)
		return self

	def crop(self,pt1:wx.Point,pt2:wx.Point):
		"""crop selected rect"""
		pos = wx.Point(min(pt1.x,pt2.x),min(pt1.y,pt2.y))
		size = calculate_size(pt1,pt2)
		self.crop(pos.x,pos.y,size.width,size.height)
		return self

	def crop(self,x,y,w,h):
		"""crop selected rect"""
		pt = wx.Point(x,y)
		sz = wx.Size(w,h)
		self.image = self.image.Resize(sz, pt, red=-1, green=-1, blue=-1)
		return self

	def resize(self,w,h,keep_ratio=True):
		"""resize image"""
		self.image = self.image.Rescale(w, h, quality=IMAGE_QUALITY_NORMAL)
		return self