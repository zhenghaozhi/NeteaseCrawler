import json
import time
import random

import execjs
import requests
from fake_useragent import UserAgent

ua = UserAgent()

def get_argument(music_id, page):
    with open('./comments.js', 'r', encoding='utf-8') as f:
        time_now = int(round(time.time() * 1000))
        aa = '{{"rid":"R_SO_4_{}","threadId":"R_SO_4_{}","pageNo":"{}","pageSize":"20","cursor":"{}","offset":"0","orderType":"1","csrf_token":""}}'.format(
            music_id, music_id, page, time_now)
        bb = '010001'
        cc = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
        dd = '0CoJUm6Qyw8W8jud'
        argument_data = execjs.compile(f.read()).call('d', aa, bb, cc, dd)
        params = argument_data['encText']
        encSecKey = argument_data['encSecKey']
    return params, encSecKey


def get_comment(params, encSecKey):
    url = 'https://music.163.com/weapi/comment/resource/comments/get?csrf_token='
    header = {
        "Origin": "https://music.163.com",
        "Pragma": "no-cache",
        "Referer": "https://music.163.com/song?id=65766",
        "Sec-Ch-Ua": "\"Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"115\", \"Chromium\";v=\"115\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "user-agent": ua.random
    }
    data = {
        "params": f"{params}",
        "encSecKey": f"{encSecKey}"
    }
    response = requests.post(url=url, headers=header, data=data, cookies=random.choice(cookies_list))
    data = response.text
    return data


def parse_data(data):
    json_data = json.loads(data)
    comments = json_data['data']['comments']
    # print('')
    for i in comments:
        #print(i)
        comment = i['content']
        nickname = i['user']['nickname']
        print(nickname, comment)


cookies1 = {
    "NMTID": "00O50xBUphWIaHLQkBxr8aWOtpYEH8AAAGQnhIQAg",
    "JSESSIONID-WYYY": "iFTBD%2FToVWFF7X%2FSTqDj4YTQIUuAwryk%2BVrc%5Cf5Ee9X7sMJosBgzOPy%5CSk5r6Q5CPCP%2BRNvoNGMwmzaFsPAkkNAXcEXe%2BmAoNgAyddNz7D8KgJAwxnYb75OXyAD%5CpncDGkxNIJM%2BsBICZ0Xzv3jFphigsT2YjW5E%5Ck%5CTh8M%2Bi4moPt9u%3A1720640702123",
    "_iuqxldmzr_": "32",
    "_ntes_nnid": "33fb20c76918f5f102af858e5acd5d19,1720638902144",
    "_ntes_nuid": "33fb20c76918f5f102af858e5acd5d19",
    "WEVNSM": "1.0.0",
    "WNMCID": "jeyxei.1720638902927.01.0",
    "WM_NI": "CvKoKH0f87v6ZbDEB9aN7vAHN14WOixP3LRns352v%2Fd3Di9AAXoLXrxsPHvyQSnwtUiuG7m5VPS1biWL5R6qHQF2viuudY7N8KRxXmYO8YdO5qBSOMyOsNlirgDXP2K2YVU%3D",
    "WM_NIKE": "9ca17ae2e6ffcda170e2e6ee8ef33cb5be83b4cb33a5e78bb3d15a968e9bb1db4a8e94bcb6ea7d88978799d42af0fea7c3b92a81aa8590ca44f4baf8d8f53e9abe8ca6c133a392f997c4448eeffcb8ce63bc90fdadd166b1edfbd3f525a8ed8c8abc4b8388a1addb7abcada0a9f573938da298f75fabab89d8f03f96909dd2e1639594fbb3b57b8c8f8ad3f563b7abacbab646fc959e99db679b91f8bae745f7af8eb4ce47bb91bdafef63b2b98cb9d33a89ee97b7d837e2a3",
    "WM_TID": "JWKkse%2BpoX5FRQFQRFLGVIf5ElgWNMlQ",
    "sDeviceId": "YD-VApG0A9tBB9AQhEQBFKSFDkHMVljieZT",
    "ntes_utid": "tid._.yY13lEt%252BzcNBFgBQBAfSFZP4Rl1Dzv3w._.0"
}

cookies2 = {
    "NMTID": "00OnBJmg4aEEfLa30ZkhhZJOPZ05WkAAAGQnalYRw",
    "JSESSIONID-WYYY": "eYeIWjgMujfIsW2d5dgxxiOPgtPVp2X2m9zhgOvOW%2FtQtxqXynXMGOolZ2obBsPxv6%5Cq7jwMFJsQCGpN3%2B%2FbJZ41H4KhjpT7z%5CEaWU5GYrxtPW9oqVm58pXBhthDvDOaxvz1G4VWHdS%2Ftv%2FFAjXAyWB6QQikZ3RcYrzyCFkMpQ6SVinh%3A1720633839689",
    "_iuqxldmzr_": "32",
    "_ntes_nnid": "95f5b8c34bdb303dd9ca4a7ae1f35750,1720632039702",
    "_ntes_nuid": "95f5b8c34bdb303dd9ca4a7ae1f35750",
    "WEVNSM": "1.0.0",
    "WNMCID": "thkabg.1720632041706.01.0",
    "WM_NI": "m8%2F95Vq3Te0mzIymDV3P97MGCazPGBczt156G4XrFWkf4ZLhnCL4FjsvjmmLs1tLwot%2B7VQURThDsE5USKw5WSClBypgak95aL%2BUZ6BS1A0dLGItb6fLLtbAOdB4yIUnYmo%3D",
    "WM_NIKE": "9ca17ae2e6ffcda170e2e6eeb4ca738a949d97fb64e9b08ab7d55e838f9f83cb5aa895fd9acd42f89283d9ec2af0fea7c3b92aafe8e1dab85eb3ed9c86b367ba97b78ec75ef190f7d8d04d81bfb6b1c64aa1a6bcd2b83e85ec9893c55da9bafcbbcf64ae9d84d5c562b1aaa68ef048b1efbcadf665b8f5f9b7d45f928ca8a5f24ff78b9dacf63f958d8d8dc173b4b9af8cbc3fa394e5b6d93e828dffa2b37090998795e13ea6948495e14b8dbc8ed5fc4397b2978eee37e2a3",
    "WM_TID": "7y0%2BmsjaPxlEEVRUAQKCUdK3jYcoYM8z",
    "sDeviceId": "YD-MR7QQT25ZQhBUhVEUROGQZO3nJI8gx2K",
    "ntes_utid": "tid._.mY0%252FvFtUD5ZEA1BFVQLDAYan3NYolg2G._.0"
}

cookies3 = {
    "NMTID": "00OkHxRDwGmGRHaFkCunyllUMUt_bMAAAGQnhHuOw",
    "JSESSIONID-WYYY": "Hagh8IOO%2FG9m3vn0nf4V%2F2SB%5CqlhYtbtdi6wsV6M1Ax9UvVUWxN%2FUh79ZQQti1u6JoFMQoOONZmY7q9ryMSWRUCOSwGF8FgU7jyK6Td%2FJvxX%2By3wZokvC5coEoYF5bodHKiRUhqFx%2BOTv88bdGn1iPv1l%2FY07iiogThd678x49j4zq4j%3A1720640693767",
    "_iuqxldmzr_": "32",
    "_ntes_nnid": "c7283d23c34c50ec5a735785ee82f1b2,1720638893791",
    "_ntes_nuid": "c7283d23c34c50ec5a735785ee82f1b2",
    "WEVNSM": "1.0.0",
    "WNMCID": "xvrgka.1720638894459.01.0",
    "WM_NI": "P2aaWU3y2csaconlX3suPkOXmqMuqpp8WOU4Dv%2BPMhZjDHIF0tyzu%2F%2Ba9yqdExm6wu8x41o3OrwF2CSsgp7MyQkDVJtww%2FDSZ1Kq6hVQkgxtuYIDXRStsuf3%2B2FnFeGMdkc%3D",
    "WM_NIKE": "9ca17ae2e6ffcda170e2e6ee95d280b6bdadb8c849f7b48ba7c85e839a8badc65ba8bafcb6b46af5ea9883ce2af0fea7c3b92a94eeaf82d65ff1a7fe84f26ba1b1a28ddb39b1aba08cce54afaf8396f47cb4e899b0d84088aae5b1d0649ab68ca9cc4ef4acb79bf825e9bff79af47087a8a3d7f67ffca8fcd2ee398daeb9a7b14991ada991b647bb8fa5a5d542b8a9b9d0c7599aef8592b564968fa588fb80b78787a5db5a91acbd96e539e9ee8a8fc56f8593ac8ce237e2a3",
    "WM_TID": "hMjRk9uwvZBEURQRFRfSFYOtV0a66HLb",
    "sDeviceId": "YD-vP4l6t64O0NAR0AAFELCQJPoFwxEAvRw",
    "ntes_utid": "tid._.2Jv3BUo%252FaopAA0UFUBbHBYfoF1xEcuRJ._.0"
}

cookies4 = {
    "NMTID": "00OqPKOtTnKRKTcmEZxrNbm3dNNdCYAAAGQnl0zmg",
    "JSESSIONID-WYYY": "Dmj%2FOf7zN9KVXF0fdxZf%5CRcnIwiUo%2Bh4YioUYjaRC5E6T9FN6Ud%2BPrP5ilmXiiu%2F%2BG7%2FGmezJPOzMSSFuRRUz5k5NcnFZRsxcFNWwFm2JjIFjpiveQcRjOsIp7%2B%5CspZMcnkj4BMsban2AxN4q4Cy2RihxpHTPsw8bvB1YtvHZwhxEKMt%3A1720645627080",
    "_iuqxldmzr_": "32",
    "_ntes_nnid": "aefe0fd4ae5519d99226ad9b6b1e2a74,1720643827094",
    "_ntes_nuid": "aefe0fd4ae5519d99226ad9b6b1e2a74",
    "WEVNSM": "1.0.0",
    "WNMCID": "jyzemu.1720643829526.01.0",
    "WM_NI": "hzhjBZ%2Fhemky8a%2FMNsUmiivrjRfd5XSLZ3o4lCxYVRt4tFvJ1%2FXMfanGLOP45p9Faa4%2FMpIPtrEaMEZ2ev1P3ClR31fYhyb2SUdXzTFEwG8q4zwmyz1cpxNIVJUFvnxJbVA%3D",
    "WM_NIKE": "9ca17ae2e6ffcda170e2e6eea8eb3cb2a7fb92b1538aac8eb7c45e978b9e86c74e9a90c085b542f398a1d2e12af0fea7c3b92aaca6a88bc152edb8ab8eea73fcbfe1aecd7997b3a78af57aaa8eaa85b854919496d4ee40b09db8bad55ab8ecbca7f542f3f198aee56bae9984b0d340f7b0f7a7e46bf8f18391cc5cb8ae8b82d04f9aeeab97b45cf19da4b3b23ba687a89ae13a918bacb9f960869bb9a8bb7bf8a6b98efc72f3bdc099cd4396969ba7f566bc96aeb7c437e2a3",
    "WM_TID": "xTH1IoMtW2BBVVEAQQeGVdOoI%2FYwDpwa",
    "ntes_utid": "tid._.1bXwBg0qx%252BVEBxEVFRLTAZP9J7JhTzNE._.0",
    "sDeviceId": "YD-w9oafKFMc%2FpBRgAAQVbGENKtJrZhXrl8"
}


cookies_list = [cookies1, cookies2, cookies3, cookies4]



def get_comment_api(id):
    comments = {}
    page = 1
    # print(id, page)
    params, encSecKey = get_argument(id, page)
    response_data = get_comment(params, encSecKey)
    json_data = json.loads(response_data)
    comments_tmp = json_data['data']['comments']
    for i in comments_tmp:
        comments[i['user']['nickname']] = i['content']
    return comments