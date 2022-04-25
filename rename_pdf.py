import fitz
from os import DirEntry, curdir, chdir, getcwd, rename
from glob import glob as glob
import re

failed_pdfs = []
count = 0
cr_regex = r'(?<=Order #: )[A-Z]{4}\d+'
text = ""

get_curr = getcwd()
directory = 'PDF_FILES'
chdir(directory)

pdf_list = glob('*.pdf')

for pdf in pdf_list:
    with fitz.open(pdf) as pdf_obj:
        for page in pdf_obj:
            text += page.get_text()
    new_file_name = re.search(cr_regex, text).group().strip() + '.pdf'
    text = ""
    
    # Tries to rename a pdf. If the filename doesn't already exist
    # then rename. If it does exist then throw an error and add to failed list
    try:
        rename(pdf, new_file_name)
    except WindowsError:
        count += 1
        failed_pdfs.append(str(count) + ' - FAILED TO RENAME: [' + pdf + " ----> " + str(new_file_name) + "]")

# If there were pdfs that couldn't be renamed (have the same name)
# then print them out to a text file to view later.
chdir(get_curr)
if (len(failed_pdfs) > 0):
    with open('PDF_FAILURES.txt', 'w') as f:
        for failure in failed_pdfs:
            f.writelines(failure + '\n')