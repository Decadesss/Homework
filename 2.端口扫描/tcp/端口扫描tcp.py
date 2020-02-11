from socket import *
from time import *
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
    s = socket(AF_INET, SOCK_STREAM)
    try:
        s.connect(Address)
        s.close()
        print('端口(', port, ')开放中', sep='', end='')
        try:
            print('--->协议:', Agreetment[port])
        except:
            pass
    except TimeoutError and timeout and OSError:
        pass


if __name__ == '__main__':
    Agreetment = {20: 'ftp-data', 21: 'ftp', 23: 'telnet',
                  25: 'smtp', 37: 'time', 53: 'domain',
                  70: 'gopher', 80: 'http', 110: 'pop3',
                  119: 'nntp', 137: 'netbios-ns', 139: 'netbios-ssn',
                  143: 'imap', 194: 'irc', 389: 'ldap',
                  443: 'https', 540: 'uucp', 636: 'ldaps', 666: 'doom',
                  1433: 'ms-sql-s', 1434: 'ms-sql-m', 1512: 'wins',
                  1720: '12tp'}
    IP = Input()
    setdefaulttimeout(0.1)
    begin_time = time()
    work()
    end_time = time()
    time = end_time - begin_time
    print('耗时：', '%.1f'%time)
