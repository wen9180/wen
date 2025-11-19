# coding = utf-8
# !/usr/bin/python

from Crypto.Util.Padding import unpad
from Crypto.Util.Padding import pad
from urllib.parse import unquote
from Crypto.Cipher import ARC4
from urllib.parse import quote
from base.spider import Spider
from Crypto.Cipher import AES
from datetime import datetime
from bs4 import BeautifulSoup
from base64 import b64decode
import urllib.request
import urllib.parse
import datetime
import binascii
import requests
import base64
import json
import time
import sys
import re
import os

sys.path.append('..')

xurl = "https://api.bilibili.com"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0',
    'Referer':'https://search.bilibili.com',
    'cookie':'bili_ticket=GciOiJIUz9.eyJleHAiOjE3NDgxODAyOTMsImlhdCI6MTotMX; '
          }
headerx = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0',
    'Referer': 'https://www.bilibili.com',
}

pm = ''


class Spider(Spider):
    global xurl
    global headerx
    global headers

    def getName(self):
        return "B站影视"

    def init(self, extend):
        pass

    def isVideoFormat(self, url):
        pass

    def manualVideoCheck(self):
        pass

    def homeContent(self, filter):
        result = {}
        result = {"class": [
            {"type_id": "热门", "type_name": "热门"},
            {"type_id": "8K", "type_name": "8K"},
            {"type_id": "12K", "type_name": "12K"},
            {"type_id": "演唱会", "type_name": "演唱会"},
            {"type_id": "纪录片", "type_name": "纪录片"},
            {"type_id": "美食", "type_name": "美食"},
            {"type_id": "食谱", "type_name": "食谱"},
            {"type_id": "体育", "type_name": "体育"},
            {"type_id": "球星", "type_name": "球星"},
            {"type_id": "旅游出行", "type_name": "旅游出行"},
            {"type_id": "风景", "type_name": "风景"},
            {"type_id": "电影", "type_name": "电影"},
            {"type_id": "电视剧", "type_name": "电视剧"},
            {"type_id": "综艺", "type_name": "综艺"},
            {"type_id": "番剧", "type_name": "番剧"},
            {"type_id": "国创", "type_name": "国创"},
            {"type_id": "沙雕动漫", "type_name": "沙雕动漫"},
            {"type_id": "沙雕动画", "type_name": "沙雕动画"},
            {"type_id": "短剧", "type_name": "短剧"},
            {"type_id": "影视", "type_name": "影视"},
            {"type_id": "娱乐", "type_name": "娱乐"},
            {"type_id": "舞蹈", "type_name": "舞蹈"},
            {"type_id": "小剧场", "type_name": "小剧场"},
            {"type_id": "动画", "type_name": "动画"},
            {"type_id": "直播", "type_name": "直播"},
            {"type_id": "音乐", "type_name": "音乐"},
            {"type_id": "MV", "type_name": "MV"},
            {"type_id": "舞曲", "type_name": "舞曲"},
            {"type_id": "教育", "type_name": "教育"},
            {"type_id": "游戏", "type_name": "游戏"},
            {"type_id": "生活", "type_name": "生活"},
            {"type_id": "说案", "type_name": "说案"},
            {"type_id": "演讲", "type_name": "演讲"},
            {"type_id": "知名up主", "type_name": "知名up主"},
            {"type_id": "探索发现", "type_name": "探索发现"},
            {"type_id": "鬼畜", "type_name": "鬼畜"},
            {"type_id": "搞笑", "type_name": "搞笑"},
            {"type_id": "儿童", "type_name": "儿童"},
            {"type_id": "动物世界", "type_name": "动物世界"},
            {"type_id": "相声", "type_name": "相声"},
            {"type_id": "小品", "type_name": "小品"},
            {"type_id": "戏曲", "type_name": "戏曲"},
            {"type_id": "解说", "type_name": "解说"},
            {"type_id": "健身", "type_name": "健身"},
            {"type_id": "小姐姐", "type_name": "小姐姐"},
            {"type_id": "荒野求生", "type_name": "荒野求生"},
            {"type_id": "帕梅拉", "type_name": "帕梅拉"},
            {"type_id": "资讯", "type_name": "资讯"},
            {"type_id": "汽车", "type_name": "汽车"},
            {"type_id": "时尚美妆", "type_name": "时尚美妆"},
            {"type_id": "户外", "type_name": "户外"},
            {"type_id": "家装房产", "type_name": "家装房产"},
            {"type_id": "科技数码", "type_name": "科技数码"},
            {"type_id": "白噪音", "type_name": "白噪音"},
            {"type_id": "软件教程", "type_name": "软件教程"},
            {"type_id": "windows", "type_name": "windows"}
        ]}
        return result

    def homeVideoContent(self):
        pass

    def format_views(self, num):
        if num >= 10000:
            return f"{num / 10000:.1f}万"
        else:
            return str(num)

    def categoryContent(self, cid, pg, filter, ext):
        result = {}
        videos = []

        # 自定义分类映射到搜索关键词
        category_keywords = {
            "热门": "热门",
            "直播": "直播",
            "8K": "8K",
            "12K": "12K",
            "演唱会": "演唱会",
            "纪录片": "纪录片",
            "美食": "美食",
            "食谱": "食谱",
            "体育": "体育",
            "球星": "球星",
            "旅游出行": "旅游出行",
            "风景": "风景",
            "电影": "电影",
            "电视剧": "电视剧",
            "综艺": "综艺",
            "番剧": "番剧",
            "国创": "国创",
            "沙雕动漫": "沙雕动漫",
            "沙雕动画": "沙雕动画",
            "短剧": "短剧",
            "影视": "影视",
            "娱乐": "娱乐",
            "舞蹈": "舞蹈",
            "小剧场": "小剧场",
            "动画": "动画",
            "音乐": "音乐",
            "MV": "MV",
            "舞曲": "舞曲",
            "教育": "教育",
            "游戏": "游戏",
            "生活": "生活",
            "说案": "说案",
            "演讲": "演讲",
            "知名up主": "知名up主",
            "探索发现": "探索发现",
            "鬼畜": "鬼畜",
            "搞笑": "搞笑",
            "儿童": "儿童",
            "动物世界": "动物世界",
            "相声": "相声",
            "小品": "小品",
            "戏曲": "戏曲",
            "解说": "解说",
            "健身": "健身",
            "小姐姐": "小姐姐",
            "荒野求生": "荒野求生",
            "帕梅拉": "帕梅拉",
            "资讯": "资讯",
            "汽车": "汽车",
            "时尚美妆": "时尚美妆",
            "户外": "户外",
            "家装房产": "家装房产",
            "科技数码": "科技数码",
            "白噪音": "白噪音",
            "软件教程": "软件教程",
            "windows": "windows",
        }

        keyword = category_keywords.get(cid, "电影")  # 默认搜索"电影"
        url = f'{xurl}/x/web-interface/wbi/search/type?search_type=video&__refresh__=true&page={pg}&page_size=42&keyword={keyword}'
        res = requests.get(url=url, headers=headers)
        res.encoding = "utf-8"
        kjson = json.loads(res.text)
        for i in kjson['data']['result']:
            if str(i['bvid']) == '':
                continue
            id = str(i['bvid'])
            name = i['title']
            pic = i['pic']
            if 'http' not in pic:
                pic = 'http:' + pic
            else:
                pic = pic
            remark = i['play']
            num_str = str(remark).strip()

            num = float(num_str)
            if num >= 100_000_000:
                remarks = f"{num / 100_000_000:.1f}亿播放量"
            elif num >= 10_000:
                remarks = f"{num / 10_000:.1f}万播放量"
            else:
                remarks = f"{num:.1f}播放量"

            video = {
                "vod_id": id,
                "vod_name": name.replace('<em class="keyword">', '').replace('</em>', ''),
                "vod_pic": pic,
                "vod_remarks": remarks
            }
            videos.append(video)

        result['list'] = videos
        result['page'] = pg
        result['pagecount'] = 9999
        result['limit'] = 90
        result['total'] = 999999
        return result

    def detailContent(self, ids):
        result = {}
        videos = []
        did = ids[0]
        url = f'https://www.bilibili.com/video/{did}'
        res = requests.get(url=url, headers=headerx)
        res.encoding = "utf-8"
        res_text = res.text

        start_str, end_str = 'window.__INITIAL_STATE__=', '}};'
        s_idx = res_text.find(start_str)
        if s_idx > -1:
            s_idx += len(start_str)
            e_idx = res_text.find(end_str, s_idx)
            if e_idx > -1:
                kjson_text = res_text[s_idx:e_idx] + '}}'
        kjson = json.loads(kjson_text)

        video_data = kjson.get('videoData', {})
        name = video_data.get('title', '未知标题')
        remarks = video_data.get('tname', '')
        director = video_data.get('owner', {}).get('name', '未知作者')
        content = video_data.get('desc', '')

        play_url = ""
        for i in kjson['availableVideoList'][0]['list']:
            play_url += i['title'] + '$' + f'https://www.bilibili.com/video/{did}?p=' + str(i['p']) + '#'
        play_url = play_url[:-1]

        video = {
            "vod_id": did,
            "vod_name": name,
            "vod_actor": '',
            "vod_director": director,
            "vod_content": content,
            "vod_remarks": remarks,
            "vod_year": '',
            "vod_area": '',
            "vod_play_from": 'B站影视',
            "vod_play_url": play_url
        }
        videos.append(video)

        result['list'] = videos
        return result

    def playerContent(self, flag, id, vipFlags):
        return {'jx': 1, 'parse': 1, 'url': id, 'header': headerx}

    def searchContentPage(self, key, quick, page):
        result = {}
        videos = []
        if not page:
            page = 1
        url = f'{xurl}/x/web-interface/wbi/search/type?search_type=video&__refresh__=true&page={page}&page_size=42&keyword={key}'
        res = requests.get(url=url, headers=headers)
        res.encoding = "utf-8"
        kjson = json.loads(res.text)
        # print(kjson)
        for i in kjson['data']['result']:
            if str(i['bvid']) == '':
                continue
            id = str(i['bvid'])
            name = i['title']
            pic = i['pic']
            if 'http' not in pic:
                pic = 'http:'+pic
            else:
                pic = pic
            remark = i['play']
            num_str = str(remark).strip()

            num = float(num_str)
            if num >= 100_000_000:
                remarks = f"{num / 100_000_000:.1f}亿播放量"
            elif num >= 10_000:
                remarks = f"{num / 10_000:.1f}万播放量"
            else:
                remarks = f"{num:.1f}播放量"

            video = {
                "vod_id": id,
                "vod_name": name.replace('<em class="keyword">', '').replace('</em>', ''),
                "vod_pic": pic,
                "vod_remarks": remarks
            }
            videos.append(video)

        result['list'] = videos
        result['page'] = page
        result['pagecount'] = 9999
        result['limit'] = 90
        result['total'] = 999999
        return result

    def searchContent(self, key, quick, pg="1"):
        return self.searchContentPage(key, quick, '1')

    def localProxy(self, params):
        if params['type'] == "m3u8":
            return self.proxyM3u8(params)
        elif params['type'] == "media":
            return self.proxyMedia(params)
        elif params['type'] == "ts":
            return self.proxyTs(params)
        return None