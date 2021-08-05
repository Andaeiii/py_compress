import os
import subprocess

# get the current working directory...
dir_path = os.path.dirname(os.path.realpath(__file__))
rootdir = dir_path + '/media/vids'

watermark = dir_path + '/media/watermark.png'

for subdirs, dirs, files in os.walk(rootdir):
    # print(dirs)
    # print(files)
    for file in files:  # iterates through all the files in all the folders...
        # print(file)
        extension = os.path.splitext(file)[-1].lower()
        if extension == ".mov":
            #print('Apple - ' + file)
            media_in = subdirs + "/" + file
            media_out = str(dir_path + "/compressed_" +
                            file).replace(" ", "\\ ")

            # run two processes on the video...
            subprocess.run("ffmpeg -i " + media_in.replace(" ", "\\ ") +
                           " -vcodec libx264 -crf 22 " + media_out, shell=True)
            subprocess.run("ffmpeg -i" + media_out + " -i " + watermark +
                           " -filter_complex \"overlay=main_w-(overlay_w+10) : main_h-(10+overlay_h)\"" + media_out, shell=True)

            pass
        elif extension == ".mp4":
            print('MP4__ - ' + file)
            pass
        else:
            pass
