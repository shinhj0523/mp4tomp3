import moviepy.editor as mp
from glob import glob

vid_file = glob("*.mp4")


for i in vid_file:
    clip = mp.VideoFileClip(i)
    clip.audio.write_audiofile(f"{i[:-4]}.mp3")