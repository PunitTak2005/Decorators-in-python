import time

def cache(func):
    cache_value = {}
    
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        else:
            result = func(*args)
            cache_value[args] = result
            return result
    
    return wrapper

@cache
def long_running_function(a, b):
    time.sleep(1)
    return a + b

print(long_running_function(2, 3))
print(long_running_function(2, 3))
