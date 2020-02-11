import dns.resolver
from time import *
import threading
#  本程序需要输入例如baidu.com的域名，然后会遍历字典进行组合，连接，返回IP并创建txt写入

class Thread(threading.Thread):
    def __init__(self, name, line):
        threading.Thread.__init__(self)
        self.name = name
        self.line = line

    def run(self):
        try:
            Connection(self.name, self.line)
        except RuntimeError:
            sleep(0.1)
            run(self)


def Wait(line, name):
    sleep(0.1)
    t = Thread(line, name)
    try:
        t.start()
    except RuntimeError:
        Wait(line, name)


def get_ip(domain):
    try:
        time1 = time()
        A = dns.resolver.query(domain, 'A')
        while 1:
            time2 = time()
            pasttime = time2 - time1
            if pasttime > 1:
                break
        for i in A.response.answer:
            for I in i:
                if I.rdtype == 1:
                    e = domain + ':' + str(I)
                    writeResult(e)
                    break
    except dns.resolver.NoAnswer:
        pass
    except dns.resolver.NXDOMAIN:
        pass
    except dns.exception.Timeout:
        pass
    except dns.resolver.NoNameservers:
        pass


def Connection(name, line):
    domain = str(line.strip("\n")) + '.' + name
    get_ip(domain)


def writeResult(e):  # 把结果写入txt
    with open('子域名.txt', "a+", encoding='utf-8') as f:
        f.write(e)
        f.write('\n')
        f.close()


def work(name):
    for line in open("./1.txt"):  # 从1.txt中拿一个字符串出来与输入的域名组合进行测试
        if threading.active_count() < 1000:
            t = Thread(name, line)
            t.start()
        else:
            Wait(line, name)


def main():
    begin_time = time()
    name = input("请输入要查询的域名(例如：baidu.com)：")
    work(name)
    while 1:
        if threading.active_count() == 1:
            end_time = time()
            run_time = end_time - begin_time
            print('耗时：', '%.1f' % run_time)
            break


if __name__ == '__main__':
    main()
