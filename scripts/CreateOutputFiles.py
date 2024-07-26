from pydub import AudioSegment
import os, sys
import argparse
import csv

rootpath = parent_dir = os.path.dirname(os.path.dirname(__file__))


def main(soundpack, filetype):
    soundpackpath = os.path.join(rootpath,"soundpacks",soundpack)
    with open(rootpath +'/sound_list.csv', newline='') as csvfile:

        soundlist = csv.reader(csvfile, delimiter=',', quotechar='\"')
        for sound in soundlist:
            
            soundnumber = sound[0].split(".")[0]+"."
            soundorigin = os.path.join(soundpackpath, soundnumber + filetype)
            sounddestination = os.path.join(soundpackpath,"output",soundnumber+"ogg")
            fullpath = os.path.join(soundpackpath,soundorigin)
            if(os.path.isfile(fullpath)):
                AudioSegment.from_file(soundorigin).export(sounddestination, format='ogg')
                #print(soundorigin)
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some parameters.')
    parser.add_argument('--soundpack', type=str, required=True, help='The name of the soundpack, you want to use')
    parser.add_argument('--filetype', type=str, required=True, help="File extensions of the original file")
    args = parser.parse_args()
    main(args.soundpack, args.filetype)


