import pygetwindow as gw
import keyboard as kb
import time
import webbrowser as wb
import shutil as shut
import subprocess as subp
import os

allWin = []

EXCEPTIONS = {
    "Program Manager",
    "Windows Input Experience",
    "Task Manager",
    "Visual Studio Code",
}

class WindowManager:
    
    def __init__(self):
        pass

    def CloseWin(self):
        for window in allWin:
            if window.title and not any(exc in window.title for exc in EXCEPTIONS): #closes everything but exception (if it contains part of exception strings)
                try:
                    window.close()
                except Exception:
                    pass
    
    def OpenBrowser(self, url: str, newWin: bool = True):

        if not url.startswith('http'):
            url = 'https://' + url

        browsers = ['brave', 'brave-browser', 'google-chrome', 'firefox', 'msedge']
            
        # try shutil.which first
        for name in browsers:
            path = shut.which(name)
            if path:
                subp.Popen([path, '--new-window', '--', url])
                return
            
            # fallback for Windows where browsers aren't on PATH

        windows_paths = [
            os.path.expandvars(r'%LOCALAPPDATA%\BraveSoftware\Brave-Browser\Application\brave.exe'),
            os.path.expandvars(r'%PROGRAMFILES%\BraveSoftware\Brave-Browser\Application\brave.exe'),
            os.path.expandvars(r'%PROGRAMFILES%\Google\Chrome\Application\chrome.exe'),
            os.path.expandvars(r'%PROGRAMFILES(X86)%\Google\Chrome\Application\chrome.exe'),
            os.path.expandvars(r'%PROGRAMFILES%\Mozilla Firefox\firefox.exe'),
            os.path.expandvars(r'%PROGRAMFILES(X86)%\Mozilla Firefox\firefox.exe'),
            os.path.expandvars(r'%PROGRAMFILES(X86)%\Microsoft\Edge\Application\msedge.exe'),
            ]
        for path in windows_paths:
            if os.path.exists(path):
                subp.Popen([path, '--new-window', '--', url])
                return

        wb.get().open(url)
        

class KeyBoardManager:

    def __init__(self):
        pass

class KeyListener:
    
    def __init__(self):
        pass
    
    def StartListen(self, triggerKey=None):
        while True:
            event = kb.read_event()
            if event.event_type == 'down':
                print("Pressed:",event.name) #debug purposes
                if triggerKey is None or event.name == triggerKey:
                    return event.name  

class Main:

    def RefreshWin(self):
        global allWin
        allWin = gw.getAllWindows()#updates all current windows when called

    def __init__(self):
        self.WindowManage=WindowManager()
        self.keyl=KeyListener()
    
    def run(self):
        while True:
            key = self.keyl.StartListen(None)
            if key=='s':
                self.RefreshWin()
                self.WindowManage.CloseWin()
            elif key == 'd':
                self.WindowManage.OpenBrowser('google.com')
        



m1=Main()
m1.run()
