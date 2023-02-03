'''
ffmpeg

- will be able to download higher than 720p + merge video-audio
- https://windowsloop.com/install-ffmpeg-windows-10/#add-ffmpeg-to-Windows-path
'''
# test link: https://youtu.be/7AwWEU5nsBA
# thumbnail: https://img.youtube.com/vi/7AwWEU5nsBA/maxresdefault.jpg
 
import sys
import os
import webbrowser
import pyperclip
import urllib.request



from tkinter import *
from tkinter import filedialog      # for browse window (adding path)
import tkinter.messagebox           # for pop-up windows
from PIL import Image,ImageTk       # PILLOW import has to be after the tkinter impoert (Image.open will not work: 'Image has no attributesm open')

from functions import settings
settings_data = settings.open_settings()        # access to the saved/default settings (settings_db.json)

# COLORS - FONT STYLE
# original tkinter grey: #F0F0F0 - FYI
background_color = settings_data['background_color'] 
field_background_color = settings_data['field_background_color'] 
font_style = settings_data['font_style']
font_color = settings_data['font_color']


# WINDOW
window = Tk()
window.title(settings_data['window_title'])
width = 500
length = 600
window.geometry(f'{width}x{length}')
window.resizable(0,0)   # locks the main window
window.configure(background="grey")  # - FYI


yt_dlp_path = 'd:\Applications\YouTube-DLP\yt-dlp.exe'      # will come from UI - browse window



### WIDGETS
# AUDIO / VIDEO OPTIONS + ROLL DOWN BUTTON
av_options = {
    "Audio Only": "audio only",
    "360p": "360",
    "480p": "480",
    "720p": "720",
    "1080p": "1080",
    "1440p": "1440",
    "2160p": "2160",
}

av_options_list=[]
for item in av_options.keys():
    av_options_list += [item]       # Audio Only - 2160p

av_options_roll_down_clicked = StringVar()
av_options_roll_down_clicked.set("Audio / Video")    
av_options_roll_down = OptionMenu( window, av_options_roll_down_clicked, *av_options_list, command=None)     
av_options_roll_down.configure(foreground=font_color, background=background_color, activeforeground = font_color, activebackground=background_color, highlightbackground=background_color)
av_options_roll_down['menu'].configure(foreground=font_color, background=background_color, activebackground=background_color)

## GET THE LINK - BUTTON
# GET URL
def get_url():
    link = pyperclip.paste()
    # counter = 0
    # while 'youtu' not in link:
    #     counter += 1
    #     # messages.error_pop_up('wrong_link')
    #     link = pyperclip.paste()
    #     if counter == 3:
    #         sys.exit()
    settings_data['yt_url'] = link
    settings.save_settings(settings_data)

# # SAVE AVAILABLE FORMATS > FORMATS.TXT
# def save_available_formats():
#     link = settings_data['yt_url']
#     parameter = '-F'
#     executable =  f'{yt_dlp_path} {parameter} {link} > formats.txt'     # writes the available formats into the txt file
#     os.system(executable)
#     print('\n')

# # GET INFORMATION > INFO.TXT
def save_info():
    link = settings_data['yt_url']
    parameter = '--get-id --get-filename --get-duration'
    executable =  f'{yt_dlp_path} {parameter} {link} > info.txt'     # writes the available formats into the txt file
    os.system(executable)
    print('\n')

# SAVE BASIC VIDEO INFORMATION
def extract_info():
    file = open(r'.\info.txt','r+')
    listFile = list(file)
    yt_video_ID = listFile[0].strip('\n')
    yt_video_title = listFile[1].strip(f'[{yt_video_ID}].webm\n')
    yt_video_duration = listFile[2].strip('\n')
    if ':' not in yt_video_duration:
        yt_video_duration = yt_video_duration + 's'
    settings_data['yt_video_ID'] = yt_video_ID
    settings_data['yt_video_title'] = yt_video_title
    settings_data['yt_video_duration'] = yt_video_duration
    settings.save_settings(settings_data)

# SAVE THUMBNAIL
def save_thumbnail():
    yt_video_ID = settings_data['yt_video_ID']
    thumbnail_found = False
    while thumbnail_found == False:
        for res in ['maxres', 'hqres', 'hq', 'mq', 'sd', '']:   # find the highest resolution available
            try:
                imgURL = f"https://img.youtube.com/vi/{yt_video_ID}/{res}default.jpg"
                urllib.request.urlretrieve(imgURL, "./thumbnail/thumbnail.jpg")
                thumbnail_found = True
            except:
                pass

# DISPLAY THUMBNAIL
def display_thumbnail():
    global img  # Garbage Collection - https://stackoverflow.com/questions/16424091/why-does-tkinter-image-not-show-up-if-created-in-a-function
    my_img = Image.open(r".\thumbnail\thumbnail.jpg")
    n = 4
    width = int(1280 / n)
    height = int(720 / n)
    resized_image = my_img.resize((width, height))
    img = ImageTk.PhotoImage(resized_image)
    Label(window, image=img).place(x=8, y=300)

  
button_get_url = Button(window, text = "Get the URL", command = lambda: [
    get_url(),
    save_info(),
    extract_info(),
    save_thumbnail(),
    display_thumbnail()
 ],foreground=font_color, background=background_color, activeforeground=background_color, activebackground=font_color)        
# no () in command = your_function() otherwise will execute it automatically before clicking the button
# binding multiple commands to the same button: command = lambda: [save_settings(), engine.start_engine()]

# YT-DLP PATH + BROWSE FIELD

# TARGET LOCATION + BROWSE FIELD


# START - BUTTON
def start():
    if av_options_roll_down_clicked.get() not in av_options_list: 
        print('Select the Audio/Video option')
        return

    settings_data['av_selected'] = av_options_roll_down_clicked.get()


    settings.save_settings(settings_data)
    av_selected = av_options_roll_down_clicked.get()
    link = settings_data['yt_url']
    selected_resolution = av_options[av_selected]       #av_options['720p']

    if selected_resolution.isdecimal():                 # 360 - 2160
        parameter = f'-S "res:{selected_resolution}"'   # Download the best video available with the largest resolution but no better than {selected_resolution},
    else:                                               # or the best video with the smallest resolution if there is no video under {selected_resolution}
        parameter = '-f bestaudio'                      # Audio Only

    executable =  f'{yt_dlp_path} {parameter} {link}'
    os.system(executable)

button_start = Button(window, text = "START", command = start, foreground=font_color, background=background_color, activeforeground=background_color, activebackground=font_color)



### DISPLAY WIDGETS
def display_widgets():
    # BASE VALUES
    # X
    x = 350
    x_button_gap = 170
    x_gap_for_path_objects = 5
    # Y
    y_base = 130
    y_gap = 30

    
    def y_location(gap_by_number):
        display_y = y_base + y_gap * gap_by_number
        return display_y


    # GET URL - BUTTON
    button_get_url.place(x=x, y=y_location(1))

    # AUDIO / VIDEO OPTIONS - ROLL DOWN BUTTON
    av_options_roll_down.place(x=x, y=y_location(2.5))



    # START - BUTTON
    button_start.place(x=x, y=y_location(8))


display_widgets()

window.mainloop()


# SAVE AVAILABLE FORMATS
def available_formats(link):
    parameter = '-F'
    executable =  f'{yt_dlp_path} {parameter} {link} > formats.txt'     # writes the available formats into the txt file
    os.system(executable)
    print('\n')

# # UPDATE YT-DLP
# def update_yt_dlp():
#     parameter = '-U'
#     executable =  f'{yt_dlp_path} {parameter}'
#     os.system(executable)

# # OPEN YT-DLP GITHUB SITE
# def launch_yt_dlp_github():
#     link = 'https://github.com/yt-dlp/yt-dlp'

#     webbrowser.open(link)

# # OPEN YT-DLP GITHUB / RELEASE FILES to donwload yt-dlp.exe
# def launch_yt_dlp_download():