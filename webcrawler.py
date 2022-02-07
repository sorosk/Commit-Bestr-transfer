import requests
import json

def login(username, password):
    headers = {
        'Connection': 'keep-alive',
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
        'Accept': 'text/plain, */*; q=0.01',
        'Content-Type': 'application/json',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'Origin': 'https://www.bestr.no',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.bestr.no/welcome/login',
        'Accept-Language': 'nb,en-US;q=0.9,en;q=0.8',
    }

    pre_data = '"password":"{}","persistent":false,"username":"{}"'.format(password, username)
    data = '{'+pre_data+'}'
    response = requests.post('https://www.bestr.no/api/membership/accounts/login', headers=headers,
                             data=data)
    print(response)
    global cookies
    cookies = response.cookies.get_dict()
    return requests

headers = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    'Accept': 'text/plain, */*; q=0.01',
    'Content-Type': 'application/json',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'Origin': 'https://www.bestr.no',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://www.bestr.no/diary',
    'Accept-Language': 'nb,en-US;q=0.9,en;q=0.8',
}


session = login('Daddahu_test', 'Terycrews123')
with open("2022-02-04.csv", 'r') as f:
   text = f.read()
   text2 = text
   print(text2)

pre_data = '"content":"{}","sportId":"08d60015402ff40ddac564839c40516d"'.format(text2)
data = '{'+pre_data+'}'.replace(("\n", "\\n"))
print(data)
r = session.post('https://www.bestr.no/api/migration/import/csv', headers=headers, cookies=cookies, data=data)

print(r.content)