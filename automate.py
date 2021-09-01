import requests

response = requests.get("https://www.flickr.com/services/rest/?method=flickr.photos.getPopular&api_key=abf9b6623439818dd01aa90c58db80e5&user_id=193835380%40N06&format=json&nojsoncallback=1")

print(response.json())
print(response.status_code)
