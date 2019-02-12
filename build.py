#import subprocess
# bashCommand = 'rm docs/*.html'
# process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
# output, error = process.communicate()

#import os
#os.remove("/home/lboylan/Documents/Homework_BE/H2/personal_profile/docs/index.html")
#os.remove("/home/lboylan/Documents/Homework_BE/H2/personal_profile/docs/abilities.html")
#os.remove("/home/lboylan/Documents/Homework_BE/H2/personal_profile/docs/projects.html")
#print("File Removed!")

top=open("templates/top.html").read()
home_msg=open("content/home_msg.html").read()
resource_btns=open("templates/resource_buttons.html").read()
bottom=open("templates/bottom.html").read()
skills_msg=open("content/skills_msg.html").read()
skills=open("content/skills.html").read()
proj=open("content/projects.html").read()

# "w" Opens a file for writing only.
# Overwrites the file if the file exists.
# If the file does not exist, creates a new file for writing.
open("docs/index.html"    , "w").write(top + home_msg + resource_btns + bottom)
open("docs/abilities.html", "w").write(top + skills_msg + resource_btns + skills + bottom)
open("docs/projects.html" , "w").write(top + resource_btns + proj + bottom)