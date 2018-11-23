import cProfile

profile_filename = 'prof/question_like.prof'
profile = cProfile.Profile()
i = 0


def profiler(func):
    """Decorator for run function profile"""
    def wrapper(*args, **kwargs):
        global i
        i += 1
        result = profile.runcall(func, *args, **kwargs)
        if i % 10 == 0:
            profile.dump_stats(profile_filename)
        return result
    return wrapper
