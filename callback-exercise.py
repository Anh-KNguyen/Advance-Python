import urllib.request

def downloadFromWeb(url, cb = None):
    rsp = urllib.request.urlopen(url)
    data = rsp.read()
    print('successfully downloaded', url)
    if cb is not None:
        cb(data)

def callback(data) -> None:
    print(data)


# callback function that prints the data downloaded from the url
downloadFromWeb("https://google.com", callback) 
