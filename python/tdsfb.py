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
def fivex_delay(o):
	while (o>1):
		o=o-1
		print(green+'['+red+'V'+green+'TEN]'+'['+green+str(o)+']','      ', end='\r')
		sleep(0.1)
		print(green+'[V'+red+'T'+green+'EN]'+'['+green+str(o)+']','      ', end='\r')
		sleep(0.1)
		print(green+'[VT'+red+'E'+green+'N]'+'['+green+str(o)+']','      ', end='\r')
		sleep(0.1)
		print(green+'[VTE'+red+'N]'+green+'['+green+str(o)+']','      ', end='\r')
		sleep(0.1)
		print(green+'[VTEN'+red+']'+green+'['+green+str(o)+']','      ', end='\r')
		sleep(0.1)
		print(green+'[VTEN]'+red+'['+green+str(o)+']','      ', end='\r')
		sleep(0.1)
		print(green+'['+red+'VTEN'+green+']'+'['+red+str(o)+green+']','      ', end='\r')
		sleep(0.1)
def logo():
    os.system("cls" if os.name == "nt" else "clear")
    logo = """

    █░█ ▀█▀ █▀▀ █▄░█ ▀█▀ █▀█ █▀█ █░░
    ▀▄▀ ░█░ ██▄ █░▀█ ░█░ █▄█ █▄█ █▄▄
          [Tool TDS facebook]
    ________________________________
    Admin1: Vu Hoang
    Admin2: Nguyen
    ________________________________

    """

    Write.Print(logo,Colors.red_to_green,interval=0.005)

logo()
while(True):
	token_tds=input(yellow+'NHẬP'+red+' ACCESS_TOKEN TDS: '+green)
	ttacc=requests.get('https://traodoisub.com/api/?fields=profile&access_token='+str(token_tds))
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
while(True):
	while(True):
		while(True):
			ck_fb=input(yellow+'NHẬP'+green+' COOKIE FACEBOOK: '+red)
			if ck_fb=='':break
			cookie=ck_fb.split(';')
			for o in range(0,len(cookie)):
				if 'c_user' in cookie[o]:
					get_id_fb=cookie[o].split('=')
					id_fb=get_id_fb[1]
			break
		if ck_fb=='':
			print(green+'THANKS BẠN ĐÃ SỬ DỤNG TOOL CỦA',fivex+' !')
			quit()
		logo()
		u_run='https://traodoisub.com/api/?fields=run&id='+id_fb+'&access_token='+token_tds
		print(green+'['+red+'ĐANG'+green+' CẤU HÌNH'+red+' ID: '+green+id_fb+red+']')
		run=requests.get(url=u_run)
		if 'success' in run.text:
			print(fivex,'['+run.json()['data']['msg'].upper()+']')
			sleep(0.5)
			break
		else:
			print(red+run.json()['error'].upper())
	logo()
	stop=int(input(green+'NHẬP '+red+'SỐ NHIỆM VỤ: '+green))
	delay=int(input(red+'NHẬP '+green+'DELAY: '+red))
	s=0
	logo()
	while(True):
		print(fivex+red+'['+green+'HẾT NHIỆM VỤ, VUI LÒNG ĐỢI !'+red+']',end="\r")
		while(True):
			try:
				list_nv=requests.get('https://traodoisub.com/api/?fields=reaction&access_token='+token_tds)
				if 'id' in list_nv.text:break
			except:
				print(fivex_no_pro+green+'['+red+'INTERNET KHÔNG ỔN ĐỊNH !!!'+green+']','               ',end='\r')
		for x in range(0,len(list_nv.json())):
			try:
				id_post=list_nv.json()[x]['id']
				type_post=list_nv.json()[x]['type']
				if str(type_post)=='LIKE':
					type_rect='LIKE'
					v=1
				if str(type_post)=='LOVE':
					type_rect='LOVE '
					v=2
				if str(type_post)=='CARE':
					type_rect='CARE '
					v=3
				if str(type_post)=='HAHA':
					type_rect='HAHA '
					v=4
				if str(type_post)=='WOW':
					type_rect='WOW  '
					v=5
				if str(type_post)=='SAD':
					type_rect='SAD  '
					v=6
				if str(type_post)=='ANGRY':
					type_rect='ANGRY'
					v=7
				host='https://mbasic.facebook.com'
				u=host+'/reactions/picker/?is_permalink=1&ft_id='+id_post
				h={'cookie':ck_fb}
				check=requests.get(url=u,headers=h).text
				if 'Trước tiên, bạn phải đăng nhập.' in check:
					break
				if 'Phẫn nộ' in check:
					cx=BeautifulSoup(check,'html.parser')
					type_cx=cx.find_all('a')
					u_cx=host+str(type_cx[v]['href'])
					rect=requests.get(url=u_cx,headers=h).text
				nhan_tien=requests.get('https://traodoisub.com/api/coin/?type='+type_post+'&id='+id_post+'&access_token='+token_tds)
				if 'success' in nhan_tien.text:
					s=s+1
					xu=str(nhan_tien.json()['data']['xu'])
					msg=str(nhan_tien.json()['data']['msg']).upper()
					time=datetime.now().strftime("%H:%M:%S")
					print(fivex_no_pro+green+'['+red+str(s)+green+']['+time+']['+red+type_rect+green+']['+yellow+msg+green+']['+yellow+xu+green+']','     ')
					if s==stop:break
					fivex_delay(delay)
			except:
				print(fivex_no_pro+green+'['+red+'Dừng tool!'+green+']','               ',end='\r')
		if s==stop:break
		if 'Trước tiên, bạn phải đăng nhập.' in check:
			print(fivex_no_pro+green+'['+red+'COOKIE FACEBOOK DIE'+green+']','                    ')
			break
	print(fivex+green+'[DỪNG TOOL ẤN'+red+' ENTER !!!'+green+']')
	ttacc=requests.get('https://traodoisub.com/api/?fields=profile&access_token='+str(token_tds)).json()
	if s==stop:print(fivex_no_pro+green+'[CHẠY TOOL SUCCESS, TỔNG XU:',yellow+str(ttacc['data']['xu'])+']')