import urllib.request as net

image_address='https://i.pinimg.com/474x/c5/20/a5/c520a593cd92539ccde694ae817677f5--christmas-balls-family-christmas.jpg'

try:
    net.urlretrieve(image_address,"Klaus.jpeg")
    print("Downloaded successfully")
except:
    print('Image not found')
