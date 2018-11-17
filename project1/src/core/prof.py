import cProfile


def profiler(func):
    """Decorator for run function profile"""
    def wrapper(*args, **kwargs):
        profile_filename = 'prof/{}.prof'.format(func.__name__)
        profile = cProfile.Profile()
        result = profile.runcall(func, *args, **kwargs)
        profile.dump_stats(profile_filename)
        return result
    return wrapper
