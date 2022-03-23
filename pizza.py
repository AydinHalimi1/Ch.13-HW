#Design a creative UI using Python's tkinter module to calculate the total cost of a pizza. The UI should have (at least) each widget that was covered in class:

#Frames
#Labels
#input box
#buttons
#radio buttons
#check boxes
#You can use check boxes for for selecting toppings (each with a different cost), 
# radio buttons for the type of crust selected (each with a different cost), buttons for calculation and quit. 
# The input box can be used to record the name of the person placing the order. 
# Use a message box to display the total cost of the pizza along with the name of the person placing the order.

#Make sure your design is well laid out and intuitive to the user. Take account of spacing and packing so that everything is properly aligned and professional looking. Be creative with font, color, size, etc.

import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry('300x400')
        self.main_window.configure(bg='red')
        self.main_window.title('Grimaldi')

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.first_frame = tkinter.Frame(self.main_window)
        self.second_frame = tkinter.Frame(self.main_window)
        self.third_frame = tkinter.Frame(self.main_window)
        self.output_frame = tkinter.Frame(self.main_window)
        self.last_frame = tkinter.Frame(self.main_window)

        #Create three IntVar Objects to use with the CheckButtons

        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()

        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)

        self.cb1 = tkinter.Checkbutton(self.top_frame,text='Pepperoni',variable=self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.top_frame,text='Sausage',variable=self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.top_frame,text='Chicken',variable=self.cb_var3)

        #Pack the CheckButtons
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()


        self.radio_var = tkinter.IntVar()
        self.rb1 = tkinter.Radiobutton(self.third_frame,text='8 in.',variable=self.radio_var, value = 10)
        self.rb2 = tkinter.Radiobutton(self.third_frame,text='12 in.',variable=self.radio_var, value = 20)
        self.rb3 = tkinter.Radiobutton(self.third_frame,text='16 in.',variable=self.radio_var, value = 30)


        self.name = tkinter.Label(self.bottom_frame,text='Grimaldi' + '\n' + 'First and Last Name:',font=('Broadway',18))
        self.topping = tkinter.Label(self.first_frame,text='Toppings:',font=('Broadway',18))
        self.crust = tkinter.Label(self.second_frame,text='Crust Size:',font=('Broadway',18))

        self.input_name = tkinter.Entry(self.bottom_frame,width=15)

        self.mybutton1 = tkinter.Button(self.main_window,text='Total',font=('Broadway',15),command=self.do_something)
        self.quit_button = tkinter.Button(self.main_window,text='Quit',font=('Broadway',15),command=self.main_window.destroy)

        self.bottom_frame.pack(side='top')
        self.first_frame.pack(side='top')
        self.top_frame.pack(side='top')

        self.second_frame.pack(side='top')

        self.output_frame.pack(side='top')

        self.third_frame.pack(side='top')

        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        self.last_frame.pack(side='bottom')

        self.name.pack(side='top')
        self.topping.pack(side='top')
        self.crust.pack(side='top')

        self.quit_button.pack(side='bottom')
        self.mybutton1.pack(side='bottom')
        self.input_name.pack(side='top')


        tkinter.mainloop()

    def do_something(self):
        self.message = self.input_name.get() + '\n' + 'Your total is: '

        cost = 0

        if self.cb_var1.get() == 1:
            cost += 3
        if self.cb_var2.get() == 1:
            cost += 1.50
        if self.cb_var3.get() == 1:
            cost += 2.25
        
        if self.radio_var.get() == 10:
            cost += 9
        if self.radio_var.get() == 20:
            cost += 13
        if self.radio_var.get() == 30:
            cost += 16

        tkinter.messagebox.showinfo('Response',self.message + '${:,.2f}'.format(cost))

my_gui = MyGUI()

