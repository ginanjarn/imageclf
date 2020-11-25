# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"PicEditor", pos = wx.DefaultPosition, size = wx.Size( 900,512 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menuItem_open = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Open", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem_open )

		self.m_menuItem_save = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Save", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem_save )

		self.m_menuItem_saveas = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Save As", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem_saveas )

		self.m_menu1.AppendSeparator()

		self.m_menuItem_exit = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem_exit )

		self.m_menubar1.Append( self.m_menu1, u"File" )

		self.m_menu2 = wx.Menu()
		self.m_menuItem_undo = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Undo", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.m_menuItem_undo )

		self.m_menuItem_redo = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Redo", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.m_menuItem_redo )

		self.m_menu2.AppendSeparator()

		self.m_menuItem_changehistory = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Change history", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.m_menuItem_changehistory )

		self.m_menubar1.Append( self.m_menu2, u"Edit" )

		self.m_menu5 = wx.Menu()
		self.m_menuItem_showfilebrowser = wx.MenuItem( self.m_menu5, wx.ID_ANY, u"File Browser", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu5.Append( self.m_menuItem_showfilebrowser )

		self.m_menu11 = wx.Menu()
		self.m_menuItem_tbstandard = wx.MenuItem( self.m_menu11, wx.ID_ANY, u"Standard", wx.EmptyString, wx.ITEM_CHECK )
		self.m_menu11.Append( self.m_menuItem_tbstandard )
		self.m_menuItem_tbstandard.Check( True )

		self.m_menuItem_tbimage = wx.MenuItem( self.m_menu11, wx.ID_ANY, u"Image", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu11.Append( self.m_menuItem_tbimage )

		self.m_menuItem_tbzoom = wx.MenuItem( self.m_menu11, wx.ID_ANY, u"Zoom", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu11.Append( self.m_menuItem_tbzoom )

		self.m_menu5.AppendSubMenu( self.m_menu11, u"Toolbars" )

		self.Zoom = wx.Menu()
		self.m_menuItem_zmin = wx.MenuItem( self.Zoom, wx.ID_ANY, u"Zoom In"+ u"\t" + u"ctrl+=", wx.EmptyString, wx.ITEM_NORMAL )
		self.Zoom.Append( self.m_menuItem_zmin )

		self.m_menuItem_zmout = wx.MenuItem( self.Zoom, wx.ID_ANY, u"Zoom Out"+ u"\t" + u"ctrl+-", wx.EmptyString, wx.ITEM_NORMAL )
		self.Zoom.Append( self.m_menuItem_zmout )

		self.m_menu5.AppendSubMenu( self.Zoom, u"Zoom" )

		self.m_menubar1.Append( self.m_menu5, u"View" )

		self.m_menu3 = wx.Menu()
		self.m_menuItem_toolcrop = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"Crop", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu3.Append( self.m_menuItem_toolcrop )

		self.m_menuItem_toolresize = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"Resize", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu3.Append( self.m_menuItem_toolresize )

		self.m_menuItem_toolrotate = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"Rotate", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu3.Append( self.m_menuItem_toolrotate )

		self.m_menu3.AppendSeparator()

		self.m_menuItem_tooladjustcolor = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"Adjust color", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu3.Append( self.m_menuItem_tooladjustcolor )

		self.m_menubar1.Append( self.m_menu3, u"Image" )

		self.m_menu4 = wx.Menu()
		self.m_menuItem_help = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu4.Append( self.m_menuItem_help )

		self.m_menubar1.Append( self.m_menu4, u"Help" )

		self.SetMenuBar( self.m_menubar1 )


		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class FileBrowsePanel
###########################################################################

class FileBrowsePanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 300,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetMinSize( wx.Size( -1,200 ) )

		bSizer20 = wx.BoxSizer( wx.VERTICAL )

		self.m_genericDirCtrl_file = wx.GenericDirCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.DIRCTRL_3D_INTERNAL|wx.SUNKEN_BORDER, wx.EmptyString, 0 )

		self.m_genericDirCtrl_file.ShowHidden( False )
		bSizer20.Add( self.m_genericDirCtrl_file, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer20 )
		self.Layout()

	def __del__( self ):
		pass


###########################################################################
## Class CanvasPanel
###########################################################################

class CanvasPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer21 = wx.BoxSizer( wx.VERTICAL )

		self.m_scrolledWindow_image = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow_image.SetScrollRate( 5, 5 )
		bSizer21.Add( self.m_scrolledWindow_image, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer21 )
		self.Layout()

	def __del__( self ):
		pass


###########################################################################
## Class ChangeHistoryPanel
###########################################################################

class ChangeHistoryPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 300,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetMinSize( wx.Size( 300,200 ) )

		bSizer19 = wx.BoxSizer( wx.VERTICAL )

		m_listBox_changesChoices = []
		self.m_listBox_changes = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox_changesChoices, 0 )
		bSizer19.Add( self.m_listBox_changes, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer19 )
		self.Layout()

	def __del__( self ):
		pass


###########################################################################
## Class ColorPanel
###########################################################################

class ColorPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 300,280 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetMinSize( wx.Size( 300,280 ) )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Color" ), wx.HORIZONTAL )

		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_radioBtn_colorful = wx.RadioButton( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Color", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_radioBtn_colorful.SetValue( True )
		bSizer8.Add( self.m_radioBtn_colorful, 0, wx.ALL, 5 )

		self.m_radioBtn_gray = wx.RadioButton( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Gray", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_radioBtn_gray, 0, wx.ALL, 5 )


		sbSizer1.Add( bSizer8, 1, wx.EXPAND, 5 )


		bSizer6.Add( sbSizer1, 0, wx.EXPAND, 5 )

		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Adjust Color" ), wx.VERTICAL )

		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText2 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Red", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer9.Add( self.m_staticText2, 1, wx.ALL, 5 )

		self.m_slider_red = wx.Slider( sbSizer2.GetStaticBox(), wx.ID_ANY, 100, 0, 200, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		bSizer9.Add( self.m_slider_red, 3, wx.ALL|wx.EXPAND, 5 )


		sbSizer2.Add( bSizer9, 1, wx.EXPAND, 5 )

		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText3 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Green", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer10.Add( self.m_staticText3, 1, wx.ALL, 5 )

		self.m_slider_green = wx.Slider( sbSizer2.GetStaticBox(), wx.ID_ANY, 100, 0, 200, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		bSizer10.Add( self.m_slider_green, 3, wx.ALL|wx.EXPAND, 5 )


		sbSizer2.Add( bSizer10, 1, wx.EXPAND, 5 )

		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText4 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Blue", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		bSizer11.Add( self.m_staticText4, 1, wx.ALL, 5 )

		self.m_slider_blue = wx.Slider( sbSizer2.GetStaticBox(), wx.ID_ANY, 100, 0, 200, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		bSizer11.Add( self.m_slider_blue, 3, wx.ALL|wx.EXPAND, 5 )


		sbSizer2.Add( bSizer11, 1, wx.EXPAND, 5 )

		bSizer93 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText23 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Brightness", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )

		bSizer93.Add( self.m_staticText23, 1, wx.ALL, 5 )

		self.m_slider_brightness = wx.Slider( sbSizer2.GetStaticBox(), wx.ID_ANY, 100, 0, 200, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		bSizer93.Add( self.m_slider_brightness, 3, wx.ALL|wx.EXPAND, 5 )


		sbSizer2.Add( bSizer93, 1, wx.EXPAND, 5 )


		bSizer6.Add( sbSizer2, 0, wx.EXPAND, 5 )

		m_sdbSizer1 = wx.StdDialogButtonSizer()
		self.m_sdbSizer1Apply = wx.Button( self, wx.ID_APPLY )
		m_sdbSizer1.AddButton( self.m_sdbSizer1Apply )
		self.m_sdbSizer1Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer1.AddButton( self.m_sdbSizer1Cancel )
		m_sdbSizer1.Realize();
		m_sdbSizer1.SetMinSize( wx.Size( -1,64 ) )

		bSizer6.Add( m_sdbSizer1, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer6 )
		self.Layout()

	def __del__( self ):
		pass


###########################################################################
## Class CropPanel
###########################################################################

class CropPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 300,280 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetMinSize( wx.Size( 220,280 ) )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Position" ), wx.VERTICAL )

		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText5 = wx.StaticText( sbSizer4.GetStaticBox(), wx.ID_ANY, u"x", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		bSizer11.Add( self.m_staticText5, 1, wx.ALL, 5 )

		self.m_spinCtrl_cropx = wx.SpinCtrl( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		bSizer11.Add( self.m_spinCtrl_cropx, 2, wx.ALL, 5 )


		sbSizer4.Add( bSizer11, 0, wx.EXPAND, 5 )

		bSizer111 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText51 = wx.StaticText( sbSizer4.GetStaticBox(), wx.ID_ANY, u"y", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )

		bSizer111.Add( self.m_staticText51, 1, wx.ALL, 5 )

		self.m_spinCtrl_cropy = wx.SpinCtrl( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		bSizer111.Add( self.m_spinCtrl_cropy, 2, wx.ALL, 5 )


		sbSizer4.Add( bSizer111, 0, wx.EXPAND, 5 )


		bSizer10.Add( sbSizer4, 0, wx.EXPAND, 5 )

		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Size" ), wx.VERTICAL )

		bSizer112 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText52 = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"w", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText52.Wrap( -1 )

		bSizer112.Add( self.m_staticText52, 1, wx.ALL, 5 )

		self.m_spinCtrl_cropw = wx.SpinCtrl( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		bSizer112.Add( self.m_spinCtrl_cropw, 2, wx.ALL, 5 )


		sbSizer5.Add( bSizer112, 0, wx.EXPAND, 5 )

		bSizer113 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText53 = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"h", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText53.Wrap( -1 )

		bSizer113.Add( self.m_staticText53, 1, wx.ALL, 5 )

		self.m_spinCtrl_croph = wx.SpinCtrl( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		bSizer113.Add( self.m_spinCtrl_croph, 2, wx.ALL, 5 )


		sbSizer5.Add( bSizer113, 0, wx.EXPAND, 5 )

		self.m_checkBox_cropkeepratio = wx.CheckBox( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Keep ratio", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox_cropkeepratio.SetValue(True)
		sbSizer5.Add( self.m_checkBox_cropkeepratio, 0, wx.ALL, 5 )


		bSizer10.Add( sbSizer5, 0, wx.EXPAND, 5 )

		m_sdbSizer2 = wx.StdDialogButtonSizer()
		self.m_sdbSizer2Apply = wx.Button( self, wx.ID_APPLY )
		m_sdbSizer2.AddButton( self.m_sdbSizer2Apply )
		self.m_sdbSizer2Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer2.AddButton( self.m_sdbSizer2Cancel )
		m_sdbSizer2.Realize();
		m_sdbSizer2.SetMinSize( wx.Size( -1,64 ) )

		bSizer10.Add( m_sdbSizer2, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer10 )
		self.Layout()

	def __del__( self ):
		pass


###########################################################################
## Class ResizePanel
###########################################################################

class ResizePanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 300,180 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetMinSize( wx.Size( 200,180 ) )

		bSizer20 = wx.BoxSizer( wx.VERTICAL )

		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Size" ), wx.VERTICAL )

		bSizer21 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText10 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"width", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		bSizer21.Add( self.m_staticText10, 1, wx.ALL, 5 )

		self.m_spinCtrl_resizew = wx.SpinCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		bSizer21.Add( self.m_spinCtrl_resizew, 2, wx.ALL, 5 )


		sbSizer3.Add( bSizer21, 1, wx.EXPAND, 5 )

		bSizer22 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText11 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"height", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		bSizer22.Add( self.m_staticText11, 1, wx.ALL, 5 )

		self.m_spinCtrl_resizeh = wx.SpinCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		bSizer22.Add( self.m_spinCtrl_resizeh, 2, wx.ALL, 5 )


		sbSizer3.Add( bSizer22, 1, wx.EXPAND, 5 )

		self.m_checkBox2 = wx.CheckBox( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Keep ratio", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox2.SetValue(True)
		sbSizer3.Add( self.m_checkBox2, 0, wx.ALL, 5 )


		bSizer20.Add( sbSizer3, 0, wx.EXPAND, 5 )

		m_sdbSizer3 = wx.StdDialogButtonSizer()
		self.m_sdbSizer3Apply = wx.Button( self, wx.ID_APPLY )
		m_sdbSizer3.AddButton( self.m_sdbSizer3Apply )
		self.m_sdbSizer3Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer3.AddButton( self.m_sdbSizer3Cancel )
		m_sdbSizer3.Realize();
		m_sdbSizer3.SetMinSize( wx.Size( -1,64 ) )

		bSizer20.Add( m_sdbSizer3, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer20 )
		self.Layout()

	def __del__( self ):
		pass


###########################################################################
## Class RotatePanel
###########################################################################

class RotatePanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 300,250 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetMinSize( wx.Size( 230,250 ) )

		bSizer23 = wx.BoxSizer( wx.VERTICAL )

		sbSizer6 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Center" ), wx.VERTICAL )

		bSizer24 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText12 = wx.StaticText( sbSizer6.GetStaticBox(), wx.ID_ANY, u"x", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		bSizer24.Add( self.m_staticText12, 1, wx.ALL, 5 )

		self.m_spinCtrl_rotatex = wx.SpinCtrl( sbSizer6.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.SP_ARROW_KEYS, 0, 10, 0 )
		bSizer24.Add( self.m_spinCtrl_rotatex, 2, wx.ALL, 5 )


		sbSizer6.Add( bSizer24, 0, wx.EXPAND, 5 )

		bSizer25 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText13 = wx.StaticText( sbSizer6.GetStaticBox(), wx.ID_ANY, u"y", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		bSizer25.Add( self.m_staticText13, 1, wx.ALL, 5 )

		self.m_spinCtrl_rotatey = wx.SpinCtrl( sbSizer6.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.SP_ARROW_KEYS, 0, 10, 0 )
		bSizer25.Add( self.m_spinCtrl_rotatey, 2, wx.ALL, 5 )


		sbSizer6.Add( bSizer25, 0, wx.EXPAND, 5 )


		bSizer23.Add( sbSizer6, 0, wx.EXPAND, 5 )

		sbSizer7 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Rotation" ), wx.VERTICAL )

		bSizer26 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText14 = wx.StaticText( sbSizer7.GetStaticBox(), wx.ID_ANY, u"Angle", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		bSizer26.Add( self.m_staticText14, 1, wx.ALL, 5 )

		self.m_spinCtrlDouble_rotateangle = wx.SpinCtrlDouble( sbSizer7.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.SP_ARROW_KEYS, 0, 360, 0, 1 )
		self.m_spinCtrlDouble_rotateangle.SetDigits( 1 )
		bSizer26.Add( self.m_spinCtrlDouble_rotateangle, 1, wx.ALL, 5 )

		self.m_staticText15 = wx.StaticText( sbSizer7.GetStaticBox(), wx.ID_ANY, u"deg", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		bSizer26.Add( self.m_staticText15, 1, wx.ALL, 5 )


		sbSizer7.Add( bSizer26, 0, wx.EXPAND, 5 )

		self.m_slider_angle = wx.Slider( sbSizer7.GetStaticBox(), wx.ID_ANY, 0, -180, 180, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		sbSizer7.Add( self.m_slider_angle, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer23.Add( sbSizer7, 0, wx.EXPAND, 5 )

		m_sdbSizer4 = wx.StdDialogButtonSizer()
		self.m_sdbSizer4Apply = wx.Button( self, wx.ID_APPLY )
		m_sdbSizer4.AddButton( self.m_sdbSizer4Apply )
		self.m_sdbSizer4Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer4.AddButton( self.m_sdbSizer4Cancel )
		m_sdbSizer4.Realize();
		m_sdbSizer4.SetMinSize( wx.Size( -1,64 ) )

		bSizer23.Add( m_sdbSizer4, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer23 )
		self.Layout()

	def __del__( self ):
		pass


