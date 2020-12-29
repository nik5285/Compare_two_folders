import os
import tkinter
from tkinter import *
import tkinter.ttk as ttk
from tkinter import filedialog

def browse_path1():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path1 
    filename1 = filedialog.askdirectory()
    folder_path1.set(filename1)

def browse_path2():
    global folder_path2
    filename2 = filedialog.askdirectory()
    folder_path2.set(filename2)

def compare():

    #counter for number of errors.
    counter = 0

    #exception handling if paths are not valid
    try:
        objT = os.scandir(folder_path1.get())
        objS = os.scandir(folder_path2.get())

    except:
        #clear the textbox first
        T.delete(1.0 ,"end")
        #display the error message in textbox
        T.insert(tkinter.END,"Error: Invalid input. Please browse and select correct paths.\n\n")

    else:
        
        #clear the textbox first
        T.delete(1.0 ,"end")
        
        #clear the lists to avoid adding up if user clicks run multiple times.
        list_of_TfFiles.clear()
        list_of_ScnFiles.clear()

        # we dont want to compare same folders
        if folder_path1.get() == folder_path2.get():
            T.insert(tkinter.END,"Error: Same path entered for both folders!\n\n")

        else:
            
            #fetch the items from directory into our list. 
            for entry in objT : 
                list_of_TfFiles.append(entry.name)

            #fetch the items from directory into our list. 
            for entry in objS : 
                list_of_ScnFiles.append(entry.name)
            

            if len(list_of_ScnFiles)==len(list_of_TfFiles):
                # if both are equal then print on same line. smart code
                T.insert(tkinter.END,"%s items found in each folder.\n\n" %len(list_of_TfFiles))
            else:
                # if not equal then display the number of itmes in folder in textbox
                T.insert(tkinter.END,"%s items found in first folder" %len(list_of_TfFiles))
                T.insert(tkinter.END, " & %s items found in second folder.\n\n" %len(list_of_ScnFiles))

            #compare the two folders for missing items    
            for i in list_of_ScnFiles:
                if i in list_of_TfFiles:
                    pass
                else:
                    message = "%s was found in second folder, but not in first folder.\n" %i
                    T.insert(tkinter.END, message)
                    counter+=1
            for j in list_of_TfFiles: 
                if j in list_of_ScnFiles:
                    pass
                else:
                    message = "%s was found in first folder, but not in second folder.\n" %j
                    T.insert(tkinter.END, message)
                    counter+=1
            if counter == 0:
                T.insert(tkinter.END, 'No errors found!')

#main display window
root = Tk()
root.title('Folders_compare')

L1 = Label(root, text="Select first folder :")
L1.grid(row=0, column=0, pady=2)
L1.configure(font=('Arial',10))

L2 = Label(root, text="Select second folder :")
L2.grid(row=1, column=0, pady=2)
L2.configure(font=('Arial',10))

L3 = Label(root, text="Click to compare :")
L3.grid(row=2, column=0, pady=2)
L3.configure(font=('Arial',10))

button1 = tkinter.Button(text='Compare', command=compare, width =10)
button1.grid(row=2, column=1, pady=2)#, ipadx=2, ipady=2, padx=2, pady=2
button1.configure(font=('Arial',10), foreground="black", background="white")

browsebutton1 = Button(text="Browse", command=browse_path1, width =10)
browsebutton1.grid(row=0, column=1, pady=2)#, ipadx=2, ipady=2, padx=2, pady=2
browsebutton1.configure(font=('Arial',10), foreground="black", background="white")

browsebutton2 = Button(text="Browse", command=browse_path2, width =10)
browsebutton2.grid(row=1, column=1, pady=2)#, ipadx=2, ipady=2, padx=2, pady=2
browsebutton2.configure(font=('Arial',10), foreground="black", background="white")

folder_path1 = StringVar()
folder_path2 = StringVar()

pathLabel1 = Label(root,textvariable=folder_path1, width=35)
pathLabel1.grid(row=0, column=2)

pathLabel2 = Label(root, textvariable=folder_path2, width=35)
pathLabel2.grid(row=1,column=2)

T = tkinter.Text(root, width=63)
T.grid(row=7, column=0, columnspan= 3, padx=2, pady=5)
T.configure(font=("Arial", 10))
T.insert(tkinter.END,"This tool can be used to compare items in two folders.\n")
T.insert(tkinter.END,"It will let you know how many items are in each folder\n")
T.insert(tkinter.END,"\nand which items are missing compared to the other folder.\n")

list_of_TfFiles = []
list_of_ScnFiles = []

# start the program
root.mainloop()