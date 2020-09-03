import getmac
import subprocess
def auth():
    global mac, hwid
    try:
        if sys.platform.startswith("linux"):
            mac = subprocess.Popen("getmac", shell=True,stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
            useragent = {'User-Agent':'QVHKKDNMXLAMEK2NEMXKSKEL3PKKKM52MMNNBFDDWQWJKLNBVCXCVBN32CSD'}
            r = requests.get('urlhere',headers=useragent)
            if mac in r.text:
                    pass
                    print(f"{bcolors.OKGREEN}You are logged with: {mac}")
            else:
                    print(f'{bcolors.RED}[ERROR] MAC Not in database')
                    print(f'{bcolors.RED}MAC: {mac}') 
                    time.sleep(999999999)
                    sys.exit()
        else:
            hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
            useragent = {'User-Agent':'QVHKKDNMXLAMEK2NEMXKSKEL3PKKKM52MMNNBFDDWQWJKLNBVCXCVBN32CSD'}
            r = requests.get('urlhere',headers=useragent)
            if hwid in r.text:
                    pass
                    print(f"{bcolors.OKGREEN}You are logged with: {hwid}")
            else:
                    print(f'{bcolors.RED}[ERROR] HWID Not in database')
                    print(f'{bcolors.RED}HWID: {hwid}') 
                    time.sleep(999999)
                    sys.exit()
    except:
                print(f'{bcolors.RED}[ERROR] No internet connection')      
                time.sleep(999999)