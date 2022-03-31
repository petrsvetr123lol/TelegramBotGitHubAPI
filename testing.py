import requests
import json
response_API = requests.get('https://api.github.com/repos/petrsvetr123lol/TestingRepo/commits/main')
data = response_API.text
parse_json = json.loads(data)
latest_commit = parse_json['html_url']
message = parse_json['commit']['message']
print("Latest commit:", latest_commit, message)
