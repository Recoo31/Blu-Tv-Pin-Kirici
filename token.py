import os,time,re

try:
  import requests
  import colorama
  from colorama import Fore
  from pystyle import Colors, Colorate   
except ModuleNotFoundError:
    print("Modul Eksik")
    print("Yukleniyor...")
    os.system("pip install requests")
    os.system("pip install colorama")
    os.system("pip install pystyle")
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

uri = "https://www.blutv.com/api/login"


data = {"remember":"false","username":mail,"password":passw,"captchaVersion":"v3","captchaToken":""}


head = {
"Host":"www.blutv.com",
"Connection":"keep-alive",
"AppPlatform":"com.blu",
"Content-Type":"text/plain;charset=UTF-8",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0",
"AppCountry":"TUR",
"AppLanguage":"tr-TR",
"Accept":"*/*",
"Origin":"https://www.blutv.com",
"Sec-Fetch-Site":"same-origin",
"Sec-Fetch-Mode":"cors",
"Sec-Fetch-Dest":"empty",
"Referer":"https://www.blutv.com/giris",
"Accept-Language":"tr-TR,tr;q=0.9",
"Accept-Encoding":"gzip, deflate",
}





r = requests.post(url=uri, json=data, headers=head)

token_a = r.cookies.get("token_a")

if "errors.wrongUsernameOrPassword" in r.text:
    print("Hesap Yanlış")
    time.sleep(2)
    os.system("py token_1.py")
    exit()
else:
    token = r.json()['accessToken']
    f = open("Blu-Access.txt", "a")
    f.write(token)
    f.close()

    
    head2 = {
    "Host":"www.blutv.com",
    "Connection":"keep-alive",
    "AppPlatform":"com.blu",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0",
    "AppCountry":"TUR",
    "AppLanguage":"tr-TR",
    "Accept":"*/*",
    "Sec-Fetch-Site":"same-origin",
    "Sec-Fetch-Mode":"cors",
    "Sec-Fetch-Dest":"empty",
    "Referer":"https://www.blutv.com/giris",
    "Accept-Language":"tr-TR,tr;q=0.9",
    "Cookie":"token_a="+token_a,
    "Accept-Encoding":"gzip, deflate",
    }

    profilidcek = requests.get("https://www.blutv.com/profil",headers=head2)
    profilid = re.findall(r'profile-avatar-(\S+)"',profilidcek.text)

    profilisim = re.findall(r'class="mt-5 text-center text-lg font-normal text-color-white">(\S+)</div></div><',profilidcek.text)

    profilid.insert(0,'')
    profilisim.insert(0,'')

    os.system('cls')
    print("Kırılacak Profil:")

#
# Aşağısı biraz karışık bunu yapma nedenim profili isterken 0'dan başlıyor ama bazıları 0 yerine 1 giriyor.
# Bunu önlemek için listenin başına boşluk ekleyip range'i 1. indexten başlatıyorum
# Varsa daha kolay yöntem, bana bildirin :)
#

    try:
          for yeteramk in range(1,len(profilid)):
              print(Fore.MAGENTA+f"\n {yeteramk}= {profilisim[yeteramk]} ({profilid[yeteramk]})")
    except:
          print("Kırılacak Profil:")
          os.system('cls')
          
          for yeteramk in range(1,len(profilid)):
              print(Fore.MAGENTA+f"\n {yeteramk}= {profilid[yeteramk]}")
  
    profi = int(input(Fore.MAGENTA+">"))

    profil=profilid[profi]

    c = open("Blu-Token.txt", "a")
    c.write(profil)
    c.close()



os.system("py pin.py")
