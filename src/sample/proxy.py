import requests

socks5_remote_proxies = {
    "https": "socks5h://root:123456@192.243.116.107:8080",
    "http": "socks5h://root:123456@192.243.116.107:8080"
}

socks5_local_proxies = {
    "https": "socks5://127.0.0.1:1080",
    "http": "socks5://127.0.0.1:1080"
}

http_proxies = {
    "https": "https://127.0.0.1:1080",
    "http": "http://127.0.0.1:1080"
}


baidu = 'https://www.baidu.com/'

google = 'https://www.google.com/'

if __name__ == '__main__':
    res = requests.get(google, proxies=socks5_remote_proxies)
    print(res.content)


