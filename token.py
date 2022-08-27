import os,socket,platform,time

try:
  import requests
  import colorama
  from colorama import Fore,Style,Back
  from pystyle import Colors, Colorate   
  from pypasser import reCaptchaV3
except ModuleNotFoundError:
    print("Modul Eksik")
    print("Yukleniyor...")
    os.system("pip install requests")
    os.system("pip install colorama")
    os.system("pip install pystyle")
    os.system("pip install pypasser")
    print("Yukleme Tamamlandı! Yeniden Acin")
    time.sleep(1.5)
    exit(0)

if os.path.exists("Pin.txt"):
  os.remove("Pin.txt")

if os.path.exists("Blu-Access.txt"):
  os.remove("Blu-Access.txt")

if os.path.exists("Blu-Token.txt"):
  os.remove("Blu-Token.txt")

os.system('cls')


print(Colorate.Horizontal(Colors.blue_to_purple, """ 
                                                (                    
                                                )\ )                 
                                                (()/(  (              
                                                /(_))))\ (  (    (   
                                                (_)) /((_))\ )\   )\  
                                                | _ (_)) ((_|(_) ((_) 
                                                |   / -_) _/ _ \/ _ \ 
                                                |_|_\___\__\___/\___/ 
                                                                    """, 1))

colorama.init()

mail = input(Fore.MAGENTA+"Mail:")
passw = input(Fore.MAGENTA+"Şifre:")


recap = reCaptchaV3('https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LdyC2cUAAAAACGuDKpXeDorzUDWXmdqeg-xy696&co=aHR0cHM6Ly9yZWNhcHRjaGEtZGVtby5hcHBzcG90LmNvbTo0NDM.&hl=tr&v=4rwLQsl5N_ccppoTAwwwMrEN&size=invisible&cb=e3k73bi96htw')


uri = "https://www.blutv.com/api/login"


data = {"username":mail,"password":passw,"remember":"false","captchaVersion":"v3","captchaToken":recap}


head = {
"Host": "www.blutv.com",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0",
"Accept": "*/*",
"Accept-Language": "en-US,en;q=0.5",
"Accept-Encoding": "gzip, deflate",
"Referer": "https://www.blutv.com/giris",
"Applanguage": "tr-TR",
"Appplatform": "com.blu",
"Appcountry": "TUR",
"Deviceresolution": "1920x1080",
"Content-Type": "text/plain;charset=UTF-8",
"X-Instana-T": "f22506a13060ad43",
"X-Instana-S": "f22506a13060ad43",
"X-Instana-L": "1,correlationType=web;correlationId=f22506a13060ad43",
"Origin": "https://www.blutv.com",
"Sec-Fetch-Dest": "empty",
"Sec-Fetch-Mode": "cors",
"Sec-Fetch-Site": "same-origin",
"Te": "trailers",
}



r = requests.post(url=uri, json=data, headers=head)


if "errors.wrongUsernameOrPassword" in r.text:
    print("Hesap Yanlış")
    time.sleep(2)
else:
    token_a = r.cookies.get("token_a")
    token_r = r.cookies.get("token_r")


    token = r.json()['accessToken']
    f = open("Blu-Access.txt", "a")
    f.write(token)
    f.close()

    profi = input("Profil ID: ")
    c = open("Blu-Token.txt", "a")
    c.write(profi)
    c.close()


os.system("start https://discord.gg/Xd8VfYPHB3")
os.system("py pin.py")
