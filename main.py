#!/usr/bin/python3

from PyPDF2 import PdfFileReader, PdfFileWriter
import sys, shutil, subprocess, random, os

def main():
    
    return 0

def transfer_files(from_path, to_path="./sorted_folder/"):
    input_dir = from_path
    output_dir = to_path

    dirpath = os.path.join(to_path)
    if os.path.exists(dirpath) and os.path.isdir(dirpath):
        shutil.rmtree(dirpath)
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)

    for f in os.listdir(input_dir):
        if not f.endswith('.pdf'):
            continue
        pdf_in = open(input_dir + f, 'rb')
        pdf_reader = PdfFileReader(pdf_in)
        pdf_writer = PdfFileWriter()
        for pagenum in range(pdf_reader.numPages):
            page = pdf_reader.getPage(pagenum)
            page.rotateClockwise(90)
            pdf_writer.addPage(page)
        pdf_out = open(output_dir + f, 'wb')
        pdf_writer.write(pdf_out)
        pdf_out.close()
        pdf_in.close()

# Create a dictionary of all file names and unique id
def create_file_dict(sorted_dir="./sorted_folder/"):
    d = {}
    i = 0
    dir_path = os.path.join(sorted_dir)
    for f in os.listdir(dir_path):
        d[i] = f
        i+=1
    return d

# randomly access key:value
def randomize(d, sorted_dir="./sorted_folder/"):
    keys = list(d.keys())
    random.shuffle(keys)
    print('After each image opens, make your guess and then verify that you are correct.')
    print('Once you have guessed, close the file and return to the terminal to press Enter for the next image.')
    print('Press Enter to begin.')
    input()
    for i in keys:
        # run the app here
        filename = os.path.join(sorted_dir, d[i])
        subprocess.call(['open', filename])
        input()
        print('That was ' + d[i])
        input('Press Enter for the next image.')


if __name__ == "__main__":
    transfer_files("./testanatomy/")
    print(randomize(create_file_dict()))


