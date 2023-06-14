# importing required modules
import PyPDF2
import os
import xlsxwriter
from tkinter import*
import tkinter as tk
import Parsing

if not os.path.isfile("/Users/coltenrodriguez/Downloads/CilasPal3.0/Dependencies/fileName.jpeg"):
    raise Exception("Forbidden Action")

py = []
master = Tk()
master.title("CilasPal: Grain Size Digitizer")
master.geometry("450x250")

e = Entry(master)
e.pack()
e.focus_set()
var = StringVar()
label = Label(master, textvariable=var, relief=RAISED, wraplength=400)

var.set("Please paste the path to the file(s) from which you would like to retrieve data by doing the "
        "following 1. Navigate to the folder (or PDF file) of the cilas data on this computer (this will "
        "most likely be located on an external drive) 2. In the file destination field (the space to the left "
        "of the file search field), left click once to highlight the directory 3. Copy and paste here and click "
        "the button corresponding to your input type")
label.pack()


def callback():
    dirt = e.get()  # This is the text you may want to use later
    print("retrieving data from directory...", dirt)
    py.append(dirt)
    master.destroy()


b = Button(master, text="Run with combined data (input is a single pdf)", width=35, command=callback)
b2 = Button(master, text="Run with separate files (input is a folder of separate pdfs)", width=35, command=callback)
b.pack()
b2.pack()
mainloop()

############################################################################
# Spreadsheet initialization

# Creating an array for Size classes
insList = ["ID", "Mean", "Median", 0.04, 0.07, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1,
           1.2, 1.3, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 3.0, 4.0, 5.0, 6.0, 6.5, 7.0,
           7.5, 8.0, 8.5, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0,
           19.0, 20.0, 22.0, 25.0, 28.0, 32.0, 36.0, 38.0, 40.0, 45.0, 50.0, 53.0, 56.0,
           63.0, 71.0, 75.0, 80.0, 85.0, 90.0, 95.0, 100.0, 106.0, 112.0, 125.0, 130.0,
           140.0, 145.0, 150.0, 160.0, 170.0, 180.0, 190.0, 200.0, 212.0, 242.0, 250.0,
           300.0, 400.0, 500.0, 600.0, 700.0, 800.0, 900.0, 1000.0, 1100.0, 1200.0, 1300.0,
           1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0,
           2400.0, 2500.0]

# creating an array for UDSC (User defined size classes)
insList2 = [0.04, 3.90, 62.00, 88.00, 125.00, 177.0, 2500.0, 350.0, 500.0, 710.0, 1000.0, 1410.0, 2000.0]

# Creates a workbook in Excel to house all the data
workbook = xlsxwriter.Workbook(py[0] + '//YourData.xlsx')
worksheet = workbook.add_worksheet("Primary Data Tables")
worksheet2 = workbook.add_worksheet("User Defined Size Classes")

# Enters the size classes into their respective worksheets
for i in range(len(insList)):
    worksheet.write(0, i, insList[i])
for i in range(len(insList2)):
    worksheet2.write(0, i + 1, insList2[i])
############################################################################

# Preparing the data
if os.path.exists(py[0]):
    print("\033[92m" + "Directory Received!")
    print("\033[92m" + "ERROR: FileNotFound IGNORED")
    print("\033[92m" + "Passing FileName(s) \n")
    pdfsList = []
else:
    raise Exception("\033[93m" + "Sorry, it appears this file or directory does not exist. Try again with a valid path."
                                 " This is likely not a problem with CilasPal")


# 1.Get all file names from directory
file_list = os.listdir(py[0])

# 2. Separate files into User defined and primary size class arrays
for i in range(len(file_list)):
    file = file_list[i]

    # If the file is .MES, add it to the PSC array
    if file.__contains__('.pdf'):
        pdfsList.append(file)

# For debugging, print the lists
print("The following list of files will be extracted: \n", pdfsList)

Parsing.singlefile(py, pdfsList, worksheet, worksheet2)
workbook.close()

# Notify the user when the program finishes running
final = Tk()
final.title("CilasPal: Grain Size Digitizer")
final.geometry("450x250")


var = StringVar()
label = Label(final, textvariable=var, relief=RAISED, wraplength=400)

var.set("Your Excel file (YourData.xlsx) has been created. "
        "You may view your data in the previously input file location. "
        "Close this window to close the app")
label.pack()
mainloop()
