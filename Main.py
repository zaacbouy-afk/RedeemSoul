import pygetwindow as gw
import keyboard as kb
import time
import webbrowser as wb
import shutil as shut
import subprocess as subp
import os

allWin = [] # stores all windows in an empty list, so it can be updated

EXCEPTIONS = {
    "Program Manager",
    "Windows Input Experience",
    "Task Manager",
    "Visual Studio Code",
}

class WindowManager: # manages windows and their state in general in this program
    
    def __init__(self):
        pass

    def CloseWin(self):
        for window in allWin:
            if window.title and not any(exc in window.title for exc in EXCEPTIONS): # closes everything but exception (if it contains part of exception strings)
                try:
                    window.close()
                except Exception:
                    pass
    
    def OpenBrowser  (self, input : str ='about:blank'):

        if input.startswith('http') or '.' in input:  # used for the checking the search type and making the first tab the correct search type
            url=input if input.startswith('http') else 'https://' + input
        else:
            url = 'https://www.google.com/search?q=' + input.replace(' ', '+')

        browsers = ['brave', 'brave-browser', 'google-chrome', 'firefox', 'msedge']
            
        # try shutil.which first
        for name in browsers:
            path = shut.which(name)
            if path:
                subp.Popen([path, '--new-window', url])
                return
            
            # fallback for Windows where browsers arent on PATH

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
                subp.Popen([path, '--new-window', url])
                return
            
        wb.get().open(url) # last fallback opening a new tab instead of window 
            

    def UrlSearch(self,url : str):
        
        if not url.startswith('http'):
            url = 'https://' + url
        wb.open_new_tab(url)
    
    def QuerySearch(self,query : str):

        url = 'https://www.google.com/search?q=' + query.replace(' ', '+')
        wb.open_new_tab(url)

class KeyBoardManager: # manages keyboard functions in general (empty idk what to use this for atm)

    def __init__(self):
        pass

class KeyListener: # listens to keys being pressed so that it can do actions in run()
    
    def __init__(self):
        pass
    
    def StartListen(self, triggerKey=None):
        while True:
            event = kb.read_event()
            if event.event_type == 'down':
                #print("Pressed:",event.name) #debug purposes (uncomment if u want to see what key is being pressed realtime)
                if triggerKey is None or event.name == triggerKey:
                    return event.name  

class Main: # where run() happens

    def RefreshWin(self):
        global allWin
        allWin = gw.getAllWindows() # updates all current windows when called

    def __init__(self): # calling the classes into 'Main' class
        self.WindowManage=WindowManager()
        self.keyl=KeyListener()
    
    def run(self): # Customisable section
        while True:
            key = self.keyl.StartListen(None)
            if key=='s': # default failsafe key (customisable) 
                self.WindowManage.OpenBrowser('youtube.com') # default (customisable)
                time.sleep(0.5) # waits for browser to open before maximising
                allWin = gw.getAllWindows() # refreshes window list to find the new browser window
                for window in allWin:
                    if any(b in window.title for b in ['Brave', 'Chrome', 'Firefox', 'Edge']): # finds the browser window universally
                        window.maximize() # maximises it
                        break # stops looking once found
                time.sleep(0.1)
                self.WindowManage.UrlSearch('gmail.com') # default (customisable)
                time.sleep(0.1)
                self.WindowManage.QuerySearch('how to pet my dog') # default (customisable)
                time.sleep(0.1)
                self.WindowManage.UrlSearch('outlook.com') # default (customisable)
                # add more if you want to !
                break
            
m1=Main()
m1.run()
