import os
import time
from bs4 import BeautifulSoup
import requests
from requests.models import stream_decode_response_unicode

# _URL = 'https://torrentj39.com/bbs/board.php?bo_table=movie&sca=%EC%84%B1%EC%9D%B8%EC%98%81%ED%99%94&page=1'  #반복되는 곳 사이트 몸통

# functional


# baseUrl  = "https://ktxtorrent25.com/"
baseUrl  = "https://cwy0675.tistory.com/category/PPT%EC%95%85%EB%B3%B4/%ED%86%B5%ED%95%A9%EC%B0%AC%EC%86%A1%EA%B0%80%28%ED%95%9C%EC%98%81%29?page=" # 구찬송가#
#baseUrl  = "https://cwy0675.tistory.com/category/PPT%EC%95%85%EB%B3%B4/%EC%83%88%EC%B0%AC%EC%86%A1%EA%B0%80%28%ED%95%9C%EC%98%81%29?page=" # 신찬송가
 
x = range(1,20)

for n in x:
    time.sleep(5)
    try:
        urls = []
        names = []
        paths = []
        refers = []
        phpsessids = []

        _URL = baseUrl + str(n)

        print("_URL : " + _URL)
        r = requests.get(_URL)
        soup = BeautifulSoup(r.text,"html.parser")

        for href in soup.find("div", class_="nonEntry").find_all("li"): 
            # time.sleep(1)
            try:
                a_link = href.find("a")["href"] 
                # if a_link.find("wr_id") > 0 and a_link.find("bo_table=" + table ) and a_link.find("sca=%EC%84%B1%EC%9D%B8%EC%98%81%ED%99%94") > 0 :
                # print("href link : " + "https://cwy0675.tistory.com" + a_link)
                full_link = "https://cwy0675.tistory.com" + a_link
                if full_link:
                    print("full_link:" + full_link)
                    r1 = requests.get(full_link)
                    soup1 = BeautifulSoup(r1.text,"html.parser")
                    for ahref in soup1.find("div", class_="article").find_all("a"):
                        
                        try:
 
                            url = ahref.attrs["href"]
                            # print("PPT url : {0}".format(url))
                            
                            if "https://cwy0675.tistory.com/attachment" in url:
                                if ".NWC" in url or ".NWC" in url:
                                    urls.append(url)
        
                                    name = ahref.text
                                    names.append(name.replace(" chan","chan")) 
                                    print("PPT : {0} - {1}".format(name,url))
                        except:
                            pass
            except:
                pass
        names_urls = zip(names, urls)
        base = os.path.dirname( os.path.abspath( __file__ ) )
        for filename, url in names_urls:
            time.sleep(1)
            try:
                print(filename + " //// " + url)
              
                r = requests.get(url)
                print("status:" + str(r.status_code))
                
                if r.status_code == 200:
                    with open(base+"//temp//" + filename, "wb") as f:
                        f.write(r.content)
                        
            except requests.exceptions.HTTPError as errh:
                print ("Http Error:",errh)
            except requests.exceptions.ConnectionError as errc:
                print ("Error Connecting:",errc)
            except requests.exceptions.Timeout as errt:
                print ("Timeout Error:",errt)
            except requests.exceptions.RequestException as err:
                print ("OOps: Something Else",err)
    except:
        pass
