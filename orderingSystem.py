#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      alatif19
#
# Created:     19/04/2022
# Copyright:   (c) alatif19 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import tkinter as tk
import time
import datetime
import sqlite3

trys = 0
trysForAdmin = 0
pizza = False
burger = False
chips = False
sausages = False
view = False



root = tk.Tk()                         #Creating root window
root.resizable(False,False)
root.state("zoomed")
root.title("Food ordering menu system")
root.configure(bg="#ACAD71")


#-------------------------------------------------------------------------------




orderTime = ""
def orderTimeFunction():
    global orderTime
    updatingTime = time.strftime("%H|%M|%S %p")
    orderTime = updatingTime
    root.after(10, orderTimeFunction)

root.after(10, orderTimeFunction)

def loader():
    wipeDataBase["text"]="Wiping.."
def loader2():
    wipeDataBase["text"]="Wiping..."
def loader3():
    wipeDataBase["text"]="Wiping Complete!"
def normal():
    wipeDataBase["text"]="Wipe DataBase Record"
    wipeDataBase['state']="normal"

def wipe():
    wipeDataBase['state']="disabled"

    connection = sqlite3.connect('test3ForOrderingSystem.db')

    cursor = connection.cursor()
    cursor.execute("DELETE FROM PIZZA")

    connection.commit()
    cursor.execute("DELETE FROM BURGER")

    connection.commit()
    cursor.execute("DELETE FROM CHIPS")

    connection.commit()
    cursor.execute("DELETE FROM SAUSAGES")

    connection.commit()



    connection.close()
    wipeDataBase["text"]="Wiping."
    root.after(500, loader)
    root.after(1200, loader2)
    root.after(1900, loader3)
    root.after(4600, normal)









def toHome():                 #Defining the home button
    enterLoginPassword.grid_forget()
    exitProgram1.grid_forget()
    loginPasswordEntry.grid_forget()
    loginLabel.grid_forget()
    frame1.grid_forget()
    homeProgram.grid_forget()
    adminLabel.grid_forget()
    password.grid_forget()
    enterAdmin.grid_forget()
    enter.grid_forget()
    passwordIs.grid_forget()
    clockTime.grid_forget()
    homeProgram.grid_forget()
    wipeDataBase.grid_forget()



    rootHelloLabel.grid(row=0, column=0, pady=40)
    loginButton.grid(row=1, column=0, pady=(150, 20))
    adminButton.grid(row=2, column=0)
    exitProgram.grid(row=3, column=0, sticky='e', padx=(0, 180))
    clockTime.grid(row=4, column=0, sticky='e', padx=(0, 180))

def buttonEffect(event):
    global loginButton
    loginButton['bg'] = "#8fbea8"

def buttonEffect2(event):
    global loginButton
    loginButton['bg'] = "#71AD90"

def buttonEffect3(event):
    global adminButton
    adminButton['bg'] = "#8fbea8"

def buttonEffect4(event):
    global adminButton
    adminButton['bg'] = "#71AD90"


def adminPasswordChecker(*args):
    global trysForAdmin
    realPasswordForAdmin = "ADMIN"
    if enterAdmin.get() == realPasswordForAdmin:
        print("Access Granted")
        password['fg'] = "Black"
    else:
        trysForAdmin = trysForAdmin + 1
        print("Access Denied")
        print(trysForAdmin)
    if trysForAdmin == 4:
        root.destroy()



def order():
    if pizza == True:
        connection = sqlite3.connect('test3ForOrderingSystem.db')

        cursor = connection.cursor()

        cursor.execute("INSERT INTO PIZZA VALUES(:pizza, :time)",

                        {

                        'pizza':"Pizza",
                        'time':orderTime


                        })

        connection.commit()


        connection.close()




    if burger == True:
        connection = sqlite3.connect('test3ForOrderingSystem.db')

        cursor = connection.cursor()

        cursor.execute("INSERT INTO BURGER VALUES(:burger, :time)",

                        {

                        'burger':"Burger",
                        'time':orderTime


                        })

        connection.commit()


        connection.close()
    if chips == True:
        connection = sqlite3.connect('test3ForOrderingSystem.db')

        cursor = connection.cursor()

        cursor.execute("INSERT INTO CHIPS VALUES(:chips, :time)",

                        {

                        'chips':"Chips",
                        'time':orderTime


                        })

        connection.commit()


        connection.close()



    if sausages == True:
        connection = sqlite3.connect('test3ForOrderingSystem.db')

        cursor = connection.cursor()

        cursor.execute("INSERT INTO SAUSAGES VALUES(:sausages, :time)",

                        {

                        'sausages':"Sausages",
                        'time':orderTime


                        })

        connection.commit()


        connection.close()








#-------------------------------------------------------------------------------



def adminPasswordChecker1(enterAdmin):
    global trysForAdmin
    realPasswordForAdmin = "ADMIN"
    if enterAdmin == realPasswordForAdmin:
        print("Access Granted")
        password['fg'] = "Black"
    else:
        trysForAdmin = trysForAdmin + 1
        print("Access Denied")
        print(trysForAdmin)
    if trysForAdmin == 4:
        root.destroy()


#-------------------------------------------------------------------------------

def pizzaCommand():
    global pizza
    if pizza == False:
        pizzaButton['bg'] = "#03fc52"
        pizza = True
        return
    else:
        pizzaButton['bg'] = "#ff304c"
        pizza = False
        return
def burgerCommand():
    global burger
    if burger == False:
        burgerButton['bg'] = "#03fc52"
        burger = True
        return
    else:
        burgerButton['bg'] = "#ff304c"
        burger = False
        return
def chipsCommand():
    global chips
    if chips == False:
        chipsButton['bg'] = "#03fc52"
        chips = True
        return
    else:
        chipsButton['bg'] = "#ff304c"
        chips = False
        return
def sausagesCommand():
    global sausages
    if sausages == False:
        sausagesButton['bg'] = "#03fc52"
        sausages = True
        return
    else:
        sausagesButton['bg'] = "#ff304c"
        sausages = False
        return



def orderingMenu():
    enterLoginPassword.grid_forget()
    exitProgram1.grid_forget()
    loginPasswordEntry.grid_forget()
    loginLabel.grid_forget()
    frame1.grid_forget()
    homeProgram.grid_forget()
    clockTime.grid_forget()





    heading.grid(row=0, column=2, pady=(50, 0), ipady=(35), ipadx=(35),
                 padx=(550, 0))

    holder.grid(row=1, column=1, columnspan=3)
    pizzaLabel.grid(row=2, column=0, sticky='w', padx=(60, 0))
    burgerLabel.grid(row=3, column=0, sticky='w', padx=(60, 0))
    pizzaButton.grid(row=2, column=0)
    burgerButton.grid(row=3, column=0)
    chipsLabel.grid(row=2, column=0, padx=(400, 0))
    sausagesLabel.grid(row=3, column=0, padx=(400, 0))
    chipsButton.grid(row=2, column=0, padx=(900, 0))
    sausagesButton.grid(row=3, column=0, padx=(900, 0))
    chooseFood.grid(row=0, column=0,columnspan=1, pady=(60, 30), padx=60)
    verifyButton.grid(row=4, column=0)









#-------------------------------------------------------------------------------





def loginPasswordChecker(userPassword):     #Password checker for Login
    global trys
    global loginPasswordEntry
    realPassword = "LOGIN"
    if trys == 3:
        root.destroy()
    if userPassword == realPassword:
        print("Access Granted")
        orderingMenu()
    else:
        trys = trys + 1
        print("Access Denied")
        print(trys)

#-------------------------------------------------------------------------------

def loginPasswordCheckerForEnterKey(*args): #Password checker for Login Enter
    global trys
    realPassword = ""
    if loginPasswordEntry.get() == realPassword:
        print("Access Granted")
        root.after(100, orderingMenu)
    else:
        trys = trys + 1
        print("Access Denied")
        print(trys)
    if trys == 4:
        root.destroy()
#-------------------------------------------------------------------------------


def lol(event):
    loginPasswordEntry['state'] = tk.NORMAL
    loginPasswordEntry.delete(0, tk.END)

def lol2(event):
    text = loginPasswordEntry.get()
    loginPasswordEntry['state'] = tk.DISABLED


#-------------------------------------------------------------------------------

def adminLol(event):
    enterAdmin['state'] = tk.NORMAL
    enterAdmin.delete(0, tk.END)

def adminLol2(event):
    text = enterAdmin.get()
    enterAdmin['state'] = tk.DISABLED

#-------------------------------------------------------------------------------

def closeTheProgram():          #closes the program
    root.destroy()

#-------------------------------------------------------------------------------



def login():                          #Opens the login menu

    time.sleep(0.09)
    loginButton.grid_forget()
    adminButton.grid_forget()
    rootHelloLabel.grid_forget()
    exitProgram.grid_forget()


    enterLoginPassword.grid(row=1, column=0)
    exitProgram1.grid(row=3, column=0, sticky='e', padx=(0,26), pady=(109, 0))
    loginPasswordEntry.grid(row=0, column=0, sticky='n')
    loginLabel.grid(row=0, column=0, padx=650, pady=(40, 0))
    frame1.grid(row=1, column=0, pady=(150, 0))
    homeProgram.grid(row=4, column=0, sticky='e', padx=(0,186))
    clockTime.grid(row=5, column=0, sticky='e', padx=(0,186))




#-------------------------------------------------------------------------------

def admin():
    time.sleep(0.09)
    loginButton.grid_forget()
    adminButton.grid_forget()
    rootHelloLabel.grid_forget()
    exitProgram.grid_forget()

    adminLabel.grid(row=0, column=4, padx=(0,0), pady=(30, 0))
    password.grid(row=1, column=1, padx=(1,0), pady=(100, 0))
    enterAdmin.grid(row=1, column=2, padx=(0,0), pady=(100, 0))
    enter.grid(row=1, column=3, padx=(0,0), pady=(100, 0))
    passwordIs.grid(row=1, column=0, padx=(0,0), pady=(100, 0))
    clockTime.grid(row=4, column=5, sticky='e', pady=(228, 0), padx=(290, 0))
    homeProgram.grid(row=5, column=5, sticky='e')
    wipeDataBase.grid(row=2, column=0, columnspan=2, padx=(0, 0))





#-------------------------------------------------------------------------------



number = 0        #Loads the Loading bar that starts when the programm starts

number1 = str(number)

labe = tk.Label(root, width=10,bd=0.5, bg="#ADA5A5",
                font=("Arial Bold", 36), fg="White", relief=tk.SUNKEN)

labe.grid(row=0, column=0, pady=(780, 0), padx=500)







def work():
    global number1
    labe['text'] = "Loading" + " " + number1 + "%"
    global number
    number = number + 1
    number1 = str(number)


num = 101
for x in range(num):
    root.update()
    root.after(0, work)
    root.after(1)

print("Loading ended")
labe.grid_remove()

#-------------------------------------------------------------------------------

#Creating the login menu

loginLabel = tk.Label(root, text="Login", width=8, height=2,
                          font=("Arial Bold", 40), bg = "#ACAD71",
                          fg = "White")
frame1 = tk.LabelFrame(root, bg="#FFFAFA", pady=100, padx = 30)
loginPasswordEntry = tk.Entry(frame1, width=20,)
enterLoginPassword = tk.Button(frame1, text="Enter", command= lambda: loginPasswordChecker(loginPasswordEntry.get()))
exitProgram1 = tk.Button(root, text="Close Program", command = closeTheProgram)
homeProgram = tk.Button(root, text="Go to home", command = toHome)
loginPasswordEntry.insert(0, "Enter")
loginPasswordEntry['state'] = tk.DISABLED
loginPasswordEntry.bind('<Return>', loginPasswordCheckerForEnterKey)
loginPasswordEntry.bind('<Enter>', lol)
loginPasswordEntry.bind('<Leave>', lol2)

enterLoginPassword.grid(row=1, column=0)
exitProgram1.grid(row=3, column=0, sticky='e', padx=(0,26), pady=(109, 0))
loginPasswordEntry.grid(row=0, column=0, sticky='n')
loginLabel.grid(row=0, column=0, padx=650, pady=(40, 0))
frame1.grid(row=1, column=0, pady=(150, 0))
homeProgram.grid(row=4, column=0, sticky='e', padx=(0,26))

enterLoginPassword.grid_forget()
exitProgram1.grid_forget()
loginPasswordEntry.grid_forget()
loginLabel.grid_forget()
frame1.grid_forget()
homeProgram.grid_forget()

heading = tk.Label(root, text="Ordering Menu",
                       font=("Arial Bold", 45), bg="#ACAD71", fg = "White")


holder = tk.LabelFrame(root, bg="#FFFAFA")

chooseFood = tk.Label(holder,
                          text="Choose the food you would like to order:",
                          font=("Calibri Bold", 23), bg="White")


pizzaLabel = tk.Label(holder, text="Pizza-", font=("Calibri Bold", 19), bg="White")
burgerLabel = tk.Label(holder, text="Burger-", font=("Calibri Bold", 19), bg="White")

pizzaButton = tk.Button(holder, width=10, height=5, text="Pizza", bg = "#ff304c", command=pizzaCommand)
burgerButton = tk.Button(holder, width=10, height=5, text="Burger", bg = "#ff304c", command=burgerCommand)

verifyButton = tk.Button(holder, width=10, height=5, text="Order", bg = "White", command=order)
chipsLabel = tk.Label(holder, text="Chips-", font=("Calibri Bold", 19), bg="White")
sausagesLabel = tk.Label(holder, text="Sausages-", font=("Calibri Bold", 19), bg="White")

chipsButton = tk.Button(holder, width=10, height=5, text="Chips", bg = "#ff304c", command=chipsCommand)
sausagesButton = tk.Button(holder, width=10, height=5, text="Sausages", bg = "#ff304c", command=sausagesCommand)

#-------------------------------------------------------------------------------

adminLabel = tk.Label(root, text="Admin", width=8, height=2,
                          font=("Arial Bold", 51), bg = "#ACAD71",
                          fg = "White")

passwordIs= tk.Label(root, height=2, bg = "#ACAD71", fg = "Black",
                   text="Password is:",font=("Arial Bold", 25))

password= tk.Label(root, height=2, bg = "#ACAD71", fg = "#ACAD71",
                   text="LOGIN",font=("Arial Bold", 30))

enterAdmin= tk.Entry(root, bg = "#ACAD71", width=11
                   ,font=("Arial Bold", 20))
wipeDataBase = tk.Button(root, text="Wipe DataBase records",
                         font=("Arial", 21), command=wipe
                             )
viewDataBase = tk.Button(root, text="View DataBase records",
                         font=("Arial", 21)
                             )
databaseRecords= tk.Label(root, bg = "#ACAD71"
                   ,font=("Arial Bold", 15))


enterAdmin.insert(0, "Enter Here")
enterAdmin['state'] = tk.DISABLED
enterAdmin.bind('<Return>', adminPasswordChecker)
enterAdmin.bind('<Enter>', adminLol)
enterAdmin.bind('<Leave>', adminLol2)

enter= tk.Button(root, bg = "#ACAD71", text="Enter"
                ,font=("Arial Bold", 25),
                command= lambda: adminPasswordChecker1(enterAdmin.get()))




#-------------------------------------------------------------------------------



#Main menu


rootHelloLabel = tk.Label(root, text = "Ordering system, please sign in",
                          bg = "#7271AD", fg="White", font=("Arial Bold", 40),
                          width=48, height=2)

loginButton = tk.Button(root, pady = 30, padx = 80, text="Login",
                        font=("Arial Bold", 27), bg="#71AD90", fg="#D0CFD1",
                        command=login)
loginButton.bind('<Enter>', buttonEffect)
loginButton.bind('<Leave>', buttonEffect2)

adminButton = tk.Button(root, pady = 10, padx = 40, text="Admin",
                        font=("Arial Bold", 27), bg="#71AD90", fg="#D0CFD1",
                        command=admin)

adminButton.bind('<Enter>', buttonEffect3)
adminButton.bind('<Leave>', buttonEffect4)

exitProgram = tk.Button(root, text="Close Program", command = closeTheProgram)

def clock():
    string = time.strftime("%H|%M %p")
    clockTime.config(text = string)
    clockTime.after(100, clock)



clockTime = tk.Label(root, bg = "#ACAD71", fg="White", font=("calibri", 30))

rootHelloLabel.grid(row=0, column=0, pady=40)
loginButton.grid(row=1, column=0, pady=(150, 20))
adminButton.grid(row=2, column=0)
exitProgram.grid(row=3, column=0, sticky='e', padx=(0, 140))
clockTime.grid(row=4, column=0, sticky='e', padx=(0, 140))

clock()


#-------------------------------------------------------------------------------


root.mainloop()
