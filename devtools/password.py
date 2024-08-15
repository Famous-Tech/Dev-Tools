def check_password(project, password):
    return project['settings']['password'] == password

def prompt_password(project):
    password = input(f"Enter password for project '{project['name']}': ")
    return password
