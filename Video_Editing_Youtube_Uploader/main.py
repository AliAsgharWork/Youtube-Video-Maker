# from selenium import webdriver

# url = "https://www.google.co.uk" #input("Enter your the job description URL: ")

# browser = webdriver.Chrome()
# browser.get(url)

# # browser.quit()

# Import everything needed to edit video clips
from moviepy.editor import *

# Load myHolidays.mp4 and select the subclip 00:00:50 - 00:00:60
clip = VideoFileClip("video\\vid.mp4").subclip(25, 30)
clip2 = VideoFileClip("video\\vid.mp4").subclip(45, 50)

# Reduce the audio volume (volume x 0.8)
clip = clip.volumex(0)
clip2 = clip2.volumex(0)

#Read the sound clip
snd = AudioFileClip("audio\\audio.mp3")

# # Generate a text clip. You can customize the font, color, etc.
# txt_clip = TextClip("My Holidays 2013",fontsize=70,color='white')
# Plays the note A (a sine wave of frequency 440HZ)

# # Say that you want it to appear 10s at the center of the screen
# txt_clip = txt_clip.set_pos('center').set_duration(10)

# Overlay the text clip on the first video clip

video = concatenate_videoclips([clip2, clip]).set_audio(snd)
# video = CompositeVideoClip([clip2, clip])

# Write the result to a file (many options available !)
video.write_videofile("myHolidays_edited.mp4")