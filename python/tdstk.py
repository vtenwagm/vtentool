import requests
from time import sleep
import os

from bs4 import BeautifulSoup
from pystyle import Write, Colors
from datetime import datetime
import re,requests,os,sys
from time import sleep
black='\033[1;90m'
white='\033[1;97m'
red='\033[1;91m'
green='\033[1;92m'
blue='\033[1;96m'
yellow='\033[1;93m'
whitex='\033[7;37m\033[1;37m'
pink='\033[1;95m'
redb='\033[7;37m\033[1;91m'
redz='\033[1;41;97m'
end='\033[0m'
fivex=white+'['+red+'VTEN'+green+']'
fivex_no_pro=green+'[VTEN]'+end
def vten_delay(o):
	while (o>1):
		o=o-1
		print(green+'['+red+'V'+green+'TEN]'+'['+green+str(o)+']','      ', end='\r')
		sleep(0.1)
		print(green+'[V'+red+'T'+green+'EN]'+'['+green+str(o)+']','      ', end='\r')
		sleep(0.1)
		print(green+'[VT'+red+'E'+green+'N]'+'['+green+str(o)+']','      ', end='\r')
		sleep(0.1)
		print(green+'[VT'+red+'E'+green+'N]'+'['+green+str(o)+']','      ', end='\r')
		sleep(0.1)
		print(green+'[VTE'+red+'N]'+green+'['+green+str(o)+']','      ', end='\r')
		sleep(0.1)
		print(green+'[VTEN'+red+']'+green+'['+green+str(o)+']','      ', end='\r')
		sleep(0.1)
		print(green+'[VTEN]'+red+'['+green+str(o)+']','      ', end='\r')
		sleep(0.1)
		sleep(0.1)
def logo():
    os.system("cls" if os.name == "nt" else "clear")
    logo = """

    █░█ ▀█▀ █▀▀ █▄░█ ▀█▀ █▀█ █▀█ █░░
    ▀▄▀ ░█░ ██▄ █░▀█ ░█░ █▄█ █▄█ █▄▄
           [Tool TDS Tiktok]
    ________________________________
    Admin1: Vu Hoang
    Admin2: Nguyen
    ________________________________
    """

    Write.Print(logo,Colors.red_to_green,interval=0.005)

def open_browser(url):
    os.system(f"start {url}" if os.name == "nt" else "xdg-open {url}" )



def tiktok_like():
    while True:
        try:
            time=datetime.now().strftime("%H:%M:%S")
            nvs = requests.get(f"https://traodoisub.com/api/?fields=tiktok_like&access_token={token}").json()
            for nv in nvs['data']:
                print(fivex_no_pro+green+'['+time+']['+yellow+'LIKE'+green+']['+yellow+nv["link"]+green+']','     ')
                open_browser(nv['link'])
                vten_delay(delay)
                requests.get(f'https://traodoisub.com/api/coin/?type=tiktok_like&id={nv["id"]}&access_token={token}')

            nvs = requests.get(f"https://traodoisub.com/api/?fields=tiktok_like&access_token={token}").json()
            try:
                s = requests.get(f'https://traodoisub.com/api/coin/?type=TIKTOK_FOLLOW&id=TIKTOK_FOLLOW_API&access_token={token}').json()
                xu = s['data']['xu']
                xu_them = s['data']['xu_them']
                msg = s['data']['msg']
                print(fivex_no_pro+green+'['+time+']['+yellow+msg+green+']['+yellow+xu+green+']','     ')
            except: pass
            for nv in nvs['data']:
                print(fivex_no_pro+green+'['+time+']['+yellow+'LIKE'+green+']['+yellow+nv["link"]+green+']','     ')
                open_browser(nv['link'])
                vten_delay(delay)
                requests.get(f'https://traodoisub.com/api/coin/?type=tiktok_like&id={nv["id"]}&access_token={token}')
            try:
                s = requests.get(f'https://traodoisub.com/api/coin/?type=TIKTOK_FOLLOW&id=TIKTOK_FOLLOW_API&access_token={token}').json()
                xu = s['data']['xu']
                xu_them = s['data']['xu_them']
                msg = s['data']['msg']
                print(fivex_no_pro+green+'['+time+']['+yellow+msg+green+']['+yellow+xu+green+']','     ')
            except: pass
        except: pass


def tiktok_fl():
    while True:
        try:
            time=datetime.now().strftime("%H:%M:%S")
            nvs = requests.get(f"https://traodoisub.com/api/?fields=tiktok_follow&access_token={token}").json()
            for nv in nvs['data']:
                print(fivex_no_pro+green+'['+time+']['+yellow+'LIKE'+green+']['+yellow+nv["link"]+green+']','     ')
                open_browser(nv['link'])
                vten_delay(delay)
                requests.get(f'https://traodoisub.com/api/coin/?type=tiktok_follow&id={nv["id"]}&access_token={token}')
            try:
                s = requests.get(f'https://traodoisub.com/api/coin/?type=TIKTOK_FOLLOW&id=TIKTOK_FOLLOW_API&access_token={token}').json()
                xu = s['data']['xu']
                xu_them = s['data']['xu_them']
                msg = s['data']['msg']
                print(fivex_no_pro+green+'['+time+']['+yellow+msg+green+']['+yellow+xu+green+']','     ')
            except: pass

            nvs = requests.get(f"https://traodoisub.com/api/?fields=tiktok_follow&access_token={token}").json()
            for nv in nvs['data']:
                print(fivex_no_pro+green+'['+time+']['+yellow+'LIKE'+green+']['+yellow+nv["link"]+green+']','     ')
                open_browser(nv['link'])
                vten_delay(delay)
                requests.get(f'https://traodoisub.com/api/coin/?type=tiktok_follow&id={nv["id"]}&access_token={token}')
            try:
                s = requests.get(f'https://traodoisub.com/api/coin/?type=TIKTOK_FOLLOW&id=TIKTOK_FOLLOW_API&access_token={token}').json()
                xu = s['data']['xu']
                xu_them = s['data']['xu_them']
                msg = s['data']['msg']
                print(fivex_no_pro+green+'['+time+']['+yellow+msg+green+']['+yellow+xu+green+']','     ')
            except: pass

        except: pass


logo()

while(True):
	token=input(yellow+'NHẬP'+red+' ACCESS_TOKEN TDS: '+green)
	ttacc=requests.get('https://traodoisub.com/api/?fields=profile&access_token='+str(token))
	if 'error' in ttacc.text:print(red+ttacc.json()['error'].upper())
	if 'success' in ttacc.text:
		logo()
		user=ttacc.json()['data']['user']
		xu=ttacc.json()['data']['xu']
		xu_die=ttacc.json()['data']['xudie']
		print(green+'['+red+'USER: '+green+user.upper()+red+']'+green+'['+yellow+xu+' XU'+green+']'+black+'['+xu_die+' XU DIE'+green+']')
		sleep(1)
		break

logo()
print()
print(green+'['+red+'1'+green+'] : ' + yellow+'Tiktok Like')
print(green+'['+red+'2'+green+'] : ' + yellow+'Tiktok Follow')

n=input(yellow+'Nhập số -> '+green)

delay = int(input(red+'NHẬP '+green+'DELAY: '+red))

if n == '1': tiktok_like()
elif n == '2': tiktok_fl()
else: print(green+'['+red+'Lựa chọn không xác định'+green+']')
