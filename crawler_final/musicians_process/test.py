import json
import requests
from bs4 import BeautifulSoup

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "max-age=0",
    "priority": "u=0, i",
    "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"
}

csrf_token = '634edee8766709b69e9d167c72d759e0'

cookies = {
    "NMTID": "00OM-YFvjH-Q3vpzUsvnQE49Qp8byoAAAGMoTyH_Q",
    "_iuqxldmzr_": "32",
    "_ntes_nnid": "d2269373aeb4272d891d86d6e1169aa1,1703512146865",
    "_ntes_nuid": "d2269373aeb4272d891d86d6e1169aa1",
    "WEVNSM": "1.0.0",
    "WNMCID": "usmpqp.1703512147064.01.0",
    "WM_TID": "R6p2eE1QnUJAVRUFVQPE4IhHCvSB+Bh+FM",
    "sDeviceId": "YD-VhUeTzHDegVFV1UVVVbRpZkTSrCCSY9M",
    "ntes_utid": "tid._.DYyLjlvOEJlFEwVQQBfE4YhWWuSTDd9A._.0",
    "__snaker__id": "wo1LR6WcJE5WpTou",
    "ntes_kaola_ad": "1",
    "playerid": "35411709",
    "_ntes_origin_from": "baidu",
    "__csrf": "634edee8766709b69e9d167c72d759e0",
    "WM_NI": "1Nqlj6UxVhqYdRp0xI3+ZLHwsxt7xPCByKvzgJMiGSK+BrSZYUJ0P1DyMwsSm6NZBtUIe99xKksDcb0dHs3fn+FIU86L7MU55gBBKayCr1rXFf0ZXKguqJh+By+Fn2kiV2BgRzU=",
    "WM_NIKE": "9ca17ae2e6ffcda170e2e6eed8b44985ee8faed146edac8fa3c44f938b8eacd64f8b88a4b7d054b89783afe12af0fea7c3b92af392bf8de93e97a89a89f453a88ec0d1fb43f1f196adcb7db1a8bcd8fb5c819eb7acf572a596838ac65989f5beb4d953979600b1b450bb93b994d267f69296a3f75f8bbbf7dafb41a9ad8c84e13ca898bdd4e566ed979bd9b548f5939bd6b86d829e8582fc49b2efbeb9c56ef48698ace67fb396a8ccfc25aeeea58ad53a82b99e9bd837e2a3",
    "NTES_P_UTID": "1tJ8CvaA7oK7TBwScq7V8W5WFGcgmiWT|1720336683",
    "__remember_me": "true",
    "NTES_YD_SESS": "1jq7jBd7LtMNyJCwuoVYHQ9LWMu5Gd9xcXhgf3Htppm_7LHE7Muc9bypMec0HQBAm3oUqYKlpzuWCu8QbS.2dXdEzyz2LjSHgMN4yzhPwWbCeJvEChKZMWjDj6kvuA46J1uEsUZVp9s.SEfZ6JQO7rh2gdQLeFgKEO.LflZrDGwcaa27a6PrEaXVIUCcnlwc4a4Ki1ksY1Z6N5aZNy6OL0X2SR_nusp2bFFNoJHTlfwPx",
    "S_INFO": "1720336773|0|0&60##|19354880947",
    "P_INFO": "19354880947|1720336773|1|music|00&99|null&null&null#bej&null#10#0|&0||19354880947",
    "__csrf": "34828eab416b5b6e2178bf6fbb3675da",
    "MUSIC_U": "005D5553654A228CDA5B6D85AF2328CD08ECC0A53D4D9B5B4F4D93F5DE66CF9F72DBED62D3BCD6B8DA00C5302E189AFF8753DCBE032D67AC891DA8B6165EEFD28CAE9730A96F29358BC0C6CC89DAC56B3F5AA49CE0F566818508FABDCCFB311AABA0D68BFF2F68F780037368DD93FA32DE7D562996E8E0017BE2F1498ECEB7659844034E4C9A70A06EDFA24323CE31ECFD2D9D9FE8B5EB02FEAA619E7F9491588A6665345AFB9951D4DD8946A1C37719885D3B06F238BB5D24D2F34CB3C892C314CBA6BA18ED59FA9E0C8C137BE832D706A194CA99AD86FAAFC80DCEC8C04E05891EAF06E62A8861AED48BDFBF9369828FEF13E50D635D35B78292DE7656F331DC2FB106DF06D0990F7B5649BD7843F0357D31AF69836E997B112C428F50F0265466608E833840690F6DAA85DF981EA8676BE5C04038BD4FDC23C206A45481FB22AD2954E803D586694649A509B89953B654B5F2345B32D64145CD5B9BFC71F7A82E5AC4DBE9C9CC971C451CC7B5365114",
    "gdxidpyhxdE": "yh+LgkA4+BaHgmimItx4DG+5CLJ4B2nCueDIi6VoZJwEzmdijmPTdsmycDkyoKI0Nz2wf0EJo6zROeYUnAlogg4u74L9mecJhf1kR0ftf20yq0i+HaCLfYJRquu+CoOUnjH285zCgixupakpCHTVHl+BwPLLx4EwG+YNGc5+V38TP47sOkTH:1720338074888",
    "JSESSIONID-WYYY": "BrgWCm5XUqApOrgMEAbNe+88+ffI4D47SE8lEqyl6i2oZKH1DpYqZqjH5URPHiS0gSw76H4XHz4oUuQ7y20FYdvz09mXzMwN2syfxhyWyrU+PoCRoy4GShY1lUWymA+Kfx8cx8C1BtFlM1+K7RY1SraS4RJ0DBcjopUmOTo3wDhndaBZ:1720340951905"
}

def extract_ids_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            ids = []
            def find_ids(obj):
                if isinstance(obj, dict):
                    for key, value in obj.items():
                        if key == 'id':
                            ids.append(value)
                        else:
                            find_ids(value)
                elif isinstance(obj, list):
                    for item in obj:
                        find_ids(item)
            find_ids(data)
            return ids
    except Exception as e:
        print(f"Error reading or processing file: {e}")
        return []

ids = extract_ids_from_file('music.json')
# print(ids,len(ids))

ids_ = extract_ids_from_file('music_.json')
# print(ids_,len(ids))

id = ids + ids_
# print(id, len(id))

song_saves = set()
for i in id:
    url = "https://music.163.com/artist?id=" + str(i)
    res = requests.get(url, headers=headers, cookies=cookies)
    soup = BeautifulSoup(res.text, features="html.parser")
    song_names = soup.find_all("ul", class_="f-hide")
    for ul in song_names:
        song_ids = ul.find_all("a")
        for songid in song_ids[:25]:
            song_saves.add(str(songid['href'])[9:])
    print("YES")

with open('song_saves.txt', 'w', encoding='utf-8') as file:
    for song_save in song_saves:
        file.write(f"{song_save}\n")