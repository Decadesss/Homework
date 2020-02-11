# coding=utf-8
import requests
from time import *
import socket
import urllib.request
import threading
#  本程序需要输入例如baidu.com的域名，然后会遍历字典进行组合，连接，返回IP并创建txt写入

class myThread(threading.Thread):
    def __init__(self, domain_name, Agreement, line):
        threading.Thread.__init__(self)
        self.domain_name = domain_name
        self.Agreement = Agreement
        self.line = line

    def run(self):
        try:
            Connection(self.domain_name, self.Agreement, self.line)
        except RuntimeError:
            sleep(0.1)
            run(self)


def Wait(line, domain_name, Agreement):
    sleep(0.1)
    t = myThread(line, domain_name, Agreement)
    try:
        t.start()
    except RuntimeError:
        Wait(line, domain_name, Agreement)


def work(domain_name, Agreement):
    for line in open("./1.txt"):  # 从1.txt中拿一个字符串出来与输入的域名组合进行测试
        if threading.active_count() < 2000:
            t = myThread(domain_name, Agreement, line)
            t.start()
        else:
            Wait(line, domain_name, Agreement)


def get_ip(url, Url, get):
    s = urllib.request.urlopen(url)
    result = socket.getaddrinfo(Url, None)
    ip = Url + ':' + result[0][4][0]
    writeResult(ip)
    # print(ip)  如果不想生成记事本，就取消改行注释，删除上一行代码。
    get.close()


def Connection(domain_name, Agreement, line):
    a = str(line.strip("\n"))
    Url = a + '.' + domain_name
    url = Agreement + Url
    try:  # 尝试进行连接并获取ip
        kv ={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
        get = requests.get(url, headers=kv, timeout=10)
        if get.status_code == 200:  # 如果连接上了就获取ip
            try:
                get_ip(url, Url, get)
            except urllib.error.URLError:
                ip = Url + ':' + '请求超时'
                writeResult(ip)
    except:
        pass


def writeResult(ip):  # 把结果写入txt
    with open('子域名.txt', "a+", encoding='utf-8') as f:
        f.write(ip)
        f.write('\n')
        f.close()


def main():
    socket.setdefaulttimeout(1)  # 连接时最长等待时间，可以改成1秒或者0.1秒
    begin_time = time()
    domain_name = input("请输入要查询的域名(例如：baidu.com)：")
    Agreement = 'http' + '://'
    work(domain_name, Agreement)
    while 1:
        print('\r', threading.active_count(), sep='', end="")
        if threading.active_count() < 5:
            end_time = time()
            run_time = end_time - begin_time
            print('耗时：', '%.1f' % run_time)
            break


if __name__ == '__main__':
    main()
