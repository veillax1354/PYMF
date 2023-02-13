
#          Copyright Veillax 2023 - 2023 .
# Distributed under the Boost Software License, Version 1.0.
#    (See accompanying file LICENSE_1_0.txt or copy at
#          https://www.boost.org/LICENSE_1_0.txt)

"""Youtube Video Downloader for MFPython"""

# pylint: disable=broad-except, global-variable-undefined, invalid-name
import os
import json
import re
import requests
import pytube
from pytube import Playlist, YouTube
from dotenv import load_dotenv
import functions
from functions import t12

load_dotenv("PYMF.env")
API_KEY = os.getenv("YT_API_KEY")

class ApiNotFoundException(Exception):
    """Custom exception for when the API Key used for the youtube data API v3, usually found in secrets, can't be found"""
if API_KEY is None:
    try:
        raise ApiNotFoundException("API_KEY required but not found. Please set up a custom secret with the name 'API_KEY' in Github or manually enter.")
    except ApiNotFoundException as e:
        pl = str(e)
        t12(pl)
else:
    pass

# Extracts video links from a playlist and outputs them to "video_links.txt"
def playlist_video_extract(playlist_link):
    """Extracts the video links from a playlist using pytube Playlist"""
    if os.path.exists('links.txt'):
        os.remove('links.txt')
    else:
        pass
    with open("links.txt", "x", encoding="utf-8") as t:
        t.write('')
        t.close()
    # Test Playlist: https://www.youtube.com/playlist?list=PLxF4AwZ2PvucJi6DJpJx1kbT6eYA86z-P
    if "list=" in playlist_link:
        p = Playlist(playlist_link)
        pl = (f'Downloading: {p.title}')
        t12(pl)
        i = 1
        for url in p.video_urls:
            pl = (f"{i}: {url}")
            t12(pl)
            with open("links.txt", "a", encoding="utf-8") as t:
                t.write(str(url) + "\n")
    elif playlist_link.lower() == 'test':
        p = Playlist("https://www.youtube.com/playlist?list=PLxF4AwZ2PvucJi6DJpJx1kbT6eYA86z-P")
        pl = (f'Downloading: {p.title}')
        t12(pl)
        i = 1
        for url in p.video_urls:
            pl = (f"{i}: {url}")
            t12(pl)
            with open("links.txt", "a", encoding="utf-8") as t:
                t.write(str(url) + "\n")
    title = "".join(ch for ch in p.title if ch.isalnum())
    if os.path.exists('links.txt'):
        os.remove('links.txt')
    else:
        pass
    return title
# Downloads videos from provided link
def video_download(video_link, audio):
    """Better download function, shows metadata and other stuff"""
    # Use regex to search for the video ID in each string
    match = re.search(r'(?:v=|\/)([0-9A-Za-z_-]{11})', video_link)
    # If a video ID is found, retrieve video information and download the video
    if match:
        vidID = match.group(1)
        vidLINK = 'https://www.youtube.com/watch?v=' + vidID
        yt = YouTube(vidLINK)
        
        # Print video information
        ytDefaultMetadata = '"' + yt.title + '"' + " by: " + yt.author
        pl = ("\nDownloading:\n" + ("-" * 80))
        t12(pl)
        pl = (vidLINK)
        t12(pl)
        pl = (ytDefaultMetadata)
        t12(pl)
        pl = ("Length:", yt.length // 60, "min", yt.length % 60, "sec")
        t12(pl)
        pl = ("Views:", functions.human_readable_number(yt.views))
        t12(pl)
        pl = ("Posted on ", functions.format_datetime(yt.publish_date))
        t12(pl)
        pl = ("-" * 80)
        t12(pl)
                
        # Direct download
        yt = YouTube(vidLINK)
        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        try:
            # download video
            video.download(os.getcwd() + "/videos")
        except Exception as exception_e:
            print(f"An error occured while downloading {vidLINK}: {exception_e}")
        dlpath = os.getcwd() + "/videos"
        pl = ('Path set to optimal working directory: ' + os.getcwd() + "/videos")
        t12(pl)
        pl = ('Video was downloaded to ' + str(os.getcwd()) + "/videos")
        t12(pl)
# Downloads videos from links in "video_links.txt", or other files containing links, links must be seperated by a new line
def file_download(file_path, audio=False, pathname=None):
    """Downloads all video links from a file as long as """
    if pathname is None:
        dlpath = (os.getcwd() + "/videos" if not audio else os.getcwd() + "/songs")
    else:
        dlpath = (os.getcwd() + "/videos/" + pathname if not audio else os.getcwd() + "/songs/" + pathname)
    with open(file_path, "r", encoding="utf-8") as file:
        for url in file:
            url = url.strip()
            video = pytube.YouTube(url)
            if audio:
                # download audio if audio flag is set to True
                audio_stream = video.streams.filter(only_audio=True, file_extension='mp3 ').first()
                audio_stream.download(dlpath)
                pl = (f"{audio_stream.default_filename} has been downloaded.")
                t12(pl)
            else:
                # download video
                video_stream = video.streams.filter(file_extension='mp4').first()
                video_stream.download(dlpath)
                pl = (f"{video_stream.default_filename} has been downloaded.")
                t12(pl)
# Finds video titles that match the query
def search_youtube(query):
    """Finds video titles that match the query"""
    url = f'https://www.googleapis.com/youtube/v3/search?part=snippet&q={query}&type=video&key={API_KEY}'
    response = requests.get(url, timeout=10)
    results = json.loads(response.text)
    try:
        items = results["items"]
    except Exception as em:
        error = results["error"]
        print(em)
        print(error)
        return error
    return json.loads(response.text)
# Returns search results
def search():
    """Searches for the query using search_youtube() then downloads the video as either audio or video"""
    query = input("Enter your search query: ")
    results = search_youtube(query)
    try:
        items = results["items"]
    except Exception as en:
        print(f"Something went wrong, please try again later; {en}")

    for i, result in enumerate(items, start=1):
        print(f"[{i}] " + result['snippet']['title'] + " | " + result['snippet']['channelTitle'] + " | " + result['id']['videoId'])


    choice = int(input("Which video would you like to download (1-5): ")) - 1
    item = items[choice]
    title = item["snippet"]["title"]
    video_id = item["id"]["videoId"]
    yt = YouTube(f"https://www.youtube.com/watch?v={video_id}")
    video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    audio = False
    check = input("Would you like to download as audio? [y/n]:")
    audio = True if check.lower() == 'y' else False
    try:
        if audio:
            # download audio if audio flag is set to True
            audio_stream = video.streams.filter(only_audio=True, file_extension='mp3').first()
            dlpath = os.getcwd() + "/videos"
            audio_stream.download(dlpath)
            print(f"{audio_stream.default_filename} has been downloaded.")
        else:
            # download video
            video_stream = video.streams.filter(file_extension='mp4').first()
            dlpath = os.getcwd() + "/songs"
            video_stream.download(dlpath)
            print(f"{video_stream.default_filename} has been downloaded.")
    except Exception as exception_e:
        print(f"An error occured while downloading https://www.youtube.com/watch?v={video_id}: {exception_e}")
    print(f"{title} has been downloaded!")

def main():
    """Main function, calling this will start the program"""
    while True:
        # display menu
        t12("\n" + "-" * 80)
        t12("\t\tWelcome to the YouTube Video Downloader")
        t12("\t\t\t\tMenu")
        t12("-" * 80)
        t12("1. Download video from YouTube link")
        t12("2. Download videos from a YouTube Playlist")
        t12("3. Download videos from file")
        t12("4. Search for YouTube video")
        t12("5. Exit")
        t12("-" * 80)
        # get user input
        choice = int(input("Enter your choice (1-5): "))
        if choice == 1:
            # download video from youtube link
            url = input("Enter YouTube link: ")
            audio = False
            if "--audio" in url:
                # download audio if --audio flag is present
                audio = True
                url = url.replace(" --audio", "")
            video_download(url, audio)
        elif choice == 3:
            # download videos from file
            file_name = input("Enter file name: ")
            audio = False
            check = input("Would you like to download as audio? [y/n]:")
            audio = True if check.lower() == 'y' else False
            file_download(file_name, audio)
        elif choice == 4:
            # search for youtube video
            search()
        elif choice == 2:
            global PLAYLIST_URL
            PLAYLIST_URL = input("Enter playlist link: ")
            audio = False
            check = input("Would you like to download as audio? [y/n]:")
            audio = True if check.lower() == 'y' else False
            file_download("video_links.txt", audio, playlist_video_extract(PLAYLIST_URL))
        elif choice == 5:
            # exit program
            t12("Goodbye!")
            break
        else:
            # invalid choice
            t12("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
