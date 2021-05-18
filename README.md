# Prolific auto-refresh

The main goal of this script is to get our beloved "start now" (or "reserve place") button back, which was recently hidden by Prolific and replaced by a rather ugly "Study is full". It accomplishes that by automatically refreshing the page as long as the current study is full. When a spot is available again it'll stop refreshing and you can finally spam the button (and hopefully get the study).

Currently it only works on Windows and with Chrome.

Step by step instructions:

1) Download python 3 from the official website: https://www.python.org/downloads/
2) Download pip manager (useful for installing software needed for the script to work) from the official website: https://bootstrap.pypa.io/get-pip.py \
    2.1) When you're on that page, right click on it, then click on "Save as" and you'll be prompted to download "get-pip.py"
3) Install pip by doing the following: \
    3.1) Open CMD by pressing WIN + R and then typing "cmd". \
    3.2) Then write "python" followed by the path in which "get-pip.py" is located, like this: python C:\Users\INSERT YOUR USER HERE\Desktop\get-pip.py
4) Install the required libraries: \
    4.1) While still in the CMD, write: pip install -r C:\Users\INSERT YOUR USER HERE\Desktop\requirements.txt -> remember to use your actual path
5) Download chrome driver from the official website and choose the latest stable one (currently v.90): https://chromedriver.chromium.org/downloads
6) Put chrome driver folder (named chromedriver_win32) inside the script's main folder (e.g. prolific_refresher/chromedriver_win32/chromedriver.exe)

You're almost done. Three more things need to be modified in order for the script to work:

1) Edit start_script.bat by inserting your actual paths to python.exe and to the script (refresher.py)
2) Open login.py with a text editor and write your prolific email (where it says "INSERT YOUR EMAIL HERE") and password ("INSERT YOUR PASSWORD HERE")
3) Edit "refresher.py" (by replacing "INSERT YOUR STUDY URL HERE") with the link to the study on which you want to use the script.

Congratulations, the prep work is done. You can start it by double clicking on start_script.bat.



For any doubts regarding the setup or any bugs you may encounter, you can also let me know through discord: https://discord.gg/RSBXApxJdB
