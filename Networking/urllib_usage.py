from urllib import request,error

try:
    url=request.urlopen("https://myanimelist.net/")
    content=url.read()
except error.HTTPError:
    print("Page not found")
    exit()

f=open("mal.html","wb")
f.write(content)
f.close()
