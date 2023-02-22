
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
import time
from time import sleep
from pytube import Playlist, YouTube
from dotenv import load_dotenv
import functions
from functions import t12, unescape, get_key_press

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

def display_video_information(yt, description=False, menu_return=False):
    # Print video information
    ue_title = unescape(yt.title)
    ytDefaultMetadata = '"' + ue_title + '"' + " by: " + yt.author
    pl = ("-" * 80)
    t12(pl)
    pl = ("https://www.youtube.com/watch?v=" + yt.video_id)
    t12(pl)
    pl = (ytDefaultMetadata)
    t12(pl)
    if description:
        pl = ("Description: \n" + yt.description + "\n")
        t12(pl)
    pl = ("Length: ", yt.length // 60, "min", yt.length % 60, "sec")
    t12(pl)
    pl = ("Views: ", functions.human_readable_number(yt.views))
    t12(pl)
    pl = ("Posted on ", functions.format_datetime(yt.publish_date).strip(", 12:00 AM"))
    t12(pl)
    pl = ("-" * 80)
    t12(pl)
    if menu_return:
        t12("Press any key to return to the menu")
        get_key_press()
    

# Downloads videos from provided link
def video_download(video_link):
    """Better download function, shows metadata and other stuff"""
    # Use regex to search for the video ID in each string
    match = re.search(r'(?:v=|\/)([0-9A-Za-z_-]{11})', video_link)
    # If a video ID is found, retrieve video information and download the video
    if match:
        vidID = match.group(1)
        vidLINK = 'https://www.youtube.com/watch?v=' + vidID
        yt = YouTube(vidLINK)
        pl = ("\nDownloading:\n")
        t12(pl)
        display_video_information(yt)
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
def file_download(file_path, pathname=None):
    """Downloads all video links from a file as long as """
    if pathname is None:
        dlpath = (os.getcwd() + "/videos")
    else:
        dlpath = (os.getcwd() + "/videos/" + pathname)
    with open(file_path, "r", encoding="utf-8") as file:
        for url in file:
            url = url.strip()
            video = pytube.YouTube(url)
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
# Returns search results https://www.dataquest.io/blog/python-projects-for-beginners/
def search():
    """Searches for the query using search_youtube() then downloads the video as either audio or video"""
    query = input("Enter your search query: ")
    results = search_youtube(query)
    try:
        items = results["items"]
    except Exception as en:
        print(f"Something went wrong, please try again later; {en}")

    for i, result in enumerate(items, start=1):
        pr = unescape(f"[{i}] " + result['snippet']['title'] + " | " + result['snippet']['channelTitle'] + " | " + result['id']['videoId'])
        t12(pr)


    choice = int(input("Which video would you like to download (1-5): ")) - 1
    item = items[choice]
    title = item["snippet"]["title"]
    video_id = item["id"]["videoId"]
    video_download(f"https://www.youtube.com/watch?v={video_id}, False")

def main():
    """Main function, calling this will start the program"""
    slep = False
    while True:
        if slep:
            sleep(3)
        os.system("clear")
        # display menu
        t12("-" * 80, 0.01)
        t12("\t\tWelcome to the YouTube Video Downloader", 0.01)
        t12("\t\t\t\tMenu", 0.02)
        t12("-" * 80, 0.01)
        t12("1. Download video from YouTube link", 0.025)
        t12("2. Display the metadata from a YouTube video", 0.025)
        t12("3. Download videos from a YouTube Playlist", 0.025)
        t12("4. Download videos from file", 0.025)
        t12("5. Search for YouTube video", 0.025)
        t12("6. Exit", 0.01)
        t12("-" * 80, 0.01)
        # get user input
        choice = int(input("Enter your choice (1-6): "))
        if choice == 1:
            # download video from youtube link
            url = input("Enter YouTube Video link: ")
            video_download(url)
        elif choice == 2:
            # displays the video metadata
            yt = YouTube(input("Enter YouTube Video link: "))
            display_video_information(yt, True, True)
        elif choice == 3:
            # downloads videos from a playlist
            global PLAYLIST_URL
            PLAYLIST_URL = input("Enter YouTube playlist link: ")
            file_download("video_links.txt", playlist_video_extract(PLAYLIST_URL))
        elif choice == 4:
            # download videos from file
            file_name = input("Enter file name: ")
            file_download(file_name)
        elif choice == 5:
            # search for youtube video
            search()
        elif choice == 6:
            # exit program
            t12("Goodbye!")
            break
        else:
            # invalid choice
            t12("Invalid choice. Try again.")
        slep = True

if __name__ == "__main__":
    main()
