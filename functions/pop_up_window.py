# SETTINGS BUTTON - POP UP WINDOW

from tkinter import *
from tkinter import filedialog

import webbrowser
import os

from functions import messages

from functions import settings
settings_data = settings.open_settings()




# SEARCH FIELD LENGTH
search_field_length = 40

def launch(window):
    settings_data = settings.open_settings()
# COLORS - FONT STYLE
    background_color = settings_data['background_color'] 
    field_background_color = settings_data['field_background_color'] 
    font_style = settings_data['font_style']
    font_size = settings_data['font_size']
    font_color = settings_data['font_color']

# BUTTON SIZE
    button_height = 1
    button_width = 10
# WINDOW     
    top_window = Toplevel(window)
    top_window.title("Settings")
    window_width = 447
    window_length = 138
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    top_window.geometry(f'{window_width}x{window_length}+%d+%d' % (screen_width/2+180, screen_height/2+27))    
    top_window.resizable(0,0)
    top_window.configure(background=settings_data['background_color'])
# ICON
    top_window.iconbitmap('./skin/icon_popup.ico')
# RECTANGLES
    canvas_color = settings_data['background_color']
    canvas_frame_color = settings_data['canvas_frame_color']
    canvas = Canvas(top_window, width=window_width, height=window_length, background = background_color)
    canvas.create_rectangle(5-1, 5+2, window_width-5, window_length-5, outline=canvas_frame_color, fill=canvas_color)
    canvas.pack()

## WIDGETS
## YT-DLP LOCATION - FIELD + BROWSE BUTTON
    yt_dlp_location_field = Text(top_window, height = 1, width = search_field_length, foreground=font_color, background="white", font=(font_style, font_size))
    # yt_dlp_location_field.place(x=x_field, y=y_field)

    if settings_data['path_yt_dlp'] == "":
        yt_dlp_location_field.insert(END,"mandatory")
    else:
        yt_dlp_location_field.insert(END, settings_data['path_yt_dlp'])

    def browse_location():
        file_name = filedialog.askopenfilename(initialdir = "/",
                    title = "Select a File",
                    filetypes = (("Executable", "*.exe"),
                                ("all files", "*.*")))
        yt_dlp_location_field.delete('1.0', END)       # once a button is clicked, removes the previous value
        yt_dlp_location_field.insert(END,file_name)     # adding the path and the name of the selected file

    yt_dlp_location_button = Button(top_window, height=button_height, width=button_width, text = "YT-DLP", command = browse_location, foreground=font_color, background=background_color, activeforeground=background_color, activebackground=font_color)


## FFMPEG LOCATION - FIELD + BROWSE BUTTON
    ffmpeg_location_field = Text(top_window, height = 1, width = search_field_length, foreground=font_color, background="white", font=(font_style, font_size))
    if settings_data['path_ffmpeg'] == "":
        ffmpeg_location_field.insert(END,"non-mandatory, if already added to system path")
    else:
        ffmpeg_location_field.insert(END, settings_data['path_ffmpeg'])

    def browse_location():
        file_name = filedialog.askopenfilename(initialdir = "/",
                    title = "Select a File",
                    filetypes = (("Executable", "*.exe"),
                                ("all files", "*.*")))
        ffmpeg_location_field.delete('1.0', END)       # once a button is clicked, removes the previous value
        ffmpeg_location_field.insert(END,file_name)     # adding the path and the name of the selected file

    ffmpeg_location_button = Button(top_window, height=button_height, width=button_width, text = "FFmpeg", command = browse_location, foreground=font_color, background=background_color, activeforeground=background_color, activebackground=font_color)

## HELP BUTTON
    def help():
        webbrowser.open('https://github.com/K4KarolE/Video_Downloader#guide')
    help_button = Button(top_window, height=button_height, width=button_width, text = "Help", command = help, foreground=font_color, background=background_color, activeforeground=background_color, activebackground=font_color)

## UPDATE YT-DLP
    def update_yt_dlp():
        path_yt_dlp = settings_data['path_yt_dlp']
        parameter = '-U'
        executable =  f'{path_yt_dlp} {parameter}'
        os.system(executable)

    update_yt_dlp_button = Button(top_window, height=button_height, width=button_width+5, text = "Update YT-DLP", command = update_yt_dlp, foreground=font_color, background=background_color, activeforeground=background_color, activebackground=font_color)

## SAVE
    def save():
        settings_data = settings.open_settings()
        path_yt_dlp = yt_dlp_location_field.get("1.0", "end-1c")
        if "mandatory" not in path_yt_dlp:
            settings_data['path_yt_dlp'] = path_yt_dlp

        path_ffmpeg = ffmpeg_location_field.get("1.0", "end-1c")
        if "mandatory" not in path_ffmpeg:
            settings_data['path_ffmpeg'] = path_ffmpeg

        settings.save_settings(settings_data)
        messages.error_pop_up('Confirmation','saved')
             

    save_button = Button(top_window, height=button_height, width=button_width, text = "Save", command = lambda: [save()], foreground=font_color, background=background_color, activeforeground=background_color, activebackground=font_color)

## DISPLAY WIDGETS
    # FIELD
    x_field = 17
    y_field = 20
    # BUTTON
    x_button = 350
    y_button_base = 15

    def y_location(gap):
        location = y_button_base + 20 * gap
        return location

    # YT-DLP LOCATION - FIELD + BROWSE BUTTON
    yt_dlp_location_field.place(x=x_field, y=y_field)
    yt_dlp_location_button.place(x=x_button, y=y_location(0)+2)

    # FFMPEG LOCATION - FIELD + BROWSE BUTTON
    ffmpeg_location_field.place(x=x_field, y=y_location(2))
    ffmpeg_location_button.place(x=x_button, y=y_location(2)-2)

    # HELP BUTTON
    help_button.place(x=x_field, y=y_location(4))

    # UPDATE YT-DLP - BUTTON
    update_yt_dlp_button.place(x=x_field+80, y=y_location(4))

    # SAVE BUTTON
    save_button.place(x=x_button, y=y_location(4))
