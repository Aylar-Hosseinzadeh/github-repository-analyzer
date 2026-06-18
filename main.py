
print("========================= \nGitHub Repository Analyzer\n=========================")

# get the repository url from  the client 

def validate_url(url):
    return url.startswith("https://github.com/")
      
url = input("ENTER URL: ")

if validate_url(url):
    print("valid")
else:
    print("invalid")








        




