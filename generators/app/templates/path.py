from .app import App
from .model import Root

@App.path(path='/', model=Root)
def get_root():
    print('Calling get_root()...')
    return Root()