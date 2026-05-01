import pygetwindow as gw
import keyboard as kb
import time
import webbrowser as wb
import shutil as shut
import subprocess as subp
import os
import AppOpener


# hotkey settings
TRIGGER_KEY = 's'

# windows with these words in the title will not be closed
EXCEPTIONS = {
    "Program Manager",
    "Windows Input Experience",
    "Task Manager",
    "Visual Studio Code",
}

# first browser page to open
FIRST_BROWSER_PAGE = 'cats are cool'

# extra browser tabs to open after the first page
TABS_TO_OPEN = [
    ('url', 'gmail.com'),
    ('url', 'youtube.com'),
    ('query', 'how to pet your dog'),
]

# apps to open after the browser tabs
APPS_TO_OPEN = [
    'spotify',
]

# browser title words used to find and maximize the browser window
BROWSER_TITLES = ['Brave', 'Chrome', 'Firefox', 'Edge']


class WindowManager:  # manages windows and their state in general in this program

    def __init__(self):
        pass

    # close every window except protected windows
    def CloseWin(self):
        for window in gw.getAllWindows():
            if window.title and not any(exc in window.title for exc in EXCEPTIONS):
                try:
                    window.close()
                except Exception:
                    pass

    # open the first browser window as either a website or google search
    def OpenBrowser(self, input: str = 'about:blank'):
        if input.startswith('http') or '.' in input:
            url = input if input.startswith('http') else 'https://' + input
        else:
            url = 'https://www.google.com/search?q=' + input.replace(' ', '+')

        # try browser command names first
        browsers = ['brave', 'brave-browser', 'google-chrome', 'firefox', 'msedge']

        for name in browsers:
            path = shut.which(name)
            if path:
                subp.Popen([path, '--new-window', url])
                return

        # fallback for Windows where browsers are not on PATH
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

        wb.get().open(url)  # last fallback: may open a tab instead of a window

    # find a window by title and maximize it
    def WindowMaximise(self, title_options):
        for window in gw.getAllWindows():
            if any(title in window.title for title in title_options):
                window.maximize()
                return

    # open a website in a new browser tab
    def UrlSearch(self, url: str):
        if not url.startswith('http'):
            url = 'https://' + url
        wb.open_new_tab(url)

    # open a google search in a new browser tab
    def QuerySearch(self, query: str):
        url = 'https://www.google.com/search?q=' + query.replace(' ', '+')
        wb.open_new_tab(url)

    # open an app and maximize it when the window appears
    def OpenApp(self, app: str):
        AppOpener.open(app)
        start = time.time()

        while time.time() - start < 5:
            for window in gw.getAllWindows():
                if app.lower() in window.title.lower():
                    window.maximize()
                    return

            time.sleep(0.2)


class KeyBoardManager:  # manages keyboard functions in general (empty idk what to use this for atm)

    def __init__(self):
        pass


class KeyListener:  # listens to keys being pressed so that it can do actions in run()

    def __init__(self):
        pass

    # wait until any key or the chosen trigger key is pressed
    def StartListen(self, triggerKey=None):
        while True:
            event = kb.read_event()
            if event.event_type == 'down':
                #print("Pressed:",event.name) #debug purposes (uncomment if u want to see what key is being pressed realtime)
                if triggerKey is None or event.name == triggerKey:
                    return event.name


class Main:  # where run() happens

    def __init__(self):  # calling the classes into 'Main' class
        self.WindowManage = WindowManager()
        self.keyl = KeyListener()

    # main hotkey routine
    def run(self):
        while True:
            key = self.keyl.StartListen(TRIGGER_KEY)

            if key == TRIGGER_KEY:
                self.WindowManage.CloseWin()
                time.sleep(0.5)

                self.WindowManage.OpenBrowser(FIRST_BROWSER_PAGE)
                time.sleep(0.5)

                self.WindowManage.WindowMaximise(BROWSER_TITLES)

                for searchType, searchContent in TABS_TO_OPEN:
                    time.sleep(0.1)

                    if searchType == 'url':
                        self.WindowManage.UrlSearch(searchContent)
                    else:
                        self.WindowManage.QuerySearch(searchContent)

                for app in APPS_TO_OPEN:
                    time.sleep(0.1)
                    self.WindowManage.OpenApp(app)

                break


# start program
m1 = Main()
m1.run()
