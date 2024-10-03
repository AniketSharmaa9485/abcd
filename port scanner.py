from socket import *
def conScan(tgthost , tgtPort):
    try:
        connskt = socket(AF_INET, SOCK_STREAM)
        connskt.connect((tgthost, tgtPort))
        print('[+]%d/tcp open'% tgtPort)
        connskt.close()
    except:
        print('[+]%d/tcp closed' % tgtPort)

def portScan(tgthost, tgtPort):
    try:
        tgtIP = gethostbyname(tgthost)
    except:
        print('[-]cannot resolve %s ' % tgthost)
        return
    try:
        tgtName = gethostbyaddr(tgtIP)
        print('\n[+] scan result of : %s ' % tgtName[0])
    except:
        print('\n[+] Scan  result of: %s' % tgtIP)
    setdefaulttimeout(1)
    for tgtPort in tgtPort:
        print('Scanning Port:  %d'%  tgtPort)
        conScan(tgthost,int(tgtPort))

if __name__ == '__main__':
    portScan('google.com',[80,22])

