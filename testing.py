import requests


response = requests.get("https://api.github.com/repos/petrsvetr123lol/TestingRepo/commits/main")
print(response.content)