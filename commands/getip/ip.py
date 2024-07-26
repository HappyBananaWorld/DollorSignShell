import requests

def ipv4():
    res = requests.get("https://api.ipify.org?format=json")
    content = res.json()
    print(content['ip'])


def ipv6():
    res = requests.get("https://api64.ipify.org?format=json")
    content = res.json()
    print(content['ip'])
    
def ip():
    ipv4()
    ipv6()