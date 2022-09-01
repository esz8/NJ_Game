import tkinter as tk
from tkinter import *

title_font = ("Arial", 18)

sub_font = ("Arial" , 14)

math_q = [None]*4
english_q = [None]*4
science_q = [None]*4
cs_q =[None]*4

math_a = [None] *4
english_a = [None]*4
science_a =[None]*4
cs_a = [None]*4


class main(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args,**kwargs)

        tk.Tk.wm_title(self, "Notecard Jeopardy")

        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for page in (HomePage, NotecardPage, MathCreate,EnglishCreate, ScienceCreate, CSCreate, JeopardyGame):

            frame = page(container, self)   
            self.frames[page] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)
    
    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class HomePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Notecard Jeopardy!", font=title_font)
        label.grid(row = 0, column = 1, columnspan = 2, padx = 150)

        notecard_button = tk.Button(self, text = "Create Notecards", command = lambda: controller.show_frame(NotecardPage),height = 3, width = 15, font = ("Arial", 10))
        notecard_button.grid(row = 1, column = 1,  padx = 5, pady=20)

        game_button = tk.Button(self, text = "Play Game", command = lambda: [controller.show_frame(JeopardyGame),app.geometry ("950x750")],  height = 3, width = 15, font = ("Arial", 10))
        game_button.grid(row = 1, column = 2, padx = 5, pady=20)


        exit_button  = tk.Button(self, text ="Exit", command = lambda: app.destroy(), height = 3, width =15 , font  =   ("Arial", 10))
        exit_button.grid(row =3, column =1, pady =30)

class NotecardPage(tk.Frame):
    def __init__(self, parent,controller):
        tk.Frame.__init__(self,  parent)
        label = tk.Label(self, text="Choose Subject:  ", font=title_font)
        label.grid(row= 0, column = 0, columnspan = 2, pady=10,padx=150)

        math_button = tk.Button(self, text = "Math", command = lambda: controller.show_frame(MathCreate), height = 3, width = 15)
        math_button.grid(row= 1, column = 0, pady=5)

        english_button = tk.Button(self, text = "English", command = lambda: controller.show_frame(EnglishCreate), height = 3, width = 15 )
        english_button.grid(row= 1, column = 1, pady=5)

        science_button = tk.Button(self, text = "Science",  command = lambda: controller.show_frame(ScienceCreate), height = 3, width = 15)
        science_button.grid(row= 2, column = 0, pady=5 )


        CS_button = tk.Button(self, text = "Computer Science", command = lambda: controller.show_frame(CSCreate), height = 3, width = 15)
        CS_button.grid(row= 2, column = 1, pady=5)
    
        home_button  = tk.Button( self, text ="Back to Home ", command = lambda: controller.show_frame ( HomePage), height = 3, width = 15)
        home_button.grid(row= 3, column = 1, pady=  50 )

class MathCreate(tk.Frame):
    def __init__(self, parent,controller):
        tk.Frame.__init__(self,  parent)
        qlabel = tk.Label(self, text="Questions:  ", font=sub_font )
        qlabel.grid(row = 0, column = 1 )
        alabel = tk.Label(self, text="Answers: ", font= sub_font)
        alabel.grid(row = 0, column = 2)

        label1 = tk.Label(self, text="Card 1: ")
        label1.grid(row = 1, column = 0)
        label2 = tk.Label(self, text="Card 2: " )
        label2.grid(row = 2, column = 0)
        label3 = tk.Label(self, text="Card 3: ")
        label3.grid(row = 3, column = 0 )
        label4 = tk.Label(self, text="Card 4: ")
        label4.grid(row = 4, column = 0)    

        self.q1 = tk.Entry(self)
        self.q1.grid(row = 1, column = 1, padx = 10, pady = 20)

        self.q2 = tk.Entry(self)
        self.q2.grid(row = 2, column = 1, padx = 10,pady = 20)

        self.q3 = tk.Entry(self)
        self.q3.grid(row = 3, column = 1, padx = 10,pady = 20)

        self.q4 = tk.Entry(self)
        self.q4.grid(row = 4, column = 1, padx = 10,pady = 20)

        self.a1 = tk.Entry(self)
        self.a1.grid(row = 1, column = 2, padx = 10,pady = 20)

        self.a2 = tk.Entry(self)
        self.a2.grid(row = 2, column = 2, padx = 10,pady = 20)

        self.a3 = tk.Entry(self)
        self.a3.grid(row = 3, column = 2, padx = 10,pady = 20)

        self.a4 = tk.Entry(self) 
        self.a4.grid(row = 4, column = 2, padx = 10,pady = 20)

        save_button = tk.Button(self, text = "Save ", command = lambda: self.get_input())
        save_button.grid(row = 5, column =1, padx =10, pady=30)
        
        home_button = tk.Button(self, text = "Back ", command = lambda: controller.show_frame(NotecardPage))
        home_button.grid(row = 5, column = 2, padx = 10,  pady=30)

    def get_input(self):
        counter = 0
        for elem in [self.q1.get(),self.q2.get(),self.q3.get(),self.q4.get()]:
            
            if elem != "":
                math_q[counter] = str(elem)
            counter += 1
        counter = 0

        
        for elem in [self.a1.get(), self.a2.get(), self.a3.get(), self.a4.get() ]:
            if elem != "":
                math_a[counter] = str(elem)
            counter +=1

class EnglishCreate(tk.Frame):
    def __init__(self, parent,controller):
        tk.Frame.__init__(self,  parent)
        qlabel = tk.Label(self, text="Questions:  ", font=sub_font )
        qlabel.grid(row = 0, column = 1 )
        alabel = tk.Label(self, text="Answers: ", font= sub_font)
        alabel.grid(row = 0, column = 2)

        label1 = tk.Label(self, text="Card 1: ")
        label1.grid(row = 1, column = 0)
        label2 = tk.Label(self, text="Card 2: " )
        label2.grid(row = 2, column = 0)
        label3 = tk.Label(self, text="Card 3: ")
        label3.grid(row = 3, column = 0 )
        label4 = tk.Label(self, text="Card 4: ")
        label4.grid(row = 4, column = 0)    

        self.q1 = tk.Entry(self)
        self.q1.grid(row = 1, column = 1, padx = 10, pady = 20)

        self.q2 = tk.Entry(self)
        self.q2.grid(row = 2, column = 1, padx = 10,pady = 20)

        self.q3 = tk.Entry(self)
        self.q3.grid(row = 3, column = 1, padx = 10,pady = 20)

        self.q4 = tk.Entry(self)
        self.q4.grid(row = 4, column = 1, padx = 10,pady = 20)

        self.a1 = tk.Entry(self)
        self.a1.grid(row = 1, column = 2, padx = 10,pady = 20)

        self.a2 = tk.Entry(self)
        self.a2.grid(row = 2, column = 2, padx = 10,pady = 20)

        self.a3 = tk.Entry(self)
        self.a3.grid(row = 3, column = 2, padx = 10,pady = 20)

        self.a4 = tk.Entry(self) 
        self.a4.grid(row = 4, column = 2, padx = 10,pady = 20)

        save_button = tk.Button(self, text = "Save ", command = lambda: self.get_input())
        save_button.grid(row = 5, column =1, padx =10, pady=30)
        
        home_button = tk.Button(self, text = "Back ", command = lambda: controller.show_frame(NotecardPage))
        home_button.grid(row = 5, column = 2, padx = 10,  pady=30)

    def get_input(self):
        counter = 0
        for elem in [self.q1.get(),self.q2.get(),self.q3.get(),self.q4.get()]:
            
            if elem != "":
                english_q[counter] = elem
            counter += 1
        counter = 0

        
        for elem in [self.a1.get(), self.a2.get(), self.a3.get(), self.a4.get() ]:
            if elem != "":
                english_a[counter] = elem
            counter +=1
class ScienceCreate(tk.Frame):
    def __init__(self, parent,controller):
        tk.Frame.__init__(self,  parent)
        qlabel = tk.Label(self, text="Questions:  ", font=sub_font )
        qlabel.grid(row = 0, column = 1 )
        alabel = tk.Label(self, text="Answers: ", font= sub_font)
        alabel.grid(row = 0, column = 2)

        label1 = tk.Label(self, text="Card 1: ")
        label1.grid(row = 1, column = 0)
        label2 = tk.Label(self, text="Card 2: " )
        label2.grid(row = 2, column = 0)
        label3 = tk.Label(self, text="Card 3: ")
        label3.grid(row = 3, column = 0 )
        label4 = tk.Label(self, text="Card 4: ")
        label4.grid(row = 4, column = 0)    

        self.q1 = tk.Entry(self)
        self.q1.grid(row = 1, column = 1, padx = 10, pady = 20)

        self.q2 = tk.Entry(self)
        self.q2.grid(row = 2, column = 1, padx = 10,pady = 20)

        self.q3 = tk.Entry(self)
        self.q3.grid(row = 3, column = 1, padx = 10,pady = 20)

        self.q4 = tk.Entry(self)
        self.q4.grid(row = 4, column = 1, padx = 10,pady = 20)

        self.a1 = tk.Entry(self)
        self.a1.grid(row = 1, column = 2, padx = 10,pady = 20)

        self.a2 = tk.Entry(self)
        self.a2.grid(row = 2, column = 2, padx = 10,pady = 20)

        self.a3 = tk.Entry(self)
        self.a3.grid(row = 3, column = 2, padx = 10,pady = 20)

        self.a4 = tk.Entry(self) 
        self.a4.grid(row = 4, column = 2, padx = 10,pady = 20)

        save_button = tk.Button(self, text = "Save ", command = lambda: self.get_input())
        save_button.grid(row = 5, column =1, padx =10, pady=30)
        
        home_button = tk.Button(self, text = "Back ", command = lambda: controller.show_frame(NotecardPage))
        home_button.grid(row = 5, column = 2, padx = 10,  pady=30)

    def get_input(self):
        counter = 0
        for elem in [self.q1.get(),self.q2.get(),self.q3.get(),self.q4.get()]:
            
            if elem != "":
                science_q[counter] = elem
                counter += 1
                
        counter = 0

        
        for elem in [self.a1.get(), self.a2.get(), self.a3.get(), self.a4.get() ]:
            if elem != "":
                science_a[counter] = elem
            counter +=1

                
class CSCreate(tk.Frame):
    def __init__(self, parent,controller):
        tk.Frame.__init__(self,  parent)
        qlabel = tk.Label(self, text="Questions:  ", font=sub_font )
        qlabel.grid(row = 0, column = 1 )
        alabel = tk.Label(self, text="Answers: ", font= sub_font)
        alabel.grid(row = 0, column = 2)

        label1 = tk.Label(self, text="Card 1: ")
        label1.grid(row = 1, column = 0)
        label2 = tk.Label(self, text="Card 2: " )
        label2.grid(row = 2, column = 0)
        label3 = tk.Label(self, text="Card 3: ")
        label3.grid(row = 3, column = 0 )
        label4 = tk.Label(self, text="Card 4: ")
        label4.grid(row = 4, column = 0)    

        self.q1 = tk.Entry(self)
        self.q1.grid(row = 1, column = 1, padx = 10, pady = 20)

        self.q2 = tk.Entry(self)
        self.q2.grid(row = 2, column = 1, padx = 10,pady = 20)

        self.q3 = tk.Entry(self)
        self.q3.grid(row = 3, column = 1, padx = 10,pady = 20)

        self.q4 = tk.Entry(self)
        self.q4.grid(row = 4, column = 1, padx = 10,pady = 20)

        self.a1 = tk.Entry(self)
        self.a1.grid(row = 1, column = 2, padx = 10,pady = 20)

        self.a2 = tk.Entry(self)
        self.a2.grid(row = 2, column = 2, padx = 10,pady = 20)

        self.a3 = tk.Entry(self)
        self.a3.grid(row = 3, column = 2, padx = 10,pady = 20)

        self.a4 = tk.Entry(self) 
        self.a4.grid(row = 4, column = 2, padx = 10,pady = 20)

        save_button = tk.Button(self, text = "Save ", command = lambda: self.get_input())
        save_button.grid(row = 5, column =1, padx =10, pady=30)
        
        home_button = tk.Button(self, text = "Back ", command = lambda: controller.show_frame(NotecardPage))
        home_button.grid(row = 5, column = 2, padx = 10,  pady=30)

    def get_input(self):    
        counter = 0
        for elem in [self.q1.get(),self.q2.get(),self.q3.get(),self.q4.get()]:
            
            if elem != "":
                cs_q[counter] = elem
                counter += 1
        counter = 0

        
        for elem in [self.a1.get(), self.a2.get(), self.a3.get(), self.a4.get() ]:
            if elem != "":
                cs_a[counter] = elem
            counter +=1


class JeopardyGame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,  parent)
        
        mathTopic= tk.Label(self, text=" Math ",bg="pink",fg="white",font=(None,50),height=2,width=6)
        englishTopic= tk.Label(self, text=" English  ",bg="orange",fg="white",font=(None,50),height=2,width=6)
        scienceTopic= tk.Label(self, text=" Science ",bg="brown",fg="white",font=(None,50),height=2,width=6)
        pythonTopic= tk.Label(self, text=" CS ",bg="indigo",fg="white",font=(None,50),height=2,width=6)

        math1= tk.Button(self, text="1",bg="green",fg="white",font=(None,50),height=1,width=6,command = lambda: self.mathOne())
        math2= tk.Button(self, text="2",bg="green",fg="white",font=(None,50),height=1,width=6,command=lambda:self.mathTwo())
        math3= tk.Button(self, text="3",bg="green",fg="white",font=(None,50),height=1,width=6,command=lambda:self.mathThree())
        math4= tk.Button(self, text="4",bg="green",fg="white",font=(None,50),height=1,width=6,command=lambda: self.mathFour())

        english1= tk.Button(self, text="1",bg="blue",fg="white",font=(None,50),height=1,width=6,command=lambda:  self.englishOne())
        english2= tk.Button(self, text="2",bg="blue",fg="white",font=(None,50),height=1,width=6,command=lambda:  self.englishTwo())
        english3= tk.Button(self, text="3",bg="blue",fg="white",font=(None,50),height=1,width=6,command= lambda: self.englishThree())
        english4= tk.Button(self, text="4",bg="blue",fg="white",font=(None,50),height=1,width=6,command=lambda: self.englishFour())


        science1= tk.Button(self, text="1",bg="purple",fg="white",font=(None,50),height=1,width=6,command=lambda: self.scienceOne())
        science2= tk.Button(self, text="2",bg="purple",fg="white",font=(None,50),height=1,width=6,command= lambda: self.scienceTwo())
        science3= tk.Button(self, text="3",bg="purple",fg="white",font=(None,50),height=1,width=6,command= lambda: self.scienceThree())
        science4= tk.Button(self, text="4",bg="purple",fg="white",font=(None,50),height=1,width=6,command= lambda: self.scienceFour())

        cs1= tk.Button(self, text="1",bg="red",fg="white",font=(None,50),height=1,width=6,command= lambda: self.csOne())
        cs2= tk.Button(self, text="2",bg="red",fg="white",font=(None,50),height=1,width=6,command= lambda: self.CSTwo())
        cs3= tk.Button(self, text="3",bg="red",fg="white",font=(None,50),height=1,width=6,command=  lambda: self.csThree())
        cs4= tk.Button(self, text="4",bg="red",fg="white",font=(None,50),height=1,width=6,command= lambda: self.csFour())

        mathTopic.grid(column=0,row=0)
        englishTopic.grid(column=1,row=0)
        scienceTopic.grid(column=2,row=0)
        pythonTopic.grid(column=3,row=0)
     
        math1.grid(column=0,row=1)
        math2.grid(column=0,row=2)
        math3.grid(column=0,row=3)
        math4.grid(column=0,row=4)

        english1.grid(column=1,row=1)
        english2.grid(column=1,row=2)
        english3.grid(column=1,row=3)
        english4.grid(column=1,row=4)

        science1.grid(column=2,row=1)
        science2.grid(column=2,row=2)
        science3.grid(column=2,row=3)
        science4.grid(column=2,row=4)

        cs1.grid(column=3,row=1)
        cs2.grid(column=3,row=2)
        cs3.grid(column=3,row=3) 
        cs4.grid(column=3,row=4)
       
        
        home_button = tk.Button(self, text = "Back to home ", command = lambda: [ controller.show_frame(HomePage),  app.geometry ("500x400") ]  )
        home_button.grid(pady=30)
    def mathOne(self):
        root1 = Tk()
        root1.config(background="dark blue")

        self.q_number = ['m',1]
        
        question = Label(root1,text=math_q[0],font=(None,30),bg="dark blue",fg="white")
        question.grid(column=0,row=0)

        label = Label(root1, text = "Answer:  ", font = (sub_font), bg="dark blue",fg="white")
        label.grid(column = 0, row =1)
        
        self.a_input = Entry(root1,font=sub_font )
        self.a_input.grid(column=1,row=1)
        answer = Button(root1, text = "Answer" , font=  sub_font, bg = "dark blue", fg ="white", command = lambda: self.check_ans())
        answer.grid(column =2, row =  1)

        destroy = Button(root1, text ="Back", font = (sub_font ), bg ="dark blue", fg =     "white" ,  command  = lambda: root1.destroy())
        destroy.grid(column = 1, row= 2)
    def mathTwo(self):
        root1 = Tk()
        root1.config(background="dark blue")

        self.q_number = ['m',2]
        
        question = Label(root1,text=math_q[1],font=(None,30),bg="dark blue",fg="white")
        question.grid(column=0,row=0)

        label = Label(root1, text = "Answer:  ", font = (sub_font), bg="dark blue",fg="white")
        label.grid(column = 0, row =1)
        
        self.a_input = Entry(root1,font=sub_font )
        self.a_input.grid(column=1,row=1)
        answer = Button(root1, text = "Answer" , font=  sub_font, bg = "dark blue", fg ="white", command = lambda: self.check_ans())
        answer.grid(column =2, row =  1)

        destroy = Button(root1, text ="Back", font = (sub_font ), bg ="dark blue", fg =     "white" ,  command  = lambda: root1.destroy())
        destroy.grid(column = 1, row= 2)
    def mathThree(self):
        root1 = Tk()
        root1.config(background="dark blue")

        self.q_number = ['m',3]
        
        question = Label(root1,text=math_q[2],font=(None,30),bg="dark blue",fg="white")
        question.grid(column=0,row=0)

        label = Label(root1, text = "Answer:  ", font = (sub_font), bg="dark blue",fg="white")
        label.grid(column = 0, row =1)
        
        self.a_input = Entry(root1,font=sub_font )
        self.a_input.grid(column=1,row=1)
        answer = Button(root1, text = "Answer" , font=  sub_font, bg = "dark blue", fg ="white", command = lambda: self.check_ans())
        answer.grid(column =2, row =  1)

        destroy = Button(root1, text ="Back", font = (sub_font ), bg ="dark blue", fg =     "white" ,  command  = lambda: root1.destroy())
        destroy.grid(column = 1, row= 2)
    def mathFour(self):
        root1 = Tk()
        root1.config(background="dark blue")

        self.q_number = ['m',4]
        
        question = Label(root1,text=math_q[3],font=(None,30),bg="dark blue",fg="white")
        question.grid(column=0,row=0)

        label = Label(root1, text = "Answer:  ", font = (sub_font), bg="dark blue",fg="white")
        label.grid(column = 0, row =1)
        
        self.a_input = Entry(root1,font=sub_font )
        self.a_input.grid(column=1,row=1)
        answer = Button(root1, text = "Answer" , font=  sub_font, bg = "dark blue", fg ="white", command = lambda: self.check_ans())
        answer.grid(column =2, row =  1)

        destroy = Button(root1, text ="Back", font = (sub_font ), bg ="dark blue", fg =     "white" ,  command  = lambda: root1.destroy())
        destroy.grid(column = 1, row= 2)

    def englishOne(self):
        root1 = Tk()
        root1.config(background="dark blue")

        self.q_number = ['e',1]
        
        question = Label(root1,text=english_q[0],font=(None,30),bg="dark blue",fg="white")
        question.grid(column=0,row=0)

        label = Label(root1, text = "Answer:  ", font = (sub_font), bg="dark blue",fg="white")
        label.grid(column = 0, row =1)
        
        self.a_input = Entry(root1,font=sub_font )
        self.a_input.grid(column=1,row=1)
        answer = Button(root1, text = "Answer" , font=  sub_font, bg = "dark blue", fg ="white", command = lambda: self.check_ans())
        answer.grid(column =2, row =  1)

        destroy = Button(root1, text ="Back", font = (sub_font ), bg ="dark blue", fg =     "white" ,  command  = lambda: root1.destroy())
        destroy.grid(column = 1, row= 2)
    def englishTwo(self):
        root1 = Tk()
        root1.config(background="dark blue")

        self.q_number = ['e',2]
        
        question = Label(root1,text=english_q[1],font=(None,30),bg="dark blue",fg="white")
        question.grid(column=0,row=0)

        label = Label(root1, text = "Answer:  ", font = (sub_font), bg="dark blue",fg="white")
        label.grid(column = 0, row =1)
        
        self.a_input = Entry(root1,font=sub_font )
        self.a_input.grid(column=1,row=1)
        answer = Button(root1, text = "Answer" , font=  sub_font, bg = "dark blue", fg ="white", command = lambda: self.check_ans())
        answer.grid(column =2, row =  1)

        destroy = Button(root1, text ="Back", font = (sub_font ), bg ="dark blue", fg =     "white" ,  command  = lambda: root1.destroy())
        destroy.grid(column = 1, row= 2)
    def englishThree(self):
        root1 = Tk()
        root1.config(background="dark blue")

        self.q_number = ['e',3]
        
        question = Label(root1,text=english_q[2],font=(None,30),bg="dark blue",fg="white")
        question.grid(column=0,row=0)

        label = Label(root1, text = "Answer:  ", font = (sub_font), bg="dark blue",fg="white")
        label.grid(column = 0, row =1)
        
        self.a_input = Entry(root1,font=sub_font )
        self.a_input.grid(column=1,row=1)
        answer = Button(root1, text = "Answer" , font=  sub_font, bg = "dark blue", fg ="white", command = lambda: self.check_ans())
        answer.grid(column =2, row =  1)

        destroy = Button(root1, text ="Back", font = (sub_font ), bg ="dark blue", fg =     "white" ,  command  = lambda: root1.destroy())
        destroy.grid(column = 1, row= 2)
    def englishFour(self):
        root1 = Tk()
        root1.config(background="dark blue")

        self.q_number = ['e',4 ]
        
        question = Label(root1,text=english_q[3],font=(None,30),bg="dark blue",fg="white")
        question.grid(column=0,row=0)

        label = Label(root1, text = "Answer:  ", font = (sub_font), bg="dark blue",fg="white")
        label.grid(column = 0, row =1)
        
        self.a_input = Entry(root1,font=sub_font )
        self.a_input.grid(column=1,row=1)
        answer = Button(root1, text = "Answer" , font=  sub_font, bg = "dark blue", fg ="white", command = lambda: self.check_ans())
        answer.grid(column =2, row =  1)
    
        destroy = Button(root1, text ="Back", font = (sub_font ), bg ="dark blue", fg =     "white" ,  command  = lambda: root1.destroy())
        destroy.grid(column = 1, row= 2)


    def scienceOne(self):
        root1 = Tk()
        root1.config(background="dark blue")

        self.q_number = ['s',1]
        
        question = Label(root1,text=science_q[0],font=(None,30),bg="dark blue",fg="white")
        question.grid(column=0,row=0)

        label = Label(root1, text = "Answer:  ", font = (sub_font), bg="dark blue",fg="white")
        label.grid(column = 0, row =1)
        
        self.a_input = Entry(root1,font=sub_font )
        self.a_input.grid(column=1,row=1)
        answer = Button(root1, text = "Answer" , font=  sub_font, bg = "dark blue", fg ="white", command = lambda: self.check_ans())
        answer.grid(column =2, row =  1)

        destroy = Button(root1, text ="Back", font = (sub_font ), bg ="dark blue", fg =     "white" ,  command  = lambda: root1.destroy())
        destroy.grid(column = 1, row= 2)
    def scienceTwo(self):
        root1 = Tk()
        root1.config(background="dark blue")

        self.q_number = ['s',2]
        
        question = Label(root1,text=science_q[1],font=(None,30),bg="dark blue",fg="white")
        question.grid(column=0,row=0)

        label = Label(root1, text = "Answer:  ", font = (sub_font), bg="dark blue",fg="white")
        label.grid(column = 0, row =1)
        
        self.a_input = Entry(root1,font=sub_font )
        self.a_input.grid(column=1,row=1)
        answer = Button(root1, text = "Answer" , font=  sub_font, bg = "dark blue", fg ="white", command = lambda: self.check_ans())
        answer.grid(column =2, row =  1)

        destroy = Button(root1, text ="Back", font = (sub_font ), bg ="dark blue", fg =     "white" ,  command  = lambda: root1.destroy())
        destroy.grid(column = 1, row= 2)
    def scienceThree(self):
        root1 = Tk()
        root1.config(background="dark blue")

        self.q_number = ['s',3]
        
        question = Label(root1,text=science_q[2],font=(None,30),bg="dark blue",fg="white")
        question.grid(column=0,row=0)

        label = Label(root1, text = "Answer:  ", font = (sub_font), bg="dark blue",fg="white")
        label.grid(column = 0, row =1)
        
        self.a_input = Entry(root1,font=sub_font )
        self.a_input.grid(column=1,row=1)
        answer = Button(root1, text = "Answer" , font=  sub_font, bg = "dark blue", fg ="white", command = lambda: self.check_ans())
        answer.grid(column =2, row =  1)

        destroy = Button(root1, text ="Back", font = (sub_font ), bg ="dark blue", fg =     "white" ,  command  = lambda: root1.destroy())
        destroy.grid(column = 1, row= 2)
    def scienceFour(self):
        root1 = Tk()
        root1.config(background="dark blue")

        self.q_number = ['s',     4]
        
        question = Label(root1,text=science_q[3],font=(None,30),bg="dark blue",fg="white")
        question.grid(column=0,row=0)

        label = Label(root1, text = "Answer:  ", font = (sub_font), bg="dark blue",fg="white")
        label.grid(column = 0, row =1)
        
        self.a_input = Entry(root1,font=sub_font )
        self.a_input.grid(column=1,row=1)
        answer = Button(root1, text = "Answer" , font=  sub_font, bg = "dark blue", fg ="white", command = lambda: self.check_ans())
        answer.grid(column =2, row =  1)
            
        destroy = Button(root1, text ="Back", font = (sub_font ), bg ="dark blue", fg =     "white" ,  command  = lambda: root1.destroy())
        destroy.grid(column = 1, row= 2)

    def csOne(self):
        root1 = Tk()
        root1.config(background="dark blue")

        self.q_number = ['cs',1]
        
        question = Label(root1,text=cs_q[0],font=(None,30),bg="dark blue",fg="white")
        question.grid(column=0,row=0)

        label = Label(root1, text = "Answer:  ", font = (sub_font), bg="dark blue",fg="white")
        label.grid(column = 0, row =1)
        
        self.a_input = Entry(root1,font=sub_font )
        self.a_input.grid(column=1,row=1)
        answer = Button(root1, text = "Answer" , font=  sub_font, bg = "dark blue", fg ="white", command = lambda: self.check_ans())
        answer.grid(column =2, row =  1)

        destroy = Button(root1, text ="Back", font = (sub_font ), bg ="dark blue", fg =     "white" ,  command  = lambda: root1.destroy())
        destroy.grid(column = 1, row= 2)
    def CSTwo(self):
        root1 = Tk()
        root1.config(background="dark blue")

        self.q_number = ['cs',2]
        
        question = Label(root1,text=cs_q[1],font=(None,30),bg="dark blue",fg="white")
        question.grid(column=0,row=0)

        label = Label(root1, text = "Answer:  ", font = (sub_font), bg="dark blue",fg="white")
        label.grid(column = 0, row =1)
        
        self.a_input = Entry(root1,font=sub_font )
        self.a_input.grid(column=1,row=1)
        answer = Button(root1, text = "Answer" , font=  sub_font, bg = "dark blue", fg ="white", command = lambda: self.check_ans())
        answer.grid(column =2, row =  1)

        destroy = Button(root1, text ="Back", font = (sub_font ), bg ="dark blue", fg =     "white" ,  command  = lambda: root1.destroy())
        destroy.grid(column = 1, row= 2)
    def csThree(self):
        root1 = Tk()
        root1.config(background="dark blue")

        self.q_number = ['cs',3]
        
        question = Label(root1,text=cs_q[2],font=(None,30),bg="dark blue",fg="white")
        question.grid(column=0,row=0)

        label = Label(root1, text = "Answer:  ", font = (sub_font), bg="dark blue",fg="white")
        label.grid(column = 0, row =1)
        
        self.a_input = Entry(root1,font=sub_font )
        self.a_input.grid(column=1,row=1)
        answer = Button(root1, text = "Answer" , font=  sub_font, bg = "dark blue", fg ="white", command = lambda: self.check_ans())
        answer.grid(column =2, row =  1)

        destroy = Button(root1, text ="Back", font = (sub_font ), bg ="dark blue", fg =     "white" ,  command  = lambda: root1.destroy())
        destroy.grid(column = 1, row= 2)
    def csFour(self):
        root1 = Tk()
        root1.config(background="dark blue")

        self.q_number = ['cs',4]
        
        question = Label(root1,text=cs_q[3],font=(None,30),bg="dark blue",fg="white")
        question.grid(column=0,row=0)

        label = Label(root1, text = "Answer:  ", font = (sub_font), bg="dark blue",fg="white")
        label.grid(column = 0, row =1)
        
        self.a_input = Entry(root1,font=sub_font )
        self.a_input.grid(column=1,row=1)
        answer = Button(root1, text = "Answer" , font=  sub_font, bg = "dark blue", fg ="white", command = lambda: self.check_ans())
        answer.grid(column =2, row =  1)

        destroy = Button(root1, text ="Back", font = (sub_font ), bg ="dark blue", fg =     "white" ,  command  = lambda: root1.destroy())
        destroy.grid(column = 1, row= 2)
        
    

    def check_ans(self):
        if self.q_number[0] == 'm':
            if str(self.a_input.get()) ==math_a[self.q_number[1]-1]:
                self.correct()
            else:
                self.Wrong()
        elif self.q_number[0] == 'e':
            if self.a_input.get() ==english_a[self.q_number[1]-1]:
                self.correct()
            else:
                self.Wrong()
        elif self.q_number[0] == 's':
            if self.a_input.get() ==science_a[self.q_number[1]-1]:
                self.correct()
            else:
                self.Wrong()
        elif self.q_number[0] == 'cs':
            if self.a_input.get() ==cs_a[self.q_number[1]-1]:
                self.correct()
            else:
                self.Wrong() 
    def correct(self):
        
        root1= Tk()
        Answer=Label(root1,text="You got it right!",font=(None,30),bg="dark blue",fg="white")
        Answer.pack()



        destroy = Button(root1, text ="Back", font = (sub_font ), bg ="dark blue", fg =     "white", command = lambda: root1.destroy())
        destroy.pack()
    def Wrong(self):
        
        root1= Tk()
        Answer=Label(root1,text="You got it wrong :(! ",font=(None,30),bg="dark blue",fg="white")
        Answer.pack()

        destroy = Button(root1, text ="Back", font = (sub_font ), bg ="dark blue", fg =     "white" ,  command  = lambda: root1.destroy())
        destroy.pack()



app = main()
app.geometry ("500x400")
app.mainloop()

