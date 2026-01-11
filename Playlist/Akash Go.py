import requests
from requests.structures import CaseInsensitiveDict

url = "https://akashgo.noobmaster.xyz/?api=iptv_m3u"

headers = CaseInsensitiveDict()
headers["User-Agent"] = "okhttp/4.12.0"
headers["X-Requested-With"] = "com.blaze.sportzfy"
headers["Accept-Encoding"] = "gzip"
headers["Connection"] = "Keep-Alive"
headers["Referer"] = "https://akashgo.noobmaster.xyz/"


resp = requests.get(url, headers=headers)

print(resp.status_code)