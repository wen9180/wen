# coding = utf-8
#!/usr/bin/python
from base.spider import Spider
from bs4 import BeautifulSoup
import requests
import json
import time
import sys
import re

sys.path.append('..')

xurl = "http://xsayang.fun:12512/index.php"

header_ = {
        'User-Agent': "Dart/2.19(dart:io)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "gzip",
        'referer': "https://www.123pan.com/",
        'origin': "https://www.123pan.com",
        'platform': "android",
        'app-version': "3",
    }
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
}
pm = ''

class Spider(Spider):
    global xurl
    global headerx
    global headers
    global header
    global headerz
    global header_

    def getName(self):
        return "首页"

    def init(self, extend):
        pass

    def isVideoFormat(self, url):
        pass

    def manualVideoCheck(self):
        pass

    def homeContent(self, filter):
        result = {}
        result = {"class": [
                        
                            {"type_id": "35", "type_name": "123"}
                           
                            ],
                  }

        return result
    def homeVideoContent(self):
        pass

    def categoryContent(self, cid, pg, filter, ext):
        result = {}
        videos = []
        url = f'{xurl}/vod/show/id/{cid}/page/{pg}.html'
        res = requests.get(url=url, headers=header)
        res.encoding = "utf-8"
        doc = BeautifulSoup(res.text, 'lxml')
        soups = doc.find_all('div', class_='module-item')
        for i in soups:
            id = i.find('a')['href']
            match = re.search(r'/id/(\d+)', id)
            if match:
                bid = match.group(1)
            name = i.find('a')['title']
            pic = i.find('img')['data-src']
            remarks = i.find('div', class_='module-item-text').text

            video = {
                "vod_id": bid,
                "vod_name": name,
                "vod_pic": pic,
                "vod_remarks": remarks
            }
            videos.append(video)
        result = {'list': videos}
        result['page'] = pg
        result['pagecount'] = 9999
        result['limit'] = 90
        result['total'] = 999999
        return result

    def detailContent(self, ids):
        result = {}
        videos = []
        play_form = ""
        play_kurl = []
        play_urls = []
        did = ids[0]
        url = f'{xurl}/vod/detail/id/{did}.html'
        res = requests.get(url=url, headers=header)
        res.encoding = "utf-8"
        doc = BeautifulSoup(res.text, 'lxml')
        soups = doc.find('div', class_='video-info')
        # print(soups)
        name = soups.find('h1').text
        actors_title = soups.find('span', class_='video-info-itemtitle', string='主演：')
        if actors_title:
            actors_container = actors_title.find_next('div', class_='video-info-item')
            actor_links = actors_container.find_all('a', target='_blank')
            actors = ' / '.join([actor.text.strip() for actor in actor_links])
        director = soups.find('span', class_='video-info-items')
        content = soups.find('p').text
        remarks = soups.find('div', class_='tag-link').text.replace('\n', '')
        tag_links = soups.find_all('a', class_='tag-link')
        if len(tag_links) > 1:
            year = tag_links[1].text.strip()
        if len(tag_links) > 1:
            area = tag_links[2].text.strip()
        kjson = doc.find('div', id='download-list')
        if kjson:
            tab_content = kjson.find('div', class_='module-tab-content')
            if tab_content:
                tabs = tab_content.find_all('div', class_='module-tab-item')
                sources = []
                for item in tabs:
                    span = item.find('span')
                    if span and span.get('data-dropdown-value'):
                        source_name = span.get('data-dropdown-value')
                        sources.append(source_name)
                play_form = '$$$'.join(sources)
            row = kjson.find('div', class_='scroll-box-y')
            if row:
                kurl = row.find_all('div', class_='module-row-info')
                for k in kurl:
                    urls = k.find('p').text.strip()
                    id = 'http://niiuma.qi-simple.top/cloud/?url=' + urls
                    res = requests.get(url=id, headers=header)
                    kjson = res.json()
                    if 'list' in kjson and kjson['list']:
                        for i in kjson['list']:
                            play_urls = i['vod_play_url']
                            play_kurl.append(''.join(play_urls).rstrip('#'))
                play_url1 = '$$$'.join(play_kurl)

            video = {
                "vod_id": did,
                "vod_name": name,
                "vod_actor": actors,
                "vod_director": director.text if director else "",
                "vod_content": '臻彩视界',
                "vod_remarks": remarks,
                "vod_year": year,
                "vod_area": area,
                "vod_play_from": play_form,
                "vod_play_url": play_url1
            }
            videos.append(video)

            result['list'] = videos
            return result
    def playerContent(self, flag, id, vipFlags):
            return {'jx': 1, 'parse': 1, 'url': id, 'header': ''}

    def searchContentPage(self, key, quick, page):
        pass

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

