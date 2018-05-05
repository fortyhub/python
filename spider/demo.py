import urllib2
import urllib

values = {}
values['username'] = "842203731@qq.com"
values['password'] = "qlb19920909//"
data = urllib.urlencode(values)
url = "http://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
user_agent = "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Mobile Safari/537.36"
headers = {'User-Agent': user_agent}
#url = "http://passport.csdn.net/account/login"
#geturl = url + "?" + data
request = urllib2.Request(url,data,headers)
#request = urllib2.Request(geturl)
response = urllib2.urlopen(request)
print response.read()