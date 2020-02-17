import os
import requests
import urllib.request
from lxml import etree

website = 'http://bp.pep.com.cn/jc/'
folder = '人教版'

req = requests.get(website)
req.encoding = 'utf-8'

if not os.path.exists(folder):
    os.mkdir(folder)

selector = etree.HTML(req.text)
types = selector.xpath('//*[@id="container"]/div[@class="list_sjzl_jcdzs2020"]')

for t in types:
    type_name = t.xpath('./div/h5')[0].text
    print(type_name+"...开始下载")
    path = folder+'/'+type_name
    if not os.path.exists(path):
        os.mkdir(path)

    subjects = t.xpath('./ul')

    for s in subjects:
        books = s.xpath('./li')
        for b in books:
            subject_name = b.xpath('./a')[0].text
            subject_page = website+b.xpath('./a/@href')[0][2:]
            path = folder+'/'+type_name+'/'+subject_name
            if not os.path.exists(path):
                os.mkdir(path)
            print("     "+subject_name+"...开始下载")

            req_subject = requests.get(subject_page)
            req_subject.encoding = 'utf-8'

            selector_subject = etree.HTML(req_subject.text)
            groups = selector_subject.xpath('//*[@id="container"]/div[2]/ul')

            for g in groups:
                units = g.xpath('./li')
                for u in units:
                    title = u.xpath('./h6/a/@title')[0]+".pdf"
                    url = subject_page + u.xpath('./div/a[2]/@href')[0][2:]
                    print("         "+url)
                    urllib.request.urlretrieve(url, folder+'/'+type_name+'/'+subject_name+'/'+title)
                    print("         "+title+"下载完毕")

print("全部下载完毕")

