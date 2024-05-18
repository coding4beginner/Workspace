course_content = {
    "title": "week08 - object-oriented programming",
    "content": [
        {
            "name": "Exercise 1: Classes and Objects",
            "python": "class Dog:\n    def __init__(self, name):\n        self.name = name\n\n    def bark(self):\n        print(f'{self.name} is barking.')\n\nmy_dog = Dog('Rex')\nmy_dog.bark()",
            "readme": "# Exercise 1: Classes and Objects\n\nIn this exercise, you will learn the basics of object-oriented programming in Python. Follow the instructions to define a Dog class and create an object of the class.",
        },
        {
            "name": "Exercise 2: Inheritance",
            "python": "class Animal:\n    def __init__(self, name):\n        self.name = name\n\n    def speak(self):\n        raise NotImplementedError('Subclass must implement this method')\n\nclass Dog(Animal):\n    def speak(self):\n        print(f'{self.name} says Woof!')\n\nclass Cat(Animal):\n    def speak(self):\n        print(f'{self.name} says Meow!')\n\nmy_dog = Dog('Rex')\nmy_cat = Cat('Whiskers')\nmy_dog.speak()\nmy_cat.speak()",
            "readme": "# Exercise 2: Inheritance\n\nIn this exercise, you will learn about inheritance in Python. Follow the instructions to define a base class Animal and derived classes Dog and Cat.",
        },
        {
            "name": "Exercise 3: Method Overriding",
            "python": "class Animal:\n    def speak(self):\n        print('Animal speaking')\n\nclass Dog(Animal):\n    def speak(self):\n        print('Dog barking')\n\nmy_dog = Dog()\nmy_dog.speak()",
            "readme": "# Exercise 3: Method Overriding\n\nIn this exercise, you will learn about method overriding in Python. Follow the instructions to override the speak method in the Dog class.",
        },
        {
            "name": "Exercise 4: Class Variables and Instance Variables",
            "python": "class Dog:\n    species = 'Canis familiaris'\n\n    def __init__(self, name):\n        self.name = name\n\nmy_dog = Dog('Rex')\nprint(Dog.species)\nprint(my_dog.name)",
            "readme": "# Exercise 4: Class Variables and Instance Variables\n\nIn this exercise, you will learn about class variables and instance variables. Follow the instructions to define class and instance variables in the Dog class.",
        },
        {
            "name": "Exercise 5: Static and Class Methods",
            "python": "class Dog:\n    species = 'Canis familiaris'\n\n    def __init__(self, name):\n        self.name = name\n\n    @staticmethod\n    def bark():\n        print('Woof!')\n\n    @classmethod\n    def get_species(cls):\n        return cls.species\n\nprint(Dog.get_species())\nDog.bark()",
            "readme": "# Exercise 5: Static and Class Methods\n\nIn this exercise, you will learn about static methods and class methods in Python. Follow the instructions to define and use static and class methods in the Dog class.",
        },
    ],
}
