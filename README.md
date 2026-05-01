# RedeemSoul
a Windows hotkey tool that closes your open windows, opens a fresh browser setup, and launches your chosen apps — all with one keypress.

## installation

**step 1** — download the code by clicking the green `Code` button at the top of this page, then `Download ZIP`. extract it anywhere on your computer.

**step 2** — open cmd or powershell and paste this:
```
pip install pygetwindow keyboard appopener
```

**step 3** — rename `Main.py` to `Main.pyw` so you can run it by double clicking it without a console window popping up.

**step 4** — open `Main.pyw` in any text editor (notepad works fine) and edit the settings at the top of the file to your liking (see customisation below).

**step 5** — double click `Main.pyw` to run it, then press your trigger key whenever you want to activate it.

## features
- closes all open windows except ones you choose to keep
- opens a fresh browser window with your chosen first page
- automatically maximises the browser window
- opens extra browser tabs from a list
- opens and maximises apps alongside the browser
- all setup is controlled from the settings section at the top of the file

## customisation

all settings are at the top of `Main.pyw` — that's the only part you need to touch.

### trigger key
```python
TRIGGER_KEY = 's'  # change to any key you want
```

### windows to keep open
```python
EXCEPTIONS = {
    "Program Manager",
    "Windows Input Experience",
    "Task Manager",
    "Visual Studio Code",  # add any window title you want to keep
}
```

### first browser page
can be a website or a search query — it'll figure it out automatically.
```python
FIRST_BROWSER_PAGE = 'cats are cool'  # search query
FIRST_BROWSER_PAGE = 'youtube.com'    # or a website
```

### extra tabs
use `'url'` for websites and `'query'` for google searches.
```python
TABS_TO_OPEN = [
    ('url', 'gmail.com'),
    ('url', 'youtube.com'),
    ('query', 'how to pet your dog'),
]
```

### apps to open
```python
APPS_TO_OPEN = [
    'spotify',  # add any app by name
]
```

### browser titles
```python
BROWSER_TITLES = ['Brave', 'Chrome', 'Firefox', 'Edge']
```
if you use a different browser, add its window title to this list.

## notes
- Windows only
- works best with Brave, Chrome, Firefox and Edge
- some systems may need the script to be run as administrator for global key listening

## feedback & feature requests
found a bug or want a new feature? open an [issue](https://github.com/zaacbouy-afk/RedeemSoul/issues) and i'll take a look!