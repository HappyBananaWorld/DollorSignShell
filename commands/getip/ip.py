import requests

def ipv4():
    result = None
    res = requests.get("https://api.ipify.org?format=json")
    content = res.json()
    result = content['ip']
    print(result)
    return result


def ipv6():
    result = None
    res = requests.get("https://api64.ipify.org?format=json")
    content = res.json()
    result = content['ip']
    print(result)
    return result
    
def ip():
    result = None
    result = ipv4()
    result = ipv6()
    return result