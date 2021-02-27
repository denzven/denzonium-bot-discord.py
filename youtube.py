import urllib.request
import re
import youtube_dl

###################################3
#youtube search command 
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': '%(id)s.mp3',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
def GetYoutubeVideo(query):
	query = query.replace(' ', '+')
	print(query)
	html = urllib.request.urlopen(f"https://www.youtube.com/results?search_query={query}")
	results = re.findall(r"watch\?v=(\S{11})", html.read().decode())
	
	return results[0]
	pass
	
def DownloadVideo(url):
	
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		ydl.download([url])
		pass

	pass