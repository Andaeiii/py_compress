import subprocess
import os
import shutil           # to move files to another folder.

from pathlib import Path

filesArr = []
finalArr = []

# get the current working directory...
dir_path = os.path.dirname(os.path.realpath(__file__))
compressed = str(dir_path) + '/media/compressed/'
rootdir = dir_path + '/media/vids'

watermark = dir_path + '/media/watermark.png'

print(compressed)

# quit()  # or os._exit(), sys.exit()  -stops execution here.... ~ same


for subdirs, dirs, files in os.walk(rootdir):
    # print(dirs)
    # print(files)
    for file in files:  # iterates through all the files in all the folders...
        # print(file)
        extension = os.path.splitext(file)[-1].lower()
        if extension == ".mov":
            # print('Apple - ' + file)
            media_in = subdirs + "/" + file

            media_out = str(dir_path+"/compressed_"+file).replace(" ", "\\ ")

            media_watermarked = str(compressed+'/'+file).replace(" ", "\\ ")

            # run two processes on the video...
            subprocess.run("ffmpeg -i " + media_in.replace(" ", "\\ ") +
                           " -vcodec libx264 -crf 22 " + media_out, shell=True)
            filesArr.append(media_in)

            print("file (" + media_in + ") - removed to server")

            subprocess.run("ffmpeg -i " + media_out + " -i " + watermark +
                           " -filter_complex \"overlay=main_w-(overlay_w+10) : main_h-(10+overlay_h)\" " + media_watermarked, shell=True)

            filesArr.append(media_out)
            finalArr.append(media_watermarked)

            print("file (" + media_out + ") - removed to server")

            # pass
        elif extension == ".mp4":
            # print('MP4__ - ' + file)
            pass
        else:
            pass


print(filesArr)

# delete files if they exist...

for file in filesArr:
    if os.path.exists(file):
        print("file (" + file + ") - removed to server")
        os.remove(file)


# for file in finalArr:
#     if os.path.exists(file):
#         shutil.move(file, dir_path + '/compressed/'+file)
#         print("file (" + file + ") - to new location")
