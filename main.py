import subprocess
import os
import time
import requests
import crayons
import webbrowser
import json
def cls():
	os.system('cls' if os.name == 'nt' else 'clear')

backend_url = ""

try:
    print(f"{crayons.cyan('[+] Connecting To BoogieFN Backend', bold=True)}")
    res = requests.get(backend_url)
    if res.status_code == 502:
        print()
        print(f"{crayons.red('[+] Backend Is Currently Offline, Please Contact Us In discord.gg/HfNfDQnPb6', bold=True)}")
        webbrowser.open('https://discord.gg/HfNfDQnPb6')
        time.sleep(5)
    else:
        cls()
        print(f"{crayons.cyan('[+] Loading Files For BoogieFN', bold=True)}")
        webbrowser.open('https://discord.gg/HfNfDQnPb6')
        ses = requests.Session()
        request = ses.get(backend_url + "/hybrid/ssl.dll")
        eacreq = ses.get(backend_url + "/hybrid/FortniteClient-Win64-Shipping_EAC.exe")
        bereq = ses.get(backend_url + "/hybrid/FortniteClient-Win64-Shipping_BE.exe")
        with open(f'cache/ssl.dll', 'wb') as f:
            f.write(request.content)
        with open(f'cache/FortniteClient-Win64-Shipping_EAC.exe', 'wb') as f:
            f.write(eacreq.content)
        with open(f'cache/FortniteClient-Win64-Shipping_BE.exe', 'wb') as f:
            f.write(bereq.content)
        print(f"{crayons.cyan('[+] Files Loaded!', bold=True)}")
        with open("config.json") as f:
            data = json.load(f)
        if data['path'] == "":
            path = input(f"{crayons.cyan('[+] Please Enter The Location Where Fortnite Is Installed: ', bold=True)}")
            data['path'] = path
            with open ("config.json",'w+') as f:
                json.dump(data, f, indent=3)
            location = f"{path}\FortniteGame\Binaries\Win64"
            os.replace("cache/FortniteClient-Win64-Shipping_BE.exe", f"{location}\FortniteClient-Win64-Shipping_BE.exe")
            os.replace("cache/FortniteClient-Win64-Shipping_EAC.exe", f"{location}\FortniteClient-Win64-Shipping_EAC.exe")
            os.replace("cache/ssl.dll", f"{location}\ssl.dll")
            print(f"{crayons.cyan('[+] Launching Fortnite...', bold=True)}")
            subprocess.call([f'{path}\FortniteGame\Binaries\Win64\FortniteClient-Win64-Shipping'])
            print(f"{crayons.cyan('[+] Launched Fortnite!', bold=True)}")
            time.sleep(5)
        else:
            path = data['path']
            location = f"{path}\FortniteGame\Binaries\Win64"
            os.replace("cache/FortniteClient-Win64-Shipping_BE.exe", f"{location}\FortniteClient-Win64-Shipping_BE.exe")
            os.replace("cache/FortniteClient-Win64-Shipping_EAC.exe", f"{location}\FortniteClient-Win64-Shipping_EAC.exe")
            os.replace("cache/ssl.dll", f"{location}\ssl.dll")
            print(f"{crayons.cyan('[+] Launching Fortnite...', bold=True)}")
            subprocess.call([f'{path}\FortniteGame\Binaries\Win64\FortniteClient-Win64-Shipping'])
            print(f"{crayons.cyan('[+] Launched Fortnite!', bold=True)}")
            time.sleep(5)
except Exception as e:
    print(f"Looks like an error has occured... :( Please Report This To The Developers in discord.gg/HfNfDQnPb6")
    print(e)
    time.sleep(5)