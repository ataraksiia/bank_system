from datetime import datetime
from typing import Any, Callable


def log(filename: str | None = None) -> Callable:
    """Декоратор, который логирует вызов функции и ее результат в файл или в консоль"""

    def my_function(func: Callable[[Any], Any]) -> Callable[[Any], Callable]:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if filename is None:
                try:
                    res = func(*args, **kwargs)
                except Exception as error:
                    print(f"{date_time} {func.__name__} error: {type(error).__name__}. Inputs: {args}, {kwargs}")
                else:
                    print(f"{date_time} {func.__name__} ok")
                    return res
            else:
                with open(filename, "a", encoding="utf-8") as file:
                    try:
                        res = func(*args, **kwargs)
                    except Exception as error:
                        file.write(
                            f"{date_time} {func.__name__} error: {type(error).__name__}. Inputs: {args}, {kwargs}\n"
                        )
                    else:
                        file.write(f"{date_time} {func.__name__} ok\n")
                        return res

        return wrapper

    return my_function
