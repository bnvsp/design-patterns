"""
Build Robot
"""

from abc import abstractmethod, ABC

class Robot:
    """
    Characteristics of Robot
    """

    def __init__(self, robot_name: str) -> None:
        self.label: str = robot_name
        self.is_bi_pedal: bool = False
        self.is_quad_pedal: bool = False
        self.is_wheeled: bool = False
        self.is_humanoid: bool = False
        self.is_military: bool = False
        self.is_acoustic: bool = False
        self.can_fly: bool = False
        self.body: list = []
        self.intelligence_systems: list = []


    def __fetch_representation(self) -> str:
        """__fetch_representation: String representation of characteristics and
        installed body systems

        Returns:
            str: _description_
        """

        __robot_info: str = f"Name: {self.label}"

        __robot_info += "\n------------------------\n"
        __robot_info += "Characteristics:"
        __robot_info += "\n------------------------\n"

        __counter = 1

        if self.is_wheeled:
            __robot_info += f"{__counter}: Wheeled\n"
            __counter += 1
        if self.is_bi_pedal:
            __robot_info += f"{__counter}: Bi-Pedal\n"
            __counter += 1
        if self.is_quad_pedal:
            __robot_info += f"{__counter}: Quad-Pedal\n"
            __counter += 1
        if self.is_humanoid:
            __robot_info += f"{__counter}: Humanoid\n"
            __counter += 1
        if self.is_military:
            __robot_info += f"{__counter}: Intended for Military\n"
            __counter += 1
        if self.is_acoustic:
            __robot_info += f"{__counter}: Can Speak\n"
            __counter += 1
        if self.can_fly:
            __robot_info += f"{__counter}: Can Fly\n"

        __robot_info += "\n------------------------\n"
        __robot_info += "Body:"
        __robot_info += "\n------------------------\n"
        for part_id, part_name in enumerate(self.body):
            __robot_info += f"{part_id}: {part_name}\n"

        __robot_info += "\n------------------------\n"
        __robot_info += "Intelligence Systems:"
        __robot_info += "\n------------------------\n"
        for sys_id, sys_name in enumerate(self.intelligence_systems):
            __robot_info += f"{sys_id}: {sys_name}\n"

        return __robot_info


    def __str__(self) -> str:
        return self.__fetch_representation()


class BiPedal:
    """
    Adds BiPedal to Body
    """

    def __str__(self) -> str:
        return "Two Legs"


class QuadPedal:
    """Adds QuadPedal to Body
    """

    def __str__(self) -> str:
        return "Four Legs"


class Wheels:
    """Add Wheels
    """

    def __init__(self, wheel_count: int=2) -> None:
        self.wheel_count: int = wheel_count


    def __str__(self) -> str:
        return f"{self.wheel_count} Wheels"


class Arms:
    """
    Adds Arms
    """

    def __init__(self, arm_count: int=2) -> None:
        self.arms = arm_count

    def __str__(self) -> str:
        return f"{self.arms} Arms"


class Face:
    """Add Face Shape
    """

    def __init__(self, face_shape: str) -> None:
        self.face_shape = face_shape

    def __str__(self) -> str:
        return f"{self.face_shape}"


class Wings:
    """Add Wings
    """
    def __init__(self, wing_count: 2) -> None:
        self.wings: int = wing_count

    def __str__(self) -> str:
        return f"{self.wings} Wings"


class Voice:
    """Add Voice
    """

    def __init__(self, gender: str=None) -> None:
        self.voice_type = "Female"
        if gender is not None:
            self.voice_type = gender

    def __str__(self) -> str:
        return f"{self.voice_type} Voice"


class InfraRedSensor:
    """Add Infrared sensor
    """

    def __str__(self) -> str:
        return "Infrared Sensor"


class Weapon:
    """Add weapons
    """

    def __init__(self, weapon_type: str=None) -> None:
        self.weapon_type: str = "Pistol"
        if weapon_type is not None:
            self.weapon_type = weapon_type


    def __str__(self) -> str:
        return f"Weapon Type: {self.weapon_type}"


class HandGestures:
    """Add HandGestures
    """

    def __str__(self) -> str:
        return "Hand Gestures"


class ObstacleDetection:
    """Add Obstacle Detection
    """

    def __str__(self) -> str:
        return "Obstacle Detection"


class RobotBuilder(ABC):
    """RobotBuilder: Interaface for building Robot
    """

    @abstractmethod
    def build_body(self):
        """build_body: Build body
        """
        raise NotImplementedError

    @abstractmethod
    def build_intelligence(self):
        """build_intelligence: Add Intelligence
        """

    @abstractmethod
    def display_specs(self):
        """display_specs: Display Robot Specs
        """


class MilitaryBot(RobotBuilder):
    """Create Military Robot
    """
    def __init__(self, bot_name: str) -> None:
        self.robot = Robot(robot_name=bot_name)

    def build_body(self):
        """build_body: Build Military Standard body
        """
        self.robot.is_military = True
        self.robot.is_wheeled = True
        self.robot.is_acoustic = True
        self.robot.can_fly = True

        square_face = Face(face_shape="Square")
        two_arms = Arms()
        male_voice = Voice(gender="Male")
        machine_gun = Weapon(weapon_type="Machine Gun")
        two_wings = Wings(wing_count=2)

        body_info = [square_face, two_arms, male_voice, machine_gun, two_wings]
        self.robot.body.extend(body_info)

    def build_intelligence(self):
        """build_intelligence: Add intelligence to military robot
        """
        self.robot.intelligence_systems.append(
            InfraRedSensor()
        )
        self.robot.intelligence_systems.append(
            ObstacleDetection()
        )

    def display_specs(self) -> str:
        """display_specs: Display Military Bot Specs

        Returns:
            str: String representation of specifications added
        """

        return self.robot


class Humanoid(RobotBuilder):
    """Create Human assistant robot
    """

    def __init__(self, bot_name: str) -> None:
        self.robot = Robot(robot_name=bot_name)

    def build_body(self):
        """build_body: Create body
        """

        self.robot.is_acoustic = True
        self.robot.is_bi_pedal = True

        oval_face = Face(face_shape="Oval")
        two_arms = Arms(arm_count=4)
        female_voice = Voice(gender="Female")

        body_info = [oval_face, two_arms, female_voice]
        self.robot.body.extend(body_info)

    def build_intelligence(self):
        """build_intelligence: Add intelligence
        """
        self.robot.intelligence_systems.append(
            HandGestures()
        )
        self.robot.intelligence_systems.append(
            ObstacleDetection()
        )

    def display_specs(self) -> str:
        """display_specs: Display Humanoid Specs

        Returns:
            str: String representation of specifications added
        """

        return self.robot


class Maker:
    """
    Robot Maker
    """

    def make_military_bot(self, builder: MilitaryBot) -> str:
        """make_robot: Create Military Robot

        Args:
            builder (object): Create robot with Military specification
        """
        builder.build_body()
        builder.build_intelligence()

        return builder.display_specs()

    def make_humanoid(self, builder: Humanoid) -> str:
        """make_humanoid: Create Humanoid

        Args:
            builder (Humanoid): Create robot with Humanoid specification
        """
        builder.build_body()
        builder.build_intelligence()

        return builder.display_specs()


def main():
    """main: Create robots
    """

    robot_maker = Maker()

    military_builder = MilitaryBot(bot_name="Killer")
    humanoid_builder = Humanoid(bot_name="Tesla")

    military_specs = robot_maker.make_military_bot(builder=military_builder)
    print(military_specs)

    humanoid_specs = robot_maker.make_humanoid(builder=humanoid_builder)
    print(humanoid_specs)


if __name__ == "__main__":
    main()
