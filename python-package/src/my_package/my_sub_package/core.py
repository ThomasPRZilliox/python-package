from my_package._utils import get_current_package

def hello():
    print(f"Hello from {get_current_package()}")