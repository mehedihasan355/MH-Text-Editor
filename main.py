
# To do    # DONE!!!!
# create text area
# able to change font size and family
# able to change style
# menubar
# able to file operation
# able to cut copy paste
# Compailer of THE NEW Extainsion '.mh' 

# bugs 
# font style   # fixed
# font style on size and family change  # fixed

# Extainsion bugs
# delect [] from text
# compile font size and family
# Remake it # Done


# undone 
# about section   ## Done
# default font family  ## Done
# default file name while to save # done
# TiTle of flie dialog  # done

from tkinter import *
import tkinter.colorchooser
import tkinter.filedialog
from tkinter.font import families
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox
from PIL import Image,ImageTk

FILE_PATH =''
CURRENT_FILE = ''
_bold = False
_italic = False
_underline = False

# window func
def str2bool(str):
    if str == 'True':
        return True
    elif str == 'False':
        return False
    else:
        return False


def about():
    aboutWin = Toplevel(master=window)
    text = '''
    Hello, World!
    I am MEHEDI from Bangladesh.....
    '''
    Label(aboutWin,text=text).pack()
    image =PhotoImage(file='src/mehedi.png')
    Label(aboutWin,image=image).pack()

    aboutWin.title('About')
    aboutWin.resizable(False,False)
    aboutWin.geometry(f'400x400+{str(int(x+200))}+{str(int(y+200))}')
    aboutWin.mainloop()


def theme():
    color = tkinter.colorchooser.askcolor()
    pad.config(bg=color[1])
def fontColor():
    color = tkinter.colorchooser.askcolor()
    pad.config(fg=color[1],insertbackground=color[1])

def change_font(*args):
    makeChanges()

def windowColor():
    color = tkinter.colorchooser.askcolor()
    window.config(bg=color[1])
   
def makeBold():
    global _bold,_italic,_underline
    _bold = not _bold
    makeChanges()

def makeItalic():
    global _bold,_italic,_underline
    _italic = not _italic
    makeChanges()
    
def makeUnderline():
    global _bold,_italic,_underline
    _underline = not _underline
    makeChanges()

def makeChanges():

    pad.config(font=(fontname.get(),font_size.get(),'underline' if _underline == True else 'roman','bold' if _bold==True else 'roman','italic' if _italic == True else 'roman') )

# Menu func
def newFile():
    global CURRENT_FILE
    ans = messagebox.askyesno('Warning','Do you want to continue?')
    if ans == 1:
        pad.delete(1.0,END)
        window.title('untitled')
        CURRENT_FILE = 'untitled'
    else:
        pass


def readFile(file):
    command = file.read()

    commandDict = dict((x.strip(), y.strip())
                     for x, y in (element.split('-')
                                  for element in command.split(', ')))

    return commandDict

def openFile():
    global FILE_PATH,CURRENT_FILE
    file = tkinter.filedialog.askopenfile(mode='r+',title='Open')
    winname = file.name.split('/')[len(file.name.split('/'))-1]
    try:
        if file == None:
            pass
        elif '.mh' in winname:
            global _underline,_bold,_italic
            commandDict = readFile(file)
            keys = list(commandDict)
            # # set propert
            _bold = str2bool(commandDict.get(keys[0]))
            _italic = str2bool(commandDict.get('italic'))
            _underline =  str2bool(commandDict.get('underline'))

            _text = commandDict.get('text')
            font_size.set(commandDict.get('font_size'))
            fontname.set(commandDict.get('fontname'))

            window.title(winname)
            pad.delete(1.0,END)
            pad.insert(1.0,_text)  #
            makeChanges()

        else:
            pad.insert(1.0,file.read())

        menubar.update()

        # Changing file properties
        CURRENT_FILE = file
        FILE_PATH = file.name
        
    except Exception as e :
        messagebox.showerror("Error",e)



def saveFile():
    global FILE_PATH,CURRENT_FILE,_bold,_italic,_underline

    if FILE_PATH == '':
        saveasFile()

    elif '.mh' in FILE_PATH.split('/')[len(FILE_PATH.split('/'))-1]:
        CURRENT_FILE.truncate(0)
        str = f"bold - {_bold}, italic - {_italic}, underline - {_underline}, font_size - {font_size.get()}, fontname - {fontname.get()}, text - {pad.get(1.0,END)}"
        CURRENT_FILE.write(str)
        
    else:
        try:
            
            with open(FILE_PATH,'w') as f:
                f.write(pad.get(1.0,END))
        except:
            pass

    CURRENT_FILE.close()
def saveasFile():
    global FILE_PATH,CURRENT_FILE,_bold,_italic,_underline
    file = tkinter.filedialog.asksaveasfile(title='Save as',
    defaultextension=".mh",initialfile='Untitled.mh',
    filetypes=[("MH files", "*.mh"),("Text files", "*.txt"),("All files", "*.*")])
    if file == None:
        messagebox.showinfo('Info',"Couldn't save file")
    else:
        try:
            window.title(file.name.split('/')[len(file.name.split('/'))-1])
            if '.mh' in file.name:
                str = f"bold - {_bold}, italic - {_italic}, underline - {_underline}, font_size - {font_size.get()}, fontname - {fontname.get()}, text - {pad.get(1.0,END)}"
                file.write(str)
                
            else:
                file.write(pad.get(1.0,END))

            CURRENT_FILE = file
            FILE_PATH = file.name

        except:
            messagebox.showerror("Error","Couldn't save file")
    CURRENT_FILE.close()


def copy():
    pad.event_generate("<<Copy>>")
def paste():
    pad.event_generate("<<Paste>>")
def Cut():
    pad.event_generate("<<Cut>>")

window = Tk()

#Menubar 

menubar = Menu(window)
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label="New", command = newFile)
filemenu.add_command(label="Open", command = openFile)

filemenu.add_command(label="Save", command = saveFile)
filemenu.add_command(label="Save As", command= saveasFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command = lambda: exit())
menubar.add_cascade(label = "File", menu = filemenu)

editmenu = Menu(menubar, tearoff = 0)
editmenu.add_command(label="Copy", command = copy)
editmenu.add_command(label="Cut", command = Cut)
editmenu.add_command(label="Paste", command = paste)
editmenu.add_separator()
menubar.add_cascade(label = "Edit", menu = editmenu)

thememenu = Menu(menubar,tearoff=0)
thememenu.add_command(label='BackGround',command=theme)
thememenu.add_command(label='Font Color',command=fontColor)
thememenu.add_command(label='Window Color',command=windowColor)
# menubar.add_cascade(label='Theme',menu = thememenu)

viewmenu = Menu(menubar,tearoff=0)
viewmenu.add_cascade(label = 'Theme',menu=thememenu)
menubar.add_cascade(label="View",menu = viewmenu)




menubar.add_command(label='About',command=about)

# Vers
fontname = StringVar(window)

font_size = StringVar(window)
font_size.set('18')

# customize panel
panel = Frame(window)
panel.grid()

fontchoser = ttk.OptionMenu(panel,fontname,*families(),command=change_font)
fontchoser.grid(row=0,columnspan=3,padx=5)
fontname.set("Arial")

font_size_choser = Spinbox(panel,from_=1,to=100,textvariable=font_size,command=change_font)
font_size_choser.grid(row=0,column=4)

boldbtn = ttk.Button(panel , text="𝗕",command=makeBold,width=4)
boldbtn.grid(row=0,column=5,padx=9,pady=4)

italicbtn = ttk.Button(panel , text="i",command=makeItalic,width=4)
italicbtn.grid(row=0,column=6,pady=4)

underlinebtn = ttk.Button(panel , text="U",command=makeUnderline,width=4)
underlinebtn.grid(row=0,column=7,padx=9,pady=4)


# # Text area
pad = Text(window,font=(fontname.get(),font_size.get()) )
pad.grid(row=1,column=0,sticky='nsew')


window.title('untitled')

window.config(menu = menubar)
# center window
scrwidth = window.winfo_screenwidth()
scrheight = window.winfo_screenheight()
x = (scrwidth/2) - (800/2)
y = (scrheight/2) - (700/2)
window.geometry(f'800x700+{str(int(x))}+{str(int(y))}')
window.grid_columnconfigure(0,weight=1)
window.grid_rowconfigure(1,weight=1)
window.iconbitmap('src/m.ico')
window.mainloop()