import fitz
from os import DirEntry, curdir, getcwd, chdir, rename
from glob import glob as glob

directory = 'PDF_FILES'
curr_dir = getcwd()

chdir(directory)

pdf_list = glob('*.pdf')

for pdf in pdf_list:
    with fitz.open(pdf) as pdf_obj:
        text = pdf_obj[0].get_text()
    new_file_name = text.split("\n", 1)[0].strip()
    rename(pdf, new_file_name + '.pdf')