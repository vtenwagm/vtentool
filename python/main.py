from pystyle import Write, Colors
import datetime
import bs4
import os
import colorama
import requests
import uuid


def banner():
    os.system("cls" if os.name == "nt" else "clear")
    logo = """

    █░█ ▀█▀ █▀▀ █▄░█ ▀█▀ █▀█ █▀█ █░░
    ▀▄▀ ░█░ ██▄ █░▀█ ░█░ █▄█ █▄█ █▄▄
    ________________________________
    Admin1: Vu Hoang
    Admin2: Nguyen
    ________________________________
    """

    Write.Print(logo,Colors.red_to_green,interval=0.005)


def banner1():
    os.system("cls" if os.name == "nt" else "clear")
    logo = f"""

    █░█ ▀█▀ █▀▀ █▄░█ ▀█▀ █▀█ █▀█ █░░
    ▀▄▀ ░█░ ██▄ █░▀█ ░█░ █▄█ █▄█ █▄▄
    ________________________________
    Admin1: Vu Hoang
    Admin2: Nguyen
    ________________________________
    """
    menu = """
    ╔══════════════════════════════╗
    ║          [Tool TDS]          ║
    ║══════════════════════════════║
    ║  [1] TDS facebook auto       ║
    ║  [2] TDS tiktok              ║
    ║  [3] TDS youtube             ║
    ╚══════════════════════════════╝

    ╔══════════════════════════════╗
    ║          [Tool TTC]          ║
    ║══════════════════════════════║
    ║  [4] TTC facebook auto       ║
    ║  [5] TTC tiktok              ║
    ║  [6] TTC youtube             ║
    ╚══════════════════════════════╝

    ╔══════════════════════════════╗
    ║       [Tool tiện ích]        ║
    ║══════════════════════════════║
    ║  [7] Reg page pro5           ║
    ║  [8] Share ảo                ║
    ║  [9] Reg clone garena        ║
    ╚══════════════════════════════╝

    [X] Thoát
    """
    Write.Print(logo,Colors.red_to_green,interval=0.005)
    Write.Print(menu,Colors.green,interval=0.0000000001)


def main():
    banner1()
    cmd = Write.Input("nhập lựa chọn => ", Colors.green_to_cyan, interval=0.05)
    if cmd == '1': exec(requests.get('url').text)

if __name__ == "__main__":
    banner()
    with open('key.txt', 'w+') as f:
        # print(f.read())
        key = int(uuid.getnode())*int(datetime.datetime.now().day)
        if f.read() == key: main()
        else:
            lk = requests.get(f'https://link4m.co/api-shorten/v2?api=647f57d6e7fe5f5a516b2188&url=https://google.com/search?q={key}').json()
            print(f"link lấy key của bạn là {lk['shortenedUrl']}, key của bạn chỉ sử dụng được cho thiết bị của bạn")
            print(key)
            while True:
                keyinp = Write.Input("nhập key đã lấy => ", Colors.green_to_red, interval=0.05)
                if keyinp == str(key) :
                    f.write(str(key))
                    main()
                    break
                else: Write.Print('key sai\n',Colors.red_to_black,interval=0.005)
    
