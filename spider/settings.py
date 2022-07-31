# Scrapy settings for DeWu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'DeWu'

SPIDER_MODULES = ['DeWu.spiders']
NEWSPIDER_MODULE = 'DeWu.spiders'

# DOWNLOAD_HANDLERS = {
#     'https': 'scrapy.core.downloader.handlers.http2.H2DownloadHandler',
# }

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'DeWu (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 2
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {':authority': 'tousu.sina.com.cn',
':method': 'GET',
':path': "/api/company/received_complaints?ts=1643471235581&rs=VbzqTMjlaroewggR&signature=cadd3746d2363b895864796f39db0c4d0f09d29c3ae7b74d430ce863e25a7e60&callback=jQuery111206935682897257829_1643471235521&couid=6416319252&type=1&page_size=10&page=10&_=1643471235531",
':scheme': 'https',
'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'zh-CN,zh;q=0.9',
'cookie': 'SCF=Aqm8vtjvXJI0H-kHbrYRefpBlxLU-iLgNt1b1bFIbhv5nd-2adu4ogow5s3PJGVuPN1boRHd4MP7KrN2SytJ67Y.; SINAGLOBAL=117.172.84.196_1597836152.487912; U_TRS1=000000c4.f4dfd9e.5f3d0b79.7da0217d; vjuids=-de7cc9fb5.177f2060f5d.0.55ce64b4675ab; vjlast=1614673219.1614673219.30; Qs_lvt_335601=1606318879%2C1606444396%2C1606444397%2C1616059213%2C1617251887; Qs_pv_335601=2667597140409554400%2C807382851167662800%2C4395900960291766000%2C5286106159018145%2C4146918925267263000; __gads=ID=1cdaf3754eefff50-22644a0751ca008e:T=1626227649:RT=1626227649:R:S=ALNI_MbpwY0LfPYt4F8FR_xdrluK70kh_Q; UOR=,,; UM_distinctid=17d6713c616696-0afda58a39dc7e-978183a-144000-17d6713c61787a; TOUSU-SINA-CN=; CNZZDATA1273941306=880586654-1643418444-%7C1643467265; Apache=117.172.80.162_1643470692.527238; SUB=_2A25M8S81DeRhGeNN7FIT9CzEyjSIHXVvhwf9rDV_PUNbm9B-LXj6kW9NSY989DwMmHhss5XyI0P2QuRnJsYdp3Mb; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFSJ1LQk7pGSjq6.Kx76iIE5NHD95Qfe0M7eoBE1h2RWs4DqcjGHsvEwHWydntt; ALF=1675006693; U_TRS2=000000a2.d7b342d7.61f55f67.cc6e3b23; ULV=1643470696039:30:3:3:117.172.80.162_1643470692.527238:1643470691563',
'referer': 'https://tousu.sina.com.cn/company/view/?couid=6416319252',
'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': 'Windows',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
'x-requested-with': 'XMLHttpRequest'}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'DeWu.middlewares.DewuSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'DeWu.middlewares.DewuDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'DeWu.pipelines.DewuPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
