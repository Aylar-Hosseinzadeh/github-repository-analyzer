
print("========================= \nGitHub Repository Analyzer\n=========================")

# get the repository url from  the client 

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


url = input("ENTER URL: ")

if not validate_url(url):
    print("Invalid GitHub URL.")
    exit()

owner , repo = extract_owner_repo(url)
print(f"owner: {owner} and repo: {repo}")














    







        




