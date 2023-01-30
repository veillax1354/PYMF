
#          Copyright Veillax 2023 - 2023 .
# Distributed under the Boost Software License, Version 1.0.
#    (See accompanying file LICENSE_1_0.txt or copy at
#          https://www.boost.org/LICENSE_1_0.txt)

import os
from bulk import run
from single import srun
check = input('Do you want to download individually, chosing whether to get a video download link, or the video mp4, or do you want to download in bulk, getting both the download url and video mp4. \nIf you want to run in single download, input "s" or "single". \nIf you want to run in bulk download, input "b" or "bulk".\nPlease choose an option: ')

if check.lower() == 'b' or check.lower() == 'bulk':
    os.system('clear')
    run()
elif check.lower() == 's' or check.lower() == 'single':
    os.system('clear')
    srun()
