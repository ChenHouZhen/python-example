import requests

proxies = {
    "https": "socks5://root:123456@localhost:8080",
    "http": "socks5://root:123456@localhost:8080"
}
store_path = ''


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
    i_file_set = read_file('E:\\training\py\\tumblr-spiber\\pictures.txt')
    print("链接数：%i" % len(i_file_set))
    for url in i_file_set:
        path_list = url.rsplit("/", 1)
        image_name = path_list[1]
        print("图片名称：%s" % image_name)
        file_path = store_path + '/' + image_name
        download(url, file_path)

