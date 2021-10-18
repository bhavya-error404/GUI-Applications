# Author Bhavya Jain
# Email bhavyajain1010@gmail.com

from tkinter import *
import Evtx.Evtx as evtx
import Evtx.Views as e_views
import webbrowser

# C:\Windows\System32\winevt\Logs\Setup.evtx


def parse_func(input_filename, resultfile):
    evtx_path = input_filename
    f = open(resultfile, 'w')
    try:
        with evtx.Evtx(evtx_path) as log:
            f.write(e_views.XML_HEADER)
            f.write("<Events>")
            for record in log.records():
                f.write(record.xml())
            f.write("</Events>")
        status = Label(top, text='SuccessFull', background='lightgreen')
        myVariable = "C:/Users/Bhavya/Python Programs/Python Files/"+resultfile
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(myVariable)
    except PermissionError:
        status = Label(top, text='Permission Denied', background='red')
    except FileNotFoundError:
        status = Label(top, text='FileNotFoundError', background='red')

    status.grid(row=4, column=1, sticky='W')


def parse_button():
    input_filename = path_location.get()
    resultfile = output_file.get()
   # print(input_filename) if input_filename else print("Enter a file path")
   # print(resultfile) if resultfile else print("Enter a output file")
    parse_func(input_filename, resultfile)


if __name__ == "__main__":
    top = Tk()
    top.geometry("500x300")
    # Code to add widgets will go here...
    top.title("Parsing Events Files")
    # button = Button(top, text='Start', width=10,command = top.destroy)
    text_area = Message(
        top, text='Enter the path to event log file !', bg='lightgreen', width=400)
    desc_1 = Label(top, text="For Example C:\Windows\System32\<filename> :")
    path_location = Entry(top, width=25)
    desc_2 = Label(top, text="Enter Output File :")
    output_file = Entry(top, width=25)
    result_button = Button(top, text='Parse', command=parse_button)
    Status_desc = Label(top, text='Status : ')
    # text_area.pack()
    text_area.grid(row=0, column=0, sticky='E')
    desc_1.grid(row=1, column=0)
    path_location.grid(row=1, column=1)
    desc_2.grid(row=2, column=0, sticky='W')
    output_file.grid(row=2, column=1)
    result_button.grid(row=3, column=1, sticky='W')
    Status_desc.grid(row=4, column=0, sticky='W')
    top.mainloop()
