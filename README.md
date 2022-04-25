# PDF-rename-V2
In this script we address the requests in video #1 (on the main branch) which include:
  1. Error handeling 
  2. Regex to isolate text in PDFs 
  
## **VIDEO TUTORIAL/EXPLANIATION:**


## **Note:** This tutorial assumes you have:
  1. Python 3.9.5 
  2. pip3
  3. Visual Studio Code (VSC)


#### STEPS
1. Change default profile within VSC:
    * CTRL + SHIFT + P
    * Search "Terminal: Select Default Profile"
    * Click "Command Prompt" 
   
2. Create and activate the virtual environment + install library (run commands in a new CMD terminal)
   1. py -m venv venv 
      * (Creates virtual environment)
   2. venv\Scripts\activate                   
      * (activates virtual environment)
   3. python -m pip install --upgrade pip     
      * (Upgrade pip in virtual environment)
   4. python -m pip install --upgrade pymupdf 
      * (Install the PyMuPDF library)
   
3. Create the python file (you can use any name or follow the tutorial)

## **LINKS TO REGEX SITES:** 
Regex101.com: https://regex101.com/ \
Regex cheat sheat: https://www.debuggex.com/cheatsheet/regex/python \
Positive lookbehind: https://stackoverflow.com/questions/2973436/regex-lookahead-lookbehind-and-atomic-groups 

## **REGEX USED IN THE VIDEO:** 
If you DO NOT care about the format of the order number use this expression instead:

(?<=Order #: ).+

![image](https://user-images.githubusercontent.com/45050434/165182953-afd73f00-e155-43cf-abf8-dd2cc2ee9cc6.png)

#### IMPORTANT
This is a brief explanation of how to use regex in a real-life scenario. Regex is a whole language which can accomplish much more than what is described in the video. If you still have questions, leave them on the YouTube video or here.
