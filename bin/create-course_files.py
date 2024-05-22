#!/usr/bin/env python

import os
import zipfile

# from course_content.course_02_javascript import course_content
# from course_content.course_10_bootstrap import course_content
# from course_content.course_11_tailwindcss import course_content
from course_content.course_03_python import course_content

# ROOT = "02_javascript"
ROOT = "03_python"
# ROOT = "10_bootstrap"
# ROOT = "11_tailwindcss"


def create_zipfile(week):
    # Create a zip file for the week
    zip_filename = f"{week}_JavaScript_Course.zip"
    with zipfile.ZipFile(zip_filename, "w") as zipf:
        for foldername, _, filenames in os.walk(week):
            for filename in filenames:
                filepath = os.path.join(foldername, filename)
                zipf.write(filepath, os.path.relpath(filepath, week))


# Function to create files and zip them
def create_week_files(folder, html, css, js, readme, python):
    if html is not None:
        with open(os.path.join(folder, "index.html"), "w") as html_file:
            html_file.write(html.strip())

    if css is not None:
        with open(os.path.join(folder, "styles.css"), "w") as js_file:
            js_file.write(js.strip())

    if js is not None:
        with open(os.path.join(folder, "script.js"), "w") as js_file:
            js_file.write(js.strip())

    if python is not None:
        with open(os.path.join(folder, "exercise.py"), "w") as js_file:
            js_file.write(python.strip())

    # Write README file
    with open(os.path.join(folder, "README.md"), "w") as readme_file:
        readme_file.write(readme.strip())


def save_foldername(foldername: str):
    return foldername.replace(":", " -")


def create_course_files(course_content):
    for title in course_content.keys():
        for exercise in course_content[title]:
            exercise_name = exercise["name"]

            exercise_dir = save_foldername(
                os.path.join(ROOT, title, exercise_name, "exercise")
            )
            os.makedirs(exercise_dir, exist_ok=True)

            create_week_files(
                exercise_dir, None, None, None, exercise["readme"], python=None
            )

            solution_dir = save_foldername(
                os.path.join(ROOT, title, exercise_name, "solution")
            )
            os.makedirs(solution_dir, exist_ok=True)

            html = exercise["html"] if "html" in exercise else None
            js = exercise["js"] if "js" in exercise else None
            css = exercise["css"] if "css" in exercise else None
            python = exercise["python"] if "python" in exercise else None

            print(f"create {solution_dir}")

            create_week_files(
                solution_dir, html, css, js, exercise["readme"], python=python
            )


# Call the function to create the course files and zip them
create_course_files(course_content)
