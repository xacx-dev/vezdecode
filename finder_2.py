import requests
import json
import time

api_url = 'https://api.vk.com/method'
token = 'a8d60760876c1a72d825f19bf112bc0ce9b28702101b8aa24ce1b3ef80181ce1f7cefb5c4d85cff321be0'
chat_id = 92

get_users_in_chat = requests.get(f"{api_url}/messages.getChat?chat_id={chat_id}&access_token={token}&v=5.130").json()['response']['users']
ids = []
print('Программа работает, ожидайте!')
if not ids:
    for i in get_users_in_chat:
        data = requests.get(f"{api_url}/friends.get?user_id={i}&access_token={token}&v=5.130").json()
        time.sleep(0.24)
        #print(data)
        if('error' not in data):
            gt = {
                'user_id': i,
                'friends':data['response']['items']
            }
            ids.append(gt)
finish = []
s = [0,{}]
for i in get_users_in_chat:
    gt = []
    for j in ids:
        if i == j['user_id']:
            break
        if i in j['friends']:
            gt.append(j['user_id'])
    if gt and len(gt)>1:
        fin_dt = {
            'user': i,
            'his_friends': gt
        }
        if s[0] < len(gt):
            s[0] = len(gt)
            s[1] = fin_dt
print(f"Больше всего друзей в данном чате у - {s[1]['user']}, в кол-ве {s[0]}")
print(f"ID друзей - {s[1]['his_friends']}")


