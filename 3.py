
def debug(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)        
    
    return wrapper






def greet(name, greeting="Hello'0:"):
    print(f"{greeting},{name}")


greet("chai", greeting="hanji")
