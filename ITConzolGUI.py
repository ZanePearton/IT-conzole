import tkinter as tk
from tkinter import * 
from tkinter import Tk, Frame, Button, Canvas
from tkinter.ttk import * 
from time import strftime 
import os
import functools
from concurrent import futures
from tkinter.font import Font
import subprocess
import time
from time import sleep
import requests
import math


# Print banner in terminal window

def banner():
    print("                                                                               ") 
    print("          ______________________________ ____________________________          ")           
    print(" ---     /        /       /   /     /   /  /       /     /   /      /    ------")
    print("         \__  ___/    ___/   /     /   /  /    ___/     /   /   ___/           ")
    print("     --    / /   /   / ____ /  /  /      /       /  /  /   /      /   ------   ")
    print("      /\__/ /__ /   /     \   /  /      /___    /  /  /   /__  __/        -----")
    print("  ---/         /   /      /     /  /   /       /     /      /   /              ") 
    print("     \________/___/\_____/_____/__/___/_______/ ____/______/___/   ------      ")
    print("") 
    print(" Coded by Z")
    print("\n")
    

banner()


thread_pool_executor = futures.ThreadPoolExecutor(max_workers=1) 

def tk_after(target):

    @functools.wraps(target)
    def wrapper(self, *args, **kwargs):
        args = (self,) + args
        self.after(0, target, *args, **kwargs)
    return wrapper

def submit_to_pool_executor(executor):

    def decorator(target):

        @functools.wraps(target)
        def wrapper(*args, **kwargs):
            return executor.submit(target, *args, **kwargs)
        return wrapper
    return decorator



# main tker app application


class TkApproot(tk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.master.iconbitmap('iconfinder_.ico')
        self.master.geometry('665x450')
        self.master.title("Chisholm IT Console")
        self.master.config(background ='black')
        self.master.resizable(width=False, height=False)

        #menu header -------- start

        file = Menu(menubar, tearoff = 0, background='black', foreground='green') 
        
        menubar.add_cascade(label ='Network Connections', menu = file,) 
        file.add_command(label ='Ping', command = self.pingBT) 
        file.add_command(label ='Traceroute', command = self.traceBT) 
        file.add_command(label ='Nmap', command = self.nmapBT)
        file.add_separator() 
        file.add_command(label ='Exit', command = root.destroy) 
        
        # Adding Edit Menu and commands 

        edit = Menu(menubar, tearoff = 0,background='black', foreground='green') 
        menubar.add_cascade(label ='DNS', menu = edit) 
        edit.add_command(label ='nslookup', command = self.nslookupBT) 
        
      

        InstallNmap = Menu(menubar, tearoff = 0,background='black', foreground='green') 
        menubar.add_cascade(label ='Download nmap', menu = InstallNmap) 
        InstallNmap.add_command(label ='click to download nmap for windows', command = self.installnmapBT) 
        
        # Adding Help Menu 

        help_ = Menu(menubar, tearoff = 0,background='black', foreground='green') 
        menubar.add_cascade(label ='Help', menu = help_) 
        help_.add_command(label ='Readme', command = self.readmeBT) 

        #menu header -------- end
       
        #terminal-------- Print to onscreen text box
       
        self.entry = tk.StringVar()
        label = tk.Label(self.master, text="TERMINAL",bg='black',fg='green')
        label.config(font=('Courier', 15))
        label.grid(row=1, column=0)
        entry = tk.Entry(self.master, textvariable=self.entry,background="grey14", foreground="green" , width = 80)
        entry.insert(-1, "Type command here....")
        entry.grid(row=2, column=0)
        self.button = tk.Button(self.master, text="RUN COMMAND...", command=self.on_button,bg='black',fg='green')
        self.button.grid(row=3, column=0)
        self.text = tk.Text(self.master)
        self.text.config(state=tk.DISABLED ,background="black", foreground="green")
        self.text.place(width = 500, height = 500)
        self.text.grid(row=1, column=0,padx=(10, 100))
     
    def Header():
        print ('hello')
    

    @tk_after
    def tkButton_null(self, enabled=True):
        state = tk.NORMAL
        if not enabled:
            state = tk.DISABLED
            
        self.button.config(state=state,background="black", foreground="green")
        
    @tk_after
    def XTerm_CLR(self):
        self.text.config(state=tk.NORMAL,background="black", foreground="green")
        self.text.delete(1.0, tk.END)
        self.text.config(state=tk.DISABLED,background="black", foreground="green")

    @tk_after
    def TXT(self, text):
       
        self.text.config(state=tk.NORMAL,background="black", foreground="green")
        self.text.insert(tk.END, text)
        self.text.config(state=tk.DISABLED ,background="black", foreground="green")

    def on_button(self):
        self.XTerm()
     
    @submit_to_pool_executor(thread_pool_executor)
    def XTerm(self):
       
        self.tkButton_null(False)
        self.XTerm_CLR()
        self.TXT(' ')
        self.TXT("----------------------------------------------------------------------------------          ______________________________ ____________________________            ---     /        /       /   /     /   /  /       /     /   /      /    ------          \__  ___/    ___/   /     /   /  /    ___/     /   /   ___/                 --    / /   /   / ____ /  /  /      /       /  /  /   /      /   ------          /\__/ /__ /   /     \   /  /      /___    /  /  /   /__  __/        -----   ---/         /   /      /     /  /   /       /     /      /   /                    \________/___/\_____/_____/__/___/_______/ ____/______/___/ ------------------")
        self.TXT("--                       -------------                           -----------")
        self.TXT("Coded by z--------------------------------------------------------------------")
        self.TXT('Running cmd....')
        # result = os.popen("ping "+self.entry.get()+" -n 2")
        result = os.popen(self.entry.get())
        for line in result:
            self.TXT(line)
        self.TXT('Command finished......')
        self.tkButton_null(True)

        #terminal--------end  
    

    #menu cascading menu buttons - start - cmds

    def pingBT(self):
        ipurl=input("Enter an ip address or a web URL address: ")
        os.system("ping %s "%ipurl) # run commands and print out results

    def traceBT(self):
        ipurl=input("Enter an ip address or a web URL address: ")
        os.system("tracert %s "%ipurl) # run commands and print out results
    
    def nmapBT(self):
        ipurl=input("Enter an ip address or a web URL address: ")
        os.system("nmap %s "%ipurl) # run commands and print out results

    def nslookupBT(self):
        ipurl=input("Enter an ip address or a web URL address: ")
        os.system("nslookup %s "%ipurl) # run commands and print out results
    
    def traceBT(self):
        ipurl=input("Enter an ip address or a web URL address: ")
        os.system("tracert %s "%ipurl) # run commands and print out results


    def installnmapBT(self):

        

        # url = "https://nmap.org/dist/nmap-7.91-win32.zip"
        # response = requests.get (url)
        # data = response.json()
        print(".... Connecting to https://nmap.org/dist/nmap-7.91-win32.zip..." )
        url = 'https://nmap.org/dist/nmap-7.91-win32.zip'
        target_path = 'nmap-7.91-win32.zip'
        print(".... Please wait... Connecting to https://nmap.org/dist/nmap-7.91-win32.zip...")
        print(".... Initialising connection with Nmap.org ...")
        print(".... Streaming Data...")
        print("|Streaming data | Q35UTUKT79PY8LJKLU9OYUIU0IPUIZHUIIFYIRDTYEW5TWEWRTWRERT |Downloading Nmap|   ")
        response = requests.get(url, stream=True)
        handle = open(target_path, "wb")
 

        
         
        for chunk in response.iter_content(chunk_size=512):

            
            print("|Streaming data | YUK7KGHJTYFDGHRTHDFGHERTYERYWE5TYSETRUESRTHDRYTHSRYJERS |Downloading Nmap|   ")
            print("|Streaming data | Q35UTUKT79PY8LJKLU9OYUJU0IPUIGHUIIFYIRDTYEW5TWEWRTWRERT |Downloading Nmap|   ")
            print("|Streaming data | 45745YW467QTYW457W5YJCVBNFGHJ898E5RYETWRTE4TERY45TWRYE7 |Downloading Nmap|   ")
            print("|Streaming data | 57565Y46767JTYUDFCGNDTJDRTURYUT7ITUDTYI67U5767U78678675 |Downloading Nmap|   ")
            print("|Streaming data | T4675IU908PIO[0-[IUO8OIOPUIY785563U80798078979-890780]] |Downloading Nmap|   ")
            print("|Streaming data | Q35UTUKT79PY8LJKLU9OYUJU0IPUIdHUIIFYIRDTYEW5TWEWRTWRERT |Downloading Nmap|   ")
            print("|Streaming data | RTYERTHJDTUKDRTJFTYGSRYKDTRHJSTYUWSRYJRTYUJXDTUKDMXCGHF |Downloading Nmap|   ")
            print("|Streaming data | YUK7KGHJTYFDGHRTHDFGHERTYERYWE5TYSETRUESRTHDRYTHSRYJERS |Downloading Nmap|   ")
            print("|Streaming data | Q35UTUKT79PY8LJKLU9OYUwU0IPUItHUIIFYIRDTYEW5TWEWRTWRERT |Downloading Nmap|   ")
            print("|Streaming data | 45745YW467QTYW457W5YJCVBNFGHJ898E5RYETWRTE4TERY45TWRYE7 |Downloading Nmap|   ")
            print("|Streaming data | 57565Y46767JTYUDFCGNDTJDRTURYUT7ITUDTYI67U5767U78678675 |Downloading Nmap|   ")
            print("|Streaming data | T4675IU908PIO[0-[IUO8OIOPUIY785563U80798078979-890780]6 |Downloading Nmap|   ")
            

            if chunk:  # filter out keep-alive new chunks
                handle.write(chunk)
        handle.close()
        print("|Streaming data | Q35UTUKT79PY8LJKLU9OYUIU0IPUIZHUIIFYIRDTYEW5TWEWRTWRERT |Downloading Nmap|   ")
        print("|Streaming data | Q35UTUKT79PY8LJKLU9OYUIU0IPUIZHUIIFYIRDTYEW5TWEWRTWRERT |    COMPLETE    |   ")
        print("| CONN. CLOSED  | Q35UTUKT79PY8LJKLU9OYUIU0IPUIZHUIIFYIRDTYEW5TWEWRTWRERT |    COMPLETE    |   ")
        print("| CONN. CLOSED  |           .... Nmap download complete......             |    COMPLETE    |   ")
       
         
        banner()
        print ("Type dir in the the run command box you will see nmap-7.91-win32.zip")
        print("Please extract and install ZIP file located here...")
        print("Visit the following link for more information on nmap installation ")
        print("https://nmap.org/book/install.html")


    #menu cascading menu buttons - end - cmds

    
    #Drops a readme file in the file path - With This info.

    def readmeBT(self):

        newfile = open("Readme.txt", "w")
        newfile.write('                                                                               \r\n') 
        newfile.write('          ______________________________ ____________________________          \r\n')
        newfile.write(' ---     /        /       /   /     /   /  /       /     /   /      /    ------\r\n')
        newfile.write('         \__  ___/    ___/   /     /   /  /    ___/     /   /   ___/           \r\n')
        newfile.write('     --    / /   /   / ____ /  /  /      /       /  /  /   /      /   ------   \r\n')
        newfile.write('      /\__/ /__ /   /     \   /  /      /___    /  /  /   /__  __/        -----\r\n')
        newfile.write('  ---/         /   /      /     /  /   /       /     /      /   /              \r\n') 
        newfile.write('     \________/___/\_____/_____/__/___/_______/ ____/______/___/   ------      \r\n')
        newfile.write('') 
        newfile.write(' Coded by Z\r\n' )
        newfile.write(' Not much to say. just write stuff in the run cmdline. \r\n Softwear can be utilised to execute sys cmds. \r\n Thanks for using ITconsole..... \r\n How to install nmap' )
        newfile.write( '\r\n \r\n \r\n How to install nmap... From  https://nmap.org/download.html \r\n \r\n r\n')
        newfile.write('Please read the Windows section of the Install Guide for limitations and installation instructions for the Windows version of Nmap. You can choose from a self-installer \r\n (includes dependencies and also the Zenmap GUI) or the much smaller command-line zip file version. We support Nmap on Windows 7 and newer, as well as Windows Server 2008 and newer. \r\n We also maintain a guide for users who must run Nmap on earlier Windows releases..The Nmap executable Windows installer can handle Npcap installation, registry performance tweaks, and decompressing the executables \r\n and data files into your preferred location. It also includes the Zenmap graphical frontend. Skip all the complexity of the Windows zip files with a self-installer:Latest \r\n stable release self-installer: nmap-7.91-setup.exe. We have written post-install usage instructions. Please notify us if you encounter any problems or have suggestions for the installer.For those who \r\n prefer the command-line zip files (Installation Instructions; Usage Instructions), they are still available. The Zenmap graphical interface is not included with these, so you need to run nmap.exe from a DOS/command window. Or you can download and install a superior command \r\n shell such as those included with the free Cygwin system. Also, you need to run the Npcap and Microsoft Visual C++ 2013 Redistributable Package installers which are included in the zip file. The main advantage is \r\n that these zip files are a fraction of the size of the executable installer:Latest stable command-line zipfile: nmap-7.91-win32.zip')
        newfile.close()


        print('                                                                               ') 
        print('          ______________________________ ____________________________          ')           
        print(' ---     /        /       /   /     /   /  /       /     /   /      /    ------')
        print('         \__  ___/    ___/   /     /   /  /    ___/     /   /   ___/           ')
        print('     --    / /   /   / ____ /  /  /      /       /  /  /   /      /   ------   ')
        print('      /\__/ /__ /   /     \   /  /      /___    /  /  /   /__  __/        -----')
        print('  ---/         /   /      /     /  /   /       /     /      /   /              ') 
        print('     \________/___/\_____/_____/__/___/_______/ ____/______/___/   ------      ')
        print('') 
        print(' Coded by Z')
        print("Thankyou for using ITconzoL. Check your current file path! I dumped a readme file in this folder. ")
        print(' Not much to say. just write stuff in the run cmdline.' )
        print(' Softwear can be utilised to execute sys cmds.' )
        print(' Thanks for using ITconsole..... ' )
    

 


        # end of read me    
    
if __name__ == '__main__':
    root = tk.Tk()
    menubar = Menu(root)
    root.config(menu = menubar) 
    main_frame = TkApproot()
    root.mainloop()
