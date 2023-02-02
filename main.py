'''

Thank you all contributors for the https://github.com/yt-dlp/yt-dlp and https://github.com/ytdl-org/youtube-dl

Youtube Downloader

- take the video link from clipboard
- make video / just audio selectable
- make the video quality selectable

- with a GUI?
'''

import os
import webbrowser


# os.chdir(r"D:\Applications\YouTube-DLP")

# link = "yt-dlp.exe -S res:1080 https://www.youtube.com/watch?v=CoNI7ToYlxE"
# os.system(link)

# -S res:1080
# Download the best video available with the largest resolution but no better than 1080p,
# or the best video with the smallest resolution if there is no video under 1080p.
# Resolution is determined by using the smallest dimension.
# So this works correctly for vertical videos as well.

# audio_link = "yt-dlp.exe -f bestaudio https://www.youtube.com/watch?v=CoNI7ToYlxE"
# audio_link = "yt-dlp.exe --list-formats https://www.youtube.com/watch?v=CoNI7ToYlxE"

yt_dlp_path = 'd:\Applications\YouTube-DLP\yt-dlp.exe'      # will come from UI - browse window

link = 'https://youtu.be/7yaMASnzoN8'                       # will come from clipboard

parameter = '-f bestaudio'                                  # will come from UI

executable =  f'{yt_dlp_path} {parameter} {link}'
print(executable)

# LIST AVAILABLE FORMATS
def available_formats():
    parameter = '-F'
    executable =  f'{yt_dlp_path} {parameter} {link}'
    os.system(executable)
    print('\n')

# UPDATE YT-DLP
def update():
    executable =  f'{yt_dlp_path} -U'
    os.system(executable)

# OPEN YT-DLP GITHUB SITE
def launch_website():
    link = 'https://github.com/yt-dlp/yt-dlp'                   # GitHub
    link = 'https://github.com/yt-dlp/yt-dlp#release-files'     # Github - Download
    webbrowser.open(link)



# os.system(executable)

# available_formats()