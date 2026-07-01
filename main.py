
print("========================= \nGitHub Repository Analyzer\n=========================")


from github_api import fetch_repository_data , fetch_contributors

from utils import (validate_url , extract_owner_repo , normalize_url , build_api_url)

from report import show_repository_report , show_contributors_report
   
# --- main flow ---

url = input("ENTER URL: ")

if not validate_url(url):
    print("Invalid GitHub URL.")
    exit()

owner , repo = extract_owner_repo(url)

api_url = build_api_url(owner , repo)

data = fetch_repository_data(api_url)

contributors_data  = fetch_contributors(owner , repo)

if data:
    show_repository_report(data)
else:
    print("Failed to fetch repository data.")

if contributors_data:
    show_contributors_report(contributors_data)
else:
    print("No contributors found.")













    







        




