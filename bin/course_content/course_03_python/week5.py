course_content = {
    "title": "week05 - modules and packages",
    "content": [
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
}
