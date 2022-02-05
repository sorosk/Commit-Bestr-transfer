import requests

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

data = '{"content":"Date(dd.mm.yyyy);TrainingPlan;Long/Short;Endurance - Easy;Endurance - Moderate;Endurarance - L-AT;Endurance - H-AT;Endurance - Maks O2;Endurance - Anaerob T;Endurance - Anaerob P;Endurance - Speed;Time Swimming;Strength -Base;Strength Max;Strength Ekspolosive;Mobility / Stretching;Swimming Crawl;Swimming Own;Swimming Kick;Swimming Legs;Swimming Arms;Swimming Other;Swimming Technique;Rest. Drink During Training;Rest. Nutrition during training;Rest. Nutrtion after training;Rest. Sleep/rest after training;Rest. Physical treatment after training;Perceived Excertion;Form 1-10;CompetitionTime;Kommentarer\\r\\n2022-02-04;\\"Hello world, \\nthis is traning program\\";;1000;2000;3000;4000;5000;6000;7000;8000;2:02:00;;;;;1100;1200;1300;1400;1500;1600;1700;;;;;;;;;\\r\\n","sportId":"08d60015402ff40ddac564839c40516d"}'

response = requests.post('https://www.bestr.no/api/migration/import/csv', headers=headers, cookies=cookies, data=data)
