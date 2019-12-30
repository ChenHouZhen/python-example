import requests

# 测试结果
# socks5_remote_proxies 、socks5_local_proxies 两个代理可以获取 baidu 数据而无法获取 google 数据
# http_proxies 代理既可以获取 baidu 也可以获取 google
# 为什么？

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


