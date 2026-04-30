# RedeemSoul

a lightweight python tool that closes all your open windows and launches a fresh browser session with your preset tabs.

## installation

paste this in cmd/powershell:

```
pip install pygetwindow keyboard
```

## getting started

open `Main.py` and scroll to `run()` — that's the only section you need to touch.

add as many tabs as you want using the three methods:

```python
self.WindowManage.OpenBrowser('youtube.com')        # opens the browser with this as the first tab
self.WindowManage.UrlSearch('outlook.com')          # adds a URL as a tab
self.WindowManage.QuerySearch('python tutorials')   # adds a search query as a tab
```

to add windows you don't want closed, add them to the `EXCEPTIONS` set at the top of the file:

```python
EXCEPTIONS = {
    "Program Manager",
    "Visual Studio Code",
    "your window here",  # add any window title you want to keep
}
```

## notes

- Windows only
- tested on Brave, Chrome, Firefox and Edge

## feedback & feature requests

found a bug or got a feature idea? open an [issue](https://github.com/zaacbouy-afk/RedeemSoul/issues) and i'll take a look!