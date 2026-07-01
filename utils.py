
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
    return f"https://api.github.com/repos/{owner}/{repo}"

