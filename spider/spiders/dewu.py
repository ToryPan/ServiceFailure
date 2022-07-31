import scrapy
from ..items import DewuItem
import json
from lxml import etree
import math


import execjs
import time
import hashlib

js1 = execjs.compile('''function aa(e, t) {
            var n = ""
              , i = t
              , a = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"];

            for (var o = 0; o < i; o++) {
                n += a[Math.round(Math.random() * (a.length - 1))]
            }
            return n;
        }''')

def get_signature(ts,rs,couid,page):

    js2 = execjs.compile('''function bb(str) {
            var new_str=str.sort().join("");
            return new_str;
        }''')
    u = ts
    d=rs
    l = "$d6eb7ff91ee257475%"
    couid = couid
    e = 1
    c = 10
    h = page
    result = js2.call('bb',[u,d,l,couid,e,c,h])
    print(result)
    hash1 = hashlib.sha256()  # Get the hash algorithm.
    hash1.update(result.encode("utf-8"))  # Hash the data.
    result2 = hash1.hexdigest()
    return(result2)

def get_url(ts,rs,couid,page,value_):
    signature = get_signature(ts,rs,couid,page)
    value_  = value_ + (page - 100)
    url = 'https://tousu.sina.com.cn/api/company/received_complaints?ts={}&rs={}&signature={}&callback=jQuery111206935682897257829_1643471235521&couid={}&type=1&page_size=10&page={}&_={}'.format(ts,rs,signature,couid,page,value_)
    return(url)

def return_url(page,couid,value_):
    # ts = int(time.time()* 1000)
    ts = 1643471235581
    # rs = js1.call('aa','!1',16)
    rs = 'VmYK9ARkx9i3mi26'
    return(get_url(ts,rs,couid,page,value_))


class DewuSpider(scrapy.Spider):
    name = 'dewu'
    allowed_domains = ['tousu.sina.com.cn']
    start_urls = ['http://tousu.sina.com.cn/']

    def parse(self, response):
        # 把所有的url地址统一扔给调度器入队列
        # 1 1198页
        couid = 3787942764
        value_ = 1643471235531
        ts_mount = 8494
        pages = math.ceil(ts_mount / 10)
        for offset in range(102, 110):
            url = return_url(offset,couid,value_)
            # 交给调度器
            print("+" * 50)
            print(offset)
            print(url)
            print("+" * 50)
            path_url = url[url.find('/api'):]
            header = {
                 'authority': 'tousu.sina.com.cn',
                         'method': 'GET',
                         'path': path_url,
                         'scheme': 'https',
                         'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
                         'accept-encoding': 'gzip, deflate, br',
                         'accept-language': 'zh-CN,zh;q=0.9',
                          'cookie': '',#cookie
                         'referer': 'https://tousu.sina.com.cn/company/view/?couid=6416319252',
                         'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
                         'sec-ch-ua-mobile': '?0',
                         'sec-ch-ua-platform': 'Windows',
                         'sec-fetch-dest': 'empty',
                         'sec-fetch-mode': 'cors',
                         'sec-fetch-site': 'same-origin',
                         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
                         'x-requested-with': 'XMLHttpRequest'}


            yield scrapy.Request(
                url=url,
                callback=self.parse_html,
                headers=header,
            )

    def parse_html(self, response):
        cc = response.text[response.text.find("result") - 2:response.text.find("catch(e)") - 3]
        dd_list = json.loads(cc)
        # for循环遍历
        for dd in dd_list["result"]["data"]["complaints"]:
            item = DewuItem()
            item['current_count']=dd_list["result"]["data"]["pager"]["current"]
            item['url_lis'] = "https:" + dd["main"]["url"]
            item['weibo_url'] = dd["author"]["wb_profile"]
            item['summary'] = dd["main"]["summary"]
            # 把爬取的数据交给管道文件pipline处理
            yield scrapy.Request(
                url=item['url_lis'],
                meta={'item': item},
                callback=self.parse_2_html
            )

    def parse_2_html(self, response):
        item = response.meta['item']
        print("_+_+_+_+_+_+_+_+_+_+_+_+_+_")
        print(item['url_lis'])
        parse_html = etree.HTML(response.text)
        item["title"] = parse_html.xpath('//div[@class="ts-d-question"]/h1[@class="article"]/text()')
        item["mtime"] = parse_html.xpath(
            '//div[@class="ts-d-question"]/div[@class="ts-q-user clearfix"]/span[@class="u-date"]/text()')
        item["username"] = parse_html.xpath(
            '//div[@class="ts-d-question"]/div[@class="ts-q-user clearfix"]/span[@class="u-name"]/text()')
        i_summary = parse_html.xpath('//div[@class="ts-d-question"]/ul[@class="ts-q-list"]')
        i_detail = parse_html.xpath('//div[@class="ts-d-steplist"]')
        conten_lis = []
        for i in i_summary[0]:
            ccc = i.xpath('./label/text()')[0][:-1]
            # ccc2 = i.xpath('./[last()]/text')
            if i.xpath('./a/text()') != []:
                ccc2 = i.xpath('./a/text()')[0].strip()
            elif i.xpath('./b/text()') != []:
                ccc2 = i.xpath('./b/text()')[0].strip()
            else:
                ccc2 = i.xpath('child::node()')[1].strip()
            conten_lis.append([ccc, ccc2])
        item["complaint_detail"] = conten_lis
        detail_lis = []
        for i in i_detail[0]:
            name = i.xpath('.//span[@class="u-name"]/text()')
            status = i.xpath('.//span[@class="u-status"]/text()')
            time = i.xpath('.//span[@class="u-date"]/text()')
            content_lis = i.xpath('.//p')
            content = []
            for l in content_lis:
                aaa = l.xpath("./text()")
                if aaa != "":
                    content = aaa
                    break
            if not content:
                try:
                    content = i.xpath('.//div[@class = "ts-reply"]/p/text()')
                except:
                    content = []
            detail_lis.append([name, status, time, content])
        item["process_detail"] = detail_lis
        print("|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|")
        yield item
        print("*******************已经完成*******************")

