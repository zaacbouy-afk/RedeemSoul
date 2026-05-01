# RedeemSoul

a Windows hotkey tool that closes your open windows, opens a fresh browser setup, and launches your chosen apps with one keypress.

## installation

**step 1** - download the code by clicking the green `Code` button at the top of this page, then `Download ZIP`. extract it anywhere on your computer.

**step 2** - open cmd or powershell and paste this:

```bash
pip install pygetwindow keyboard appopener
```

**step 3** - rename `Main.py` to `Main.pyw` so you can run it by double clicking it without a console window popping up.

## features

- closes all open windows except ones you choose to keep
- opens a fresh browser window with your chosen first page
- automatically maximises the browser window
- opens extra browser tabs from a list
- can open and maximise apps alongside the browser
- trigger key is customisable
- setup is controlled from the settings section at the top of the file

## customisation

open `Main.pyw` in any text editor and edit the settings section near the top of the file.

### trigger key

```python
TRIGGER_KEY = ']'
```

### windows to keep open

```python
EXCEPTIONS = {
    "Program Manager",
    "Windows Input Experience",
    "Task Manager",
    "lovely cat game",
}
```

### first browser page

```python
FIRST_BROWSER_PAGE = 'youtube.com'
```

### extra tabs

```python
TABS_TO_OPEN = [
    'outlook.com',
    'gmail.com',
    'github.com/zaacbouy-afk/RedeemSoul',
]
```

### apps to open

```python
APPS_TO_OPEN = [
    'spotify',
]
```

### browser titles

```python
BROWSER_TITLES = ['Brave', 'Chrome', 'Firefox', 'Edge']
```

if you use another browser, add its window title to the list.

## notes

- Windows only
- works best with Brave, Chrome, Firefox and Edge
- app names must roughly match the app's window title for maximising to work
- some systems may need the script to be run as administrator for global key listening

## feedback & feature requests

found a bug or want a new feature? open an [issue](https://github.com/zaacbouy-afk/RedeemSoul/issues) and i'll take a look!
