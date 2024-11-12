import time


def time_log(func):

    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        action_time = end - start
        print(f'{func.__name__}: {round(action_time, 4)} сек')
        return return_value

    return wrapper
