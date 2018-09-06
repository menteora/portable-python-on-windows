import wx
import sys
import os
import json
# Append core folder
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'core'))
# Import core Classes
from MyClass import MyClass
from Utils import PathHelper

c = MyClass()
c.function()

print(PathHelper.getConfigJson('config.json'))

def ask(parent=None, message='', default_value=''):
    dlg = wx.TextEntryDialog(parent, message, value=default_value)
    dlg.ShowModal()
    result = dlg.GetValue()
    dlg.Destroy()
    return result

PathHelper.getUserConfigJson()

# Initialize wx App
app = wx.App()
app.MainLoop()

# Call Dialog
message_respose = ask(message = 'Inserisci il codice Zebra:')
if message_respose:
    print(message_respose)

'''
data = {}
data['key'] = 'value'
json_data = json.dumps(data)
'''