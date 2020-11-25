from generated.wxui import CropPanel
import wx
from pubsub import pub

class CropPanel(CropPanel):
	def __init__(self,parent):
		super().__init__(parent)

		self.Bind(wx.EVT_BUTTON,self.OnApply,self.m_sdbSizer2Apply)

	def OnApply(self,event):
		rect :wx.Rect = None
		pub.sendMessage("Crop",arg1=rect)