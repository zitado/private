import requests
#send sms
headers = {
    'Accept': '*/*',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 9; ASUS_I003DD Build/PI)',
    'Host': 'apim.djezzy.dz',
    'Connection': 'close',
    # 'Accept-Encoding': 'gzip, deflate, br',
    # 'Content-Length': '71',
}

data = {
    'scope': 'smsotp',
    'msisdn': '213797815762',
    'client_id': '6E6CwTkp8H1CyQxraPmcEJPQ7xka',
}

response = requests.post('https://apim.djezzy.dz/oauth2/registration', headers=headers, data=data, verify=False)


