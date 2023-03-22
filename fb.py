
import facebook 
import requests
from dotenv import load_dotenv
import os

load_dotenv()

graph = facebook.GraphAPI(os.getenv('USER_ACCESS_FACEBOOK_TOKEN'))

#api-end
url = f"https://graph.facebook.com/zarzadzanieagh/feed?fields=comments.limit(1).summary(true),likes.limit(1).summary(true)&access_token={os.getenv('APP_FACEBOOK_TOKEN')}"
output = requests.get(url).json()
print(output)

# To work it requires Page Public Content Access and for that it is necessary to contact facebook