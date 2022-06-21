import os
import time
from bs4 import BeautifulSoup
import requests
from requests.models import stream_decode_response_unicode
import os; import locale;

# functional
baseUrl  = "https://yasulcafe2.com/bbs/board.php?bo_table=yasub_1&page="
# https://yasulcafe2.com/bbs/board.php?bo_table=yasub_1 (673)
# https://yasulcafe2.com/bbs/board.php?bo_table=yasub_2 (107 )

x = range(1,674)

for n in reversed(x):
    time.sleep(1)
    urls = []
    names = []
    paths = []
    refers = []
    phpsessids = []
    requestUrl = baseUrl + str(n)
    r = requests.get(requestUrl)
    soup = BeautifulSoup(r.text,"html.parser",from_encoding="utf-8") 

    for href in soup.find("ul", class_="list-body").find_all("div", class_="wr-subject"):
        a_tag = href.find("a")
        a_link = href.find("a")["href"]
        url = a_link.replace(" ","")
        title = (a_tag.text).replace("","")

        word_list = title.split()
        title = " ".join(word_list)

        title = title.replace("?","")
        title = title.replace("/","")
        title = title.replace("\\","")
        title = title.replace("|","")
        title = title.replace("*","")
        title = title.replace("<","")
        title = title.replace(">","")
        title = title.replace(":","-")

        # print("[" + title + "]")
        print(url)

        urls.append(url)
        names.append(title)


    names_urls = zip(urls,names)
    base = os.path.dirname( os.path.abspath( __file__ ) )
    for  url, name in names_urls:
        print(" url1: [" + url +"]")
        #print("name:" + name + " url: " + url.encode('utf-8'))
        r = requests.get(url)
        encoding = r.encoding if "charset" in r.headers.get("content-type", "").lower() else None
        soup = BeautifulSoup(r.text,"html.parser",from_encoding=encoding) 
        # print(soup)
        for href in soup.find("div", class_="view-wrap").find_all("div", class_="view-content"):
            # print(href.get_text())
            context = href.get_text()
            context = str(context).replace('\u2003',' ')
            context = str(context).replace('\u200b',' ')
            context = str(context).replace('\xa0','') 
 
            #context = str(href.get_text().encode('utf-8'))
            with open(base+"//temp//" + name+ ".txt", "w") as f:
                f.write(context)