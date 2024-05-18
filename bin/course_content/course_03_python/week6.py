course_content = {
    "title": "week06 - file handling",
    "content": [
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
}
