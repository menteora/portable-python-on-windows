#https://www.blog.pythonlibrary.org/2012/07/12/wxpython-how-to-create-a-generic-wizard/
#http://www.blog.pythonlibrary.org/2011/01/27/wxpython-a-wizard-tutorial/

# adv_wizard.py
import wx
import wx.adv as wiz

file_picker = False
########################################################################
class TitledPage(wiz.WizardPageSimple):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, parent, title):
        """Constructor"""
        wiz.WizardPageSimple.__init__(self, parent)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer = sizer
        self.SetSizer(sizer)
        
        title = wx.StaticText(self, -1, title)
        title.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
        sizer.Add(title, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
        sizer.Add(wx.StaticLine(self, -1), 0, wx.EXPAND|wx.ALL, 5)

########################################################################
class FileCheck(TitledPage):
    def __init__(self, parent, title):
        """Constructor"""
        super(FileCheck, self).__init__(parent, title)
        
        #File Picker
        self.AddSpacer()
        self.AddText("1. Seleziona il file del fornitore:")
        self.AddSpacer()
        self.file_picker = wx.FilePickerCtrl(self, -1)
        self.sizer.Add(self.file_picker, 0, wx.EXPAND)
        self.file_picker.Bind(wx.EVT_FILEPICKER_CHANGED, self.FilePickerChanged)

        #Button
        self.AddSpacer()
        self.sizer.Add(wx.StaticText(self, -1,"- La colonna codice fornitore si deve chiamare Codice"))
        self.sizer.Add(wx.StaticText(self, -1,"- La colonna nuovo prezzo si deve chiamare Prezzo"))
        self.button = wx.Button(self, -1, "Apri il documento")
        self.sizer.Add(self.button, 0, wx.EXPAND)
        self.button.Enable(False) 
        self.button.Bind(wx.EVT_BUTTON,self.ButtonClicked) 

    def FilePickerChanged(self, event):
        self.button.Enable(True)

    def ButtonClicked(self, event):
        btn = event.GetEventObject().GetLabel() 
        print("Bottone premuto = ",btn)

    def AddSpacer(self):
        self.sizer.Add((-1, 10)) 

    def AddText(self, text):
        self.sizer.Add(wx.StaticText(self, -1, text))
########################################################################
class Runner():
    def __init__(self):
        wizard = wiz.Wizard(None, -1, "Importazioni Listini Fornitore")
        page1 = FileCheck(wizard, "Excel Fornitore")
        page2 = TitledPage(wizard, "Page 2")
        page3 = FileCheck(wizard, "Page 3")
        page4 = TitledPage(wizard, "Page 4")
        page5 = TitledPage(wizard, "Page 5")
            
        wizard.FitToPage(page1)
        page5.sizer.Add(wx.StaticText(page5, -1, "\nThis is the last page."))


        # Set the initial order of the pages
        page1.SetNext(page2)
        page2.SetPrev(page1)
        page2.SetNext(page3)
        page3.SetPrev(page2)
        page3.SetNext(page4)
        page4.SetPrev(page3)
        page4.SetNext(page5)
        page5.SetPrev(page4)

        wizard.GetPageAreaSizer().Add(page1)
        wizard.RunWizard(page1)
        wizard.Destroy()

def OnClicked(event): 
   btn = event.GetEventObject().GetLabel() 
   print("Label of pressed button = ",btn) 
   print(file_picker.GetPath())

def main():
    """"""
    wizard = wiz.Wizard(None, -1, "Dynamic Wizard")
    page1 = TitledPage(wizard, "Page 1")
    page2 = TitledPage(wizard, "Page 2")
    page3 = FileCheck(wizard, "Page 3")
    page4 = TitledPage(wizard, "Page 4")
    page5 = TitledPage(wizard, "Page 5")
        
    wizard.FitToPage(page1)
    page5.sizer.Add(wx.StaticText(page5, -1, "\nThis is the last page."))
    

    file_picker = wx.FilePickerCtrl(page1, -1)
    page1.sizer.Add(file_picker)
    file_picker.Bind(wx.EVT_FILEPICKER_CHANGED, OnClicked)

    button = wx.Button(page1, -1, "click Me")
    page1.sizer.Add(button)
    button.Bind(wx.EVT_BUTTON,OnClicked) 

    page2.sizer.Add(wx.StaticText(page2, -1, "\nThis is the page." + file_picker.GetPath() ))
    # Set the initial order of the pages
    page1.SetNext(page2)
    page2.SetPrev(page1)
    page2.SetNext(page3)
    page3.SetPrev(page2)
    page3.SetNext(page4)
    page4.SetPrev(page3)
    page4.SetNext(page5)
    page5.SetPrev(page4)

    wizard.GetPageAreaSizer().Add(page1)
    wizard.RunWizard(page1)
    wizard.Destroy()
    
#----------------------------------------------------------------------
if __name__ == "__main__":
    app = wx.App(False)
    #main()
    wizard = Runner()
    app.MainLoop()