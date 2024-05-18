course_content = {
    "Week 01: Introduction to Python": [
        {
            "name": "Exercise 1: Hello World",
            "python": "print('Hello, World!')",
            "readme": "# Exercise 1: Hello World\n\nIn this exercise, you will write your first Python program to print 'Hello, World!' to the console.",
        },
        {
            "name": "Exercise 2: Variables and Data Types",
            "python": "name = 'Alice'\nage = 30\nprint(f'My name is {name} and I am {age} years old.')",
            "readme": "# Exercise 2: Variables and Data Types\n\nIn this exercise, you will learn about variables and data types. Follow the instructions to declare variables and print their values.",
        },
        {
            "name": "Exercise 3: Basic Arithmetic",
            "python": "a = 10\nb = 5\nprint(f'Addition: {a + b}')\nprint(f'Subtraction: {a - b}')\nprint(f'Multiplication: {a * b}')\nprint(f'Division: {a / b}')",
            "readme": "# Exercise 3: Basic Arithmetic\n\nIn this exercise, you will perform basic arithmetic operations in Python. Follow the instructions to add, subtract, multiply, and divide two numbers.",
        },
        {
            "name": "Exercise 4: Strings and String Methods",
            "python": "text = 'Hello, Python!'\nprint(text.upper())\nprint(text.lower())\nprint(text.replace('Python', 'World'))",
            "readme": "# Exercise 4: Strings and String Methods\n\nIn this exercise, you will explore string methods in Python. Follow the instructions to manipulate strings using various methods.",
        },
        {
            "name": "Exercise 5: User Input",
            "python": "name = input('Enter your name: ')\nprint(f'Hello, {name}!')",
            "readme": "# Exercise 5: User Input\n\nIn this exercise, you will learn how to take user input in Python. Follow the instructions to prompt the user for their name and print a greeting message.",
        },
    ],
    "Week 02: Control Flow": [
        {
            "name": "Exercise 1: If Statements",
            "python": "age = int(input('Enter your age: '))\nif age >= 18:\n    print('You are an adult.')\nelse:\n    print('You are a minor.')",
            "readme": "# Exercise 1: If Statements\n\nIn this exercise, you will learn about if statements in Python. Follow the instructions to check if a user is an adult or a minor based on their age.",
        },
        {
            "name": "Exercise 2: For Loops",
            "python": "for i in range(1, 11):\n    print(i)",
            "readme": "# Exercise 2: For Loops\n\nIn this exercise, you will learn about for loops in Python. Follow the instructions to print numbers from 1 to 10 using a for loop.",
        },
        {
            "name": "Exercise 3: While Loops",
            "python": "count = 1\nwhile count <= 10:\n    print(count)\n    count += 1",
            "readme": "# Exercise 3: While Loops\n\nIn this exercise, you will learn about while loops in Python. Follow the instructions to print numbers from 1 to 10 using a while loop.",
        },
        {
            "name": "Exercise 4: Break and Continue",
            "python": "for i in range(1, 11):\n    if i == 5:\n        break\n    print(i)\n\nfor i in range(1, 11):\n    if i == 5:\n        continue\n    print(i)",
            "readme": "# Exercise 4: Break and Continue\n\nIn this exercise, you will learn how to use break and continue statements in loops. Follow the instructions to see how they affect loop execution.",
        },
        {
            "name": "Exercise 5: Nested Loops",
            "python": "for i in range(1, 6):\n    for j in range(1, 6):\n        print(f'({i}, {j})')",
            "readme": "# Exercise 5: Nested Loops\n\nIn this exercise, you will learn about nested loops in Python. Follow the instructions to print pairs of numbers using nested for loops.",
        },
    ],
    "Week 03: Functions": [
        {
            "name": "Exercise 1: Defining Functions",
            "python": "def greet(name):\n    print(f'Hello, {name}!')\n\ngreet('Alice')\ngreet('Bob')",
            "readme": "# Exercise 1: Defining Functions\n\nIn this exercise, you will learn how to define functions in Python. Follow the instructions to create a greeting function and call it with different names.",
        },
        {
            "name": "Exercise 2: Function Arguments",
            "python": "def add(a, b):\n    return a + b\n\nresult = add(3, 5)\nprint(f'Result: {result}')",
            "readme": "# Exercise 2: Function Arguments\n\nIn this exercise, you will learn about function arguments in Python. Follow the instructions to create an addition function and call it with different arguments.",
        },
        {
            "name": "Exercise 3: Default Arguments",
            "python": "def greet(name, greeting='Hello'):\n    print(f'{greeting}, {name}!')\n\ngreet('Alice')\ngreet('Bob', 'Hi')",
            "readme": "# Exercise 3: Default Arguments\n\nIn this exercise, you will learn about default arguments in Python functions. Follow the instructions to create a greeting function with a default greeting message.",
        },
        {
            "name": "Exercise 4: Keyword Arguments",
            "python": "def describe_pet(animal_type, pet_name):\n    print(f'I have a {animal_type} named {pet_name}.')\n\ndescribe_pet(animal_type='dog', pet_name='Rover')\ndescribe_pet(pet_name='Whiskers', animal_type='cat')",
            "readme": "# Exercise 4: Keyword Arguments\n\nIn this exercise, you will learn about keyword arguments in Python functions. Follow the instructions to create a function that describes a pet and call it with keyword arguments.",
        },
        {
            "name": "Exercise 5: Return Values",
            "python": "def square(x):\n    return x * x\n\nresult = square(4)\nprint(f'Square: {result}')",
            "readme": "# Exercise 5: Return Values\n\nIn this exercise, you will learn how to return values from functions in Python. Follow the instructions to create a function that calculates the square of a number and returns the result.",
        },
    ],
    "Week 04: Data Structures": [
        {
            "name": "Exercise 1: Lists",
            "python": "fruits = ['apple', 'banana', 'cherry']\nfor fruit in fruits:\n    print(fruit)",
            "readme": "# Exercise 1: Lists\n\nIn this exercise, you will learn about lists in Python. Follow the instructions to create a list of fruits and print each fruit.",
        },
        {
            "name": "Exercise 2: Tuples",
            "python": "dimensions = (800, 600)\nprint(f'Width: {dimensions[0]}, Height: {dimensions[1]}')",
            "readme": "# Exercise 2: Tuples\n\nIn this exercise, you will learn about tuples in Python. Follow the instructions to create a tuple representing dimensions and print each value.",
        },
        {
            "name": "Exercise 3: Dictionaries",
            "python": "person = {'name': 'Alice', 'age': 30}\nprint(f'Name: {person['name']}, Age: {person['age']}')",
            "readme": "# Exercise 3: Dictionaries\n\nIn this exercise, you will learn about dictionaries in Python. Follow the instructions to create a dictionary representing a person and print each value.",
        },
        {
            "name": "Exercise 4: Sets",
            "python": "fruits = {'apple', 'banana', 'cherry'}\nfor fruit in fruits:\n    print(fruit)",
            "readme": "# Exercise 4: Sets\n\nIn this exercise, you will learn about sets in Python. Follow the instructions to create a set of fruits and print each fruit.",
        },
        {
            "name": "Exercise 5: List Comprehensions",
            "python": "squares = [x * x for x in range(1, 11)]\nprint(squares)",
            "readme": "# Exercise 5: List Comprehensions\n\nIn this exercise, you will learn about list comprehensions in Python. Follow the instructions to create a list of squares using a list comprehension.",
        },
    ],
    "Week 05: Modules and Packages": [
        {
            "name": "Exercise 1: Importing Modules",
            "python": "import math\nprint(math.sqrt(16))",
            "readme": "# Exercise 1: Importing Modules\n\nIn this exercise, you will learn how to import modules in Python. Follow the instructions to import the math module and use it to calculate the square root of a number.",
        },
        {
            "name": "Exercise 2: Creating Modules",
            "python": "# my_module.py\ndef greet(name):\n    return f'Hello, {name}!'\n\n# main.py\nimport my_module\nprint(my_module.greet('Alice'))",
            "readme": "# Exercise 2: Creating Modules\n\nIn this exercise, you will learn how to create your own modules in Python. Follow the instructions to create a module with a greeting function and use it in another script.",
        },
        {
            "name": "Exercise 3: Using Packages",
            "python": "# my_package/__init__.py\n# my_package/module1.py\ndef add(a, b):\n    return a + b\n\n# main.py\nfrom my_package import module1\nprint(module1.add(3, 5))",
            "readme": "# Exercise 3: Using Packages\n\nIn this exercise, you will learn how to use packages in Python. Follow the instructions to create a package with a module and use it in another script.",
        },
        {
            "name": "Exercise 4: Exploring Standard Library",
            "python": "import random\nnumbers = [random.randint(1, 100) for _ in range(10)]\nprint(numbers)",
            "readme": "# Exercise 4: Exploring Standard Library\n\nIn this exercise, you will explore the Python Standard Library. Follow the instructions to use the random module to generate a list of random numbers.",
        },
        {
            "name": "Exercise 5: Installing and Using Third-Party Packages",
            "python": "# Run `pip install requests` to install the requests package\nimport requests\nresponse = requests.get('https://api.github.com')\nprint(response.json())",
            "readme": "# Exercise 5: Installing and Using Third-Party Packages\n\nIn this exercise, you will learn how to install and use third-party packages in Python. Follow the instructions to install the requests package and use it to make an HTTP request.",
        },
    ],
    "Week 06: File Handling": [
        {
            "name": "Exercise 1: Reading Files",
            "python": "with open('example.txt', 'r') as file:\n    content = file.read()\nprint(content)",
            "readme": "# Exercise 1: Reading Files\n\nIn this exercise, you will learn how to read files in Python. Follow the instructions to read the content of a text file and print it to the console.",
        },
        {
            "name": "Exercise 2: Writing Files",
            "python": "with open('output.txt', 'w') as file:\n    file.write('Hello, World!')",
            "readme": "# Exercise 2: Writing Files\n\nIn this exercise, you will learn how to write files in Python. Follow the instructions to write a string to a text file.",
        },
        {
            "name": "Exercise 3: Appending to Files",
            "python": "with open('output.txt', 'a') as file:\n    file.write('\\nHello again!')",
            "readme": "# Exercise 3: Appending to Files\n\nIn this exercise, you will learn how to append to files in Python. Follow the instructions to append a string to an existing text file.",
        },
        {
            "name": "Exercise 4: Working with CSV Files",
            "python": "import csv\nwith open('data.csv', 'r') as file:\n    reader = csv.reader(file)\n    for row in reader:\n        print(row)",
            "readme": "# Exercise 4: Working with CSV Files\n\nIn this exercise, you will learn how to work with CSV files in Python. Follow the instructions to read and print the content of a CSV file.",
        },
        {
            "name": "Exercise 5: JSON Files",
            "python": "import json\nwith open('data.json', 'r') as file:\n    data = json.load(file)\nprint(data)",
            "readme": "# Exercise 5: JSON Files\n\nIn this exercise, you will learn how to work with JSON files in Python. Follow the instructions to read and print the content of a JSON file.",
        },
    ],
    "Week 07: Error Handling": [
        {
            "name": "Exercise 1: Try and Except",
            "python": "try:\n    result = 10 / 0\nexcept ZeroDivisionError:\n    print('Cannot divide by zero.')",
            "readme": "# Exercise 1: Try and Except\n\nIn this exercise, you will learn how to handle errors using try and except blocks. Follow the instructions to handle a division by zero error.",
        },
        {
            "name": "Exercise 2: Handling Multiple Exceptions",
            "python": "try:\n    result = 10 / 'a'\nexcept ZeroDivisionError:\n    print('Cannot divide by zero.')\nexcept TypeError:\n    print('Invalid type for division.')",
            "readme": "# Exercise 2: Handling Multiple Exceptions\n\nIn this exercise, you will learn how to handle multiple exceptions. Follow the instructions to handle both ZeroDivisionError and TypeError.",
        },
        {
            "name": "Exercise 3: Else and Finally",
            "python": "try:\n    result = 10 / 2\nexcept ZeroDivisionError:\n    print('Cannot divide by zero.')\nelse:\n    print(f'Result: {result}')\nfinally:\n    print('Execution completed.')",
            "readme": "# Exercise 3: Else and Finally\n\nIn this exercise, you will learn how to use else and finally blocks with try and except. Follow the instructions to see how else and finally blocks work.",
        },
        {
            "name": "Exercise 4: Raising Exceptions",
            "python": "def check_age(age):\n    if age < 0:\n        raise ValueError('Age cannot be negative.')\n    return age\n\ntry:\n    check_age(-1)\nexcept ValueError as e:\n    print(e)",
            "readme": "# Exercise 4: Raising Exceptions\n\nIn this exercise, you will learn how to raise exceptions in Python. Follow the instructions to raise and handle a ValueError for invalid age.",
        },
        {
            "name": "Exercise 5: Custom Exceptions",
            "python": "class CustomError(Exception):\n    pass\n\ntry:\n    raise CustomError('This is a custom error.')\nexcept CustomError as e:\n    print(e)",
            "readme": "# Exercise 5: Custom Exceptions\n\nIn this exercise, you will learn how to create and use custom exceptions. Follow the instructions to define a custom exception and raise it.",
        },
    ],
    "Week 08: Object-Oriented Programming": [
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
    "Week 09: Advanced Data Structures": [
        {
            "name": "Exercise 1: Linked Lists",
            "python": "class Node:\n    def __init__(self, data):\n        self.data = data\n        self.next = None\n\nclass LinkedList:\n    def __init__(self):\n        self.head = None\n\n    def append(self, data):\n        if not self.head:\n            self.head = Node(data)\n        else:\n            current = self.head\n            while current.next:\n                current = current.next\n            current.next = Node(data)\n\n    def display(self):\n        current = self.head\n        while current:\n            print(current.data, end=' -> ')\n            current = current.next\n\nll = LinkedList()\nll.append(1)\nll.append(2)\nll.append(3)\nll.display()",
            "readme": "# Exercise 1: Linked Lists\n\nIn this exercise, you will implement a linked list in Python. Follow the instructions to create a linked list and append/display elements.",
        },
        {
            "name": "Exercise 2: Stacks",
            "python": "class Stack:\n    def __init__(self):\n        self.items = []\n\n    def push(self, item):\n        self.items.append(item)\n\n    def pop(self):\n        return self.items.pop() if self.items else None\n\n    def peek(self):\n        return self.items[-1] if self.items else None\n\n    def is_empty(self):\n        return len(self.items) == 0\n\nstack = Stack()\nstack.push(1)\nstack.push(2)\nprint(stack.pop())\nprint(stack.peek())",
            "readme": "# Exercise 2: Stacks\n\nIn this exercise, you will implement a stack in Python. Follow the instructions to create a stack and perform push, pop, and peek operations.",
        },
        {
            "name": "Exercise 3: Queues",
            "python": "class Queue:\n    def __init__(self):\n        self.items = []\n\n    def enqueue(self, item):\n        self.items.insert(0, item)\n\n    def dequeue(self):\n        return self.items.pop() if self.items else None\n\n    def is_empty(self):\n        return len(self.items) == 0\n\nqueue = Queue()\nqueue.enqueue(1)\nqueue.enqueue(2)\nprint(queue.dequeue())\nprint(queue.dequeue())",
            "readme": "# Exercise 3: Queues\n\nIn this exercise, you will implement a queue in Python. Follow the instructions to create a queue and perform enqueue and dequeue operations.",
        },
        {
            "name": "Exercise 4: Binary Trees",
            "python": "class TreeNode:\n    def __init__(self, value):\n        self.value = value\n        self.left = None\n        self.right = None\n\n    def insert(self, value):\n        if value < self.value:\n            if self.left is None:\n                self.left = TreeNode(value)\n            else:\n                self.left.insert(value)\n        elif value > self.value:\n            if self.right is None:\n                self.right = TreeNode(value)\n            else:\n                self.right.insert(value)\n\n    def inorder(self):\n        elements = []\n        if self.left:\n            elements += self.left.inorder()\n        elements.append(self.value)\n        if self.right:\n            elements += self.right.inorder()\n        return elements\n\nroot = TreeNode(10)\nroot.insert(5)\nroot.insert(15)\nroot.insert(2)\nprint(root.inorder())",
            "readme": "# Exercise 4: Binary Trees\n\nIn this exercise, you will implement a binary tree in Python. Follow the instructions to create a binary tree and perform insert and inorder traversal operations.",
        },
        {
            "name": "Exercise 5: Graphs",
            "python": "class Graph:\n    def __init__(self):\n        self.graph = {}\n\n    def add_edge(self, node, neighbor):\n        if node not in self.graph:\n            self.graph[node] = []\n        self.graph[node].append(neighbor)\n\n    def bfs(self, start):\n        visited = []\n        queue = [start]\n        while queue:\n            node = queue.pop(0)\n            if node not in visited:\n                visited.append(node)\n                queue.extend(set(self.graph[node]) - set(visited))\n        return visited\n\n    def dfs(self, start, visited=None):\n        if visited is None:\n            visited = []\n        visited.append(start)\n        for neighbor in self.graph[start]:\n            if neighbor not in visited:\n                self.dfs(neighbor, visited)\n        return visited\n\ng = Graph()\ng.add_edge(0, 1)\ng.add_edge(0, 2)\ng.add_edge(1, 2)\ng.add_edge(2, 0)\ng.add_edge(2, 3)\ng.add_edge(3, 3)\nprint('BFS:', g.bfs(2))\nprint('DFS:', g.dfs(2))",
            "readme": "# Exercise 5: Graphs\n\nIn this exercise, you will implement a graph in Python. Follow the instructions to create a graph and perform BFS and DFS traversals.",
        },
    ],
    "Week 10: Decorators and Generators": [
        {
            "name": "Exercise 1: Function Decorators",
            "python": "def decorator_function(original_function):\n    def wrapper_function(*args, **kwargs):\n        print(f'Wrapper executed before {original_function.__name__}')\n        return original_function(*args, **kwargs)\n    return wrapper_function\n\n@decorator_function\ndef display():\n    print('Display function ran')\n\ndisplay()",
            "readme": "# Exercise 1: Function Decorators\n\nIn this exercise, you will learn about function decorators in Python. Follow the instructions to create a decorator and apply it to a function.",
        },
        {
            "name": "Exercise 2: Class Decorators",
            "python": "class DecoratorClass:\n    def __init__(self, original_function):\n        self.original_function = original_function\n\n    def __call__(self, *args, **kwargs):\n        print(f'Call method executed before {self.original_function.__name__}')\n        return self.original_function(*args, **kwargs)\n\n@DecoratorClass\ndef display():\n    print('Display function ran')\n\ndisplay()",
            "readme": "# Exercise 2: Class Decorators\n\nIn this exercise, you will learn about class decorators in Python. Follow the instructions to create a decorator class and apply it to a function.",
        },
        {
            "name": "Exercise 3: Generator Functions",
            "python": "def square_numbers(nums):\n    for i in nums:\n        yield i * i\n\nsquares = square_numbers([1, 2, 3, 4, 5])\nfor square in squares:\n    print(square)",
            "readme": "# Exercise 3: Generator Functions\n\nIn this exercise, you will learn about generator functions in Python. Follow the instructions to create a generator function that yields square of numbers.",
        },
        {
            "name": "Exercise 4: Generator Expressions",
            "python": "nums = [1, 2, 3, 4, 5]\nsquares = (x * x for x in nums)\nfor square in squares:\n    print(square)",
            "readme": "# Exercise 4: Generator Expressions\n\nIn this exercise, you will learn about generator expressions in Python. Follow the instructions to create a generator expression that yields square of numbers.",
        },
        {
            "name": "Exercise 5: Chaining Generators",
            "python": "def generator1(nums):\n    for num in nums:\n        yield num\n\ndef generator2(nums):\n    for num in nums:\n        yield num * num\n\nchained = generator2(generator1([1, 2, 3, 4, 5]))\nfor value in chained:\n    print(value)",
            "readme": "# Exercise 5: Chaining Generators\n\nIn this exercise, you will learn how to chain generators in Python. Follow the instructions to create and chain multiple generators.",
        },
    ],
    "Week 11: Advanced Functions": [
        {
            "name": "Exercise 1: Lambda Functions",
            "python": "square = lambda x: x * x\nprint(square(5))\n\nadd = lambda x, y: x + y\nprint(add(3, 5))",
            "readme": "# Exercise 1: Lambda Functions\n\nIn this exercise, you will learn about lambda functions in Python. Follow the instructions to create and use lambda functions for simple operations.",
        },
        {
            "name": "Exercise 2: Map Function",
            "python": "nums = [1, 2, 3, 4, 5]\nsquares = list(map(lambda x: x * x, nums))\nprint(squares)",
            "readme": "# Exercise 2: Map Function\n\nIn this exercise, you will learn how to use the map function in Python. Follow the instructions to apply a function to each item in a list using map.",
        },
        {
            "name": "Exercise 3: Filter Function",
            "python": "nums = [1, 2, 3, 4, 5]\nevens = list(filter(lambda x: x % 2 == 0, nums))\nprint(evens)",
            "readme": "# Exercise 3: Filter Function\n\nIn this exercise, you will learn how to use the filter function in Python. Follow the instructions to filter items in a list using filter.",
        },
        {
            "name": "Exercise 4: Reduce Function",
            "python": "from functools import reduce\nnums = [1, 2, 3, 4, 5]\nsum = reduce(lambda x, y: x + y, nums)\nprint(sum)",
            "readme": "# Exercise 4: Reduce Function\n\nIn this exercise, you will learn how to use the reduce function in Python. Follow the instructions to reduce a list to a single value using reduce.",
        },
        {
            "name": "Exercise 5: Function Composition",
            "python": "def add(x, y):\n    return x + y\n\ndef multiply(x, y):\n    return x * y\n\nprint(multiply(add(2, 3), add(4, 5)))",
            "readme": "# Exercise 5: Function Composition\n\nIn this exercise, you will learn how to compose functions in Python. Follow the instructions to combine simple functions to perform complex operations.",
        },
    ],
    "Week 12: File IO and Serialization": [
        {
            "name": "Exercise 1: Working with Text Files",
            "python": "with open('example.txt', 'w') as file:\n    file.write('Hello, World!')\n\nwith open('example.txt', 'r') as file:\n    content = file.read()\nprint(content)",
            "readme": "# Exercise 1: Working with Text Files\n\nIn this exercise, you will learn how to work with text files in Python. Follow the instructions to write to and read from a text file.",
        },
        {
            "name": "Exercise 2: CSV Files",
            "python": "import csv\n\nwith open('example.csv', 'w', newline='') as file:\n    writer = csv.writer(file)\n    writer.writerow(['name', 'age'])\n    writer.writerow(['Alice', 30])\n    writer.writerow(['Bob', 25])\n\nwith open('example.csv', 'r') as file:\n    reader = csv.reader(file)\n    for row in reader:\n        print(row)",
            "readme": "# Exercise 2: CSV Files\n\nIn this exercise, you will learn how to work with CSV files in Python. Follow the instructions to write to and read from a CSV file.",
        },
        {
            "name": "Exercise 3: JSON Files",
            "python": "import json\n\nperson = {'name': 'Alice', 'age': 30}\n\nwith open('example.json', 'w') as file:\n    json.dump(person, file)\n\nwith open('example.json', 'r') as file:\n    data = json.load(file)\nprint(data)",
            "readme": "# Exercise 3: JSON Files\n\nIn this exercise, you will learn how to work with JSON files in Python. Follow the instructions to write to and read from a JSON file.",
        },
        {
            "name": "Exercise 4: Pickle Module",
            "python": "import pickle\n\ndata = {'a': [1, 2.0, 3, 4+6j], 'b': ('string', u'unicode string'), 'c': None}\n\nwith open('data.pkl', 'wb') as file:\n    pickle.dump(data, file)\n\nwith open('data.pkl', 'rb') as file:\n    data_loaded = pickle.load(file)\nprint(data_loaded)",
            "readme": "# Exercise 4: Pickle Module\n\nIn this exercise, you will learn how to use the pickle module in Python. Follow the instructions to serialize and deserialize Python objects using pickle.",
        },
        {
            "name": "Exercise 5: Working with Binary Files",
            "python": "data = bytearray([1, 2, 3, 4, 5])\n\nwith open('binary.bin', 'wb') as file:\n    file.write(data)\n\nwith open('binary.bin', 'rb') as file:\n    data_loaded = file.read()\nprint(data_loaded)",
            "readme": "# Exercise 5: Working with Binary Files\n\nIn this exercise, you will learn how to work with binary files in Python. Follow the instructions to write to and read from a binary file.",
        },
    ],
    "Week 13: Regular Expressions": [
        {
            "name": "Exercise 1: Basic Patterns",
            "python": "import re\n\npattern = r'\\d+'\ntext = 'There are 123 apples and 45 bananas.'\nresult = re.findall(pattern, text)\nprint(result)",
            "readme": "# Exercise 1: Basic Patterns\n\nIn this exercise, you will learn the basics of regular expressions in Python. Follow the instructions to find all numbers in a given text.",
        },
        {
            "name": "Exercise 2: Character Classes",
            "python": "import re\n\npattern = r'[a-zA-Z]+'\ntext = 'Hello, World! 123'\nresult = re.findall(pattern, text)\nprint(result)",
            "readme": "# Exercise 2: Character Classes\n\nIn this exercise, you will learn about character classes in regular expressions. Follow the instructions to find all words in a given text.",
        },
        {
            "name": "Exercise 3: Quantifiers",
            "python": "import re\n\npattern = r'\\d{2,4}'\ntext = '123 4567 89'\nresult = re.findall(pattern, text)\nprint(result)",
            "readme": "# Exercise 3: Quantifiers\n\nIn this exercise, you will learn about quantifiers in regular expressions. Follow the instructions to find all numbers with 2 to 4 digits in a given text.",
        },
        {
            "name": "Exercise 4: Grouping and Capturing",
            "python": "import re\n\npattern = r'(\\d{3})-(\\d{3})-(\\d{4})'\ntext = 'Phone number: 123-456-7890'\nresult = re.search(pattern, text)\nif result:\n    print(result.groups())",
            "readme": "# Exercise 4: Grouping and Capturing\n\nIn this exercise, you will learn about grouping and capturing in regular expressions. Follow the instructions to extract parts of a phone number from a given text.",
        },
        {
            "name": "Exercise 5: Replacing Patterns",
            "python": "import re\n\npattern = r'\\s+'\ntext = 'Hello,   World!'\nnew_text = re.sub(pattern, ' ', text)\nprint(new_text)",
            "readme": "# Exercise 5: Replacing Patterns\n\nIn this exercise, you will learn how to replace patterns in a string using regular expressions. Follow the instructions to replace multiple spaces with a single space in a given text.",
        },
    ],
    "Week 14: Multithreading and Multiprocessing": [
        {
            "name": "Exercise 1: Multithreading",
            "python": "import threading\n\ndef print_numbers():\n    for i in range(1, 6):\n        print(i)\n\nthread = threading.Thread(target=print_numbers)\nthread.start()\nthread.join()",
            "readme": "# Exercise 1: Multithreading\n\nIn this exercise, you will learn the basics of multithreading in Python. Follow the instructions to create and start a thread.",
        },
        {
            "name": "Exercise 2: Thread Synchronization",
            "python": "import threading\n\nclass Counter:\n    def __init__(self):\n        self.count = 0\n        self.lock = threading.Lock()\n\n    def increment(self):\n        with self.lock:\n            self.count += 1\n\ncounter = Counter()\nthreads = []\nfor _ in range(100):\n    thread = threading.Thread(target=counter.increment)\n    threads.append(thread)\n    thread.start()\n\nfor thread in threads:\n    thread.join()\n\nprint(counter.count)",
            "readme": "# Exercise 2: Thread Synchronization\n\nIn this exercise, you will learn how to synchronize threads in Python. Follow the instructions to create a thread-safe counter using a lock.",
        },
        {
            "name": "Exercise 3: Multiprocessing",
            "python": "from multiprocessing import Process\n\ndef print_numbers():\n    for i in range(1, 6):\n        print(i)\n\nprocess = Process(target=print_numbers)\nprocess.start()\nprocess.join()",
            "readme": "# Exercise 3: Multiprocessing\n\nIn this exercise, you will learn the basics of multiprocessing in Python. Follow the instructions to create and start a process.",
        },
        {
            "name": "Exercise 4: Sharing Data Between Processes",
            "python": "from multiprocessing import Process, Value, Lock\n\ndef increment(counter, lock):\n    with lock:\n        counter.value += 1\n\ncounter = Value('i', 0)\nlock = Lock()\nprocesses = []\nfor _ in range(100):\n    process = Process(target=increment, args=(counter, lock))\n    processes.append(process)\n    process.start()\n\nfor process in processes:\n    process.join()\n\nprint(counter.value)",
            "readme": "# Exercise 4: Sharing Data Between Processes\n\nIn this exercise, you will learn how to share data between processes in Python. Follow the instructions to create a process-safe counter using a lock.",
        },
        {
            "name": "Exercise 5: Pool of Workers",
            "python": "from multiprocessing import Pool\n\ndef square(x):\n    return x * x\n\nwith Pool(5) as p:\n    result = p.map(square, [1, 2, 3, 4, 5])\nprint(result)",
            "readme": "# Exercise 5: Pool of Workers\n\nIn this exercise, you will learn how to use a pool of workers in Python. Follow the instructions to create a pool of processes to perform parallel computation.",
        },
    ],
    "Week 15: Networking": [
        {
            "name": "Exercise 1: TCP Client",
            "python": "import socket\n\nclient_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\nclient_socket.connect(('localhost', 12345))\nclient_socket.sendall(b'Hello, server')\nresponse = client_socket.recv(1024)\nprint(f'Received: {response.decode()}')\nclient_socket.close()",
            "readme": "# Exercise 1: TCP Client\n\nIn this exercise, you will learn how to create a TCP client in Python. Follow the instructions to connect to a server and send/receive data.",
        },
        {
            "name": "Exercise 2: TCP Server",
            "python": "import socket\n\nserver_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\nserver_socket.bind(('localhost', 12345))\nserver_socket.listen()\nprint('Server is listening...')\n\nwhile True:\n    client_socket, addr = server_socket.accept()\n    print(f'Connection from {addr}')\n    data = client_socket.recv(1024)\n    print(f'Received: {data.decode()}')\n    client_socket.sendall(b'Hello, client')\n    client_socket.close()",
            "readme": "# Exercise 2: TCP Server\n\nIn this exercise, you will learn how to create a TCP server in Python. Follow the instructions to listen for incoming connections and send/receive data.",
        },
        {
            "name": "Exercise 3: UDP Client",
            "python": "import socket\n\nclient_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)\nclient_socket.sendto(b'Hello, server', ('localhost', 12345))\nresponse, addr = client_socket.recvfrom(1024)\nprint(f'Received: {response.decode()}')\nclient_socket.close()",
            "readme": "# Exercise 3: UDP Client\n\nIn this exercise, you will learn how to create a UDP client in Python. Follow the instructions to send/receive data to/from a server.",
        },
        {
            "name": "Exercise 4: UDP Server",
            "python": "import socket\n\nserver_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)\nserver_socket.bind(('localhost', 12345))\nprint('Server is listening...')\n\nwhile True:\n    data, addr = server_socket.recvfrom(1024)\n    print(f'Received from {addr}: {data.decode()}')\n    server_socket.sendto(b'Hello, client', addr)",
            "readme": "# Exercise 4: UDP Server\n\nIn this exercise, you will learn how to create a UDP server in Python. Follow the instructions to listen for incoming data and send responses.",
        },
        {
            "name": "Exercise 5: HTTP Requests",
            "python": "import requests\n\nresponse = requests.get('https://jsonplaceholder.typicode.com/posts')\nprint(response.json())",
            "readme": "# Exercise 5: HTTP Requests\n\nIn this exercise, you will learn how to make HTTP requests in Python. Follow the instructions to send a GET request and print the JSON response.",
        },
    ],
    "Week 16: Web Scraping": [
        {
            "name": "Exercise 1: Fetching a Web Page",
            "python": "import requests\n\nresponse = requests.get('https://www.example.com')\nprint(response.text)",
            "readme": "# Exercise 1: Fetching a Web Page\n\nIn this exercise, you will learn how to fetch a web page using the requests library in Python. Follow the instructions to send a GET request and print the response text.",
        },
        {
            "name": "Exercise 2: Parsing HTML with BeautifulSoup",
            "python": "from bs4 import BeautifulSoup\nimport requests\n\nresponse = requests.get('https://www.example.com')\nsoup = BeautifulSoup(response.text, 'html.parser')\nprint(soup.title.text)",
            "readme": "# Exercise 2: Parsing HTML with BeautifulSoup\n\nIn this exercise, you will learn how to parse HTML using BeautifulSoup in Python. Follow the instructions to fetch a web page and extract the title.",
        },
        {
            "name": "Exercise 3: Extracting Data from HTML",
            "python": "from bs4 import BeautifulSoup\nimport requests\n\nresponse = requests.get('https://www.example.com')\nsoup = BeautifulSoup(response.text, 'html.parser')\nlinks = soup.find_all('a')\nfor link in links:\n    print(link.get('href'))",
            "readme": "# Exercise 3: Extracting Data from HTML\n\nIn this exercise, you will learn how to extract data from HTML using BeautifulSoup in Python. Follow the instructions to fetch a web page and extract all links.",
        },
        {
            "name": "Exercise 4: Handling Pagination",
            "python": "import requests\nfrom bs4 import BeautifulSoup\n\nurl = 'https://example.com/page={}'\nfor page in range(1, 4):\n    response = requests.get(url.format(page))\n    soup = BeautifulSoup(response.text, 'html.parser')\n    items = soup.find_all('div', class_='item')\n    for item in items:\n        print(item.text)",
            "readme": "# Exercise 4: Handling Pagination\n\nIn this exercise, you will learn how to handle pagination while web scraping in Python. Follow the instructions to fetch multiple pages and extract items from each page.",
        },
        {
            "name": "Exercise 5: Saving Data to a CSV File",
            "python": "import csv\nimport requests\nfrom bs4 import BeautifulSoup\n\nurl = 'https://example.com/page={}'\ndata = []\nfor page in range(1, 4):\n    response = requests.get(url.format(page))\n    soup = BeautifulSoup(response.text, 'html.parser')\n    items = soup.find_all('div', class_='item')\n    for item in items:\n        data.append([item.text])\n\nwith open('data.csv', 'w', newline='') as file:\n    writer = csv.writer(file)\n    writer.writerow(['Item'])\n    writer.writerows(data)",
            "readme": "# Exercise 5: Saving Data to a CSV File\n\nIn this exercise, you will learn how to save scraped data to a CSV file in Python. Follow the instructions to fetch multiple pages, extract items, and save them to a CSV file.",
        },
    ],
    "Week 17: Testing and Debugging": [
        {
            "name": "Exercise 1: Writing Unit Tests",
            "python": "import unittest\n\ndef add(x, y):\n    return x + y\n\nclass TestMath(unittest.TestCase):\n    def test_add(self):\n        self.assertEqual(add(3, 4), 7)\n        self.assertEqual(add(-1, 1), 0)\n\nif __name__ == '__main__':\n    unittest.main()",
            "readme": "# Exercise 1: Writing Unit Tests\n\nIn this exercise, you will learn how to write unit tests in Python. Follow the instructions to write tests for a simple addition function using the unittest module.",
        },
        {
            "name": "Exercise 2: Using Assertions",
            "python": "def divide(x, y):\n    assert y != 0, 'Division by zero is not allowed'\n    return x / y\n\nprint(divide(10, 2))\nprint(divide(10, 0))",
            "readme": "# Exercise 2: Using Assertions\n\nIn this exercise, you will learn how to use assertions in Python. Follow the instructions to write a function that performs division and uses an assertion to prevent division by zero.",
        },
        {
            "name": "Exercise 3: Debugging with pdb",
            "python": "import pdb\n\ndef add(x, y):\n    pdb.set_trace()\n    return x + y\n\nresult = add(3, 4)\nprint(result)",
            "readme": "# Exercise 3: Debugging with pdb\n\nIn this exercise, you will learn how to debug code using the pdb module in Python. Follow the instructions to set a breakpoint and step through the code.",
        },
        {
            "name": "Exercise 4: Mocking with unittest.mock",
            "python": "from unittest.mock import MagicMock\n\nclass MyClass:\n    def method(self):\n        pass\n\nobj = MyClass()\nobj.method = MagicMock(return_value=3)\nprint(obj.method())",
            "readme": "# Exercise 4: Mocking with unittest.mock\n\nIn this exercise, you will learn how to use mocks in Python. Follow the instructions to mock a method and define its return value using unittest.mock.",
        },
        {
            "name": "Exercise 5: Testing with pytest",
            "python": "def add(x, y):\n    return x + y\n\ndef test_add():\n    assert add(3, 4) == 7\n    assert add(-1, 1) == 0\n\nif __name__ == '__main__':\n    import pytest\n    pytest.main()",
            "readme": "# Exercise 5: Testing with pytest\n\nIn this exercise, you will learn how to write tests using pytest in Python. Follow the instructions to write tests for a simple addition function and run them with pytest.",
        },
    ],
    "Week 18: Logging and Monitoring": [
        {
            "name": "Exercise 1: Basic Logging",
            "python": "import logging\n\nlogging.basicConfig(level=logging.INFO)\nlogging.info('This is an info message')\nlogging.warning('This is a warning message')\nlogging.error('This is an error message')",
            "readme": "# Exercise 1: Basic Logging\n\nIn this exercise, you will learn the basics of logging in Python. Follow the instructions to configure the logging module and log messages at different levels.",
        },
        {
            "name": "Exercise 2: Logging to a File",
            "python": "import logging\n\nlogging.basicConfig(filename='app.log', level=logging.INFO)\nlogging.info('This message will be logged to a file')",
            "readme": "# Exercise 2: Logging to a File\n\nIn this exercise, you will learn how to log messages to a file in Python. Follow the instructions to configure the logging module to write logs to a file.",
        },
        {
            "name": "Exercise 3: Rotating Logs",
            "python": "import logging\nfrom logging.handlers import RotatingFileHandler\n\nhandler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)\nlogging.basicConfig(handlers=[handler], level=logging.INFO)\nfor i in range(1000):\n    logging.info(f'This is log message {i}')",
            "readme": "# Exercise 3: Rotating Logs\n\nIn this exercise, you will learn how to use rotating logs in Python. Follow the instructions to configure the logging module to rotate log files based on size.",
        },
        {
            "name": "Exercise 4: Logging with Context",
            "python": "import logging\n\nlogger = logging.getLogger(__name__)\n\nclass MyClass:\n    def __init__(self, name):\n        self.name = name\n\n    def greet(self):\n        logger.info(f'Greeting from {self.name}')\n\nobj = MyClass('Test')\nobj.greet()",
            "readme": "# Exercise 4: Logging with Context\n\nIn this exercise, you will learn how to add context to log messages in Python. Follow the instructions to create a logger and use it within a class.",
        },
        {
            "name": "Exercise 5: Monitoring with Prometheus",
            "python": "from prometheus_client import start_http_server, Summary\nimport random\nimport time\n\nREQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')\n\n@REQUEST_TIME.time()\ndef process_request(t):\n    time.sleep(t)\n\nif __name__ == '__main__':\n    start_http_server(8000)\n    while True:\n        process_request(random.random())",
            "readme": "# Exercise 5: Monitoring with Prometheus\n\nIn this exercise, you will learn how to use Prometheus for monitoring in Python. Follow the instructions to create a simple application that exposes metrics to Prometheus.",
        },
    ],
    "Week 19: Working with Databases": [
        {
            "name": "Exercise 1: Connecting to SQLite",
            "python": "import sqlite3\n\nconnection = sqlite3.connect('example.db')\ncursor = connection.cursor()\ncursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)''')\nconnection.commit()\nconnection.close()",
            "readme": "# Exercise 1: Connecting to SQLite\n\nIn this exercise, you will learn how to connect to an SQLite database in Python. Follow the instructions to create a database and a table.",
        },
        {
            "name": "Exercise 2: Inserting Data",
            "python": "import sqlite3\n\nconnection = sqlite3.connect('example.db')\ncursor = connection.cursor()\ncursor.execute('''INSERT INTO users (name) VALUES ('Alice')''')\nconnection.commit()\nconnection.close()",
            "readme": "# Exercise 2: Inserting Data\n\nIn this exercise, you will learn how to insert data into an SQLite database in Python. Follow the instructions to insert a record into a table.",
        },
        {
            "name": "Exercise 3: Querying Data",
            "python": "import sqlite3\n\nconnection = sqlite3.connect('example.db')\ncursor = connection.cursor()\ncursor.execute('''SELECT * FROM users''')\nrows = cursor.fetchall()\nfor row in rows:\n    print(row)\nconnection.close()",
            "readme": "# Exercise 3: Querying Data\n\nIn this exercise, you will learn how to query data from an SQLite database in Python. Follow the instructions to select and print all records from a table.",
        },
        {
            "name": "Exercise 4: Updating Data",
            "python": "import sqlite3\n\nconnection = sqlite3.connect('example.db')\ncursor = connection.cursor()\ncursor.execute('''UPDATE users SET name = 'Bob' WHERE name = 'Alice' ''')\nconnection.commit()\nconnection.close()",
            "readme": "# Exercise 4: Updating Data\n\nIn this exercise, you will learn how to update data in an SQLite database in Python. Follow the instructions to update a record in a table.",
        },
        {
            "name": "Exercise 5: Deleting Data",
            "python": "import sqlite3\n\nconnection = sqlite3.connect('example.db')\ncursor = connection.cursor()\ncursor.execute('''DELETE FROM users WHERE name = 'Bob' ''')\nconnection.commit()\nconnection.close()",
            "readme": "# Exercise 5: Deleting Data\n\nIn this exercise, you will learn how to delete data from an SQLite database in Python. Follow the instructions to delete a record from a table.",
        },
    ],
    "Week 20: Web Development with Flask": [
        {
            "name": "Exercise 1: Basic Flask App",
            "python": "from flask import Flask\n\napp = Flask(__name__)\n\n@app.route('/')\ndef home():\n    return 'Hello, Flask!'\n\nif __name__ == '__main__':\n    app.run(debug=True)",
            "readme": "# Exercise 1: Basic Flask App\n\nIn this exercise, you will learn how to create a basic Flask application. Follow the instructions to create a simple web server with Flask.",
        },
        {
            "name": "Exercise 2: Flask Templates",
            "python": "from flask import Flask, render_template\n\napp = Flask(__name__)\n\n@app.route('/')\ndef home():\n    return render_template('home.html', title='Home')\n\nif __name__ == '__main__':\n    app.run(debug=True)",
            "readme": "# Exercise 2: Flask Templates\n\nIn this exercise, you will learn how to use templates in Flask. Follow the instructions to create an HTML template and render it in a route.",
        },
        {
            "name": "Exercise 3: Flask Forms",
            "python": "from flask import Flask, render_template, request\n\napp = Flask(__name__)\n\n@app.route('/', methods=['GET', 'POST'])\ndef home():\n    if request.method == 'POST':\n        name = request.form['name']\n        return f'Hello, {name}!'\n    return render_template('form.html')\n\nif __name__ == '__main__':\n    app.run(debug=True)",
            "readme": "# Exercise 3: Flask Forms\n\nIn this exercise, you will learn how to handle forms in Flask. Follow the instructions to create a form and process its data.",
        },
        {
            "name": "Exercise 4: Flask Database Integration",
            "python": "from flask import Flask, render_template\nfrom flask_sqlalchemy import SQLAlchemy\n\napp = Flask(__name__)\napp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'\ndb = SQLAlchemy(app)\n\nclass User(db.Model):\n    id = db.Column(db.Integer, primary_key=True)\n    name = db.Column(db.String(80), nullable=False)\n\n@app.route('/')\ndef home():\n    users = User.query.all()\n    return render_template('home.html', users=users)\n\nif __name__ == '__main__':\n    db.create_all()\n    app.run(debug=True)",
            "readme": "# Exercise 4: Flask Database Integration\n\nIn this exercise, you will learn how to integrate a database with Flask. Follow the instructions to create a model, query the database, and display data in a template.",
        },
        {
            "name": "Exercise 5: Flask REST API",
            "python": "from flask import Flask, jsonify, request\n\napp = Flask(__name__)\n\nusers = []\n\n@app.route('/users', methods=['GET'])\ndef get_users():\n    return jsonify(users)\n\n@app.route('/users', methods=['POST'])\ndef add_user():\n    user = request.get_json()\n    users.append(user)\n    return jsonify(user), 201\n\nif __name__ == '__main__':\n    app.run(debug=True)",
            "readme": "# Exercise 5: Flask REST API\n\nIn this exercise, you will learn how to create a REST API with Flask. Follow the instructions to create endpoints for getting and adding users.",
        },
    ],
    "Week 21: Asynchronous Programming": [
        {
            "name": "Exercise 1: Asyncio Basics",
            "python": "import asyncio\n\nasync def say_hello():\n    print('Hello')\n    await asyncio.sleep(1)\n    print('World')\n\nasyncio.run(say_hello())",
            "readme": "# Exercise 1: Asyncio Basics\n\nIn this exercise, you will learn the basics of asynchronous programming with asyncio in Python. Follow the instructions to create and run an asynchronous function.",
        },
        {
            "name": "Exercise 2: Asyncio Tasks",
            "python": "import asyncio\n\nasync def say(message, delay):\n    await asyncio.sleep(delay)\n    print(message)\n\nasync def main():\n    task1 = asyncio.create_task(say('Hello', 1))\n    task2 = asyncio.create_task(say('World', 2))\n    await task1\n    await task2\n\nasyncio.run(main())",
            "readme": "# Exercise 2: Asyncio Tasks\n\nIn this exercise, you will learn how to work with asyncio tasks in Python. Follow the instructions to create and run multiple asynchronous tasks.",
        },
        {
            "name": "Exercise 3: Asyncio Gather",
            "python": "import asyncio\n\nasync def say(message, delay):\n    await asyncio.sleep(delay)\n    return message\n\nasync def main():\n    messages = await asyncio.gather(say('Hello', 1), say('World', 2))\n    for message in messages:\n        print(message)\n\nasyncio.run(main())",
            "readme": "# Exercise 3: Asyncio Gather\n\nIn this exercise, you will learn how to gather multiple asynchronous tasks in Python. Follow the instructions to run tasks concurrently and collect their results.",
        },
        {
            "name": "Exercise 4: Asyncio Queue",
            "python": "import asyncio\n\nasync def producer(queue, n):\n    for i in range(n):\n        await queue.put(i)\n        print(f'Produced {i}')\n\nasync def consumer(queue):\n    while True:\n        item = await queue.get()\n        if item is None:\n            break\n        print(f'Consumed {item}')\n        queue.task_done()\n\nasync def main():\n    queue = asyncio.Queue()\n    await asyncio.gather(producer(queue, 5), consumer(queue))\n    await queue.join()\n    await queue.put(None)\n\nasyncio.run(main())",
            "readme": "# Exercise 4: Asyncio Queue\n\nIn this exercise, you will learn how to use asyncio queues in Python. Follow the instructions to create a producer-consumer pattern using asyncio queues.",
        },
        {
            "name": "Exercise 5: Asyncio with HTTP Requests",
            "python": "import asyncio\nimport aiohttp\n\nasync def fetch(url):\n    async with aiohttp.ClientSession() as session:\n        async with session.get(url) as response:\n            return await response.text()\n\nasync def main():\n    urls = ['https://www.example.com', 'https://www.python.org', 'https://www.github.com']\n    tasks = [fetch(url) for url in urls]\n    responses = await asyncio.gather(*tasks)\n    for response in responses:\n        print(response)\n\nasyncio.run(main())",
            "readme": "# Exercise 5: Asyncio with HTTP Requests\n\nIn this exercise, you will learn how to make asynchronous HTTP requests in Python. Follow the instructions to fetch multiple URLs concurrently using aiohttp and asyncio.",
        },
    ],
    "Week 22: Advanced Object-Oriented Programming": [
        {
            "name": "Exercise 1: Class Methods",
            "python": "class MyClass:\n    class_variable = 'Hello'\n\n    @classmethod\n    def class_method(cls):\n        return cls.class_variable\n\nprint(MyClass.class_method())",
            "readme": "# Exercise 1: Class Methods\n\nIn this exercise, you will learn how to use class methods in Python. Follow the instructions to create a class method and access class variables.",
        },
        {
            "name": "Exercise 2: Static Methods",
            "python": "class MyClass:\n    @staticmethod\n    def static_method():\n        return 'Hello, World!'\n\nprint(MyClass.static_method())",
            "readme": "# Exercise 2: Static Methods\n\nIn this exercise, you will learn how to use static methods in Python. Follow the instructions to create a static method and call it without creating an instance of the class.",
        },
        {
            "name": "Exercise 3: Properties",
            "python": "class MyClass:\n    def __init__(self, value):\n        self._value = value\n\n    @property\n    def value(self):\n        return self._value\n\n    @value.setter\n    def value(self, value):\n        self._value = value\n\nobj = MyClass(10)\nprint(obj.value)\nobj.value = 20\nprint(obj.value)",
            "readme": "# Exercise 3: Properties\n\nIn this exercise, you will learn how to use properties in Python. Follow the instructions to create getter and setter methods using the @property decorator.",
        },
        {
            "name": "Exercise 4: Method Resolution Order",
            "python": "class A:\n    def greet(self):\n        return 'Hello from A'\n\nclass B(A):\n    def greet(self):\n        return 'Hello from B'\n\nclass C(A):\n    def greet(self):\n        return 'Hello from C'\n\nclass D(B, C):\n    pass\n\nobj = D()\nprint(obj.greet())\nprint(D.mro())",
            "readme": "# Exercise 4: Method Resolution Order\n\nIn this exercise, you will learn about the method resolution order (MRO) in Python. Follow the instructions to create a class hierarchy and understand the order in which methods are resolved.",
        },
        {
            "name": "Exercise 5: Metaclasses",
            "python": "class Meta(type):\n    def __new__(cls, name, bases, dct):\n        dct['class_name'] = name\n        return super().__new__(cls, name, bases, dct)\n\nclass MyClass(metaclass=Meta):\n    pass\n\nprint(MyClass.class_name)",
            "readme": "# Exercise 5: Metaclasses\n\nIn this exercise, you will learn about metaclasses in Python. Follow the instructions to create a metaclass and use it to modify class behavior.",
        },
    ],
    "Week 23: Design Patterns": [
        {
            "name": "Exercise 1: Singleton Pattern",
            "python": "class Singleton:\n    _instance = None\n\n    def __new__(cls, *args, **kwargs):\n        if not cls._instance:\n            cls._instance = super().__new__(cls, *args, **kwargs)\n        return cls._instance\n\nsingleton1 = Singleton()\nsingleton2 = Singleton()\nprint(singleton1 is singleton2)",
            "readme": "# Exercise 1: Singleton Pattern\n\nIn this exercise, you will learn how to implement the Singleton design pattern in Python. Follow the instructions to create a class that ensures only one instance is created.",
        },
        {
            "name": "Exercise 2: Factory Pattern",
            "python": "class Dog:\n    def speak(self):\n        return 'Woof!'\n\nclass Cat:\n    def speak(self):\n        return 'Meow!'\n\nclass AnimalFactory:\n    def create_animal(self, animal_type):\n        if animal_type == 'dog':\n            return Dog()\n        elif animal_type == 'cat':\n            return Cat()\n\nfactory = AnimalFactory()\nanimal = factory.create_animal('dog')\nprint(animal.speak())",
            "readme": "# Exercise 2: Factory Pattern\n\nIn this exercise, you will learn how to implement the Factory design pattern in Python. Follow the instructions to create a factory class that creates different types of animals.",
        },
        {
            "name": "Exercise 3: Observer Pattern",
            "python": "class Subject:\n    def __init__(self):\n        self._observers = []\n\n    def attach(self, observer):\n        self._observers.append(observer)\n\n    def detach(self, observer):\n        self._observers.remove(observer)\n\n    def notify(self, message):\n        for observer in self._observers:\n            observer.update(message)\n\nclass Observer:\n    def update(self, message):\n        pass\n\nclass ConcreteObserver(Observer):\n    def update(self, message):\n        print(f'Received message: {message}')\n\nsubject = Subject()\nobserver1 = ConcreteObserver()\nobserver2 = ConcreteObserver()\nsubject.attach(observer1)\nsubject.attach(observer2)\nsubject.notify('Hello, Observers!')",
            "readme": "# Exercise 3: Observer Pattern\n\nIn this exercise, you will learn how to implement the Observer design pattern in Python. Follow the instructions to create a subject and attach observers that receive notifications.",
        },
        {
            "name": "Exercise 4: Strategy Pattern",
            "python": "class Strategy:\n    def execute(self, a, b):\n        pass\n\nclass AddStrategy(Strategy):\n    def execute(self, a, b):\n        return a + b\n\nclass SubtractStrategy(Strategy):\n    def execute(self, a, b):\n        return a - b\n\nclass Context:\n    def __init__(self, strategy):\n        self._strategy = strategy\n\n    def set_strategy(self, strategy):\n        self._strategy = strategy\n\n    def execute_strategy(self, a, b):\n        return self._strategy.execute(a, b)\n\ncontext = Context(AddStrategy())\nprint(context.execute_strategy(3, 4))\ncontext.set_strategy(SubtractStrategy())\nprint(context.execute_strategy(3, 4))",
            "readme": "# Exercise 4: Strategy Pattern\n\nIn this exercise, you will learn how to implement the Strategy design pattern in Python. Follow the instructions to create strategies for different operations and use them in a context.",
        },
        {
            "name": "Exercise 5: Decorator Pattern",
            "python": "class Coffee:\n    def cost(self):\n        return 5\n\nclass MilkDecorator(Coffee):\n    def __init__(self, coffee):\n        self._coffee = coffee\n\n    def cost(self):\n        return self._coffee.cost() + 1\n\nclass SugarDecorator(Coffee):\n    def __init__(self, coffee):\n        self._coffee = coffee\n\n    def cost(self):\n        return self._coffee.cost() + 0.5\n\ncoffee = Coffee()\nmilk_coffee = MilkDecorator(coffee)\nsugar_milk_coffee = SugarDecorator(milk_coffee)\nprint(sugar_milk_coffee.cost())",
            "readme": "# Exercise 5: Decorator Pattern\n\nIn this exercise, you will learn how to implement the Decorator design pattern in Python. Follow the instructions to create decorators that add functionality to a coffee object.",
        },
    ],
    "Week 24: Advanced Web Development with Django": [
        {
            "name": "Exercise 1: Setting Up Django",
            "python": "import os\nos.system('django-admin startproject myproject')\nos.chdir('myproject')\nos.system('python manage.py startapp myapp')",
            "readme": "# Exercise 1: Setting Up Django\n\nIn this exercise, you will learn how to set up a new Django project and app. Follow the instructions to create a project and an app using Django's command-line tools.",
        },
        {
            "name": "Exercise 2: Django Models",
            "python": "from django.db import models\n\nclass User(models.Model):\n    name = models.CharField(max_length=100)\n    email = models.EmailField(unique=True)\n\n    def __str__(self):\n        return self.name\n\n# In settings.py, add 'myapp' to INSTALLED_APPS\n\n# Run migrations\nos.system('python manage.py makemigrations')\nos.system('python manage.py migrate')",
            "readme": "# Exercise 2: Django Models\n\nIn this exercise, you will learn how to define models in Django. Follow the instructions to create a User model, add it to INSTALLED_APPS, and run migrations.",
        },
        {
            "name": "Exercise 3: Django Views",
            "python": "from django.http import HttpResponse\n\n# In myapp/views.py\n\ndef home(request):\n    return HttpResponse('Hello, Django!')\n\n# In myapp/urls.py\nfrom django.urls import path\nfrom .views import home\nurlpatterns = [\n    path('', home),\n]\n\n# In myproject/urls.py\nfrom django.urls import include\nurlpatterns = [\n    path('', include('myapp.urls')),\n]",
            "readme": "# Exercise 3: Django Views\n\nIn this exercise, you will learn how to create views in Django. Follow the instructions to create a simple view that returns an HTTP response and configure the URLs.",
        },
        {
            "name": "Exercise 4: Django Templates",
            "python": "{% raw %}{% extends 'base.html' %}\n{% block content %}\n    <h1>Hello, Django!</h1>\n{% endblock %}{% endraw %}\n\n# In myapp/views.py\nfrom django.shortcuts import render\n\ndef home(request):\n    return render(request, 'home.html')\n\n# In settings.py, add 'DIRS': [os.path.join(BASE_DIR, 'templates')] to TEMPLATES\n\n# Create templates directory and base.html",
            "readme": "# Exercise 4: Django Templates\n\nIn this exercise, you will learn how to use templates in Django. Follow the instructions to create a base template and extend it in a view-specific template.",
        },
        {
            "name": "Exercise 5: Django Forms",
            "python": "from django import forms\nfrom django.shortcuts import render\nfrom django.http import HttpResponseRedirect\n\nclass NameForm(forms.Form):\n    name = forms.CharField(label='Your name', max_length=100)\n\n# In myapp/views.py\n\ndef get_name(request):\n    if request.method == 'POST':\n        form = NameForm(request.POST)\n        if form.is_valid():\n            return HttpResponseRedirect('/thanks/')\n    else:\n        form = NameForm()\n    return render(request, 'name.html', {'form': form})\n\n# In myapp/urls.py\nurlpatterns = [\n    path('name/', get_name),\n]",
            "readme": "# Exercise 5: Django Forms\n\nIn this exercise, you will learn how to use forms in Django. Follow the instructions to create a form, handle form submissions, and render the form in a template.",
        },
    ],
}
