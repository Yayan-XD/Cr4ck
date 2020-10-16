#!/usr/bin/python2
#coding=utf-8
#Mau recode bro? 
#gak papa recode saja soalnya file ini kosong yahaha yahukkk
import os, sys, time, mechanize, itertools, datetime, random, hashlib, re, threading, json, getpass, urllib, cookielib
from multiprocessing.pool import ThreadPool
P = '\033[1;97m'
M = '\033[1;91m'
H = '\033[1;92m'
K = '\033[1;93m'
B = '\033[1;94m'
U = '\033[1;95m'
O = '\033[1;96m'
my_color = [
 P, M, H, K, B, U, O]
warna = random.choice(my_color)
warni = random.choice(my_color)
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')

try:
    import requests
except ImportError:
    os.system('pip2 install requests')
    os.system('python2 run.py')

from requests.exceptions import ConnectionError
from mechanize import Browser
from datetime import datetime
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
os.system('clear')
done = False

def animate():
    for c in itertools.cycle(['\x1b[1;91m||', '\x1b[1;92m/', '\x1b[1;93m─', '\x1b[1;96m|', '\x1b[1;95m\\']):
        if done:
            break
        sys.stdout.write('\r\x1b[1;93mYayanXD\x1b[1;94m:) ' + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c)
        sys.stdout.flush()
        time.sleep(0.1)


t = threading.Thread(target=animate)
t.start()
time.sleep(5)
done = True

def keluar():
    print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} \x1b[1;93mSelamat Tinggal..'
    os.sys.exit()


def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '%s;' % str(31 + j))

    x += ''
    x = x.replace('!0', '')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.0003)
	
		
##### LOGO #####
logo = """
\033[1;94m────────────────────────────────────────────────
\033[1;96m  ▼￣＞-―-＜￣▼  \033[1;95mAuthor   \033[1;91m: \033[1;92mYayanXD
\033[1;96m   Ｙ　     Ｙ   \033[1;95mGithub   \033[1;91m: \033[1;92mgithub.com/Yayan-XD
\033[1;96m/\ /   \033[1;91m●  \033[1;92mω \033[1;91m●\033[1;96m）  \033[1;95mWhatsApp \033[1;91m: \033[1;92m08560303XNXX
\033[1;96m\ ｜　 つ　  ヽつ\033[1;95mInstagram \033[1;91m: \033[1;92m@yayanxd_
\033[1;94m────────────────────────────────────────────────
\033[1;95m         {\033[1;97mWELCOME BACK SLURD DI SC AING\033[1;95m}                     
\033[1;92m   Jangan lupa follow instagram gua😎
\033[1;94m────────────────────────────────────────────────"""

os.system("clear")
print  """
\033[1;94m /$$        /$$$$$$   /$$$$$$    /$$   /$$   /$$
\033[1;93m| $$       /$$$_  $$ /$$__  $$ /$$$$  | $$$ | $$
\033[1;94m| $$      | $$$$\ $$| $$  \__/|_  $$  | $$$$| $$
\033[1;93m| $$      | $$ $$ $$| $$$$$$$   | $$  | $$ $$ $$
\033[1;94m| $$      | $$\ $$$$| $$__  $$  | $$  | $$  $$$$
\033[1;93m| $$      | $$ \ $$$| $$  \ $$  | $$  | $$\  $$$
\033[1;94m| $$$$$$$$|  $$$$$$/|  $$$$$$/ /$$$$$$| $$ \  $$
\033[1;93m|________/ \______/  \______/ |______/|__/  \__/"""

jalan("\033[1;94m────────────────────────────────────────────────")
jalan("\033[1;96m  ▼￣＞-―-＜￣▼  \033[1;95mAuthor   \033[1;91m: \033[1;92mYayanXD")
jalan("\033[1;96m   Ｙ　     Ｙ   \033[1;95mGithub   \033[1;91m: \033[1;92mgithub.com/Yayan-XD")
jalan("\033[1;96m/\ /   \033[1;91m●  \033[1;92mω \033[1;91m●\033[1;96m）  \033[1;95mWhatsApp \033[1;91m: \033[1;92m08560303XNXX")
jalan("\033[1;96m\ ｜　 つ　  ヽつ\033[1;95mInstagram \033[1;91m: \033[1;92m@yayanxd_")
jalan("\033[1;94m────────────────────────────────────────────────")
jalan("\033[1;95mSudahkah anda mempunyai username&password untuk login tools?")             
jalan("\033[1;92mKalo tidak punya ngasal saja tod nanti di alihkan")
print "\033[1;94m────────────────────────────────────────────────"""
CorrectUsername = "Yayan"
CorrectPassword = "Ganteng"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;92m 🔒 \x1b[1;92mUsername \x1b[1;97m»» \x1b[1;94m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;92m 🔒 \x1b[1;92mPassword \x1b[1;97m»» \x1b[1;94m")
        if (password == CorrectPassword):
            print "Loggin berhasil"
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;93mSalah jembut:v"
            os.system('xdg-open https://api.whatsapp.com/send/?phone=%2B6285603036683&text&app_absent=0')
    else:
        print "\033[1;93mSalah jembut:v"
        os.system('xdg-open https://api.whatsapp.com/send/?phone=%2B6285603036683&text&app_absent=0')

##### LICENSE #####
#=================#
def lisensi():
	os.system('clear')
	login()
####login#########
def login():
	os.system('python Contoh.py')

															
if __name__ == '__main__':
	login()
