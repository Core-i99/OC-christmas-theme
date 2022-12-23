import os
import shutil

if (os.path.exists("./Build/Output")):
    shutil.rmtree("./Build/Output")

os.mkdir("./Build/Output")
os.mkdir("./Build/Output/Temp")
os.mkdir("./Build/Output/Temp/Core-i99")

shutil.copytree("./Export/icns", "./Build/Output/Temp/Core-i99/Christmas/")

shutil.make_archive("./Build/Output/Core-i99-christmas-theme", "zip", "./Build/Output/Temp/")