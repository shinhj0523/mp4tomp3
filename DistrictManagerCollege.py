import moviepy.editor as mp

for i in range(1,10+1):
    for j in range(1,2+1):

        clip = mp.VideoFileClip(f"{i}-{j}.mp4")
        clip.audio.write_audiofile(f"구역장{i}-{j}.mp3")
