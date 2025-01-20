# SETTINGS BUTTON - POP UP WINDOW

from tkinter import *
from tkinter import filedialog

import sys
import webbrowser
import os
from pathlib import Path

from functions import messages
from functions import settings
settings_data = settings.open_settings()



# SEARCH FIELD LENGTH
search_field_length = 40
os_linux: bool = sys.platform == 'linux'

def get_path_yt_dlp():
    path_yt_dlp = settings_data['path_yt_dlp']
    return path_yt_dlp


def launch(window):
    settings_data = settings.open_settings()

    # COLORS - FONT STYLE
    background_color = settings_data['background_color']
    font_style = settings_data['font_style']
    font_size = settings_data['font_size']
    font_color = settings_data['font_color']

    # BUTTON SIZE
    button_height = 1
    if os_linux:
        button_width = 7
    else:
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
    if not os_linux:
        working_directory = os.path.dirname(__file__).strip('functions')
        path_icon_popup = Path(working_directory, "skin", "icon_popup.ico") 
        top_window.iconbitmap(path_icon_popup)
    # RECTANGLES
    canvas_color = settings_data['background_color']
    canvas_frame_color = settings_data['canvas_frame_color']
    canvas = Canvas(top_window, width=window_width, height=window_length, background = background_color)
    canvas.create_rectangle(5-1, 5+2, window_width-5, window_length-5, outline=canvas_frame_color, fill=canvas_color)
    canvas.pack()
    
    # CLASSES
    class Buttons:
        def __init__(self, text, command):
            self.text = text
            self.command = command
        
        def create(self):
            return Button(top_window, 
                          height=button_height,
                          width=button_width,
                          text = self.text,
                          command = self.command,
                          foreground=font_color,
                          background=background_color,
                          activeforeground=background_color,
                          activebackground=font_color)

    class Fields:
        def __init__(self, width, background):
            self.width = width
            self.background = background
        
        def create(self):
            return Text(top_window,
                        height = 1,
                        width = self.width,
                        foreground=font_color,
                        background=self.background,
                        font=(font_style, font_size))


    ## WIDGETS
    ## YT-DLP LOCATION - FIELD + BROWSE BUTTON
    yt_dlp_location_field_instance = Fields(search_field_length, "white")
    yt_dlp_location_field = yt_dlp_location_field_instance.create()

    if settings_data['path_yt_dlp'] == "":
        yt_dlp_location_field.insert(END,"mandatory")
    else:
        yt_dlp_location_field.insert(END, settings_data['path_yt_dlp'])

    def browse_location_yt_dlp():
        if os_linux:
            messages.error_pop_up(
                'Information',
                'linux_add_yt_dlp_path')
            file_name = filedialog.askdirectory()
        else:
            file_name = filedialog.askopenfilename(initialdir = "/",
                        title = "Select a File",
                        filetypes = (("Executable", "*.exe"),
                                    ("all files", "*.*")))
        yt_dlp_location_field.delete('1.0', END)       # once a button is clicked, removes the previous value
        yt_dlp_location_field.insert(END,file_name)     # adding the path and the name of the selected file

    yt_dlp_location_button_instance = Buttons("YT-DLP", lambda:[browse_location_yt_dlp()])
    yt_dlp_location_button = yt_dlp_location_button_instance.create()


    ## FFMPEG LOCATION - FIELD + BROWSE BUTTON
    ffmpeg_location_field_instance = Fields(search_field_length,"white")
    ffmpeg_location_field = ffmpeg_location_field_instance.create()

    if settings_data['path_ffmpeg'] == "":
        if os_linux:
            field_text = "LINUX: it have to be added to the system path"
        else:
            field_text = "non-mandatory, if already added to system path"
        ffmpeg_location_field.insert(END,field_text)
    else:
        ffmpeg_location_field.insert(END, settings_data['path_ffmpeg'])

    def browse_location_ffmpeg():
        file_name = filedialog.askopenfilename(initialdir = "/",
                    title = "Select a File",
                    filetypes = (("Executable", "*.exe"),
                                ("all files", "*.*")))
        ffmpeg_location_field.delete('1.0', END)       # once a button is clicked, removes the previous value
        ffmpeg_location_field.insert(END,file_name)     # adding the path and the name of the selected file

    ffmpeg_location_button_instance = Buttons("FFmpeg", lambda: [browse_location_ffmpeg()])
    ffmpeg_location_button = ffmpeg_location_button_instance.create()
    if os_linux:
        ffmpeg_location_button.configure(state=DISABLED)

    ## HELP BUTTON
    def help():
        webbrowser.open('https://github.com/K4KarolE/Video_Downloader#guide')
    
    help_button_instance = Buttons("Help", lambda:[help()])
    help_button = help_button_instance.create()

    ## UPDATE YT-DLP - BUTTON
    def update_yt_dlp():
        path_yt_dlp = get_path_yt_dlp()
        # parameter = "-U" # standard build
        parameter = "--update-to nightly"   # nightly build // https://github.com/yt-dlp/yt-dlp#update-channels
        executable =  f'{path_yt_dlp} {parameter}'
        os.system(executable)

    update_yt_dlp_button_instance = Buttons("Update YT-DLP", lambda:[update_yt_dlp()])
    update_yt_dlp_button = update_yt_dlp_button_instance.create()
    update_yt_dlp_button.configure(width=button_width+5)

    ## SAVE - BUTTON
    def save():
        settings_data = settings.open_settings()
        path_yt_dlp = yt_dlp_location_field.get("1.0", "end-1c")
        if os.path.isfile(path_yt_dlp):
            settings_data['path_yt_dlp'] = path_yt_dlp

        path_ffmpeg = ffmpeg_location_field.get("1.0", "end-1c")
        if os.path.isfile(path_ffmpeg):
            settings_data['path_ffmpeg'] = path_ffmpeg

        settings.save_settings(settings_data)
        messages.error_pop_up('Confirmation','saved')
             
    save_button_instance = Buttons("Save", lambda: [save()])
    save_button = save_button_instance.create()


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
