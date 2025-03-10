import requests
import bs4

# headers for requests
h = {
"accept":"application/json",
"accept-encoding":"gzip, deflate, br, zstd",
"accept-language":"en",
"content-length":"36",
"content-type":"application/json",
"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
     }



# site1 proxy info
def site1():
  site1=requests.get("https://www.freeproxy.world").text
  i=0
  td=bs4.BeautifulSoup(site1,"html.parser").find_all("td")
  while len(td)!=i:
    try:
      ip=td[i].text.replace(" ", "").replace("\n", "")
      port=td[i+1].a.text.replace(" ", "").replace("\n", "")
      protocol=td[i+5].a.text.replace(" ", "").replace("\n", "")
      country=td[i+2].a.text.replace(" ", "").replace("\n", "")
      proxy_checker(ip,port,protocol,country)
      i=i+8
    except:
      i=i+1

# site2 proxy info
def site2():
  site2=requests.get("https://iproyal.com/free-proxy-list/?entries=100").text
  i=0
  div=bs4.BeautifulSoup(site2,"html.parser").find_all("div",class_="flex items-center astro-gpo2soo6")
  while len(div)!=i:
      ip=div[i].text.replace(" ", "").replace("\n", "")
      port=div[i+1].text.replace(" ", "").replace("\n", "")
      protocol=div[i+2].text.replace(" ", "").replace("\n", "")
      country=div[i+3].text.replace(" ", "").replace("\n", "")
      proxy_checker(ip,port,protocol,country)
      i=i+5


# site3 proxy info       
def site3():
  site3=requests.get("https://api.lumiproxy.com/web_v1/free-proxy/list?page_size=60").json()
  i=0
  while 60>i:
      ip=site3["data"]["list"][i]["ip"]
      port=site3["data"]["list"][i]["port"]
      protocol=site3["data"]["list"][i]["protocol"]
      if protocol=="2":
        protocol="https"
      elif protocol=="4" or protocol=="8":
        protocol="socks"
      country=site3["data"]["list"][i]["country_code"]
      proxy_checker(ip,port,protocol,country)
      i=i+1   

#proxy checker function
def proxy_checker(ip,port,protocol,country):
  try:
    if requests.get("https://httpbin.org/ip",proxies={"https": protocol + "://" + ip + ":" + port},timeout=5).status_code==200:
      print(ip+"\t\t"+port+"\t\t"+protocol+"\t  \t"+country+"\n")
  except:
      pass

    
print("ip\t\t\tport\t\tprotocol  \tcountry\n")
site1()
site2()
site3()
