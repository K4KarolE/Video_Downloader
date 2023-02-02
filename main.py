'''
ffmpeg

- will be able to download higher than 720p + merge video-audio
- add ffmpeg to PATH - C:\ffmpeg
- https://windowsloop.com/install-ffmpeg-windows-10/#add-ffmpeg-to-Windows-path
'''


import os
import webbrowser


yt_dlp_path = 'd:\Applications\YouTube-DLP\yt-dlp.exe'      # will come from UI - browse window

link = 'https://youtu.be/7yaMASnzoN8'                       # will come from UI / clipboard
link = 'https://www.youtube.com/watch?v=0NV-fvpM6_Y' 


## VIDEO
resolutions = {
    "360p": "360",
    "480p": "480",
    "720p": "720",
    "1080p": "1080",
    "1440p": "1440",
    "2160p": "2160",
}


resolutions_list=[]
for item in resolutions.keys():
    resolutions_list += [item]


selected_resolution = resolutions["720p"]

parameter = f'-S "res:{selected_resolution}"'
# Download the best video available with the largest resolution but no better than 480p,
# or the best video with the smallest resolution if there is no video under 480p
# Resolution is determined by using the smallest dimension.
# So this works correctly for vertical videos as well    

executable =  f'{yt_dlp_path} {parameter} {link}'
# print(executable)

### AUDIO
parameter = '-f bestaudio'

# LIST AVAILABLE FORMATS
def available_formats():
    parameter = '-F'
    executable =  f'{yt_dlp_path} {parameter} {link} > formats.txt'     # writes the available formats into the txt file
    os.system(executable)
    print('\n')

# UPDATE YT-DLP
def update():
    parameter = '-U'
    executable =  f'{yt_dlp_path} {parameter}'
    os.system(executable)

# OPEN YT-DLP GITHUB SITE
def launch_yt_dlp_github():
    link = 'https://github.com/yt-dlp/yt-dlp'

    webbrowser.open(link)

# OPEN YT-DLP GITHUB / RELEASE FILES to donwload yt-dlp.exe
def launch_yt_dlp_download():
    link = 'https://github.com/yt-dlp/yt-dlp#release-files'
    webbrowser.open(link)



os.system(executable)