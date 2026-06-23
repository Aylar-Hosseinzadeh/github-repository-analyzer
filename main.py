
print("========================= \nGitHub Repository Analyzer\n=========================")
 
 from github_api import fetch_repository_data

def validate_url(url):
    return url.startswith("https://github.com/")
      

def normalize_url(url):
    if url.endswith("/"):
        return url[:-1]
    return url

def extract_owner_repo(url):
    parts = url.split("/")
    owner = parts[3]
    repo = parts[4]
    return owner , repo

def build_api_url(owner, repo):
    return f"https://api.github.com/{owner}/{repo}"
   
# --- main flow ---

url = input("ENTER URL: ")

if not validate_url(url):
    print("Invalid GitHub URL.")
    exit()

owner , repo = extract_owner_repo(url)

api_url = build_api_url(owner , repo)

data = fetch_repository_data(api_url)

if data:
    if data:
    print("\nRepository Info")
    print("----------------")
    print("Name:", data["name"])
    print("Stars:", data["stargazers_count"])
    print("Forks:", data["forks_count"])
    print("Language:", data["language"])
else:
    print("Failed to fetch repository data.")














    







        




