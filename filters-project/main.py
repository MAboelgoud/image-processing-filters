from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np

img = None
img_is_found = False


def choose():
    global img, img_is_found, image2
    ifile = filedialog.askopenfile(parent=window, mode='rb', title='Choose a file') # open the file dialog (select file) window when a user presses a button by calling the function open:
    if ifile:
        path = Image.open(ifile)
        image2 = ImageTk.PhotoImage(path)
        label.configure(image=image2) #displaying img in label
        label.image = image2
        img = np.array(path) #convert img to matrix

        img = np.mean(img, axis=2).copy() #convert img to gray level
        img_is_found = True #flag


#####function filter
def change_negative(img):
    height, width = img.shape
    for row in range(height):
        for col in range(width):
            img[row][col] = 255 - img[row][col]
    return img

def change_PowerLow(img):
    height, width = img.shape
    for row in range(height):
        for col in range(width):
            img[row][col] = 255 * (img[row][col] / 255) ** 5
    return img



def change_Thresholding(img):
    height, width = img.shape
    for row in range(height):
        for col in range(width):
            if (img[row][col] < 150):
                img[row][col] = 0
    return img



def change_GaussianFiltering(img):
    width, height = img.shape
    for row in range(width - 1):
        for col in range(height - 1):
            img[row][col] = (1 / 16) * (1 * img[row - 1][col + 1] + 2 * img[row][col + 1] +
                                        1 * img[row + 1][col + 1] + 2 * img[row - 1][col] +
                                        4 * img[row][col] + 2 * img[row + 1][col] + 1 * img[row - 1][col - 1] +
                                        2 * img[row][col - 1] + 1 * img[row + 1][col - 1])
    return img



def change_MedianFiltering(img):
    height, width = img.shape
    new_image = np.zeros((height, width))

    for i in range(1, height - 1):
        for j in range(1, width - 1):
            nieghbours = [img[i - 1][j - 1], img[i][j - 1], img[i + 1][j - 1],  # first row
                          img[i - 1][j], img[i][j], img[i + 1][j],  # second row
                          img[i - 1][j + 1], img[i][j + 1], img[i + 1][j + 1]]  # third row
            Median = np.median(nieghbours)
            new_image[i][j] = Median
    img = np.array(new_image, dtype=np.uint8)
    return img

#####################################################
def negative():
    if img_is_found:
        img_after = change_negative(img)
        img_after = ImageTk.PhotoImage(Image.fromarray(img_after)) #conver img from matrix to jpg
        label.configure(image=img_after)
        label.image = img_after #shows the real-time result


def PowerLow():
    if img_is_found:
        img_after = change_PowerLow(img)
        img_after = ImageTk.PhotoImage(Image.fromarray(img_after) )#conver img from matrix to jpg
        label.configure(image=img_after)
        label.image = img_after #shows the real-time result


#####Thresholding
def Thresholding():
    if img_is_found:
        img_after = change_Thresholding(img)
        img_after = ImageTk.PhotoImage(Image.fromarray(img_after))#conver img from matrix to jpg
        label.configure(image=img_after)
        label.image = img_after  #shows the real-time result


####Gaussian
def GaussianFiltering():
    if img_is_found:
        img_after = change_GaussianFiltering(img)
        img_after = ImageTk.PhotoImage(Image.fromarray(img_after))#conver img from matrix to jpg
        label.configure(image=img_after)
        label.image = img_after  #shows the real-time result


#####Filtering
def MedianFiltering():
    if img_is_found:
        img_after = change_MedianFiltering(img)
        img_after = ImageTk.PhotoImage(Image.fromarray(img_after))#conver img from matrix to jpg
        label.configure(image=img_after)
        label.image = img_after #shows the real-time result



def show():
    if clicked.get() == "negative": return negative()
    if clicked.get() == "PowerLow": return PowerLow()
    if clicked.get() == "Thresholding": return Thresholding()
    if clicked.get() == "GaussianFiltering": return GaussianFiltering()
    if clicked.get() == "MedianFiltering": return MedianFiltering()



def reset():
    if img_is_found:
        label.configure(image=image2)
        label.image = image2 #for real-time show

#GUI
######################
window = Tk()
window.title('hFilters ')
window.geometry("1080x1080")
w,h =window.winfo_screenwidth(),window.winfo_screenheight() #return H & W
window.columnconfigure(0,weight=1)#set all content in center.

bg = ImageTk.PhotoImage(file='IMG.jpg')



file = Button(window,command=choose, height=1, width=18, text='Browse', bg='#BD1616', fg='#ffffff',font='button_font', activebackground="#ffffff") #linked the to choose function

clicked = StringVar()
clicked.set("Filter")

drop = OptionMenu(window, clicked, "negative", "PowerLow", "Thresholding", "GaussianFiltering","MedianFiltering")
drop.config(bg='#BD1616', fg='#ffffff',  font='button_font', height=1, width=15)

apply = Button(window,command=show,  text='apply filter', padx=5, pady=5, bg='#FF2626', fg='#ffffff', bd=0, font='button_font', activebackground="#ffffff")
apply.config(height=1, width=10)

resett = Button(window,command=reset , text='reset', padx=5, pady=5, bg='#808080' , fg='#ffffff', bd=0, font='button_font', activebackground="#ffffff")
resett.config(height=1, width=10)

label = Label(image=None) #initial = none

file.place(relx=0.5,rely=0.05,anchor=CENTER)
drop.place(relx=0.5,rely=0.1,anchor=CENTER)
apply.place(relx=0.5,rely=0.15,anchor=CENTER)
resett.place(relx=0.5,rely=0.2,anchor=CENTER)
label.place(relx=0.5,rely=0.6,anchor=CENTER)


window.mainloop()








