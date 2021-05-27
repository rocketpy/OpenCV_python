#  cv2-tools - Library to help the drawing process with OpenCV. Thought to add labels to the images. Classification of images, etc.

# PyPi: https://pypi.org/project/cv2-tools/
# Github: https://github.com/fernaper/cv2-tools

# pip install cv2-tools

#  Installation
"""
You will need to install:

   1. opencv >= 3.6.2
   2. numpy >= 1.13.3
   3. python-constraint >= 1.4.0

You can simply execute: pip install -r requirements.txt

Finally you can install the library with:

pip install cv2-tools

When you install cv2-tools, it will automatically download numpy but not opencv becouse in some cases you will need another version.
"""

# Test
import cv2_tools

print('Name: {}\nVersion:{}\nHelp:{}'.format(cv2_tools.name,cv2_tools.__version__,cv2_tools.help))
webcam_test()

# For example:
# Open a a stream (your webcam).

from cv2_tools.Managment import ManagerCV2
import cv2

# keystroke=27 is the button `esc`
manager_cv2 = ManagerCV2(cv2.VideoCapture(0), is_stream=True, keystroke=27, wait_key=1, fps_limit=60)

  # This for will manage file descriptor for you
for frame in manager_cv2:
    cv2.imshow('Example easy manager', frame)
      
cv2.destroyAllWindows()
print(manager_cv2.get_fps())

# If you want to use another button and you don't know the ID, you can check easily using the following code:

from cv2_tools.Managment import ManagerCV2
import cv2

# keystroke=27 is the button `esc`
manager_cv2 = ManagerCV2(cv2.VideoCapture(0), is_stream=True, keystroke=27, wait_key=1, fps_limit=60)

# This for will manage file descriptor for you
for frame in manager_cv2:
    # Each time you press a button, you will get its id in your terminal
    last_keystroke = manager_cv2.get_last_keystroke()
    if last_keystroke != -1:
        print(last_keystroke)
    cv2.imshow('Easy button checker', frame)
cv2.destroyAllWindows()



