import requests
from requests import ConnectionError

proxies = {
    "https": "https://127.0.0.1:1080",
    "http": "http://127.0.0.1:1080"
}
store_path = 'F:/迅雷下载/images'
images_url_file_path = 'E:\\project\\py\\tumblr-spider\\pictures.txt'


def download(url, store_file):
    r = requests.get(url, proxies=proxies)
    with open(store_file, 'wb') as f:
        f.write(r.content)


def read_file(file_path):
    file_set = set()
    for line in open(file_path):
        file_set.add(line)

    return file_set


if __name__ == '__main__':
    i_file_set = read_file(images_url_file_path)
    print("链接数：%i" % len(i_file_set))
    for url in i_file_set:
        print("正在下载。%s" % url)
        path_list = url.rsplit("/", 1)
        image_name = path_list[1].strip()
        print("图片名称：%s" % image_name)
        file_path = store_path + '/' + image_name
        try:
            download(url, file_path)
        except (TimeoutError, ConnectionError):
            print("出错：%s" % url)
