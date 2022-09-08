from tkinter import *
from PIL import ImageTk, Image
import cv2

def resize_img():
    IMG_SIZE = 100
    img_array = cv2.imread('img/screenshot.jpg',cv2.IMREAD_GRAYSCALE)
    cv2.bitwise_not(img_array)
    new_array = cv2.resize(img_array,(IMG_SIZE,IMG_SIZE))
    cv2.imwrite('img/new_image.jpg',new_array)
    img = ImageTk.PhotoImage(Image.open('img/new_image.jpg'))
    return img


def popup(number):
    
    def choice(option):
        if option == "yes":
            pop.destroy()
            from src.guess import guess_num
            guess_num() 
        else:
            pop.destroy()

    pop = Tk()

    img = resize_img()
      
    pop.title("Number Guesser")
    pop.geometry("300x300")
    pop['background']= '#D3D3D3'
    pop.resizable(width=False, height=False)
    pop.eval('tk::PlaceWindow . center')
    pop.attributes('-topmost', True)
    
    Label(pop, text="I Think Your Number is a {}".format(number), bg='grey' , font=('helvetica', 15)).place(relx=.5,rely=.1, anchor=CENTER)
    
    num_pic = Label(image=img)
    num_pic.image = img
    num_pic.place(relx=.5,rely=.35, anchor=CENTER)
    
    pop_label2 = Label(pop, text="Run Again?" , bg='grey' , font=('helvetica', 15))
    pop_label2.place(relx=.5,rely=.60, anchor=CENTER)
    
    yes = Button(pop, text="YES", command=lambda: choice('yes'), bg='grey', font=('helvetica', 12))
    yes.place(relx=.42,rely=.72, anchor=CENTER)

    no = Button(pop, text="NO", command=lambda: choice('no'), bg='grey', font=('helvetica', 12))
    no.place(relx=.58,rely=.72, anchor=CENTER)
 
    pop.mainloop()

