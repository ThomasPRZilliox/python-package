import inspect

def get_current_package():
    frame = inspect.currentframe()
    module = inspect.getmodule(frame.f_back)
    return module.__package__


