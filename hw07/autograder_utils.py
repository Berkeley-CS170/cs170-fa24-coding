import time
import signal
import contextlib
import cProfile
    
def validate_tour(tour, adj_list):
    """Returns the length of the tour if it is valid, -1 otherwise
    """
    n = len(tour)
    cost = 0
    for i in range(n):
        if tour[i] in adj_list[tour[i-1]]:
            cost += adj_list[tour[i-1]][tour[i]]
        else:
            return -1
    return cost

class TimeoutException(Exception):
    def __init__(self, message="Operation timed out"):
        super().__init__(message)

@contextlib.contextmanager
def handle_timeout(seconds):
    def timeout_handler(num, stack):
        raise TimeoutException("Code execution timed out")
    
    # no-op if signal module is not available (for Windows compatability)
    if hasattr(signal, 'SIGALRM') and hasattr(signal, 'alarm'):
        # Set up the signal handler for SIGALRM (alarm signal)`
        signal.signal(signal.SIGALRM, timeout_handler)
        # Set the alarm to trigger after the specified number of seconds
        signal.alarm(seconds)
    
    try:
        yield
    except TimeoutException as e:
        print(e)
    finally:
        # no-op if signal module is not available (for Windows compatability)
        if hasattr(signal, 'SIGALRM') and hasattr(signal, 'alarm'):
            # Cancel the alarm regardless of whether an exception occurred or not
            signal.alarm(0)

def profile(func):
        def wrapper(*args, **kwargs):
            profiler = cProfile.Profile()
            profiler.enable()

            out = func(*args, **kwargs)

            profiler.disable()

            profile_data = profiler.getstats()
            return out, sum(dd.callcount for dd in profile_data)
        return wrapper
    