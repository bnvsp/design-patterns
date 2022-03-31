"""
Abstract Factory Design Pattern
"""

from abc import abstractmethod, ABC


class CuisineFactory(ABC):
    """CuisineFactory:
    Interface to be used by family of different abstract products
    """

    @abstractmethod
    def get_starter(self):
        """create_starters: Starters
        """

    @abstractmethod
    def get_main_course(self):
        """create_meal: Meal
        """

    @abstractmethod
    def get_dessert(self):
        """create_desert: Desert
        """


class StartersFactory(ABC):
    """ChairFactory: Abstraction of Starters
    """

    @abstractmethod
    def starter_info(self):
        """starter_info:
        """


class MainCourseFactory(ABC):
    """MainCourse: Abstraction of Meals
    """

    @abstractmethod
    def meal_info(self):
        """meal_info:
        """


class DesertsFactory(ABC):
    """DesertsFactory: Abstraction of Deserts
    """

    @abstractmethod
    def dessert_info(self):
        """dessert_info:
        """


class ItalianCuisine(CuisineFactory):
    """ArtDecoFurniture: Create Art Deco style of furniture
    """

    def get_starter(self):
        return Bruschetta()

    def get_main_course(self):
        return Lasagna()

    def get_dessert(self):
        return Cassata()


class Bruschetta(StartersFactory):
    """Bruschetta: Italian Starter
    """

    def starter_info(self):
        return "Cooked Bruschetta"


class Lasagna(MainCourseFactory):
    """Lasagna: Italian Meal
    """

    def meal_info(self):
        return "Cooked Lasagna"


class Cassata(DesertsFactory):
    """Cassata: Italian Desert
    """

    def dessert_info(self):
        return "Served Cassata"


class ThaiCuisine(CuisineFactory):
    """ModernFurniture: Create Modern style of furniture
    """

    def get_starter(self):
        return CornFritters()

    def get_main_course(self):
        return Satay()

    def get_dessert(self):
        return ThaiJelly()


class CornFritters(StartersFactory):
    """CornFritters: Thai Starter
    """

    def starter_info(self):
        return "Cooked Thai Corn Fritters"


class Satay(MainCourseFactory):
    """Satay: Thai Meal
    """

    def meal_info(self):
        return "Cooked Thai Chicken Satay"


class ThaiJelly(DesertsFactory):
    """ThaiJelly: Thai Dessert
    """

    def dessert_info(self):
        return "Served Thai Jelly"


class IndianCuisine(CuisineFactory):
    """VictorianFurniture: Create Victorian style of furniture
    """

    def get_starter(self):
        return PannerTikka()

    def get_main_course(self):
        return Biryani()

    def get_dessert(self):
        return GulabJamun()


class PannerTikka(StartersFactory):
    """PannerTikka: Indian Starter
    """

    def starter_info(self):
        return "Cooked Panner Tikka"


class Biryani(MainCourseFactory):
    """Biryani: Indian main course
    """

    def meal_info(self):
        return "Dum Biryani"


class GulabJamun(DesertsFactory):
    """GulabJamun: Indian Dessert
    """

    def dessert_info(self):
        return "Served Gulab Jamun"


class ServeCuisine:
    """
    Serve Cuisine based on selection
    """

    def get_cuisine(self, cuisine_type: str):
        """get_cuisine: Get cuisine based on given type

        Args:
            cuisine_type (str): Cuisine Name
        """

        if cuisine_type.lower() == "italian":
            return ItalianCuisine()

        if cuisine_type.lower() == "indian":
            return IndianCuisine()

        if cuisine_type.lower() == "thai":
            return ThaiCuisine()


def main():
    """main: Returns cuisine dishes using given cuisine

    Args:
        cuisine_name (str): Cuisine label

    Returns:
        str: Cuisine dishes
    """

    available_cuisines = ("Indian", "Italian", "Thai",)
    cuisine_producer = ServeCuisine()

    for cuisine in available_cuisines:
        menu: str = ""
        cuisine_factory = cuisine_producer.get_cuisine(cuisine_type=cuisine)

        starter = cuisine_factory.get_starter()
        main_course = cuisine_factory.get_main_course()
        dessert = cuisine_factory.get_dessert()

        menu = "\n------------------------\n"
        menu += f"Selected Cuisine: {cuisine}\n"
        menu += "------------------------\n"
        menu += f"Starter: {starter.starter_info()}\n"
        menu += f"Main Course: {main_course.meal_info()}\n"
        menu += f"Desserts: {dessert.dessert_info()}\n"

        print(menu)

if __name__ == "__main__":
    main()
