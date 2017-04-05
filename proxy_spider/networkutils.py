# coding:utf-8

import socket
from settings import SCAN_TIMEOUT


def scan(ip, port):
    """
    代理扫描器
    """
    s = socket.socket()
    s.settimeout(SCAN_TIMEOUT)
    if s.connect_ex((ip, port)) == 0:
        s.close()
        return True
    else:
        s.close()
        return False
