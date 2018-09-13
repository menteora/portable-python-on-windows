#https://www.blog.pythonlibrary.org/2012/07/12/wxpython-how-to-create-a-generic-wizard/
#http://www.blog.pythonlibrary.org/2011/01/27/wxpython-a-wizard-tutorial/
#http://www.blog.pythonlibrary.org/2010/03/26/creating-a-simple-photo-viewer-with-wxpython/
#https://stackoverflow.com/questions/21766289/how-do-i-pass-information-between-pages-of-a-wxpython-pywizardpage-wizard
#https://www.blog.pythonlibrary.org/2013/09/04/wxpython-how-to-update-a-progress-bar-from-a-thread/
import os
import wx
import wx.adv as wiz
import sys
import json
from pandas import DataFrame
import pandas as pd
from threading import Thread
from wx.lib.pubsub import pub
#from wx.adv import Animation, AnimationCtrl
# Append core folder
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'core'))
# Import core Classes
from Utils import PathHelper
from Utils import Singleton
from MssqlHelper import MssqlHelper
import datetime

########################################################################
class ImportToNavision(Thread):
    """Test Worker Thread Class."""
 
    #----------------------------------------------------------------------
    def __init__(self):
        """Init Worker Thread Class."""
        Thread.__init__(self)
        self.start()    # start the thread
 
    #----------------------------------------------------------------------
    def run(self):
        """Run Worker Thread."""
        # This is the code executing in the new thread.
        database = MssqlHelper()
        engine = database.getEngine()
        file_to_read = WizardData().getWizardData()['file_picker_page1']
        df = pd.read_excel(file_to_read)[['Codice', 'Prezzo']]
        df.to_sql('ListinoZebra', con=engine, if_exists='replace')
        #Get results from Navision
        result = engine.execute("SELECT * FROM MIGLISTINO07_ALLCROSS_LISTINOZEBRA")
        df = DataFrame(result.fetchall())
        df.columns = result.keys()

        writer = pd.ExcelWriter('incrocio_zebra_crossnav.xlsx', 
                        engine='xlsxwriter', 
                        datetime_format='dd/mm/yyyy',
                        date_format='dd/mm/yyyy')
        sheetname = 'report'
        df.to_excel(writer, index=False, sheet_name=sheetname)


        #df["Data di Inizio"] = df["Data di Inizio"].dt.strftime(r"%d/%m/%Y")
        #Indicate workbook and worksheet for formatting
        workbook = writer.book
        worksheet = writer.sheets[sheetname]

        #Iterate through each column and set the width == the max length in that column. A padding length of 2 is also added.
        for i, col in enumerate(df.columns):
            # find length of column i
            column_len = df[col].astype(str).str.len().max()
            # Setting the length if the column header is larger
            # than the max column value length
            column_len = max(column_len, len(col)) + 2
            # set the column length
            worksheet.set_column(i, i, column_len)

        writer.save()

        wx.CallAfter(pub.sendMessage, "update", msg="end")

########################################################################
class WizardData(metaclass=Singleton):
    def __init__(self):
        self.data = {}

    def getWizardData(self):
        return self.data
    
    def setWizardData(self, data):
        self.data = data

########################################################################
class TitledPage(wiz.WizardPageSimple):
    """"""

    #----------------------------------------------------------------------
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
        sizer.Add(title, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
        sizer.Add(wx.StaticLine(self, -1), 0, wx.EXPAND|wx.ALL, 5)

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

        if bold==True:
            txt.SetFont(txt.GetFont().MakeBold())

        if italic==True:
            txt.SetFont(txt.GetFont().MakeItalic())

        self.sizer.Add(txt)
########################################################################
class FileCheck(TitledPage):
    def __init__(self, parent, title):
        """Constructor"""
        super(FileCheck, self).__init__(parent, title)
        
        forward_btn = self.FindWindowById(wx.ID_FORWARD) 
        forward_btn.Disable()

        #File Picker
        self.AddSpacer()
        self.AddText("1. Seleziona il file del fornitore:",bold=True)
        self.AddSpacer()
        self.file_picker = wx.FilePickerCtrl(self, -1)
        self.sizer.Add(self.file_picker, 0, wx.EXPAND)
        self.file_picker.Bind(wx.EVT_FILEPICKER_CHANGED, self.FilePickerChanged)

        #Description
        self.AddSpacer()
        self.AddText("2. Il file lo devi modificare in questo modo:", bold=True)
        self.AddSpacer()
        self.AddText("- La colonna codice fornitore si deve chiamare Codice")
        self.AddText("- La colonna nuovo prezzo si deve chiamare Prezzo")
        self.AddSpacer()
        self.AddText("come da figura", italic=True)

        #Image
        self.AddSpacer()
        png = wx.Image(PathHelper.getCustomConfigPath('formattazione _excel.png'), wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.sizer.Add(wx.StaticBitmap(self, -1, png, (10, 5), (png.GetWidth(), png.GetHeight())))
        self.AddSpacer()

        #Button
        self.AddText("3. Apri il file e salvalo come da indicazioni precedenti:", bold=True)
        self.AddSpacer()
        self.button = wx.Button(self, -1, "Apri il file selezionato")
        self.sizer.Add(self.button, 0, wx.EXPAND)
        self.AddSpacer()
        self.button.Enable(False) 
        self.button.Bind(wx.EVT_BUTTON,self.ButtonClicked) 
        ''' too fast
        anim = Animation('C:\\isakk tests\\isakk sql server\\configs\\homer.gif')
        ctrl = AnimationCtrl(self, -1, anim)
        ctrl.Play()
        self.sizer.Add(ctrl)
        #self.SetSizerAndFit(self.sizer)
        #self.Show()
        '''
        self.AddText("4. Se hai seguito le indicazioni puoi procedere", bold=True)
        self.AddSpacer()

    def FilePickerChanged(self, event):
        self.button.Enable(True)
        forward_btn = self.FindWindowById(wx.ID_FORWARD) 
        forward_btn.Enable()
        wdata = WizardData()
        data = {
            "file_picker_page1": self.file_picker.GetPath()
        }
        wdata.setWizardData(data)

    def ButtonClicked(self, event):
        os.startfile(self.file_picker.GetPath())
########################################################################
class ImportToNavisionPage(TitledPage):
    def __init__(self, parent, title):
        """Constructor"""
        super(ImportToNavisionPage, self).__init__(parent, title)
        
        self.AddText("1. Elabora il file precedentemente selezionato:", bold=True)
        self.AddSpacer()
        self.button = wx.Button(self, -1, "Elabora il file")
        self.sizer.Add(self.button, 0, wx.EXPAND)
        self.AddSpacer()
        self.button.Bind(wx.EVT_BUTTON,self.ButtonClicked)
        self.AddSpacer()
        self.progress_bar = wx.Gauge(self, -1, range = 20)
        self.sizer.Add(self.progress_bar, 0, wx.EXPAND)

    def ButtonClicked(self, event):
        btn = event.GetEventObject()
        btn.Disable()
        
        # create a pubsub receiver
        pub.subscribe(self.updateProgress, "update")
        self.progress_bar.Pulse()
        thread = ImportToNavision()
        thread.run()


    def updateProgress(self, msg):
        if msg == "end":
            self.progress_bar.SetValue(20) 
 
        #self.progress.SetValue(self.count)
 
########################################################################
class Runner():
    def __init__(self):
        wizard = wiz.Wizard(None, -1, "Importazioni Listini Fornitore")
        page1 = FileCheck(wizard, "Excel Fornitore")
        page2 = ImportToNavisionPage(wizard, "Elaborazione Dati")
        #page3 = FileCheck(wizard, "Page 3")
        #page4 = TitledPage(wizard, "Page 4")
        #page5 = TitledPage(wizard, "Page 5")
            
        wizard.FitToPage(page1)
        #page5.sizer.Add(wx.StaticText(page5, -1, "\nThis is the last page."))


        # Set the initial order of the pages
        page1.SetNext(page2)
        page2.SetPrev(page1)
        #page2.SetNext(page3)
        #page3.SetPrev(page2)
        #page3.SetNext(page4)
        #page4.SetPrev(page3)
        #page4.SetNext(page5)
        #page5.SetPrev(page4)

        wizard.GetPageAreaSizer().Add(page1)
        wizard.RunWizard(page1)
        wizard.Destroy()

#----------------------------------------------------------------------
if __name__ == "__main__":
    app = wx.App(False)
    wizard = Runner()
    app.MainLoop()