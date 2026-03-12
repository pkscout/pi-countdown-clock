from importlib import reload

defaults = {'end_year': 2025,
            'end_month': 1,
            'end_day': 1,
            'end_hour': 0,
            'font': 'Helvetica',
            'header_size': 200,
            'countdown_size': 160,
            'header_color': 'white',
            'countdown_color': 'white',
            'header_text': 'BDay',
            'fullscreen': False,
            'screen_width': 800,
            'screen_height': 480,
            'header_y_pos': 0.24,
            'countdown_y_pos': 0.7,
            'debug': False}

try:
    import data.settings as overrides
    has_overrides = True
except ImportError:
    has_overrides = False


def Reload():
    if has_overrides:
        reload(overrides)


def Get(name):
    setting = None
    if has_overrides:
        setting = getattr(overrides, name, None)
    if not setting:
        setting = defaults.get(name, None)
    return setting
