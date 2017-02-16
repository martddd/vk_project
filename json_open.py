import json


def setting():
    with open('SETTING.json') as json_setting:
        file_setting = json.load(json_setting)
        json_setting.close()
    return file_setting