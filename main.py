# Import the requests
import requests
api = "https://api.windy.com/api/webcams/v2/list/country=JP/category=beach?show=webcams:url"

header = {
    'x-windy-key': "hqBLppeg5XtzL0f88L7IhJPjWVdpR7w6"
}
response = requests.get(url=api, headers=header)

print(response.json())
