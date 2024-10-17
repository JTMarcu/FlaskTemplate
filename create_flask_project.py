import os

def create_flask_project():
    project_name = input("Enter your project name: ")
    try:
        os.makedirs(f"{project_name}/app/static/css")
        os.makedirs(f"{project_name}/app/static/js")
        os.makedirs(f"{project_name}/app/templates")

        open(f"{project_name}/app/__init__.py", 'a').close()
        open(f"{project_name}/app/routes.py", 'a').close()
        open(f"{project_name}/app/models.py", 'a').close()
        open(f"{project_name}/config.py", 'a').close()
        open(f"{project_name}/run.py", 'a').close()
        open(f"{project_name}/README.md", 'a').close()
        open(f"{project_name}/.gitignore", 'a').close()
        
        print(f"Flask project '{project_name}' created successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

create_flask_project()
