import tkinter as tk 
import mysql.connector as mysql  
from tkinter import *
from PIL import ImageTk,Image 

from tkinter import messagebox
from plyer import notification
import requests
from bs4 import BeautifulSoup
import time
   
  
def submit(): 
      
    user = Username.get() 
    passw = password.get() 
   
    print(f"The name entered by you is {user} {passw}") 
   
    login(user, passw)


def insertdetails(name,email,city,password):
    data = (name,email,city,password)
    if name == "":
             messagebox.showinfo("Alert!","Enter Username First")
    elif password == "":
             messagebox.showinfo("Alert!", "Enter Password first")
    else:
     
        db =mysql.connect(host = 'localhost', user = 'root' , passwd ='yourpassword',database = 'yourdatabase')
        if db.is_connected():
            print("successfully connected") 
        cursor = db.cursor() 
        sql = "INSERT INTO notify(username, email,city,password) VALUES ('%s', '%s','%s','%s')" % (name,email,city,password)
        try:
            # implement sql Sentence
            cursor.execute(sql)
            print ("Data insertion success!!!")
            # Submit to database for execution
            db.commit()
        except:
            print ("Data insertion failed!!!")
            # Rollback in case there is any error
            db.rollback()
        cursor.execute("select * from  notify;")
        myresult = cursor.fetchall()
        print(myresult)


def SignIn():
    newWin = Toplevel(root)
    newWin.title("SignIn Form")
    newWin.geometry("500x400")
    Label(newWin,text = "Sign Up",font= ("Impact" ,25,"bold"),fg = "#006400",bg ="white").place(x=170 ,y= 20)



    l1 = Label(newWin , text = "Name",font= "comicsanms 15 bold",fg = "#006400",bg ="white",padx=6,pady =6).place(x=60,y=80)
    l2 = Label(newWin , text = "E-mail",font= "comicsanms 15 bold",fg = "#006400",bg ="white",padx=6,pady =6).place(x=60,y=120)
    l3 = Label(newWin , text = "City",font= "comicsanms 15 bold",fg = "#006400",bg ="white",padx=6,pady =6).place(x=60,y=160)
    l4 = Label(newWin , text = "Password",font= "comicsanms 15 bold",fg = "#006400",bg ="white",padx=6,pady =6).place(x=60,y=200)

    namevalue = StringVar()
    emailvalue = StringVar()
    cityvalue = StringVar()
    passwordvalue = StringVar()




    nameentry = Entry(newWin,textvariable =namevalue,font=("lucida 15 bold"), relief=SUNKEN, borderwidth=3).place(x=200,y=80)
    emailentry = Entry(newWin ,textvariable = emailvalue,font=("lucida 15 bold"), relief=SUNKEN, borderwidth=3).place(x=200,y=120)
    cityentry = Entry(newWin,textvariable = cityvalue,font=("lucida 15 bold"), relief=SUNKEN, borderwidth=3).place(x=200,y=160)
    passwordentry = Entry(newWin, show="*",textvariable = passwordvalue,font=("lucida 15 bold"), relief=SUNKEN, borderwidth=3).place(x=200,y=200)


    b1 = Button(newWin , text = "Create Account",command =lambda: insertdetails(namevalue.get(),emailvalue.get(),cityvalue.get(),passwordvalue.get()),font = "comicsanms 10 bold").place(x=100,y= 300,width = 120)
    b2 = Button(newWin , text = "Cancel",command = quit,font= "comicsanms 10 bold").place(x=250,y= 300,width = 100)
    

   
   
def login(user, passw): 
      
    # If paswword is enetered by the  
    # user 
    data = (user,passw)
    username = user
    if user == "":
             messagebox.showinfo("Alert!","Enter Username First")
    elif passw == "":
             messagebox.showinfo("Alert!", "Enter Password first")
    else:
     
        db =mysql.connect(host = 'localhost', user = 'root' , passwd ='prachi123',database = 'sample') 
        cursor = db.cursor() 
        query = "select username , password from notify"
        
        cursor.execute(query) 
        myresult = cursor.fetchall() 
        print(data)
          
        # Printing the result of the 
        # query 
        for x in myresult: 
            print(x) 
            print("Query Excecuted succesfully")
        if  data == x :
                    messagebox.showinfo("Message", "Login Successfully")
                    messagebox.showinfo("Info","You will be Notify soon...")
                    sql1 = ("SELECT city FROM notify WHERE username = '{}'").format(username)
                    cursor.execute(sql1)
                    myresult = cursor.fetchall()
                    for x in myresult:
                        print(x)
                    getNotify(x)
                    
                
        else:
                messagebox.showinfo("ALert!", "Wrong username/password")


def getNotify(city):
    def notifyme(title, message):
       notification.notify(
        title=title,
        message=message,
        #app_icon=r"C:\Users\Kush\Desktop\c.ico",
        timeout=10

      )
    def getData(url):
       r = requests.get(url)
       return r.text


    while True:
        # notifyme("Corona Update", "lets stop this togther")
        myHtmlData = getData('https://www.mohfw.gov.in/')
    
        soup = BeautifulSoup(myHtmlData, 'html.parser')
        # print(soup.prettify())
        myDatastr= ""
        for tr in soup.find_all('tbody')[0].find_all('tr'):
            myDatastr += tr.get_text()
        myDatastr = myDatastr[1:]
        itemList = myDatastr.split("\n\n")
            
        states = city
        for item in itemList[0:29]:
            datalist = item.split('\n')
            # print(datalist)
            if datalist[1] in states:
                nTitle = 'Cases of COVOID-19'
                nText = f"State - {datalist[1]}\nTotal case: {datalist[2]}\n Cured: {datalist[3]}\n Deaths: {datalist[4]}"
                notifyme(nTitle, nText)
                #time.sleep(2)
        time.sleep(1200)




        
          
     
   
   
root = tk.Tk() 
 
root.geometry("1125x770")
root.minsize(1125,770)
root.maxsize(1125,770)
bg = ImageTk.PhotoImage( Image.open("C:\\Users\\user\\Desktop\\python\\summertraining\\tkinter\\database\\get botify by tkinter\\COVID-19-CoronavirusBG.jpg"))
bg_Image = tk.Label(root,image = bg ).place(x=0,y=0,relwidth = 1 ,relheight = 1)
root.title("Login Page") 
#defining frame 
f = tk.Frame(root,bg="white")


title = tk.Label(f,text = "Login Here",font = ("Impact" ,35,"bold"),fg = "#006400",bg ="white")
title.place(x=110,y=10)

desc = tk.Label(f,text = "(Get realtime notification of Corona Virus Cases of your City)",font = ("Goudy old style",13,"bold"),fg ="#006400",bg="white").place(x=25,y=70)
   

  
# Definging the first row 
lbl1 = tk.Label(f, text ="Username -",font= "comicsanms 15 bold",fg = "#006400",bg ="white" ) 
lbl1.place(x = 60, y = 150) 
  
Username = tk.Entry(f, width = 35,font=("lucida 15 bold"), relief=SUNKEN, borderwidth=3) 
Username.place(x = 175, y = 150, width = 150) 
   
lbl2 = tk.Label(f, text ="Password -",font= "comicsanms 15 bold",fg = "#006400",bg ="white") 
lbl2.place(x = 60, y = 200) 
  
password = tk.Entry(f, width = 35,show="*",font=("lucida 15 bold"), relief=SUNKEN, borderwidth=3 ) 
password.place(x = 175, y = 200, width = 150) 
  
submitbtn = tk.Button(f, text ="Login",font= "comicsanms 15 bold",  
                       command = submit) 
submitbtn.place(x = 100, y = 300, width = 100) 
submitbtn = tk.Button(f, text ="Forget",font= "comicsanms 15 bold",  
                       command = submit) 
submitbtn.place(x = 250, y = 300, width = 100)


lbl3 = tk.Label(f, text ="Create an Account?",font= "comicsanms 10 bold",fg = "#006400",bg ="white") 
lbl3.place(x = 150, y = 400) 

submitbtn = tk.Button(f, text ="Sign Up",font= "comicsanms 10 bold",  
                       command = SignIn) 
submitbtn.place(x = 300, y = 400, width = 80) 
f.place(x=100,y=150,height=500,width=500)
  
root.mainloop() 