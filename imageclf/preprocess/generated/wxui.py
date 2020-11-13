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

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_splitter1 = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
		self.m_splitter1.Bind( wx.EVT_IDLE, self.m_splitter1OnIdle )

		self.m_panel1 = wx.Panel( self.m_splitter1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_genericDirCtrl_filebrowser = wx.GenericDirCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.DIRCTRL_3D_INTERNAL|wx.SUNKEN_BORDER, wx.EmptyString, 0 )

		self.m_genericDirCtrl_filebrowser.ShowHidden( False )
		bSizer3.Add( self.m_genericDirCtrl_filebrowser, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel1.SetSizer( bSizer3 )
		self.m_panel1.Layout()
		bSizer3.Fit( self.m_panel1 )
		self.m_scrolledWindow_image = wx.ScrolledWindow( self.m_splitter1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow_image.SetScrollRate( 5, 5 )
		self.m_scrolledWindow_image.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )

		self.m_splitter1.SplitVertically( self.m_panel1, self.m_scrolledWindow_image, 200 )
		bSizer1.Add( self.m_splitter1, 1, wx.EXPAND, 0 )


		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )
		self.m_toolBar1 = self.CreateToolBar( wx.TB_HORIZONTAL, wx.ID_ANY )
		self.m_tool_open = self.m_toolBar1.AddLabelTool( wx.ID_ANY, u"open", wx.ArtProvider.GetBitmap( wx.ART_FILE_OPEN, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool_save = self.m_toolBar1.AddLabelTool( wx.ID_ANY, u"save", wx.ArtProvider.GetBitmap( wx.ART_FILE_SAVE, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_toolBar1.AddSeparator()

		self.m_tool_undo = self.m_toolBar1.AddLabelTool( wx.ID_ANY, u"undo", wx.ArtProvider.GetBitmap( wx.ART_UNDO, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool_redo = self.m_toolBar1.AddLabelTool( wx.ID_ANY, u"redo", wx.ArtProvider.GetBitmap( wx.ART_REDO, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_toolBar1.Realize()


		self.Centre( wx.BOTH )

	def __del__( self ):
		pass

	def m_splitter1OnIdle( self, event ):
		self.m_splitter1.SetSashPosition( 200 )
		self.m_splitter1.Unbind( wx.EVT_IDLE )


###########################################################################
## Class ColorPanel
###########################################################################

class ColorPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 290,-1 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

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

		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"RGB" ), wx.VERTICAL )

		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText2 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Red", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer9.Add( self.m_staticText2, 1, wx.ALL, 5 )

		self.m_slider_red = wx.Slider( sbSizer2.GetStaticBox(), wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		bSizer9.Add( self.m_slider_red, 3, wx.ALL|wx.EXPAND, 5 )


		sbSizer2.Add( bSizer9, 1, wx.EXPAND, 5 )

		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText3 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Green", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer10.Add( self.m_staticText3, 1, wx.ALL, 5 )

		self.m_slider_green = wx.Slider( sbSizer2.GetStaticBox(), wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		bSizer10.Add( self.m_slider_green, 3, wx.ALL|wx.EXPAND, 5 )


		sbSizer2.Add( bSizer10, 1, wx.EXPAND, 5 )

		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText4 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Blue", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		bSizer11.Add( self.m_staticText4, 1, wx.ALL, 5 )

		self.m_slider_blue = wx.Slider( sbSizer2.GetStaticBox(), wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		bSizer11.Add( self.m_slider_blue, 3, wx.ALL|wx.EXPAND, 5 )


		sbSizer2.Add( bSizer11, 1, wx.EXPAND, 5 )


		bSizer6.Add( sbSizer2, 0, wx.EXPAND, 5 )

		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"HSL" ), wx.VERTICAL )

		bSizer91 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText21 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"HUE", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		bSizer91.Add( self.m_staticText21, 1, wx.ALL, 5 )

		self.m_slider_hue = wx.Slider( sbSizer3.GetStaticBox(), wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		bSizer91.Add( self.m_slider_hue, 3, wx.ALL|wx.EXPAND, 5 )


		sbSizer3.Add( bSizer91, 1, wx.EXPAND, 5 )

		bSizer92 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText22 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Saturation", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )

		bSizer92.Add( self.m_staticText22, 1, wx.ALL, 5 )

		self.m_slider_saturation = wx.Slider( sbSizer3.GetStaticBox(), wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		bSizer92.Add( self.m_slider_saturation, 3, wx.ALL|wx.EXPAND, 5 )


		sbSizer3.Add( bSizer92, 1, wx.EXPAND, 5 )

		bSizer93 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText23 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Lightness", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )

		bSizer93.Add( self.m_staticText23, 1, wx.ALL, 5 )

		self.m_slider_lightness = wx.Slider( sbSizer3.GetStaticBox(), wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		bSizer93.Add( self.m_slider_lightness, 3, wx.ALL|wx.EXPAND, 5 )


		sbSizer3.Add( bSizer93, 1, wx.EXPAND, 5 )


		bSizer6.Add( sbSizer3, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer6 )
		self.Layout()

	def __del__( self ):
		pass


###########################################################################
## Class ImageChangePanel
###########################################################################

class ImageChangePanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 290,-1 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer19 = wx.BoxSizer( wx.VERTICAL )

		self.m_button_revert = wx.Button( self, wx.ID_ANY, u"Revert Changes", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer19.Add( self.m_button_revert, 0, wx.ALL, 5 )

		m_listBox_changesChoices = []
		self.m_listBox_changes = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox_changesChoices, 0 )
		bSizer19.Add( self.m_listBox_changes, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer19 )
		self.Layout()

	def __del__( self ):
		pass


