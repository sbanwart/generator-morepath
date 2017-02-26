from .app import App
from .model import Root

@App.view(model=Root)
def root_get(self, request):
    print('Root view invoked...')
    return "Hello, world!"