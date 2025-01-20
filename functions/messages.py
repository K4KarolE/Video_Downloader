import tkinter.messagebox

popup_message_dic = {
    'no_yt_dlp': 'Please add YT-DLP via the "Settings" button',
    'destination_folder':'Please add the destination folder with the "Destination" button',
    'no_URL':'Please add a video link with the "Get URL" button',
    'no_resolution':'Please select the target format with the "Save as" button',
    'saved': 'Fields are saved',
    'linux_add_yt_dlp_path': 'Add the directory via the pop-up window'
                                  '\nand add the file name to the path manually.',
    'invalid_url_in_clipboard': 'Invalid URL in the clipboard'
    }

def error_pop_up(window_title, popup_message_dic_key):
    tkinter.messagebox.showinfo( window_title, f"{popup_message_dic[popup_message_dic_key]}")     # tkinter.messagebox.showinfo ( popup window title, message )

# EXAMPLE
# error_pop_up('Error','destination_folder')
# messages.error_pop_up('Error','destination_folder')