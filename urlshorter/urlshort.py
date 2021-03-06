from .models import Url

ALPHABET = "abcdefghijklmnopqrstuvwxuzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
BASE = 62

def add_shorted_url(long_url):
    if long_url == "":
        return None
    else:
        try:
            url_obj = Url.objects.get(URL=long_url)
            return url_obj.Code
        except:
            add_url = Url(URL=long_url, Code="")
            add_url.save()
            add_url.Code = "http://127.0.0.1:8000/" + encode(add_url.id)
            add_url.save()
            return add_url.Code

def encode(num):
    sb = ""
    while num > 0:
        sb += ALPHABET[(num % BASE)]
        num = int(num / BASE)

    builder = ""
    for i in range(len(sb)):
        builder = sb[i] + builder

    return builder


def decode(str):
    num = 0
    for i in range(len(str)):
        num = num * BASE + ALPHABET.index(str[i])

    return num

