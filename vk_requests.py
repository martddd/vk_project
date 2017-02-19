import requests
from builtins import id

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
user_id_msg = '14937004'
# user_id_msg = '15606483'

msg = 'Сообщение'


def choice_method(id_method):
    methods = {
        "9" : "friends",
        "11" : "groups.get",
        "15" : "messages",
    }
    method = methods[id_method]
    return method


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


def vk_groups_get(id_method):
    url_request = '%s%s?user_id=%s&count=%d&access_token=%s&v=5.62' % (API_URL, choice_method('11'), user_id, 10, TOKEN)
    r = requests.get(url_request)
    json_r = json.loads(r.text)
    return json_r['response']['items']


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
# print(vk_messages_send())
print(vk_groups_get('11'))