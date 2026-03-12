from tkinter import *
from tkinter import ttk
from tkinter import font
import datetime
import resources.config as config

global endTime


def quit(*args):
    root.destroy()


def show_time():
    # Get the time remaining until the event
    remaining = (endTime - datetime.datetime.now()).total_seconds()
    if remaining < 0:
        countdown_string = config.Get('passed_text')
    else:
        # calculate the seconds remaining
        secs_remaining = int(remaining % 60)
        remaining //= 60
        secs_string = ('%sS' % str(secs_remaining)).rjust(2, '0')
        # calculate the minutes remaining
        mins_remaining = remaining % 60
        remaining //= 60
        mins_string = ('%sM' % str(mins_remaining)).rjust(2, '0')
        # calculate the hours remaining
        hours_remaining = int(remaining % 24)
        remaining //= 24
        hours_string = ('%sH' % str(hours_remaining).rjust(2, '0'))
        # calculate the days remaining
        days_remaining = int(remaining)
        days_string = "%sD" % str(days_remaining)
        # pack the calculated times into a string to show
        if days_remaining > 0:
            countdown_string = "%s %s" % (days_string, hours_string)
        else:
            countdown_string = "%s %s" % (hours_string, mins_string)
    # Show the time left
    txt.set(countdown_string)
    # Trigger the countdown after 1000ms
    root.after(1000, show_time)


# Use tkinter lib for showing the clock
root = Tk()
if config.Get('fullscreen'):
    root.attributes("-fullscreen", True)
else:
    root.geometry(
        f"{config.Get('screen_width')}x{config.Get('screen_height')}")
root.configure(background='black')
root.bind("x", quit)
root.after(1000, show_time)

# Set the end date and time for the countdown
endTime = datetime.datetime(config.Get('end_year'), config.Get(
    'end_month'), config.Get('end_day'), config.Get('end_hour'), 0, 0)

txt = StringVar()
fnt_header = font.Font(family=config.Get(
    'font'), size=config.Get('header_size'), weight='bold')
fnt_countdown = font.Font(family=config.Get(
    'font'), size=config.Get('countdown_size'), weight='bold')
style = ttk.Style(root)
style.theme_use('classic')
style.configure('Header.TLabel', font=fnt_header,
                foreground=config.Get('header_color'), background='black')
style.configure('Countdown.TLabel', font=fnt_countdown,
                foreground=config.Get('countdown_color'), background='black')
lbl1 = ttk.Label(root, text=config.Get('header_text'), style='Header.TLabel')
lbl1.place(relx=0.5, rely=config.Get('header_y_pos'), anchor=CENTER)
lbl2 = ttk.Label(root, textvariable=txt, style='Countdown.TLabel')
lbl2.place(relx=0.5, rely=config.Get('countdown_y_pos'), anchor=CENTER)

root.mainloop()
