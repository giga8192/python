import urllib
import requests

def f1(url,command):
    headers = {
        'Host': '127.0.0.1',
        'Authorization': 'Basic YWRtaW46aG9yaXpvbjM=',
        'X-F5-Auth-Token': 'asdf',        
        'Connection': 'X-F5-Auth-Token',
        'Content-Type': 'application/json'
           
    }
    j = {"command":"run","utilCmdArgs":"-c '{0}'".format(command)}
    r = requests.post(url,headers=headers,json=j)

    return r


url ="https://httpbin.org/post"
res = f1(url,"ls")

print("-----------------------------")
url2 = "https://www.example.com/index.html"
response2 = urllib.request.urlopen(url2)
print("url: ", response2.geturl())
print("code: ", response2.getcode())
print(response2.info())
content = response2.read()
print("---------------")
print("バイト列で")
print(content) # バイト列で
print("------------------")
print(content.decode("utf-8"))
response2.close() # クローズ

param1 = {"param1": "テスト", "param2":"hoge"}
print(urllib.parse.urlencode(param1))
res3 = urllib.request.urlopen(url2 + "?" + urllib.parse.urlencode(param1))
print(res3.geturl())
print("レスポンスヘッダ")
print(res3.status)
print("" + res3.headers.get_content_charset())
content3 = res3.read()
print(content3.decode())
res3.close()
