import os

import subprocess
from pathlib import Path


# get the current working directory...
dir_path = os.path.dirname(os.path.realpath(__file__))

vidfile = dir_path + '/media/vids/mv1.mov'

watermark = dir_path + '/media/watermark.png'
compressed = str(dir_path) + '/media/compressed/'


media_out = str(dir_path + "/compressed_mv1s.mov").replace(" ", "\\ ")
media_watermarked = str(compressed + '/w_mv1.mov').replace(" ", "\\ ")

print(compressed)
print(media_watermarked)
# quit()

# run two processes on the video...
subprocess.run("ffmpeg -i " + vidfile.replace(" ", "\\ ") +
               " -vcodec libx264 -crf 22 " + media_out, shell=True)

subprocess.run("ffmpeg -i " + media_out + " -i " + watermark +
               " -filter_complex \"overlay=main_w-(overlay_w+10) : main_h-(10+overlay_h)\" " + media_watermarked, shell=True)
