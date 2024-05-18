course_content = {
    "title": "week07 - error handling",
    "content": [
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
}
