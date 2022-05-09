import requests,random,string

class feiniao():
    def __init__(self):
        pass
    @staticmethod
    def register(email,password,proxy=None):
        url="https://feiniaoyun.tk/api/v1/passport/auth/register"
        headers= {
            "User-Agent":'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
            "Referer": "https://feiniaoyun.tk/"
        }
        data={
            "email":email,
            "password":password,
            "invite_code":None,
            "email_code":None
        }
        req=requests.post(url,headers=headers,data=data,timeout=5,proxies=proxy)
        return req
    
    @staticmethod
    def login(email,password):
        url="https://feiniaoyun.tk/api/v1/passport/auth/login"
        headers= {
            "User-Agent":'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
            "Referer": "https://feiniaoyun.tk/"
        }
        data={
            "email":email,
            "password":password
        }
        req=requests.post(url,headers=headers,data=data,verify=False,timeout=5)
        return req

    @staticmethod
    def getSubscribe(proxy=None):
        #api="https://api.wcc.best/sub?target=v2ray&url="
        api=""
        password=''.join(random.sample(string.ascii_letters + string.digits + string.ascii_lowercase, 10))
        email=password+"@gmail.com"
        req=feiniao.register(email,password,proxy)
        try:
            token=req.json()["data"]["token"]
            subscribe=f"https://feiniaoyun.tk/api/v1/client/subscribe?token={token}"
            return api+subscribe
        except:
            return req
        
    @staticmethod
    def saveconf():
        url=ckcloud.getSubscibe()
        req=requests.get(url)
        with open("./freev2/feiniao") as f:
            f.write(req.text)
            
class ckcloud():
    def __init__(self):
        pass
    
    @staticmethod
    def register(email,password,proxy=None):
        url="https://www.ckcloud.xyz/api/v1/passport/auth/register"
        headers= {
            "User-Agent":'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
            "Referer": "https://www.ckcloud.xyz/"
        }
        data={
            "email":email,
            "password":password,
            "invite_code":None,
            "email_code":None
        }
        req=requests.post(url,headers=headers,data=data,verify=False,timeout=5,proxies=proxy)
        return req

    @staticmethod
    def getSubscribe(proxy=None):
        api=""
        password=''.join(random.sample(string.ascii_letters + string.digits + string.ascii_lowercase, 10))
        email=password+"@gmail.com"
        req=ckcloud.register(email,password,proxy)
        try:
            token=req.json()["data"]["token"]
            subscribe=f"https://www.ckcloud.xyz/api/v1/client/subscribe?token={token}"
            return api+subscribe
        except:
            return req
    
    @staticmethod
    def saveconf():
        url=ckcloud.getSubscibe()
        req=requests.get(url)
        with open("./freev2/ckcloud") as f:
            f.write(req.text)

def getconf():
    ckcloud.saveconf()
    feiniao.saveconf()
    
    
