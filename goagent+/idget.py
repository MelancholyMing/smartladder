# Copyright 2013 kirito and all WoW Browser Authors
# A python script to get appid generated on Server
import urllib.request, urllib.parse, urllib.error
import base64
import random

def get_appids():
    fly = bytes.maketrans(
    b"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
    b"nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"
    )
    f = urllib.request.urlopen(url="http://idupd.sdapp.cn/v").read().translate(fly)
    d = base64.b64decode(f)
    e = str(d, encoding='ascii').split('\r\n')
    random.shuffle(e)
    return  e

if __name__ == '__main__':
    appids=get_appids()
    print(appids)
