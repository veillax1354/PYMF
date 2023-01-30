import re
import os
from datetime import datetime
from pytube import YouTube

#          Copyright Veillax 2023 - 2023 .
# Distributed under the Boost Software License, Version 1.0.
#    (See accompanying file LICENSE_1_0.txt or copy at
#          https://www.boost.org/LICENSE_1_0.txt)

# Function to format views into a human-readable format (K for thousands, M for millions)
def human_readable_number(number):
    if number < 1000:
        return str(number)
    elif number < 1000000:
        return "{:.1f}K".format(number / 1000)
    elif number < 1000000000:
        return "{:.1f}M".format(number / 1000000)
    else:
        return "{:.1f}B".format(number / 1000000000)
# Function to format datetime into "Month Day, Year, Hour:Minute AM/PM" format
def format_datetime(dt):
    return dt.strftime("%b %d, %Y, %I:%M %p")

    

def srun():
    # Open file and read its first line, split it into a list of strings
    with open('links.txt', 'r') as f:
        file = f.readline().split(',')
    # Loop through the list of strings
    for x in file:
        # Use regex to search for the video ID in each string
        match = re.search(r'(?:v=|\/)([0-9A-Za-z_-]{11})', x)
        # If a video ID is found, retrieve video information and download the video
        if match:
            vidID = match.group(1)
            vidLINK = 'https://www.youtube.com/watch?v=' + vidID
            yt = YouTube(vidLINK)
    
            # Print video information
            ytDefaultMetadata = yt.title + "by:" + yt.author
            print("\n" + ("-" * 80))
            print(vidLINK)
            print(ytDefaultMetadata)
            print("-" * 80)
            print("\nDescription:\n", yt.description)
            print("-" * 80)
            print("Length:", yt.length // 60, "min", yt.length % 60, "sec")
            print("Views:", human_readable_number(yt.views))
            print("Posted on", format_datetime(yt.publish_date))
            print("-" * 80)
    
            # Prompt user to choose between direct download or using a video downloader website
            check = input(
                '\nDo you want to directly download the video, or use a video downloader website? Input "Direct", or "Web": '
            )
    
            # Direct download
            if check.lower() == 'direct' or check.lower() == 'd':
                yt = YouTube(vidLINK)
                video = yt.streams.filter(
                    progressive=True,
                    file_extension='mp4').order_by('resolution').desc().first()
                dlpath = '/home/runner/PYdl/video'
    
                # Try to create a download folder, if it already exists set download path to current working directory
                dlpath = str(os.getcwd()) + '/videos'
                print('Path set to optimal working directory: ' + dlpath)
    
                video.download(dlpath)
                print('Video was downloaded to ' + dlpath)
                os.system('clear')
            # Use a video downloader website
            elif check.lower() == 'web' or check.lower() == 'w':
                dlink = f'https://btclod.com/watch?v={vidID}'
                with open('web_download_links.txt', 'a') as file:
                    file.write("\n" + ("-" * 80))
                    file.write(ytDefaultMetadata)
                    file.write(f"Download Link: {dlink} \n")
                    print("-" * 80 + '\n')
                os.system('clear')

def testrun():
    if os.path.exists('test.txt'):
        os.remove('test.txt')

    # Open file and read its first line, split it into a list of strings
    with open('test.txt', 'x') as a:
        a.write('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
        a.close()

    with open('test.txt', 'r') as f:
        file = f.readline().split(',')

    # Loop through the list of strings
    for x in file:
        # Use regex to search for the video ID in each string
        match = re.search(r'(?:v=|\/)([0-9A-Za-z_-]{11})', x)
        # If a video ID is found, retrieve video information and download the video
        if match:
            vidID = match.group(1)
            vidLINK = 'https://www.youtube.com/watch?v=' + vidID
            yt = YouTube(vidLINK)
    
            # Print video information
            ytDefaultMetadata = 'Downloading Test Video File'
            print("\n" + ("-" * 80))
            print(ytDefaultMetadata)
            print("-" * 80)
            print("Length:", yt.length // 60, "min", yt.length % 60, "sec")
            print("-" * 80)
            f.close()
            # Directy downloads the video
            check = 'd'
            # Direct download
            if check.lower() == 'direct' or check.lower() == 'd':
                yt = YouTube(vidLINK)
                video = yt.streams.filter(
                    progressive=True,
                    file_extension='mp4').order_by('resolution').desc().first()
                dlpath = '/home/runner/PYdl/video'
    
                # Try to create a download folder, if it already exists set download path to current working directory
                dlpath = str(os.getcwd()) + '/videos'
                print('Path set to optimal working directory: ' + dlpath)
    
                video.download(dlpath)
                print('Video was downloaded to ' + dlpath)
                os.system('clear')