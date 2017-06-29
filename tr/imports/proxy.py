"""
            author: @Hacknology
            contact: utkucolak05@gmail.com
            date: 16.06.2017
            ENTER TO VALHALLA2
"""

import urllib
import random
def add_proxy():
    global liste
    liste = []
    
    dosya = open(raw_input(" Proxy ip listesinin bulundugu dosyanin adi \n IP:PORT \n Ornek: 1.1.1.1:2313 \n ==> "), "r").readlines()
    for a in dosya:
        a = a.replace("\n", "")
        liste.append(a)
        
        
def check_proxy():
    add_proxy()
    global proxyy
    for i in range(len(liste)):
        
        proxyy = {
            'http': 'http://{}'.format(random.choice(liste)),
            }
        try:
            ip = urllib.urlopen("http://icanhazip.com/ip").read()
            yeni_ip = urllib.urlopen("http://icanhazip.com/ip", proxies=proxyy).read()
            if ip != yeni_ip:
                
                print "Odin? Loki? Thor? Who... K-Kimsin sen?! Seni taniyamiyorum!"
                break
        except:
            pass
        
def use_proxy():
    check_proxy()
    return proxyy


