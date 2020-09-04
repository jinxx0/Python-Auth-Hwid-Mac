import getmac
import sys
import time
import requests
import subprocess

class colors:
    OKGREEN = '\033[92m'
    RED = '\033[1;31;48m'

def auth():
    global mac, hwid
    try:
        if sys.platform.startswith("linux"):
            mac = subprocess.Popen("getmac", shell=True,stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
            useragent = {'User-Agent':'Python3 Auth System - Linux'}
            r = requests.get('https://lilcsz.ml/gdj63acjbvge3s1aax',headers=useragent)
            if mac in r.text:
                    pass
                    print(f"{colors.OKGREEN}You are logged with: {mac}")
            else:
                    print(f'{colors.RED}[ERROR] MAC Not in database')
                    print(f'{colors.RED}MAC: {mac}') 
                    time.sleep(999999999)
                    time.sleep(999999999)
                    time.sleep(999999999)
                    time.sleep(999999999)
                    time.sleep(999999999)
                    sys.exit()
        else:
            hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
            useragent = {'User-Agent':'Python3 Auth System - Windows'}
            r = requests.get('https://lilcsz.ml/gdj63acjbvge3s1aax',headers=useragent)
            if hwid in r.text:
                    pass
                    print(f"{colors.OKGREEN}You are logged with: {hwid}")
            else:
                    print(f'{colors.RED}[ERROR] HWID Not in database')
                    print(f'{colors.RED}HWID: {hwid}') 
                    time.sleep(999999)
                    time.sleep(999999)
                    time.sleep(999999)
                    time.sleep(999999)
                    time.sleep(999999)
                    time.sleep(999999)
                    time.sleep(999999)
                    time.sleep(999999)                    
                    sys.exit()
    except:
                print(f'{colors.RED}[ERROR] No internet connection')      
                time.sleep(999999)
                time.sleep(999999)
                time.sleep(999999)
                time.sleep(999999)
                time.sleep(999999)
                time.sleep(999999)
                time.sleep(999999)
                time.sleep(999999)   
auth()
