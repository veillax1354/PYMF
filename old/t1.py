
#          Copyright Veillax 2023 - 2023 .
# Distributed under the Boost Software License, Version 1.0.
#    (See accompanying file LICENSE_1_0.txt or copy at
#          https://www.boost.org/LICENSE_1_0.txt)

import os
from bulk import run
from single import srun, testrun
from functions import search, is_file_empty, playlist_video_extract, video_download_fileEmpty

os.system('clear')
if os.path.exists('tmp.txt'):
    os.remove('tmp.txt')
file_path = "links.txt"
if is_file_empty(file_path):
    choice = input(f'"{file_path}" was found to be empty, would you like to search for a video, or add video links to "{file_path}".\nInput "search" or "s" if you would like to search for a video.\nInput "add" or "a" to add files to {file_path}.\nInput "link" or "l" to provide a video link to download.\nInput "playlist" or "p" to provide a playlist link to download.\nInput your option choice: ')
    if list(choice.lower())[0] == 'a': 
        print(f'Please add youtube full links (https://www.youtube.com/watch?v=<id>) or shortlinks (https://youtu.be/<id>) into {file_path}')
    elif list(choice.lower())[0] == 's': 
        print("\n")
        search()
    elif list(choice.lower())[0] == 'p': 
        print("\n")
        playlist_video_extract(input("Please input a link to a youtube playlist: "))
    elif list(choice.lower())[0] == 'l':
        print("\n")
        video_download_fileEmpty(input("Please input a link to a youtube video: "))

while True:
    if is_file_empty(file_path):
        break
    try:
        print('Do you want to download individually, chosing whether to get a video download link, or the video mp4, or do you want to download in bulk, getting both the download url and video mp4. \nIf you want to run in single download, input "s" or "single". \nIf you want to run in bulk download, input "b" or "bulk".')
        check = input('Input "search" or "e" if you would like to search for a video.\nInput "link" or "l" to provide a video link to download.\nInput "playlist" or "p" to provide a playlist link to download.\nInput your option choice: ')
        t = ''
        try:
            if list(check.lower())[0] == 'b':
                os.system('clear')
                run("links.txt")
            elif list(check.lower())[0] == 'e':
                os.system('clear')
                srun()
            elif list(check.lower())[0] == 't':
                os.system('clear')
                testrun()
            elif list(check.lower())[0] == 's': 
                print("\n")
                search()
            elif list(check.lower())[0] == 'p': 
                print("\n")
                playlist_video_extract(input("Please input a link to a youtube playlist: "))
            elif list(check.lower())[0] == 'l':
                print("\n")
                video_download_fileEmpty(input("Please input a link to a youtube video: "))
            if t != '':
                run(t)
            # Test Playlist: https://www.youtube.com/playlist?list=PLxF4AwZ2PvucJi6DJpJx1kbT6eYA86z-P
            # Test Video: https://www.youtube.com/watch?v=qoBIyxWEiOw
        except KeyboardInterrupt:
            print()
    except KeyboardInterrupt:
        print()
        os.system('clear')
        break
