import os
import flickr_api as flickr
import requests

flickr.auth.keys.API_KEY = '26b13d51dba44b795d8cf292599a6e6b'
flickr.auth.keys.API_SECRET = 'c7f66d655eff5f61'

birds = flickr.Photo.search(tags='pigeon', per_page=100, page=1)

for bird in birds:
    for fname in os.listdir('.'):
        if fname.startswith('photo_' + bird.id):
            print('We already have this photo, skip it')
            break
        else:
            photoInfo = bird.getSizes()
            print(photoInfo)
            if 'Large' in photoInfo:
                img_data = requests.get(photoInfo['Large']['source']).content
                with open('photo_' + bird.id + '.jpg', 'wb') as handler:
                    handler.write(img_data)
            break
