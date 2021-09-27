def parameter_check(func):
    def wrapper(*args, **kwargs):
        print("parameter_check started")
        func(*args, **kwargs)
        print("parameter_check ended")

    return wrapper
