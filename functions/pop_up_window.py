from tkinter import *
from tkinter import filedialog

from functions import settings
settings_data = settings.open_settings()

# COLORS - FONT STYLE
background_color = settings_data['background_color'] 
field_background_color = settings_data['field_background_color'] 
font_style = settings_data['font_style']
font_color = settings_data['font_color']

# BUTTON SIZE
button_height = 1
button_width = 10

# SEARCH FIELD LENGTH
search_field_length = 40

## SETTINGS BUTTON - POP UP WINDOW
def launch(window):
    top_window = Toplevel(window)
    top_window.title("Settings")
    window_width = 447
    window_length = 200
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    top_window.geometry(f'{window_width}x{window_length}+%d+%d' % (screen_width/2+180, screen_height/2-35))    
    top_window.resizable(0,0)
    top_window.configure(background=settings_data['background_color'])
    #ICON
    top_window.iconbitmap('./skin/icon_popup.ico')
    # RECTANGLES
    canvas_color = settings_data['background_color']
    canvas_frame_color = settings_data['canvas_frame_color']
    canvas = Canvas(top_window, width=window_width, height=window_length, background = background_color)
    canvas.create_rectangle(5-1, 5+2, window_width-5, window_length-5, outline=canvas_frame_color, fill=canvas_color)
    canvas.pack()

    # FIELD
    x_field = 17
    y_field = 20
    # BUTTON
    x_button = 350
    y_button_base = 15

    def y_location(gap):
        location = y_button_base + 20 * gap
        return location

    ## YT-DLP LOCATION - FIELD + BROWSE BUTTON
    yt_dlp_location_field = Text(top_window, height = 1, width = search_field_length, foreground=font_color, background="white")
    yt_dlp_location_field.place(x=x_field, y=y_field)

    def browse_location():
        file_name = filedialog.askopenfilename(initialdir = "/",
                    title = "Select a File",
                    filetypes = (("Executable", "*.exe"),
                                ("all files", "*.*")))
        yt_dlp_location_field.delete('1.0', END)       # once a button is clicked, removes the previous value
        yt_dlp_location_field.insert(END,file_name)     # adding the path and the name of the selected file

    yt_dlp_location_button = Button(top_window, height=button_height, width=button_width, text = "YT-DLP", command = browse_location, foreground=font_color, background=background_color, activeforeground=background_color, activebackground=font_color)
    yt_dlp_location_button.place(x=x_button, y=y_location(0))

    ## FFMPEG LOCATION - FIELD + BROWSE BUTTON
    ffmpeg_location_field = Text(top_window, height = 1, width = search_field_length, foreground=font_color, background="white")
    ffmpeg_location_field.place(x=x_field, y=y_location(2))

    def browse_location():
        file_name = filedialog.askopenfilename(initialdir = "/",
                    title = "Select a File",
                    filetypes = (("Executable", "*.exe"),
                                ("all files", "*.*")))
        ffmpeg_location_field.delete('1.0', END)       # once a button is clicked, removes the previous value
        ffmpeg_location_field.insert(END,file_name)     # adding the path and the name of the selected file

    ffmpeg_location_button = Button(top_window, height=button_height, width=button_width, text = "FFmpeg", command = browse_location, foreground=font_color, background=background_color, activeforeground=background_color, activebackground=font_color)
    ffmpeg_location_button.place(x=x_button, y=y_location(2))
