import morepath
from .app import App

def run():
    print('Running app...')
    morepath.autoscan()
    App.commit()
    morepath.run(App())

if __name__ == '__main__':
    run()