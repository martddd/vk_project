import requests
import vk_access
import json
import json_open

# 'https://api.vk.com/method/METHOD_NAME?PARAMETERS&access_token=ACCESS_TOKEN&v=V'
API_URL = json_open.setting()['app']['api_url']
APP_ID = json_open.setting()['app']['APP_ID']
TOKEN = json_open.setting()['user']['token']

# METHOD = 'friends.get'
METHOD = 'messages.send'

user_id = '14937004'
user_id_msg = '131524133'

msg = '''
это всё еще я)
https://pp.vk.me/c322924/v322924100/25e0/RiacpvqUas4.jpg
'''

def vk_friends():
    url_request = '%s%s?user_id=%s&count=10&fields=name,bdate&order=hints&access_token=%s' % (API_URL, METHOD, user_id, TOKEN)
    r = requests.get(url_request)
    json_r = json.loads(r.text)
    return json_r


def vk_messages_send():
    url_request = '%s%s?user_id=%s&message=%s&access_token=%s' % (API_URL, METHOD, user_id_msg, msg, TOKEN)
    r = requests.get(url_request)
    json_r = json.loads(r.text)
    return json_r

def parse_json(json_list):
    list_friends = {}
    for i in range(len(json_list['response'])):
        try:
            user_id = json_list['response'][i]['user_id']
            first_name = json_list['response'][i]['first_name']
            last_name = json_list['response'][i]['last_name']
            bdate = json_list['response'][i]['bdate']
        except:
            bdate = 'none'

        list_friends[last_name]={
            'user_id':user_id,
            'first_name':first_name,
            'last_name':last_name,
            'bdate':bdate
        }

    return list_friends['Гришутин']


# print(parse_json(vk_friends()))
# print(vk_req())
print(vk_messages_send())
