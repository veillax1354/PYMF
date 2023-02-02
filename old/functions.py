from pytube import YouTube, Playlist
from datetime import datetime
import requests, json, re, os

# Function to format views into a human-readable format (K for thousands, M for millions)

# Function to allow for video searching on youtube
def search_youtube(query):
    url = f'https://www.googleapis.com/youtube/v3/search?part=snippet&q={query}&type=video&key={API_KEY}'
    response = requests.get(url)
    return json.loads(response.text)
# Function to allows users to input a playlist link and download videos from the playlist
def playlist_video_extract(playlist_link):
    if "list=" in playlist_link:
        p = Playlist(playlist_link)
        print(f'Downloading: {p.title}')
        l = p.video_urls[:0]
        i = 0
        for url in p.video_urls:
            print(url)
        return p.video_urls
            
# Test Playlist: https://www.youtube.com/playlist?list=PLxF4AwZ2PvucJi6DJpJx1kbT6eYA86z-P

def video_download(video_link):
    # Use regex to search for the video ID in each string
    match = re.search(r'(?:v=|\/)([0-9A-Za-z_-]{11})', video_link)
    # If a video ID is found, retrieve video information and download the video
    if match:
        vidID = match.group(1)
        vidLINK = 'https://www.youtube.com/watch?v=' + vidID
        yt = YouTube(vidLINK)
        
        # Print video information
        ytDefaultMetadata = '"' + yt.title + '"' + " by: " + yt.author
        print("\nDownloading:\n" + ("-" * 80))
        print(vidLINK)
        print(ytDefaultMetadata)
        print("Length:", yt.length // 60, "min", yt.length % 60, "sec")
        print("Views:", human_readable_number(yt.views))
        print("Posted on", format_datetime(yt.publish_date))
        print("-" * 80)
                
        # Direct download
        yt = YouTube(vidLINK)
        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
                    
        # Try to create a download folder, if it already exists set download path to current working directory
        dlpath = str(os.getcwd()) + '/videos'
        print('Path set to optimal working directory: ' + dlpath)
        
        video.download(dlpath)
        print('Video was downloaded to ' + dlpath)

def search():
    query = input("Enter your search query: ")
    results = search_youtube(query)
    items = results["items"]

    for i, result in enumerate(items, start=1):
        print(f"[{i}] " + result['snippet']['title'] + " - " + result['snippet']['channelTitle'] + " | " + result['id']['videoId'])


    choice = int(input("Which video would you like to download (1-5): ")) - 1
    item = items[choice]
    title = item["snippet"]["title"]
    video_id = item["id"]["videoId"]
    yt = YouTube(f"https://www.youtube.com/watch?v={video_id}")
    video = yt.streams.first()
    video.download()
    print(f"{title} has been downloaded!")

def is_file_empty(file_path):
    try:
        with open(file_path) as file:
            return not bool(file.read().strip())
    except FileNotFoundError:
        open(file_path, "w").close()
        return True

if __name__ == "__main__":
    video_urls = playlist_video_extract('https://www.youtube.com/playlist?list=PLAjULYyNSE9aa7aQW31IupW685MO-ZBHc')
    for url in video_urls:
        video_download(url)
