#!/usr/bin/env python

import sys
from ollama import Client

def log(line):
    print(f"LOG: {line}")

#--------------------------------------------------------------------------------------------------
host="ubuntu"

if len(sys.argv) == 1:
  print("Missing topic")
  sys.exit()


topic=sys.argv[1]

ollama = Client(host=host)

prompt="Why is the sky blue?"
prompt=f"""
The topic is '{topic}'.
""" + """
Create a course for this topic that consists of 3 parts with 20 chapters each.
- Part One   with Chapter 01-20 covers the basic elements of the topic, syntax and language elements.
- Part Two   with Chapter 21-40 covers the patterns, components and framework basics.
- Part Three with Chapter 41-60 covers best practices, features, and tips and tricks.

The final course contains content for 60 weeks.
The level for the weeks should range from beginner to advanced to expert level.

Create the table of content with all parts and chapters, structured in part, chapter, topic.
"""

prompt_content="""
Then, for each of topic of the table of content, create a Python dictionary that contains all of the created content for that week.
- each week cover a specific topic and contain 5 examples with solutions.
- each example contains the code required to run the example and a README.md file in Markdown that describes the exercise.

Finale, you create dictonaries for week01 - week60.

Show only the dictonary for the week and no additional output.

The dictionary for each week should have this structure:
course_content = {
    '<WEEK>': [
        {
            "name": <NAME OF EXERCISE>,
            "html": <HTML CODE>,
            "css": <CSS CODE>,
            "js": <JAVASCRIPT CODE>,
            "code": <PROGRAM CODE>
            "readme": <README.md>
        },
    ]
}
"""

response = ollama.chat(model='llama3', messages=[
  {
    'role': 'user',
    'content': prompt,
  },
])

print(response['message']['content'])
