import requests

def download_playlist():
    """Simple function to download and save the IPTV playlist"""
    
    headers = {
        'Accept': '*/*',
        'User-Agent': 'okhttp/4.12.0',
        'X-Requested-With': 'com.blaze.sportzfy',
        'Accept-Encoding': 'gzip',
        'Connection': 'Keep-Alive',
        'Referer': 'https://akashgo.noobmaster.xyz/'
    }
    
    url = "https://akashgo.noobmaster.xyz/"
    params = {"api": "iptv_m3u"}
    
    try:
        print("Downloading IPTV playlist...")
        response = requests.get(url, headers=headers, params=params, timeout=30)
        response.raise_for_status()
        
        # Check if it's an M3U file
        if response.text.strip().startswith('#EXTM3U'):
            with open('iptv_playlist.m3u', 'w', encoding='utf-8') as f:
                f.write(response.text)
            print("✅ Playlist saved as 'iptv_playlist.m3u'")
            return True
        else:
            print("Response doesn't appear to be M3U format")
            print(f"First 500 chars: {response.text[:500]}")
            return False
            
    except Exception as e:
        print(f"Error: {e}")
        return False

# Run the simple download
download_playlist()
