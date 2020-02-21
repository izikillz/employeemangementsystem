import csv
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
'''This is a employee gui  wehre i can add,delete,see help and show single employee or search all employee.
I have also have added error handling in this where it shows error if something is not according to the code'''

class employee_gui :


    def __init__(self , master):

        self.master = master

        #configuring the title of the main window , aswell as the background color
        master.title(string = 'Softwarica Employee Management System')
        master.configure(background = 'black')

        #employee first name
        self.firstname_label = Label(master, text = 'Employee First Name *' ,bg= 'black', fg ='white')
        self.firstname_label.grid(row = 1 , column = 0 , sticky ='we', padx=5, pady=5)



        self.first_name = ttk.Entry(master)
        self.first_name.grid(row = 2 ,column  = 0 , sticky = 'we',padx=5, pady=5 )

        #employee lastname
        self.lastname_label = Label(master, text = 'Employee last Name *',bg= 'black', fg ='white')
        self.lastname_label.grid(row = 1 , column = 1 , sticky ='we',padx=5, pady=5)


        self.last_name = ttk.Entry(master)
        self.last_name.grid(row = 2 ,column  = 1 , sticky = 'we',padx=2, pady=2)

        #employee email 
        self.employee_email = Label(master, text = 'Employee Email *',bg= 'black', fg ='white')
        self.employee_email.grid(row = 3 , column  = 0 , columnspan = 2 , sticky = 'we')

        self.employee_email_entry = ttk.Entry(master)
        self.employee_email_entry.grid(row = 4  , column = 0 , columnspan = 3 , sticky = 'we', padx=5, pady=5)







                                                                   #day
        self.DAY= Label(master, text = 'Day*',bg= 'black', fg ='white')
        self.DAY.grid(row = 5 , column = 0 , sticky = 'we',padx=5, pady=5)
        #day options
        self.dayoptions = ['1','2' , '3' , '4' , '5' , '6' , '7' , '8' , '9', '10' , '11' , '12' , '13' , '14' , '15' , '16' , '17' , '18' , '19', '20' , '21' , '22' , '23' , '24' , '25' , '26' , '27' , '28' , '29' , '30' , '31']
        #day container
        self.dayvar= StringVar()
        self.dayvar.set('none')
        #day option menu
        self.dropdown_day = ttk.OptionMenu(master,self.dayvar , *self.dayoptions)
        self.dropdown_day.grid(row = 6 , column = 0 , sticky= 'we')



                                                                     #month    
        self.month= Label(master, text = 'month*',bg= 'black', fg ='white')
        self.month.grid(row = 5 , column = 1 , sticky = 'we',padx=5, pady=5)
        #month options
        self.monthoptions = ['1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , '10' , '11' , '12']

        #month container
        self.monthvar = StringVar()
        self.monthvar.set('select')

        #MONTH DROPDOWN MENU
        self.dropdown_month = ttk.OptionMenu(master, self.monthvar , *self.monthoptions)
        self.dropdown_month.grid(row = 6 , column = 1 , sticky = 'we',padx=5, pady=5)


                                                                         # year



        #year options
        self.years_unsplit       =  '2029 - 2028 - 2027 - 2026 - 2025 - 2024 - 2023 - 2022 - 2021 -2020 - 2019 - 2018 - 2017 - 2016 - 2015 - 2014 - 2013 - 2012 - 2011 -2010 - 2009 - 2008 - 2007 - 2006 - 2005 - 2004 - 2003 - 2002 - 2001 -2000 - 1999 - 1998 - 1997 - 1996 - 1995 - 1994 - 1993 - 1992 - 1991 - 1990 - 1989 - 1988 - 1987 - 1986 - 1985 - 1984 - 1983 - 1982 - 1981 -1980 - 1979 - 1978 - 1977 - 1976 - 1975 - 1974 - 1973 - 1972 - 1971 -1970 - 1969 - 1968 - 1967 - 1966 - 1965 - 1964 - 1963 - 1962 - 1961 -1960 - 1959 - 1958 - 1957 - 1956 - 1955 - 1954 - 1953 - 1952 - 1951 -1950 - 1949 - 1948 - 1947 - 1946 - 1945 - 1944 - 1943 - 1942 - 1941 -1940 - 1939 - 1938 - 1937 - 1936 - 1935 - 1934 - 1933 - 1932 - 1931 -1930 - 1929 - 1928 - 1927 - 1926 - 1925 - 1924 - 1923 - 1922 - 1921'

        self.yearoptions2 = self.years_unsplit.split('-')
        #year variable
        self.yearvar = StringVar()                                                                                                                                                                                                                                                                                                                                                                                                  

        self.dropdown_year = ttk.OptionMenu(master , self.yearvar , *self.yearoptions2)
        self.dropdown_year.grid(row = 6 ,column = 2 , sticky = 'we')

        self.year = Label(master, text = 'Year*' ,bg= 'black', fg ='white')
        self.year.grid(row = 5 , column = 2, sticky = 'we', padx=5, pady=5)





        #the address section
        self.Address = Label(master ,text = 'Address',bg= 'black', fg ='white')
        self.Address.grid(row = 7 , column = 0 ,sticky = 'we',padx=5, pady=5)
        self.Address_entry = ttk.Entry(master)
        self.Address_entry.grid(row = 8 , column = 0 , columnspan = 3, sticky = 'we',padx=5, pady=5)    


        #the position_ occupation section
        self.Position = Label(master , text= 'Position/Occupation*' , bg= 'black', fg ='white')
        self.Position.grid(row = 9 , column = 0 , sticky = 'we',padx=5, pady=5)
        self.Position_entry = ttk.Entry(master)
        self.Position_entry.grid(row = 10 , column = 0 ,columnspan = 3, sticky = 'we',padx=5, pady=5)


        #the worked section
        self.workez = Label(master , text = 'Worked Department*',bg= 'black', fg ='white')
        self.workez.grid(row = 11 , column = 0 , sticky = 'we',padx=5, pady=5)

        self.workez_entry = ttk.Entry(master)
        self.workez_entry.grid(row = 12 , column = 0 , sticky = 'we',padx=5, pady=5)

        #the employee id informaiton


        self.employee_id_label = Label(master, text = 'Employee Id *',bg= 'black', fg ='white')
        self.employee_id_label.grid(row = 13 , column = 0 , sticky = 'we',padx=5, pady=5)

        self.employee_id_entry = ttk.Entry(master)
        self.employee_id_entry.grid(row = 14 , column = 0 , sticky = 'we' ,padx=5, pady=5 )


        #the main menu bar

        self.titlebaroptions = Menu(master)
        #the file section in the menu bar
        self.filesystem = Menu(master,tearoff=False)
        self.filesystem.add_command(label = 'Display Employee Information'  , command =self.display_information_window)
        self.savesystem = Menu(master,tearoff=False)
        self.savesystem.add_command(label= 'Save Employee File' , command= self.save_information_window)
        self.deletesystem =Menu(master,tearoff=False)
        self.deletesystem.add_command(label = 'Delete Employee' , command = self.delete_information_window)
        self.help = Menu(master, tearoff = False)
        self.help.add_command(label= 'Help' , command = self.help_window)
        #adding the sections  to the main menu bar
        self.titlebaroptions.add_cascade(label = 'Open' , menu = self.filesystem)
        self.titlebaroptions.add_cascade(label = 'Save' , menu = self.savesystem)
        self.titlebaroptions.add_cascade(label = 'Remove Employee' , menu =self.deletesystem)
        self.titlebaroptions.add_cascade(label = 'Help' ,  menu = self.help)


        # adding main menu to the master window
        master.config(menu = self.titlebaroptions)
    def save_information_window(self):
        global csvwriter
        #grabbing all the information from our entrys
        first_info = self.first_name.get()
        last_info = self.last_name.get()
        email_info = self.employee_email_entry.get()
        day_info = self.dayvar.get()
        month_info = self.monthvar.get()
        year_info = self.yearvar.get()
        position_info = self.Position_entry.get()
        employee_workez_info = self.workez_entry.get()
        employee_id_info = self.employee_id_entry.get()
        adress_info = self.Address_entry.get()
#if no information error
        if not first_info or not last_info or not email_info or not day_info or not \
        month_info or not year_info or not position_info or not \
            employee_id_info or not employee_workez_info or not adress_info:
            messagebox.showinfo("Error","fill all the entries:")
        else:
            #putting our information into a list of strings , 
            fieldnames_list = ['first name' , 'last name' , 'email' , 'DOB' ,'adress' ,'position' , 'worked department' , 'employee id'  ]
            whole_information = [str(first_info) , str(last_info) , str(email_info) , str(month_info + '-' +day_info +'-' + year_info ) ,str(adress_info),  str(position_info) , str(employee_workez_info) , str(employee_id_info) ]
            #creating our dictonary , using the fieldnames as the key and the whole information as the value of the dictionary
            my_whole_info_dict = dict(zip(fieldnames_list , whole_information))

            #opening our csv file in write mode and adding the data from the entrys



            with open('employees.csv', 'a' ,newline = "") as employee_file:
                            csvwriter = csv.DictWriter(employee_file, fieldnames = fieldnames_list , delimiter = ',')



                            csvwriter.writeheader()



                            csvwriter.writerow(my_whole_info_dict)




        

    def delete_information_method(self):
        #a tkinter entry
        global delete_entry, csv_writer1
        #opening csv in read
        with open('employees.csv' , 'r', newline='') as emp_read:
            #creating our dictreader
            csv_dictreader = csv.DictReader(emp_read)
            fieldnames = csv_dictreader.fieldnames
            contents = [line for line in csv_dictreader]
        #opening csv file in write mode
        if not delete_entry.get():
                    message = messagebox.showerror("Failed",'FIELD IS REQUIRED')
        else:
            with open ('employees.csv' , 'w', newline='') as emp_write:
                #creating our writer
                csv_writer1 = csv.DictWriter(emp_write, fieldnames=fieldnames)
                csv_writer1.writeheader()
                #our loop to check each line inside of our csv file is not equal to what is inside the delete entry
                
                for line in contents:
                

                    if line['employee id'] != str(delete_entry.get()):
                        csv_writer1.writerow(line)
            
                message = messagebox.showinfo("Deleted",'The employee has benn deleted')
        

        #grabbing all the employee data and inserting it inside of the listbox
    def all_emp_search(self):
        global information_box
        #deleting data out of the listbox , that was previously there
        information_box.delete(0 , 'end')
        #our read file
        with open ('employees.csv' , 'r') as employee_read_file:
            #inserting all information inside of the csv file into the listbox
            for line in employee_read_file:
                information_box.insert(END , line)
        #grabbing a single employee data and inserting it inside the listbox
    def single_emp_search(self):

        global search_label_entry,information_box
        #deleting data out of the listbox , that was previously there
        information_box.delete(0 , END)
        #our read file
        with open ('employees.csv' , 'r') as employee_read_file:
            #searching to see if the contents of the csv file matches what is put inside of the entry and if so inserting the line into the listbox
            for line in employee_read_file:
                if line.find(str(search_label_entry.get())) > -1:
                    information_box.insert(END , line)



        #the information deletion window 

    def delete_information_window(self):
        global delete_entry
        delete_frame = Toplevel()
        delete_frame.config(background = 'black')

        #intro label(title)
        delete_intro_header = Label(delete_frame , text = 'Welcome to the Delete section' , font = 'times 14 bold',bg= 'black', fg ='white')
        delete_intro_header.grid(row  = 2 , column = 0 , sticky = 'we')

        #The entry label/header
        delete_entry_header = Message(delete_frame , text = 'Enter in the employee ID , you would like to remove , if you dont recall , you can access the employee information , by going to Mainpage/Open/Display Employee Information, here you can search for an employee name , and all the information including the ID will be present',bg= 'black', fg ='white')
        delete_entry_header.grid(row = 3, column = 0 , sticky= 'we')


        # delete entry
        delete_note_header = Label(delete_frame , text = 'Note: Once You Delete An Employee There is no recovery , be careful with this process',bg= 'black', fg ='white')
        delete_note_header.grid(row = 4, column = 0 , sticky = 'we')

        delete_entry = ttk.Entry(delete_frame )
        delete_entry.grid(row = 5, column = 0 , sticky  = 'we')
        
        #the delete button(submit button)
        delete_button = Button(delete_frame , text = 'Delete Employee' ,  fg = 'white', bg = 'black',command = self.delete_information_method)
        delete_button.grid(row = 5 , column = 1, sticky = 'we')













    #the information display window

    def display_information_window(self):
        global search_label_entry,information_box
        display_frame = Toplevel()
        display_frame.config(background = 'black')

        #the intro message(title)
        intro_message = Label(display_frame, text = 'Welcome to the Display section' , font = 'times 14 bold',bg= 'black', fg ='white')

        #the header for the search_label_entry
        search_label = Label(display_frame , text = 'Search for one Employee information',bg= 'black', fg ='white')
        search_label.grid(row = 3 , column = 0 , sticky = 'we')
        #the search entry
        search_label_entry = ttk.Entry(display_frame)
        search_label_entry.grid(row = 4, column = 0 , sticky = 'we')



        all_information_label = Label(display_frame , text = 'All employee information',bg= 'black', fg ='white')
        all_information_label.grid(row = 3 , column =2 , sticky = 'we')

        #our listbox
        information_box = Listbox(display_frame, bd = 0 , width = 70)
        information_box.grid(row  = 6 , column = 0, sticky= 'we')
        #all information button
        all_information_button = Button(display_frame , text = 'All Information',bg = 'black' , fg = 'white',  command = self.all_emp_search)
        all_information_button.grid(row = 4 , column = 2 , sticky = 'we')
        #emp single search Button
        search_single_emp = Button(display_frame , text  = 'Search Single Employee', command  = self.single_emp_search,bg = 'black' , fg = 'white' )

        search_single_emp.grid(row = 5 , column = 2 , sticky = 'we')







    #help window
    def help_window(self):
        help_frame = Toplevel()

        intro_message = Label(help_frame, text = 'Welcome to the help section of Softwarica employee management system' , font = 'times 14 bold')
        intro_message.grid(row = 3  , column = 0 , sticky = 'we')

        mainmessage = Message(help_frame, text = 'This program allows you to  store your employee information , you can add all the information and acess it later on')
        mainmessage.grid(row = 4 , column = 0 , sticky  ='we')

        help_frame.iconbitmap('employeeicon.ico')



    #saving the information to the csv file method
        
