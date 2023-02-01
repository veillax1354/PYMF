
#          Copyright Veillax 2023 - 2023 .
# Distributed under the Boost Software License, Version 1.0.
#    (See accompanying file LICENSE_1_0.txt or copy at
#          https://www.boost.org/LICENSE_1_0.txt)

import requests, pytube, os
from pytube import YouTube
from bs4 import BeautifulSoup
API_KEY = os.environ.get("API_KEY")

class BaseException(Exception):
    pass

try:
    raise BaseException("API_KEY required but not found. Please set up a custom secret with the name 'API_KEY' in Github or manually enter.")
except BaseException as e:
    print(e)


def get_video_links(playlist_url):
    # send a GET request to the playlist URL
    response = requests.get(playlist_url)
    # parse the HTML content of the page
    soup = BeautifulSoup(response.content, "html.parser")
    # find all the video links in the playlist
    video_links = [a["href"] for a in soup.find_all("a", class_="pl-video-title-link")]
    # return the list of video links
    return video_links

def yt_download(url, audio=False):
    # download video from given url
    video = pytube.YouTube(url)
    if audio:
        # download audio if audio flag is set to True
        audio_stream = video.streams.filter(only_audio=True, file_extension='mp4').first()
        audio_stream.download(os.getcwd() + "/videos")
        print(f"{audio_stream.default_filename} has been downloaded.")
    else:
        # download video
        video_stream = video.streams.filter(file_extension='mp4').first()
        video_stream.download(os.getcwd() + "/videos")
        print(f"{video_stream.default_filename} has been downloaded.")

        
def file_download(file_path, audio):
    with open(file_path, "r") as file:
        for url in file:
            url = url.strip()
            video = pytube.YouTube(url)
            try:
                if audio:
                    # download audio if audio flag is set to True
                    audio_stream = video.streams.filter(only_audio=True, file_extension='mp4').first()
                    audio_stream.download(os.getcwd() + "/videos")
                    print(f"{audio_stream.default_filename} has been downloaded.")
                else:
                    # download video
                    video_stream = video.streams.filter(file_extension='mp4').first()
                    video_stream.download(os.getcwd() + "/videos")
                    print(f"{video_stream.default_filename} has been downloaded.")
            except Exception as e:
                print(f"An error occured while downloading {url}: {e}")


def yt_search(query):
    if API_KEY:
        search_url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={query}&type=video&key={API_KEY}"
        response = requests.get(search_url)
        results = response.json()["items"]
        for i, result in enumerate(results[:5], start=1):
            print(f"{i}. {result['snippet']['title']} by {result['snippet']['channelTitle']}")
    else:
        print()


        
def main():
    while True:
        # display menu
        print("\n" + "-" * 80)
        print("\t\tWelcome to the YouTube Video Downloader")
        print("\t\t\t\tMenu")
        print("-" * 80)
        print("1. Download video from YouTube link")
        print("2. Download videos from file")
        print("3. Search for YouTube video")
        print("4. Scrape video links from a YouTube Playlist")
        print("5. Exit")
        print("-" * 80)
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
            yt_download(url, audio)
        elif choice == 2:
            # download videos from file
            file_name = input("Enter file name: ")
            audio = False
            check = input("Would you like to download as audio? [y/n]:")
            audio = True if check.lower() == 'y' else False if check.lower() == 'n' else False
            file_download(file_name, audio)
        elif choice == 3:
            # search for youtube video
            query = input("Enter search query: ")
            yt_search(query)
        elif choice == 4:
            playlist_url = input("Enter playlist link: ")
            try:
                with open('video_links.txt', 'x') as x:
                    x.write(get_video_links(playlist_url))
            except Exception as e:
                with open('video_links.txt', 'a') as x:
                    x.write(get_video_links(playlist_url))
        elif choice == 5:
            # exit program
            print("Goodbye!")
            break
        else:
            # invalid choice
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
