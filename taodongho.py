from tkinter import*
from PIL import Image,ImageTk
a=Tk()
a.geometry('1200x630')
class an():
    dem=0
    canvas=Canvas(a,background='black')
    canvas.pack(expand=True,fill="both",anchor='center')
    x1=430
    img=Image.open(r"C:\Users\LENOVO\Pictures\dhbkhn-6920-1658994052-1-16702134834751920701721.jpg")
    img1=img.resize((700,500),Image.BILINEAR)
    img2=ImageTk.PhotoImage(img1)
    l=Label(a,text='',image=img2,borderwidth=0,highlightthickness=0)
    l.place(x=x1,y=200)
    img3=Image.open(r"C:\Users\LENOVO\Pictures\69216849_1200x675_1_ncda.jpg")
    img4=img3.resize((700,500),Image.BILINEAR)
    img5=ImageTk.PhotoImage(img4)
    l1=Label(a,text='',image=img5,borderwidth=0,highlightthickness=0,bg="white")
    l1.place(x=x1+1200,y=200)
    img6=Image.open(r"C:\Users\LENOVO\Pictures\-4772-1663217379.jpg")
    img7=img6.resize((700,500),Image.BILINEAR)
    img8=ImageTk.PhotoImage(img7)
    l2=Label(a,text='',image=img8,borderwidth=0,highlightthickness=0)
    l2.place(x=x1+1200,y=200)
    img9=Image.open(r"C:\Users\LENOVO\Pictures\242481655_2344964658971083_7905287510387238215_n_1.jpeg")
    img10=img9.resize((700,500),Image.BILINEAR)
    img11=ImageTk.PhotoImage(img10)
    l3=Label(a,text='',image=img11,borderwidth=0,highlightthickness=0)
    l3.place(x=x1+1200,y=200)
    def an2(self):
        an.dem+=1
        if(an.dem==1):
            an.l1.place(x=an.x1,y=200)
        elif(an.dem==2):
            an.l2.place(x=an.x1,y=200)
        elif(an.dem==3):
            an.l3.place(x=an.x1,y=200)
        else:
             an.dem=3
    def an1(self):
        an.dem-=1
        if(an.dem==0):
                an.l1.place(x=an.x1+1200,y=200)
        elif(an.dem==1):
            an.l2.place(x=an.x1+1200,y=200)
        elif(an.dem==2):
            an.l3.place(x=an.x1+1200,y=200)
        else:
             an.dem=0
def dem(giay): 
        b,c=divmod(giay,3600)
        c1,c2=divmod(c,60)
        if giay==0:
            l=Label(a,text='00:00:00',font=("Times New Roman",80))
            l.place(x=590,y=50)
        else:
            l=Label(a,text='{:02d}:{:02d}:{:02d}'.format(b,c1,c2),font=("Times New Roman",80))
            l.place(x=590,y=50)
            a.after(1000,dem,giay-1)
s=an()
but=Button(a,text="<",font=("Times New Roman",15),bg="white",borderwidth=0,highlightthickness=0,width=3,activebackground='white',command=s.an1)
but.place(x=387,y=457)
but.lift()
but=Button(a,text=">",font=("Times New Roman",15),bg="white",borderwidth=0,highlightthickness=0,width=3,activebackground='white',command=s.an2)
but.place(x=1140,y=450)
but.lift()
dem(4*3600)# nhập số giây bạn muốn đếm
mainloop()