

def show_repository_report(data):
    name = data["name"]
    stars = data["stargazers_count"]
    forks = data["forks_count"]
    language = data["language"]
    description = data["description"]
    open_issues = data["open_issues_count"]
    default_branch = data["default_branch"]

    if data["license"] :
        license_name = data["license"]["name"]
    else:
        license_name = "No license"

    print(f"name : {name}")
    print(f"description : {description}")
    print(f"language : {language}")
    print(f"stars : {stars}")
    print(f"forks : {forks}")
    print(f"open issues : {open_issues}")
    print(f"default branch : {default_branch}")
    print(f"license : {license_name}")


    




