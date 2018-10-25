import requests

page = requests.get("https://www.instagram.com/explore/tags/amor/")
page.encoding = 'ISO-8859-1'
print(page.encoding)
