# Video Downloader
- Takes the video link from clipboard
    - Displaying the thumbnail, video title and duration
- Video resolution / just audio selectable
- Able to add via browse window or field:
    - Destination folder
    - [YT-DLP](https://github.com/yt-dlp/yt-dlp) path
    - [FFmpeg](https://ffmpeg.org/) path

<div align="center">
    <img src="screenshot/screenshot_1.png" </img> 
</div>
<br>
<div align="center">
    <img src="screenshot/screenshot_2.png" </img> 
</div>
<br>
<div align="center">
    <img src="screenshot/screenshot_3.png" </img> 
</div>
<br>
<div align="center">
    <img src="screenshot/screenshot_4.png" </img> 
</div>

# Requirements
### Install packages\dependencies
```
pip install -r requirements.txt
```

### Python 3 - used: 3.12
- https://www.python.org/


### YT-DLP [(link)](https://github.com/yt-dlp/yt-dlp#release-files)
- WINDOWS / LINUX
    - You are able to add the path of the `YT-DLP.exe / yt-dlp_linux` in the `Settings` window
    - Download the binary file: https://github.com/yt-dlp/yt-dlp?tab=readme-ov-file#installation
    - Updates to the latest `nightly` version by default (functions / pop_up_window / update_yt_dlp())

### FFmpeg [(link)](https://ffmpeg.org/)
- WINDOWS
    - If `FFmpeg` is not added to the system path:
        - You are able to add the path of the `ffmpeg.exe` in the `Settings` window
    - [Install FFmpeg on Windows 10/11](https://windowsloop.com/install-ffmpeg-windows-10/)
- LINUX
    - Via `Software Manager`

### Tkinter (LINUX only)
- Ubuntu/Mint: `sudo apt install python3-tk`

### Pyperclip (LINUX only)
- [https://pypi.org/project/pyperclip/](https://pypi.org/project/pyperclip/)
- " On Linux, this module makes use of the xclip or xsel commands,
which should come with the os. Otherwise run “sudo apt-get install xclip”
or “sudo apt-get install xsel” (Note: xsel does not always seem to work.) "

### OS
- Tested on `Windows 11` and `Linux Mint 22`

# Guide
- `Save as` \ `MP3` - saves the best audio source and converts it to MP3
- `Save as` \ video resolutions:
    - Download the best video available with the largest resolution but no better than the selected_resolution (no conversion)
    - Or the best video with the smallest resolution if there is no video under the selected_resolution (no conversion)

# Video Downloader - Where can be used
- `YouTube`
- `Vimeo`
- `Twitch`
- I used to have an imaginary friend, who heard from someone, that on this internet thing there are websites, where uncovered human body parts are displayed in motion. For real.
Well, I cannot confirm personally, but I would say there is a chance the `Video Downloader` works just fine on these sites too.


## Thank you all contributors of the `Python modules`, `YT-DLP` and `FFmpeg`!