import os
import glob


for filepath in sorted(glob.glob('./*.mid')):
    midfile = os.path.basename(filepath)
    os.system("sudo python play.py " + str(midfile))
