import requests

class Photo:
    def __init__(self, albumId=0, id=0, title='', url='', thumbnailUrl=''):
        self.albumId = albumId
        self.id = id
        self.title = title
        self.url = url
        self.thumbnailUrl = thumbnailUrl

    def __repr__(self):
        return f'(albumId:{self.albumId}, id:{self.id}, title:{self.title}, url:{self.url})'


url = 'https://jsonplaceholder.typicode.com/photos'

response = requests.get(url)
photos = []
for p in response.json():
    photos.append(Photo(**p))
# print(response.json()[0])
# print(photos)
for p in photos:
    print(p)