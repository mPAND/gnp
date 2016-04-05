#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
gnp (Google News Parser)
========================



gnp (Google News Parser) is a simple python module to parse news articles from google news website
It offers output in json format for all available editions, along with location overloading.
Also, it offers search results of news article for user supplied text.

Basic Usage:

::: Get news for Google News Indian Edition
>>> import gnp
>>> a = gnp.get_google_news(gnp.EDITION_ENGLISH_INDIA)

::: Get news for Google News US Version as if browsing from London,UK
>>> import gnp
>>> b = gnp.get_google_news(gnp.EDITION_ENGLISH_US,geo='London,UK')

::: Get news for search Query "What's happening on earth".
    Default you get results for 'Barack Obama'
>>> import gnp
>>> c = gnp.get_google_news_query("What's happening on earth")

::: Method to write to flatfile

>>> import gnp
>>> d = gnp.get_google_news(gnp.EDITION_ENGLISH_INDIA)

>>> import codecs
>>> import json

>>> j = json.dumps(d, indent=4, ensure_ascii=False )
>>> f = codecs.open( 'news.json', 'w', encoding='utf-8')
>>> f.write(j.decode('utf-8'))
>>> f.close()

List of Editions :

+------------------------------+--------------------------------+
|         Edition Name         |             Region             |
+------------------------------+--------------------------------+
| EDITION_SPANISH_ARGENTINA    | Argentina                      |
| EDITION_ENGLISH_AUSTRALIA    | Australia                      |
| EDITION_DUTCH_BELGIUM        | België                         |
| EDITION_FRENCH_BELGIUM       | Belgique                       |
| EDITION_ENGLISH_BOTSWANA     | Botswana                       |
| EDITION_PORTUGESE_BRAZIL     | Brasil                         |
| EDITION_ENGLISH_CANADA       | Canada English                 |
| EDITION_FRENCH_CANADA        | Canada Français                |
| EDITION_CZECH_CZECH_REPUBLIC | Česká republika                |
| EDITION_SPANISH_CHILE        | Chile                          |
| EDITION_SPANISH_COLUMBIA     | Colombia                       |
| EDITION_SPANISH_CUBA         | Cuba                           |
| EDITION_DEUTSCH_DEUTSCHLAND  | Deutschland                    |
| EDITION_SPANISH_SPAIN        | España                         |
| EDITION_SPANISH_US           | Estados Unidos                 |
| EDITION_ENGLISH_ETHIOPIA     | Ethiopia                       |
| EDITION_FRENCH_FRANCE        | France                         |
| EDITION_ENGLISH_GHANA        | Ghana                          |
| EDITION_ENGLISH_INDIA        | India                          |
| EDITION_ENGLISH_IRELAND      | Ireland                        |
| EDITION_ENGLISH_ISREAL       | Israel English                 |
| EDITION_ITALIAN_ITALY        | Italia                         |
| EDITION_ENGLISH_KENYA        | Kenya                          |
| EDITION_HUNGARIAN_HUNGARY    | Magyarország                   |
| EDITION_ENGLISH_MALAYSIA     | Malaysia                       |
| EDITION_FRENCH_MORACCO       | Maroc                          |
| EDITION_SPANISH_MEXICO       | México                         |
| EDITION_ENGLISH_NAMIBIA      | Namibia                        |
| EDITION_DUTCH_NEDERLAND      | Nederland                      |
| EDITION_ENGLISH_NEW_ZEALAND  | New Zealand                    |
| EDITION_ENGLISH_NIGERIA      | Nigeria                        |
| EDITION_NORSK_NORWAY         | Norge                          |
| EDITION_DEUTSCH_AUSTRIA      | Österreich                     |
| EDITION_ENGLISH_PAKISTAN     | Pakistan                       |
| EDITION_SPANISH_PERU         | Perú                           |
| EDITION_ENGLISH_PHILIPPINES  | Philippines                    |
| EDITION_POLISH_POLAND        | Polska                         |
| EDITION_PORTUGUESE_PORTUGAL  | Portugal                       |
| EDITION_GERMAN_SWITZERLAND   | Schweiz                        |
| EDITION_FRENCH_SENEGAL       | Sénégal                        |
| EDITION_ENGLISH_SINGAPORE    | Singapore                      |
| EDITION_ENGLISH_SOUTH_AFRICA | South Africa                   |
| EDITION_FRENCH_SWITZERLAND   | Suisse                         |
| EDITION_SWEDISH_SWEDEN       | Sverige                        |
| EDITION_ENGLISH_TANZANIA     | Tanzania                       |
| EDITION_TURKISH_TURKEY       | Türkiye                        |
| EDITION_ENGLISH_UK           | U.K.                           |
| EDITION_ENGLISH_US           | U.S.                           |
| EDITION_ENGLISH_UGANDA       | Uganda                         |
| EDITION_SPANISH_VENEZUELA    | Venezuela                      |
| EDITION_VIETNAMESE_VIETNAM   | Việt Nam (Vietnam)             |
| EDITION_ENGLISH_ZIMBABWE     | Zimbabwe                       |
| EDITION_GREEK_GREECE         | Ελλάδα (Greece)                |
| EDITION_RUSSIAN_RUSSIA       | Россия (Russia)                |
| EDITION_SERBIAN_SERBIA       | Србија (Serbia)                |
| EDITION_RUSSIAN_UKRAINE      | Украина / русский (Ukraine)    |
| EDITION_UKRAINIAN_UKRAINE    | Україна / українська (Ukraine) |
| EDITION_HEBREW_ISRAEL        | ישראל (Israel)                 |
| EDITION_ARABIC_UAE           | الإمارات (UAE)                     |
| EDITION_ARABIC_SAUDI_ARABIA  | السعودية (KSA)                    |
| EDITION_ARABIC_ARAB_WORLD    | العالم العربي (Arabic)              |
| EDITION_ARABIC_LEBANON       | لبنان (Lebanon)                  |
| EDITION_ARABIC_EGYPT         | مصر (Egypt)                     |
| EDITION_HINDI_INDIA          | हिन्दी (India)                    |
| EDITION_TAMIL_INDIA          | தமிழ் (India)                    |
| EDITION_TELUGU_INDIA         | తెలుగు (India)                |
| EDITION_MALAYALAM_INDIA      | മലയാളം (India)                 |
| EDITION_KOREAN_SOUTH_KOREA   | 한국 (Korea)                    |
| EDITION_CHINESE_CHINA        | 中国 (China)                    |
| EDITION_CHINESE_TAIWAN       | 台灣 (Taiwan)                   |
| EDITION_JAPANESE_JAPAN       | 日本 (Japan)                    |
| EDITION_JAPANESE_HONG_KONG   | 香港 (Hong Kong)                |
+------------------------------+--------------------------------+

Copyright (c) 2016,  Manuel David Pandian
License : MIT (see LICENSE for details)
"""

__author__ = ' Manuel David Pandian'
__version__ = '0.0.2'
__license__ = 'MIT'
__all__ = ['get_google_news', 'get_google_news_query']


import urllib
import urllib.request
import urllib.parse
from lxml import etree
import datetime

# List of Constants

EDITION_SPANISH_ARGENTINA = 'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=es_ar'
EDITION_ENGLISH_AUSTRALIA =	'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=au'
EDITION_DUTCH_BELGIUM = 'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=nl_be'
EDITION_FRENCH_BELGIUM = 'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=fr_be'
EDITION_ENGLISH_BOTSWANA = 'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=en_bw'
EDITION_PORTUGESE_BRAZIL = 'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=pt-BR_br'
EDITION_ENGLISH_CANADA = 'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=ca'
EDITION_FRENCH_CANADA = 'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=fr_ca'
EDITION_CZECH_CZECH_REPUBLIC = 'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=cs_cz'
EDITION_SPANISH_CHILE =	'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=es_cl'
EDITION_SPANISH_COLUMBIA = 'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=es_co'
EDITION_SPANISH_CUBA = 'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=es_cu'
EDITION_DEUTSCH_DEUTSCHLAND	= 'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=de'
EDITION_SPANISH_SPAIN = 'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=es'
EDITION_SPANISH_US	= 'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=es_us'
EDITION_ENGLISH_ETHIOPIA = 'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=en_et'
EDITION_FRENCH_FRANCE =	'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=fr'
EDITION_ENGLISH_GHANA =	'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=en_gh'
EDITION_ENGLISH_INDIA =	'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=in'
EDITION_ENGLISH_IRELAND	= 'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=en_ie'
EDITION_ENGLISH_ISREAL	= 'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=en_il'
EDITION_ITALIAN_ITALY =	'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=it'
EDITION_ENGLISH_KENYA = 'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=en_ke'
EDITION_HUNGARIAN_HUNGARY =	'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=hu_hu'
EDITION_ENGLISH_MALAYSIA = 'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=en_my'
EDITION_FRENCH_MORACCO = 'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=fr_ma'
EDITION_SPANISH_MEXICO = 'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=es_mx'
EDITION_ENGLISH_NAMIBIA	= 'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=en_na'
EDITION_DUTCH_NEDERLAND	= 'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=nl_nl'
EDITION_ENGLISH_NEW_ZEALAND	=	'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=nz'
EDITION_ENGLISH_NIGERIA	= 'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=en_ng'
EDITION_NORSK_NORWAY = 'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=no_no'
EDITION_DEUTSCH_AUSTRIA	= 'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=de_at'
EDITION_ENGLISH_PAKISTAN = 'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=en_pk'
EDITION_SPANISH_PERU = 'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=es_pe'
EDITION_ENGLISH_PHILIPPINES	= 'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=en_ph'
EDITION_POLISH_POLAND = 'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=pl_pl'
EDITION_PORTUGUESE_PORTUGAL	= 'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=pt-PT_pt'
EDITION_GERMAN_SWITZERLAND = 'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=de_ch'
EDITION_FRENCH_SENEGAL = 'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=fr_sn'
EDITION_ENGLISH_SINGAPORE = 'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=en_sg'
EDITION_ENGLISH_SOUTH_AFRICA = 'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=en_za'
EDITION_FRENCH_SWITZERLAND = 'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=fr_ch'
EDITION_SWEDISH_SWEDEN	= 'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=sv_se'
EDITION_ENGLISH_TANZANIA = 'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=en_tz'
EDITION_TURKISH_TURKEY	= 'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=tr_tr'
EDITION_ENGLISH_UK	= 'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=uk'
EDITION_ENGLISH_US	= 'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=us'
EDITION_ENGLISH_UGANDA	= 'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=en_ug'
EDITION_SPANISH_VENEZUELA = 'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=es_ve'
EDITION_VIETNAMESE_VIETNAM	= 'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=vi_vn'
EDITION_ENGLISH_ZIMBABWE = 'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=en_zw'
EDITION_GREEK_GREECE = 'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=el_gr'
EDITION_RUSSIAN_RUSSIA = 'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=ru_ru'
EDITION_SERBIAN_SERBIA = 'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=sr_rs'
EDITION_RUSSIAN_UKRAINE	= 'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=ru_ua'
EDITION_UKRAINIAN_UKRAINE = 'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=uk_ua'
EDITION_HEBREW_ISRAEL = 'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=iw_il'
EDITION_ARABIC_UAE = 'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=ar_ae'
EDITION_ARABIC_SAUDI_ARABIA	= 'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=ar_sa'
EDITION_ARABIC_ARAB_WORLD = 'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=ar_me'
EDITION_ARABIC_LEBANON	= 'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=ar_lb'
EDITION_ARABIC_EGYPT = 'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=ar_eg'
EDITION_HINDI_INDIA	= 'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=hi_in'
EDITION_TAMIL_INDIA	= 'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=ta_in'
EDITION_TELUGU_INDIA = 'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=te_in'
EDITION_MALAYALAM_INDIA	= 'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=ml_in'
EDITION_KOREAN_SOUTH_KOREA	= 'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=kr'
EDITION_CHINESE_CHINA = 'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=cn'
EDITION_CHINESE_TAIWAN	= 'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=tw'
EDITION_JAPANESE_JAPAN	= 'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=jp'
EDITION_JAPANESE_HONG_KONG	= 'https://news.google.com/news?hl=en&tab=nn&edchanged=1&authuser=0&ned=hk'


def _parse_url(url):
    r = urllib.request.urlopen(url).read()
    page = etree.HTML(r)
    return page


def _parse_stories_page(page, category):
    h2 = page[1][5][0][0][0][2][0][0][0][1][0][0][2][0][0]
    c = len(h2)
    pg0 = []
    for cj in range(0, c):
        if h2[cj].attrib['class'].split()[0] == 'blended-wrapper':
            ll = len(h2[cj][0][0][0][1][0][0][0])
            for cl in range(0, ll):
                if h2[cj][0][0][0][1][0][0][0][cl].attrib['class'] == 'esc-layout-article-cell':
                    SRC = h2[cj][0][0][0][1][0][0][0][cl][1][0][0][0][0][0]\
                        .xpath("string()").encode('utf-8')
                    HL = h2[cj][0][0][0][1][0][0][0][cl][0][0][0][0]\
                        .xpath("string()").encode('utf-8')
                    CONTEXT = h2[cj][0][0][0][1][0][0][0][cl][2]\
                        .xpath("string()").encode('utf-8')
                    URLLINK = h2[cj][0][0][0][1][0][0][0][cl][0][0][0]\
                        .attrib['url'].encode('utf-8')
                    pg = {}
                    pg["title"] = HL
                    pg["link"] = URLLINK
                    pg["source"] = SRC
                    pg["content_snippet"] = CONTEXT
                    pg["category"] = category
                    pg0.append(pg)
    return pg0


def get_google_news(url, geo="detect_metro_area", detailed=False):
    page = _parse_url(url)
    # print "List of Topics"
    i = len(page[1][5][0][0][0][1][0][0])
    data = {}
    data['topics'] = []
    data['subtopics'] = {}
    data['stories'] = []
    data['meta'] = {}
    data['meta']['url'] = url
    now = datetime.datetime.now()
    data['meta']['timestamp'] = str(now)
    for idx in range(0, i):
        t = page[1][5][0][0][0][1][0][0][idx][0].text.encode('utf-8')
        data['topics'].append(t)
        data['subtopics'][t] = []
        if page[1][5][0][0][0][1][0][0][idx][0].tag == 'span':
            if len(page[1][5][0][0][0][1][0][0][idx]) > 1:
                j = len(page[1][5][0][0][0][1][0][0][idx][1])
                for idx2 in range(0, j):
                    st = page[1][5][0][0][0][1][0][0][idx][1][idx2][0]\
                        .text.encode('utf-8')
                    data['subtopics'][t].append(st)
        elif page[1][5][0][0][0][1][0][0][idx][0].tag == 'a':
            url2 = 'https://news.google.com' + page[1][5][0][0][0][1][0][0][idx][0]\
                .attrib['href']
            if 'detect_metro_area' in url2:
                url2 = url2.replace('detect_metro_area',
                                    urllib.parse.quote(geo))
                page2 = _parse_url(url2)
                t2 = page2[1][5][0][0][0][2][0][0][0][1][0][0][2][0][0][0][0][0][0][0]\
                    .text
                data['topics'].remove(t)
                data['topics'].append(t2)
                del data['subtopics'][t]
                data['subtopics'][t2] = []
                t = t2
            else:
                page2 = _parse_url(url2)
            if page2[1][5][0][0][0][1][0][0][idx][0].tag == 'span' \
                    and len(page2[1][5][0][0][0][1][0][0][idx]) == 2:
                j2 = len(page2[1][5][0][0][0][1][0][0][idx][1])
                for idx3 in range(0, j2):
                    st = page2[1][5][0][0][0][1][0][0][idx][1][idx3][0].text
                    sthref = 'https://news.google.com' + page2[1][5][0][0][0][1][0][0][idx][1][idx3][0]\
                        .attrib['href']
                    data['subtopics'][t].append({st: sthref})
                    if detailed:
                        data['stories'].extend(
                            _parse_stories_page(_parse_url(sthref), st)
                        )
            # else:
                # print ">> No Side Sub Topics. Need to Parse next pane <<"
            data['stories'].extend(
                _parse_stories_page(page2, t)
            )
    return data


def get_google_news_query(q="Barack Obama"):
    page = _parse_url('https://news.google.com/news?q='+urllib.parse.quote(q))
    data = {}
    data['stories'] = []
    now = datetime.datetime.now()
    data['meta'] = {}
    data['meta']['timestamp'] = str(now)
    data['stories'].extend(
        _parse_stories_page(page, q)
    )
    data['meta']['url'] = 'https://news.google.com/news?q=' +\
        urllib.parse.quote(q)
    return data
