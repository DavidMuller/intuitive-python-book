import cProfile

def a():
    b()
    b()

def b():
    for i in range(250000):
        pass

profiler = cProfile.Profile()
profiler.enable()

a()

profiler.disable()
profiler.dump_stats("example.stats")
