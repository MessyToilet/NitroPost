import requests

url = 'https://api.discord.gx.games/v1/direct-fulfillment'
headers = {
    'authority': 'api.discord.gx.games',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://www.opera.com',
    'referer': 'https://www.opera.com/',
    'sec-ch-ua': '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0',
}
data = {
    'partnerUserId': 'd5c4204872690962c2a3d9ebcf86e7712341efc8bc43727611940a6a08c85bda'
}
preTxt = 'https://discord.com/billing/partner-promotions/1180231712274387115/'

print(f'''   
 _   _ _____ _______ _____   ____    _____   ____   _____ _______ 
| \ | |_   _|__   __|  __ \ / __ \  |  __ \ / __ \ / ____|__   __|
|  \| | | |    | |  | |__) | |  | | | |__) | |  | | (___    | |   
| . ` | | |    | |  |  _  /| |  | | |  ___/| |  | |\___ \   | |   
| |\  |_| |_   | |  | | \ \| |__| | | |    | |__| |____) |  | |   
|_| \_|_____|  |_|  |_|  \_\\____/  |_|     \____/|_____/   |_|                
By: MessyToilet''')
input("\n( Enter ) to begin...")

for i in range(1, 100):
    file   = 'nitro_posts{i}.txt'
    runs = 48
    collection = []
    for _ in range(runs):
        response = requests.post(url, headers=headers, json=data)
        print(f'Status: {response.status_code}\nResponse: {response.text}\n')

        data_dict = response.json()
        token_value = data_dict.get('token', None)

        print(f'Stuffing: {token_value}\n')
        collection.append(preTxt + token_value)

    with open(file, 'w') as FILE:
        FILE.write(f'Keys: {runs}\n')
        for token in collection:
            FILE.write(token + '\n\n')
print(f'\n\n------ ! (48 x 100) NITRO KEYS GENERATED ! ------')