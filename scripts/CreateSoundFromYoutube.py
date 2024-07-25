from pytubefix import YouTube
from moviepy.editor import VideoFileClip
import os, sys
import argparse

def main(youtube_url, soundpack, sound_id):
    yt = YouTube(youtube_url).streams.filter(file_extension='mp4').first().download()

    # Load the MP4 file
    video = VideoFileClip(yt)

    # Extract audio and write it as an OGG file
    audio = video.audio
    audioname = soundpack + "../soundpacks/output/" + sound_id + ".ogg"
    audio.write_audiofile(audioname, codec='libvorbis')
    video.close()

    try: 
        os.remove(yt)
    except FileNotFoundError: 
        print(f"File '{yt}' not found.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some parameters.')
    
    parser.add_argument('--youtube_url', type=str, required=True, help='URL of the video, where we will extract the audio from')
    parser.add_argument('--soundpack', type=str, required=True, help='The name of the soundpack, you want to use')
    parser.add_argument('--sound_id', type=str, required=True, help='The id of the sound, corresponding to the list')
    args = parser.parse_args()
    main(args.youtube_url, args.soundpack, args.sound_id)