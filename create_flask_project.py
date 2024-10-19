import os
import shutil
import stat

def set_permissions_recursively(path):
    for root, dirs, files in os.walk(path):
        for dir_name in dirs:
            os.chmod(os.path.join(root, dir_name), stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
        for file_name in files:
            os.chmod(os.path.join(root, file_name), stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)

def create_flask_project():
    project_name = input("Enter your project name: ")
    try:
        os.makedirs(f"{project_name}/app/static/css")
        os.makedirs(f"{project_name}/app/static/js")
        os.makedirs(f"{project_name}/app/templates")
        
        with open(f"{project_name}/app/__init__.py", 'w') as f:
            f.write('''from flask import Flask\n\napp = Flask(__name__)\n\nfrom app import routes\n''')
        
        with open(f"{project_name}/app/routes.py", 'w') as f:
            f.write('''from app import app\n\n@app.route('/')\ndef home():\n    return "Hello, Flask!"\n''')
        
        with open(f"{project_name}/run.py", 'w') as f:
            f.write('''from app import app\n\nif __name__ == "__main__":\n    app.run(debug=True)\n''')
        
        with open(f"{project_name}/config.py", 'w') as f:
            f.write('')  # Empty file
        
        with open(f"{project_name}/README.md", 'w') as f:
            f.write(f'''# {project_name}\n\nThis is the {project_name} Flask application.''')
        
        with open(f"{project_name}/.gitignore", 'w') as f:
            f.write('venv/\n__pycache__/\ninstance/\n.webassets-cache\n')

        print(f"Flask project '{project_name}' created successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if os.path.exists("FlaskTemplate"):
            set_permissions_recursively("FlaskTemplate")
            shutil.rmtree("FlaskTemplate")
            print("FlaskTemplate folder deleted successfully!")

create_flask_project()
