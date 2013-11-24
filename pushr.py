#Written By Roger Aiudi
#Revised By Collin Lakeland

import os

msg = raw_input("Please enter a commit reason: ")
os.system("git add .")
os.system("git commit -m \"{0}\"".format(msg))
os.system("git push")
