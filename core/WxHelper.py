# Wizard
import wx
import wx.adv as wiz


class EmptyTitledPage(wiz.WizardPageSimple):

    def __init__(self, parent, title):
        """Constructor"""
        wiz.WizardPageSimple.__init__(self, parent)
        font = wx.Font(wx.Font(12, wx.SWISS, wx.NORMAL, wx.FONTWEIGHT_NORMAL))
        wx.Window.SetFont(self, font)

        sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer = sizer
        self.SetSizer(sizer)

        title = wx.StaticText(self, -1, title)
        title.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
        sizer.Add(title, 0, wx.ALIGN_CENTRE | wx.ALL, 5)
        sizer.Add(wx.StaticLine(self, -1), 0, wx.EXPAND | wx.ALL, 5)

        '''
        prev_btn = wx.Window.FindWindowById(wx.ID_BACKWARD)
        prev_btn.SetLabel("< Precedente")
        next_btn = wx.Window.FindWindowById(wx.ID_FORWARD)
        next_btn.SetLabel("Successivo >")
        exit_btn = wx.Window.FindWindowById(wx.ID_CANCEL)
        exit_btn.SetLabel("Esci")
        '''

    def AddSpacer(self):
        self.sizer.Add((-1, 10))

    def AddText(self, text, bold=False, italic=False):
        txt = wx.StaticText(self, -1, text)
        if bold is True:
            txt.SetFont(txt.GetFont().MakeBold())
        if italic is True:
            txt.SetFont(txt.GetFont().MakeItalic())
        self.sizer.Add(txt)
        return txt
