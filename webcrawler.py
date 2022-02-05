import requests
import json


def login(username, password):
    cookies = {
        'locale': 'nb-NO',
        '_ga': 'GA1.1.940420002.1641239911',
        '_hjSessionUser_2749362': 'eyJpZCI6IjI1N2ZkNTQxLTQ0MTgtNTQzNi1iZjNkLTA5ZmFkM2UwYTUxNCIsImNyZWF0ZWQiOjE2NDEyMzk5MTA5ODUsImV4aXN0aW5nIjp0cnVlfQ==',
        '_hjSession_2749362': 'eyJpZCI6IjlkZTU4YWJmLTlhMWYtNGRiOC05NmIzLWJkMmE0OTU2MWQyNiIsImNyZWF0ZWQiOjE2NDQwNTE3MzEwNDEsImluU2FtcGxlIjpmYWxzZX0=',
        '_hjAbsoluteSessionInProgress': '0',
        '_hjIncludedInPageviewSample': '1',
        '_hjIncludedInSessionSample': '1',
        'authentication': 'CfDJ8JCnWWnWZg5HtInfGoQkTiuPBFdw8OO8c3UetUcvfCEJmX79NOK9F7xkPr6ejaE7QjzyMOzwUaz9MF6UMsq3eCTXEv2VNHh40TvGgzYOluWP61qq4p76WHS1QNCgFcLfCheV_OqHvhzQMolbqQXFhnrRj9B4rWaYFMG4neieIB4YGYD_9o2V4WcrJs_0m-eM7gZi_5f_XdR-twJGhSbxsQhZiJ1OlQYRnJ0cGrTq1181v6GVRYxH9bqEzJ6M0yHU99S5Xyo5d01sf93ZggvC9qY9igZd-LEqG6cm35PvmlRd1qgFKuWkyQx46KhV3OnpYlNus56kCgMJdoZo5IBM7_N77mK0uhWBK-p_r38ET8CX1ADHhKilBARw9UATIveRTGWFEtIqfX2Ylgvy-kErGwrWXiLlPS7vj3aKe3qO0GrXMpgxsxM3Cu7V9shpyS4aJP6bazxSUVJJEwAebNOa7FgNeNDUQCyg3zJN4ILhNofcXqgimttlKQ5Ui3m0cQOmHRZpY5HzbHY1ZVbYmt_5-DU',
        '_ga_VNK9X5XJ3H': 'GS1.1.1644051730.46.1.1644054672.0',
    }

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

    pre_data = '"password":"{}","persistent":false,"username":"{}"'.format(
        password, username)
    data = '{'+pre_data+'}'
    response = requests.post('https://www.bestr.no/api/membership/accounts/login', headers=headers, cookies=cookies,
                             data=data)
    print(response)
    return requests


cookies = {
    'locale': 'nb-NO',
    '_ga': 'GA1.1.940420002.1641239911',
    '_hjSessionUser_2749362': 'eyJpZCI6IjI1N2ZkNTQxLTQ0MTgtNTQzNi1iZjNkLTA5ZmFkM2UwYTUxNCIsImNyZWF0ZWQiOjE2NDEyMzk5MTA5ODUsImV4aXN0aW5nIjp0cnVlfQ==',
    'authentication': 'CfDJ8JCnWWnWZg5HtInfGoQkTiv5aC84EIZ2FLcMKtHpk7ShJk43d4-LAYetMc-KgPw5PArXyPWEX2ACwfRqYlRyhFYopXBBydOSWyQ5YalyPcmRmCaA4zcEwCz3P--OaSMDx0pa_nJUbgBP5qjDVC2oX_cQos3MoVp4sQMEUH9ANAvxe0oKJwmNH_i2YqzZ5eUxXrnYkDgie1syE3nLLiCA7Dn5LojcR7299X2TRlaOUgKZGK6SDm_wjJZYi9KS7viX4FND1HS_sGa_mq2I3Gg2zdl7XcfelEKrKzqgo0mfhzYrJJIlUTOh2oTgKfmFdUdDxToc3zq_broMIWm4uoCrlX5ZR2cPUyoi8Yj4HkDLrPCQHKanB9Mm1YxYQDA1yn5UqmRC8Naanf3sNzhYyIMEsauMpLsmSvmfEkfxBgVxibnYhXRSyFDmpv03taXJKTVILF6jgiigIBMIYf3RrqtnsTubveBJMMJmQ_Y0Ebdgh2syOWme53dxX0H-FcIDTbPQZDgLCwlD8SY1HFuwsB5IoYY',
    '_hjSession_2749362': 'eyJpZCI6Ijg1M2FjNTFlLWQxOWYtNGI5Mi1iMDJhLWJiYzM3NjIwMGQ3OCIsImNyZWF0ZWQiOjE2NDQwNjc0MjUxNDYsImluU2FtcGxlIjp0cnVlfQ==',
    '_hjAbsoluteSessionInProgress': '0',
    '_hjIncludedInPageviewSample': '1',
    '_hjIncludedInSessionSample': '0',
    '_ga_VNK9X5XJ3H': 'GS1.1.1644067424.48.1.1644068790.0',
}

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

pre_data = '"content":"{}","sportId":"08d60015402ff40ddac564839c40516d"'.format(
    text2)
data = '{'+pre_data+'}'
print(data)
r = session.post('https://www.bestr.no/api/migration/import/csv',
                 headers=headers, cookies=cookies, data=data)

print(r.content)
