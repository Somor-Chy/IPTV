import requests

url = "https://akashgo.noobmaster.xyz/"
params = {"api": "iptv_m3u"}
headers = {
    "User-Agent": "okhttp/4.12.0",
    "X-Requested-With": "com.blaze.sportzfy",
    "Accept-Encoding": "gzip"
}

response = requests.get(url, params=params, headers=headers)
print(response.text)
