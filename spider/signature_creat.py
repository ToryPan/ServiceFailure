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
    value_  = value_ + (page-1)
    url = 'https://tousu.sina.com.cn/api/company/received_complaints?ts={}&rs={}&signature={}&callback=jQuery111209852954769752549_1643429153980&couid={}&type=1&page_size=10&page={}&_={}'.format(ts,rs,signature,couid,page,value_)
    return(url)

def return_url(page,couid,value_):
    # ts = int(time.time()* 1000)
    ts = 1643442276779
    # rs = js1.call('aa','!1',16)
    rs = 'VmYK9ARkx9i3mi26'
    return(get_url(ts,rs,couid,page,value_))

couid = 3787942764
value_ = 1643429153981
ts_mount = 8494


print(return_url(100,couid,value_))