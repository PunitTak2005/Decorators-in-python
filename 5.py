def debug(func):
    def wrapper(*args, **kwargs):
        # Converting positional arguments to string
        args_value = ','.join(str(arg) for arg in args)
        # Converting keyword arguments to string
        kwargs_value = ','.join(f"{k}={v}" for k, v in kwargs.items())
        print(f"Calling {func.__name__} with args {args_value} and kwargs {kwargs_value}")

        return func(*args, **kwargs)
    
    return wrapper

@debug
def hello():
    print("hello")

@debug
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}")

# Testing the functions
hello()
greet("chai", greeting="hanji")
