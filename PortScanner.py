# -*- coding: utf-8 -*-
# Version: 1.0
from socket import *
import threading

lock = threading.Lock()
openNum = 0
threads = []


def get_ip(url):
    if 'http' in url or 'https' in url:
        url = url.split('//')
        url = url[len(url) - 1].rsplit('/')[0]
        print('[*]', url)
    try:
        return gethostbyname(url)
    except:
        print('wrong address!')
        exit(0)


def port_scanner(host, port):
    global openNum
    try:
        s = socket(AF_INET, SOCK_STREAM)
        s.connect((host, port))
        lock.acquire()
        openNum += 1
        print('[+] %d open' % port)
        lock.release()
        s.close()
    except:
        pass


def main():
    ip = get_ip(input('please input the address of website(url):'))
    print('[*]', ip, '\n------------------------')
    setdefaulttimeout(1)
    for p in range(1, 10000):
        t = threading.Thread(target=port_scanner, args=(ip, p))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print('------------------------\n[*] complete! A total of %d open port ' % (openNum))


if __name__ == '__main__':
    main()
