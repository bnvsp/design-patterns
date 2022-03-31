"""
Chain of Responsibility Design Pattern
"""

from abc import abstractmethod, ABC

class Handler(ABC):
    """
    Interface to build chain of handlers and process food
    """

    @abstractmethod
    def pass_it(self, handler: object) -> object:
        """pass_it: Pass to next Handler

        Args:
            handler (object): Handler object

        Returns:
            object: _description_
        """

    @abstractmethod
    def grab_it(self, food: str, iterated_animals: list) -> str:
        """grab_it: Handle the food

        Args:
            food (str): food from client

        Returns:
            str: Affirmation text
        """


class BaseHandler(Handler):
    """
    The default chaining behavior can be implemented inside a base handler
    class.
    """

    _next_handler: Handler = None

    def pass_it(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def grab_it(self, food: str, iterated_animals: list) -> str:
        if self._next_handler and iterated_animals:
            return self._next_handler.grab_it(food, iterated_animals)

        return None


class DogHandler(BaseHandler):
    """DogHandler
    """

    __name__ = "Dog"

    def grab_it(self, food: str, iterated_animals: list) -> str:
        """grab_it: Handle the food
        Args:
            food (str): food to handle

        Returns:
            str: _description_
        """

        if food in ("Ball", "Meat",):
            return f"{self.__name__} grabbed {food}"

        if self.__name__ in iterated_animals:
            iterated_animals.remove(self.__name__)

        return super().grab_it(food, iterated_animals)


class CatHandler(BaseHandler):
    """CatHandler
    """

    __name__ = "Cat"

    def grab_it(self, food: str, iterated_animals) -> str:
        """grab_it: Handle the food
        Args:
            food (str): food to handle

        Returns:
            str: _description_
        """

        if food in ("Milk", "Sausage",):
            return f"{self.__name__} grabbed {food}"

        if self.__name__ in iterated_animals:
            iterated_animals.remove(self.__name__)

        return super().grab_it(food, iterated_animals)


class MonkeyHandler(BaseHandler):
    """MonkeyHandler
    """

    __name__ = "Monkey"

    def grab_it(self, food: str, iterated_animals: list) -> str:
        """grab_it: Handle the food
        Args:
            food (str): food to handle

        Returns:
            str: _description_
        """

        if food in ("Banana", "Coconut", "Camera",):
            return f"{self.__name__} grabbed {food}"

        if self.__name__ in iterated_animals:
            iterated_animals.remove(self.__name__)

        return super().grab_it(food, iterated_animals)


class DolphinHandler(BaseHandler):
    """DolphinHandler
    """

    __name__ = "Dolphin"

    def grab_it(self, food: str, iterated_animals: list) -> str:
        """grab_it: Handle the food
        Args:
            food (str): food to handle

        Returns:
            str: _description_
        """

        if food in ("Rings",):
            return f"{self.__name__} grabbed {food}"

        if self.__name__ in iterated_animals:
            iterated_animals.remove(self.__name__)

        return super().grab_it(food, iterated_animals)


def chain_responsibility(food_pack: list=None):
    """offer_food to Animals and see which one has grabbed it

    Args:
        food_pack (list, optional): Food items. Defaults to None.
    """

    if food_pack is None:
        food_pack = ("Meat", "Ball", "Rings", "Banana", "Milk", "Chocolates",)

    animal_chain: str = ""
    delimiter = ">"
    first_handler = None
    current_handler = None

    animal_handlers = BaseHandler.__subclasses__()

    # Create a chain map of all BaseHandler sublclasses
    for class_id, each_class in enumerate(animal_handlers):

        # Break the chain once all handlers are sequentually linked
        if class_id == len(animal_handlers)-1:
            break

        if not animal_chain: # Chains starts here
            first_handler = current_handler = each_class()
            animal_chain += f"{first_handler.__name__}"

        # Fetch next handler object
        next_handler = animal_handlers[class_id+1]()

        # Link current handler object to next handler object
        current_handler.pass_it(next_handler)
        animal_chain += f" {delimiter} {next_handler.__name__}"
        current_handler = next_handler

    # Link the last handler object to first handler object to complete the chain
    if current_handler != first_handler:
        current_handler.pass_it(first_handler)
        animal_chain += f" {delimiter} {first_handler.__name__}"

    # Fetch the handler identifiers (actual names)
    all_animals = list(
        map(
            lambda animal: animal.strip(), animal_chain.split(f"{delimiter}")
        )
    )

    print("Animal Chain", animal_chain, sep=" ---> ")

    # Offer the food pack and see which handler has grabbed it
    for food_item in food_pack:
        result = current_handler.grab_it(food_item, all_animals)
        if result:
            print(result)
        else:
            print(f"No animal has grabbed: {food_item}")


if __name__ == "__main__":
    chain_responsibility()
