# -*- coding:utf8 -*- 
# Author: shizhenyu96@gamil.com
# github: https://github.com/imndszy
import json
import requests
import sys

if sys.version_info < (3, 0):
    reload(sys)
    sys.setdefaultencoding('utf8')

from nova_weixin.app.weixin.get_acc_token import get_token
from nova_weixin.app.weixin.weixinconfig import MENU


def create_menu():
    acc_token = get_token()
    if acc_token:
        url = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s" % acc_token
        data = MENU
        r = requests.post(url, data=json.dumps(data, ensure_ascii=False))
        return r.text
    else:
        return "failed to get access_token!--menu.py"


if __name__ == "__main__":
    print(create_menu())
