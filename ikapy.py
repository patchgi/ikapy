'''
@license ikapy v0.0.1
(c) 2017 ikapy https://yagi.me
License: MIT
'''

import urllib
from urllib.request import build_opener, HTTPCookieProcessor
from urllib.parse import urlencode
import http
from http.cookiejar import CookieJar
import codecs
import json

class Ikaring:
    def __init__(self, _session):
        session = "iksm_session=" + _session
        self.opener = build_opener(HTTPCookieProcessor(CookieJar()))
        self.opener.addheaders.append(("Cookie", session))

    def getShopLineUp(self):
        res = self.opener.open("https://app.splatoon2.nintendo.net/api/onlineshop/merchandises")
        return codecs.decode(res.read(), 'unicode-escape')

    def getResults(self):
        res = self.opener.open("https://app.splatoon2.nintendo.net/api/results")
        return codecs.decode(res.read(), 'unicode-escape')

    def getResult(self, _battle_number):
        res = self.opener.open("https://app.splatoon2.nintendo.net/api/results/" + _battle_number)
        return codecs.decode(res.read(), 'unicode-escape')

    def getStageSchejules(self):
        res = self.opener.open("https://app.splatoon2.nintendo.net/api/schedules")
        return codecs.decode(res.read(), 'unicode-escape')

    def getTimeline(self):
        res = self.opener.open("https://app.splatoon2.nintendo.net/api/timeline")
        return codecs.decode(res.read(), 'unicode-escape')

    def getStages(self):
        res = self.opener.open("https://app.splatoon2.nintendo.net/api/data/stages")
        return codecs.decode(res.read(), 'unicode-escape')
