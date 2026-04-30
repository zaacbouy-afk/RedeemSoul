# RedeemSoul

a tool that closes all your open windows and opens a fresh browser with your chosen tabs — all with one keypress.

## Installation

**step 1** — download the code by clicking the green `code` button at the top of this page, then `download ZIP`. extract it anywhere on your computer.

**step 2** — open cmd or powershell and paste this:

```
pip install pygetwindow keyboard
```

**step 3** — rename `Main.py` to `Main.pyw` so you can run it by just double clicking it with no console window popping up.

## Features

- closes all open windows except ones you want to keep
- opens a fresh browser window with your preset tabs
- supports direct URLs and search queries as tabs
- trigger key is customisable (defaults to `s`)
- add any windows you don't want closed to the `EXCEPTIONS` set at the top of the file

## Customisation

open `Main.pyw` in any text editor (notepad works fine) and scroll to the `run()` section at the bottom — that's the only part you need to touch.

**trigger key** — defaults to `s`, change it to anything you want:
```python
if key == 's':  # change s to any key you want
```

**your tabs** — add or remove lines to control what opens:
```python
self.WindowManage.OpenBrowser('youtube.com')       # first tab (can be any website or search)
self.WindowManage.UrlSearch('outlook.com')         # adds a website as a tab
self.WindowManage.QuerySearch('python tutorials')  # adds a google search as a tab
```

**keeping windows open** — add any window titles you don't want closed:
```python
EXCEPTIONS = {
    "Visual Studio Code",
    "your window title here",  # add whatever you want to keep
}
```

once you're happy with your setup, just double click `Main.pyw` to run it, then press your trigger key whenever you want to activate it.

## notes

- Windows only
- works with Brave, Chrome, Firefox and Edge

## Feedback & Feature requests

found a bug or want a new feature? open an [issue](https://github.com/zaacbouy-afk/RedeemSoul/issues) and i'll take a look!