import timeit
from functools import wraps
from typing import Any, Callable, TypeVar

T = TypeVar("T")

def calculate_exec_time(func: Callable[..., T]) -> Callable[..., T]:
    @wraps(func)
    def execution_time_wrapper(*args: Any, **kwargs: Any) -> T:
        start_time = timeit.default_timer()
        result = func(*args, **kwargs)
        end_time = timeit.default_timer()
        execution_time = end_time - start_time
        print(f"Execution time of {func.__name__}: {execution_time} seconds")
        return result

    return execution_time_wrapper