# PDF-rename-V2
A small script that renames PDF files using a string of text from inside the PDF.

**VIDEO TUTORIAL/EXPLANIATION:**

https://www.youtube.com/watch?v=9kyBEaGw_Ic


**Note:** This tutorial assumes you have:
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

#### IMPORTANT
This is a basic template on how to rename files using text from inside the PDF.

Leave a comment on the YouTube video or here if you have a question for another specific case.

If you want to try and modify the project for your specfic case, I suggest looking into **regular expresions** (python has a library called re).
