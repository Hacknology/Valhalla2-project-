# -*- coding: cp1254 -*-
logo = """
  |\     /|(  ___  )( \      |\     /|(  ___  )( \      ( \      (  ___  )
  | )   ( || (   ) || (      | )   ( || (   ) || (      | (      | (   ) |
  | |   | || (___) || |      | (___) || (___) || |      | |      | (___) |
  ( (   ) )|  ___  || |      |  ___  ||  ___  || |      | |      |  ___  |
   \ \_/ / | (   ) || |      | (   ) || (   ) || |      | |      | (   ) |
    \   /  | )   ( || (____/\| )   ( || )   ( || (____/\| (____/\| )   ( |
     \_/   |/     \|(_______/|/     \||/     \|(_______/(_______/|/     \|

                                             Hacknology
                                             https://github.com/Hacknology/
                                             "Hammer of hate is our faith"

    """
import warnings,glob,os
import sys
warnings.filterwarnings('ignore')
from imports import *
from colorama import Fore, Back, Style, init
red     = Fore.RED
cyan    = Fore.CYAN
blue    = Fore.BLUE
green   = Fore.GREEN
white   = Fore.WHITE
yellow  = Fore.YELLOW
magenta = Fore.MAGENTA
bright  = Style.BRIGHT

    


print bright + blue + logo
def help():
    print yellow + """
\t\t\tCommands:
\t\t\t\tsite ara: Wordpress siteleri online tarar.
\t\t\t\tyardim: Bu mesaji gosterir.
\t\t\t\tcik: cikar
\t\t\t\tsqli test: Verdiginiz .txt dosyasinin icindeki sitelerin acikli olup olmadigini kontrol eder
\t\t\t\tbrute: Wordpress sitelere brute-force(kaba kuvvet) saldirisi uygular 
\t\t\t\tcrawler: Daha once verdiginiz sitelerden yeni siteler bulur.
\t\t\t\tselam: Odin'i selamla!
"""
while True:
    komut = raw_input(bright + green + "\nkomut => ").lower()
    
    if komut == "site ara":
        scan_site.create_word()
        scan_site.create_dork(5)
        scan_site.wp_get_query(10)
    elif komut == "yardim":
        help()
    elif komut == "cik":
        sys.exit()
    elif komut == "selam":
        print """
Odin'e selamlar!
Thor'a selamlar!
Freja'a selamlar!
Kral Kemiksiz Ivar'a selamlar!
İmparator Ragnar Lodbrok'a selamlar!
Ve Valhalla'dan gelen gerçek viking savaşçısı coder Hacknology'e selamlar!"""
    elif komut == "sqli test":
        sqltest.control_sql(f=raw_input(bright+yellow+"File: "))
    elif komut == "crawler":
        dosya = open(raw_input(bright+yellow+"Lutfen url listesinin bulundugu dosya adini verin: "), "r+").readlines()
        try:
            for url in dosya:
                crawl.get_title(url)
            
        except Exception as e:
            print e
    elif komut == "brute":
        try:
            wp_brute.run()
        except:
            raise
            print red + "Hata olustu... Sonra tekrar deneyin!"
    
    else:
        locals()[komut].run()
            
        
            
        
        
    
        
