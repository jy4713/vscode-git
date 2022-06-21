import os
import time
from bs4 import BeautifulSoup
import requests
from requests.models import stream_decode_response_unicode

# _URL = 'https://torrentj39.com/bbs/board.php?bo_table=movie&sca=%EC%84%B1%EC%9D%B8%EC%98%81%ED%99%94&page=1'  #반복되는 곳 사이트 몸통

# functional


# baseUrl  = "https://ktxtorrent25.com/"
baseUrl  = "https://torrentj54.com/"
print('Enter Table : (movie,drama,entertain) ')
table = input()
print('Enter sca : ')
sca = input()
print ('search parameter :')
search = input()

print('Enter start number : ')
st = input()
print ('Enter end number : ')
ed = input()

if len(st) <= 0:
    stInt = 1
else :
    stInt= int(st)

if len(ed) <= 0:
    edInt= 6
else:
    edInt= int(ed)

x = range(stInt,edInt)

for n in x:
    try:
        urls = []
        names = []
        paths = []
        refers = []
        phpsessids = []

        if len(search) < 0 :
            # _URL = "https://ktxtorrent25.com/bbs/board.php?bo_table=movie&sca=%EC%84%B1%EC%9D%B8%EC%98%81%ED%99%94&page=" + str(n)
            if len(sca) > 0 : 
                _URL = baseUrl + "bbs/board.php?bo_table=" + table + "&sca=" + sca + "&page=" + str(n)
            else:
                _URL = baseUrl + "bbs/board.php?bo_table=" + table + "&page=" + str(n)
                                
        else :
            _URL = baseUrl + "bbs/board.php?bo_table=" + table + "&sfl=wr_subject&stx=" + search + "&sop=and&page=" + str(n)

        print("_URL : " + _URL)
        r = requests.get(_URL)
        soup = BeautifulSoup(r.text,"html.parser")

        for href in soup.find("div", class_="list-board").find_all("li"): 
            try:
                a_link = href.find("a")["href"] 
                # if a_link.find("wr_id") > 0 and a_link.find("bo_table=" + table ) and a_link.find("sca=%EC%84%B1%EC%9D%B8%EC%98%81%ED%99%94") > 0 :
                if a_link.find("wr_id") > 0 and a_link.find("bo_table=" + table ):
                    print("a_link:" + a_link)
                    r1 = requests.get(a_link)
                    soup1 = BeautifulSoup(r1.text,"html.parser")
                    for ahref in soup1.find("div", class_="list-group").find_all("a"):
                        try:
                            if len(search)> 0 and ahref.text.find(search) < 0 :
                                continue
                            time.sleep(1)
                            # print(r1.headers.get('Set-Cookie'))
                            phpsessid = r1.headers.get('Set-Cookie').split(';')[0] 
                            phpsessids.append(phpsessid)
                            # print("------------------" + phpsessid)
                            # print("----------------" + str(ahref))
                            url = ahref.attrs["href"]
                            # print("url : " + url)
                            urls.append(url)
                            name_link = ahref.text.split(" ")
                            # print(ahref.text)
                            # print(name_link)
                            count = len(name_link)
                            # print(count)

                            new_name = ahref.text
                            new_name = new_name.replace(name_link[0],"")
                            new_name = new_name.replace(name_link[1],"")
                            new_name = new_name.replace(name_link[2],"")
                            new_name = new_name.replace(name_link[count-1],"")
                            new_name = new_name.replace(name_link[count-2],"")
                            new_name = new_name.replace(name_link[count-3],"")
                            new_name = new_name.replace("   ","")
                            new_name = new_name.replace(" ","_")

                            names.append(new_name) 

                            referer = url.replace("https://ktxtorrent25.com/bbs/download.php?","")
                            referers = referer.split("&")
                            paths.append("/bbs/download.php?" + referers[0] + "&" +  referers[1] + "&" + referers[2])
                            refers.append("https://ktxtorrent25.com/bbs/board.php?" + referers[0] + "&" +  referers[1])
                        except:
                            pass
            except:
                pass
        names_urls = zip(names, urls,paths,refers,phpsessids)
        base = os.path.dirname( os.path.abspath( __file__ ) )
        for filename, url, path, refer,phpsessid in names_urls:
            try:
                # print(filename + " //// " + url)
                headers = {
                    'authority':'ktxtorrent25.com',
                    'scheme':'https',
                    'path':path,                      # /bbs/download.php?bo_table=movie&wr_id=16858&no=1 
                    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
                    'sec-ch-ua-mobile':'?0',
                    'upgrade-insecure-requests':'1',
                    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
                    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'sec-fetch-site':'same-origin',
                    'sec-fetch-mode':'navigate',
                    'sec-fetch-user':'?1',
                    'sec-fetch-dest':'document',
                    'referer':refer,                      #    https://ktxtorrent25.com/bbs/board.php?bo_table=movie&wr_id=16858
                    'accept-encoding':'gzip, deflate, br',
                    'accept-language':'en-GB,en;q=0.9,ko-KR;q=0.8,ko;q=0.7,en-US;q=0.6',
                    'cookie': phpsessid + '; 2a0d2363701f23f8a75028924a3af643=ODYuMTQ3LjEyMC4yNDA%3D; UM_distinctid=17c6b97aab217-09466780897b4c-3a67410c-144000-17c6b97aab47d; CNZZDATA1278735195=730947496-1633896118-%7C1633896118; e1192aefb64683cc97abb83c71057733=bW92aWU%3D',
                }
                r = requests.get(url , headers=headers)
                # print("status:" + str(r.status_code))
                if r.status_code == 200:
                    with open(base+"//torrent//" + filename, "wb") as f:
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