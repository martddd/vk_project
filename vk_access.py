# -*- coding: utf-8
from http.client import HTTPConnection

import requests
# import urllib2
import webbrowser
# import cookielib
import json
import re
import json_open


USER_ID = json_open.setting()['user']['user_id']
EMAIL = json_open.setting()['user']['login']
PASSWORD = json_open.setting()['user']['password']

API_URL = json_open.setting()['app']['api_url']
APP_ID = json_open.setting()['app']['APP_ID']
SETTINGS = json_open.setting()['app']['SETTINGS']
RESPONESE_TYPE = json_open.setting()['app']['RESPONESE_TYPE']
REDIRECT_URI = json_open.setting()['app']['REDIRECT_URI']
DISPLAY = json_open.setting()['app']['DISPLAY']


def service_access_token():
    r = requests.get('https://oauth.vk.com/access_token?client_id=5857160&client_secret=mbi3R2PNkAxVZtsunVYa&grant_type=client_credentials&v=5.62')
    json_r = json.loads(r.text)
    access_token = json_r['access_token']
    return access_token


# def user_access_token():
#     # r = requests.get('https://oauth.vk.com/authorize?client_id=%s&scope=%s&redirect_uri=%s&display=%s&response_type=token' % (APP_ID, SETTINGS, REDIRECT_URI, DISPLAY))
#     # r = requests.get('https://oauth.vk.com/authorize?client_id=%s&scope=%s&redirect_uri=%s&display=%s&response_type=token' % (APP_ID, SETTINGS, REDIRECT_URI, DISPLAY))
#     # new_site = webbrowser.open_new_tab('https://oauth.vk.com/authorize?client_id=%s&scope=%s&redirect_uri=%s&display=%s&response_type=token' % (APP_ID, SETTINGS, REDIRECT_URI, DISPLAY))
#     header_tags_print = {}
#     # site = r.text
#     # header_tags = re.findall(r'<input type="hidden" name="(.+?)" value="(\w.+?)"(| \/)>', site)
#     # for i in range(4):
#     #     header_tags_print.update({header_tags[i][0]: header_tags[i][1]})
#     # return str(header_tags_print['ip_h'])
#     # return new_site
#     return 'https://oauth.vk.com/authorize?client_id=%s&scope=%s&redirect_uri=%s&display=%s&response_type=token' % (APP_ID, SETTINGS, REDIRECT_URI, DISPLAY)
# def user_access_token():
#     r = requests.get('https://oauth.vk.com/authorize?client_id=%s&scope=%s&redirect_uri=%s&display=%s&response_type=%s' % (APP_ID, SETTINGS, REDIRECT_URI, DISPLAY, RESPONESE_TYPE))
#     site = r.text
#     header_tags_print = {}
#     header_tags = re.findall(r'<input type="hidden" name="(.+?)" value="(\w.+?)"(| \/)>', site)
#     for i in range(4):
#         header_tags_print.update({header_tags[i][0]: header_tags[i][1]})
#
#     # form_auth()
#     ip_h = header_tags_print['ip_h']
#     lg_h = header_tags_print['lg_h']
#     to = header_tags_print['to']
#     email = u'medov-artem@mail.ru'
#     passw = u'leavemealone_291089_vkontakte'
#     url = 'https://login.vk.com/?act=login&soft=1&utf8=1&q=1&ip_h=%s&from_host=oauth.vk.com&to=%s&expire=0&email=%s&pass=%s' % (ip_h, to, EMA, passw)
#     req = requests.get('https://login.vk.com/?act=login&soft=1&utf8=1&q=1&ip_h=%s&from_host=oauth.vk.com&lg_h=%s&to=%s&expire=0&email=%s&pass=%s' % (ip_h, lg_h, to, email, passw))
#     # return 'https://login.vk.com/?act=login&soft=1&utf8=1&q=1&ip_h=%s&from_host=oauth.vk.com&to=%s&expire=0&email=%s&pass=%s' % (ip_h, to, email, passw)+'\n'+'https://oauth.vk.com/authorize?client_id=%s&scope=%s&redirect_uri=%s&display=%s&response_type=%s' % (APP_ID, SETTINGS, REDIRECT_URI, DISPLAY, RESPONESE_TYPE)
#     # return req.text+'\n'+ip_h+'\n'+lg_h+'\n'+to

def user_access_token():
    with requests.Session() as s:
        # s.auth(EMAIL, PASSWORD)
        r = s.get('https://oauth.vk.com/authorize?client_id=%s&scope=%s&redirect_uri=%s&display=%s&response_type=%s' % (APP_ID, SETTINGS, REDIRECT_URI, DISPLAY, RESPONESE_TYPE))
        site = r.text
        header_tags_print = {}
        header_tags = re.findall(r'<input type="hidden" name="(.+?)" value="(\w.+?)"(| \/)>', site)
        for i in range(4):
            header_tags_print.update({header_tags[i][0]: header_tags[i][1]})

        ip_h = header_tags_print['ip_h']
        to = header_tags_print['to']
        # req = s.get('https://login.vk.com/?act=login&soft=1&utf8=1&q=1&ip_h=%s&from_host=oauth.vk.com&to=%s&expire=0' % (ip_h, to), auth=(EMAIL, PASSWORD))
        # req = s.auth(EMAIL, PASSWORD)
        url = 'https://oauth.vk.com/authorize?client_id=%s&scope=%s&redirect_uri=%s&display=%s&response_type=%s' % (APP_ID, SETTINGS, REDIRECT_URI, DISPLAY, RESPONESE_TYPE)
    return url


# print(user_access_token())

# print(api_url)
