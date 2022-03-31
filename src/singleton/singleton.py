"""
Singleton Design Pattern
"""

from typing import Any
from threading import Lock, Thread

class SingletonBase(type):
    """SingletonBase: Base class which will keep track of instance created

    Args:
        type (_type_): MetaClass

    """
    _base_instances: dict = {}
    _thread_lock: Lock = Lock()

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        """__call__
        """
        with cls._thread_lock:
            if cls not in cls._base_instances:
                singleton_instance = super().__call__(*args, **kwargs)
                cls._base_instances[cls] = singleton_instance
            else:
                singleton_instance = cls._base_instances[cls]

        return singleton_instance

class Singleton(metaclass=SingletonBase):
    """Singleton
    """

    def __init__(self) -> None:
        self.names: list = []

    def add_names(self, names_data: list) -> None:
        """add_names: Add given names to names list

        Args:
            names_data (list): _description_
        """

        if not names_data:
            raise ValueError("Cannot add empty sequence")

        if not isinstance(names_data, list):
            raise TypeError("Given names_data should be of 'list' type")

        self.names.extend(names_data)

    def get_names(self) -> list:
        """get_names Get added names

        Returns:
            list: List of added names
        """

        return self.names

def test_normal(is_multi_threaded=False):
    """test_normal_singleton
    """
    if is_multi_threaded:
        print("Multi-Threaded Singleton")
    else:
        print("Normal Singleton")
    singleton_obj_1 = Singleton()
    singleton_obj_1.add_names(names_data=["Hello World !, "])
    singleton_obj_2 = Singleton()
    names = singleton_obj_2.get_names()
    print("Added names: ", names)


def test_multi_threaded():
    """test_multi_threaded
    """
    thread_1 = Thread(target=test_normal, kwargs={"is_multi_threaded":True,})
    thread_2 = Thread(target=test_normal, kwargs={"is_multi_threaded":True,})
    thread_1.start()
    thread_2.start()
    thread_1.join()
    thread_2.join()

if __name__ == "__main__":
    test_normal()
    test_multi_threaded()
