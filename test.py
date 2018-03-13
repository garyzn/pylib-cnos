import sys
from connect import *
import time
from system import *


if __name__ == '__main__':
    params = dict()
    params['transport'] = 'https'
    params['port'] = '443'
    params['ip'] = '10.240.177.152'
    params['user'] = 'admin'
    params['password'] = 'admin'
    conn = Connection(params)

    system=System()
    print system.get_hostname(conn)

#time.sleep(8)
