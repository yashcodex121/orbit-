from .start import register as start_register
from .help import register as help_register
from .download import register as download_register

def load_handlers(app):

    start_register(app)
    help_register(app)
    download_register(app)
