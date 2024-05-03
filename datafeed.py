from pywinauto.application import Application

#ff7-battle-mod
try:
    dlg_spec = Application(backend='uia').connect(title='ff7-battle-mod', timeout=20)
except TimeoutError:
    print('ff7-battle-mod.exe application was not started.  Please start the application before running.')
