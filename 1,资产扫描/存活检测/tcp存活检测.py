from socket import *
import requests
import urllib.request
import threading
import os
class myThread (threading.Thread):
    def __init__(self, port):
        threading.Thread.__init__(self)
        self.port = port
    def run(self):
        try:
            tcp(self.port)
        except RuntimeError:
            sleep(0.1)
            run(self)
def FindIp(IP):  # 如果输入的是域名就会有一个转换为ip的过程
    url = 'http://' + IP
    r = requests.get(url, headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'})
    if r.status_code == 200:
        try:
            ss = urllib.request.urlopen(url)
            result = getaddrinfo(IP, None)
            IP = result[0][4][0]
            ss.close()
        except urllib.error.URLError:
            print('转换ip失败')
            os._exit(1)

def Input():
    IP = input('请输入一个域名(例如www.baidu.com)或ipv4地址:')
    if IP.count('.') == 2:
        FindIp(IP)
    elif IP.count('.') != 3:
        print('请确认是否输入了符合要求的域名或ipv4地址')
        tcp()
    return IP


def work():
    for i in range(1, 65536):
        if threading.active_count() < 1000:
            t = myThread(i)
            t.start()
        else:
            Wait(i)

def Wait(i):
    sleep(0.1)
    t = myThread(i)
    try:
        t.start()
    except RuntimeError:
        Wait(i)


def tcp(port):
    Address = (IP, port)
    s = socket(AF_INET, SOCK_STREAM, )
    try:
        s.connect(Address)
        s.close()
        print('主机存活')
        os._exit(1)
    except TimeoutError and timeout and OSError:
        pass


if __name__ == '__main__':
    IP = Input()
    setdefaulttimeout(3)
    work()
