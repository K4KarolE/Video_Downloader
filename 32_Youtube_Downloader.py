'''

Thank you all contributors for the https://github.com/yt-dlp/yt-dlp and https://github.com/ytdl-org/youtube-dl

Youtube Downloader

- take the video link from clipboard
- make video / just audio selectable
- make the video quality selectable

- with a GUI?
'''

import os
os.chdir(r"D:\Applications\YouTube-DLP")

# link = "yt-dlp.exe -S res:1080 https://www.youtube.com/watch?v=CoNI7ToYlxE"
# os.system(link)

# -S res:1080
# Download the best video available with the largest resolution but no better than 1080p,
# or the best video with the smallest resolution if there is no video under 1080p.
# Resolution is determined by using the smallest dimension.
# So this works correctly for vertical videos as well.

audio_link = "yt-dlp.exe -f bestaudio https://www.youtube.com/watch?v=CoNI7ToYlxE"
# audio_link = "yt-dlp.exe --list-formats https://www.youtube.com/watch?v=CoNI7ToYlxE"
os.system(audio_link)