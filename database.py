from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox
root = Tk()
root.title('JKUAT Database')
#creating the tree widgets

#creating the columns
columns = ('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#10')
tree = ttk.Treeview(root, columns=columns, show='headings', height=20)
# creating the headings for the treeview
tree.heading('#1', text='Reg No')
tree.heading('#2', text='First Name')
tree.heading('#3', text='Middle Name')
tree.heading('#4', text='Last Name')
tree.heading('#5', text='College')
tree.heading('#6', text='School')
tree.heading('#7', text='Department')
tree.heading('#8', text='Course')
tree.heading('#9', text='Year')
tree.heading('#10', text='Gender')

# making the stripped rows using tag_configure that creates tags for the odd and even rows
tree.tag_configure('oddrow', background='#8FBC8F')
tree.tag_configure('evenrow', background='#2F4F4F')

tree.grid(column=0, row=0, columnspan=15)

#formatting the treeview widget by configuring the colors for different parts of the treeview
style = ttk.Style()
style.theme_use('default')
style.configure("Treeview", background='silver', foreground='#000000', rowheight=25, fieldbackground='#000000')
style.map('Treeview', background=[('selected', 'blue')])

#positioning data in the treeview
tree.column('#1', anchor=CENTER, width=160, minwidth=20)
tree.column('#2', anchor=CENTER, width=120, minwidth=20)
tree.column('#3', anchor=CENTER, width=120, minwidth=20)
tree.column('#4', anchor=CENTER, width=120, minwidth=20)
tree.column('#5', anchor=CENTER, width=120, minwidth=20)
tree.column('#6', anchor=CENTER, width=190, minwidth=20)
tree.column('#7', anchor=CENTER, width=190, minwidth=20)
tree.column('#8', anchor=CENTER, width=190, minwidth=20)
tree.column('#9', anchor=CENTER, width=70, minwidth=20)
tree.column('#10', anchor=CENTER, width=80, minwidth=20)
#creating the y and x scroll bars
# y scroll bar
y_scrollbar = ttk.Scrollbar(root, orient=VERTICAL, command=tree.yview)
tree.configure(yscrollcommand=y_scrollbar.set)
y_scrollbar.grid(row=0, column=15, sticky='ns')

# x scroll bar
x_scrollbar = ttk.Scrollbar(root, orient=HORIZONTAL, command=tree.xview)
tree.config(xscrollcommand=x_scrollbar.set)
x_scrollbar.grid(row=1, column=0, sticky='we', columnspan=15)

tree.columnconfigure(0, weight=1)
tree.columnconfigure(1, weight=1)
tree.columnconfigure(2, weight=1)
tree.columnconfigure(3, weight=1)
tree.columnconfigure(4, weight=1)
tree.columnconfigure(5, weight=1)
tree.columnconfigure(6, weight=1)
tree.columnconfigure(7, weight=1)
tree.columnconfigure(8, weight=1)
tree.columnconfigure(9, weight=1)
tree.columnconfigure(10, weight=1)

tree.rowconfigure(0, weight=1)
tree.rowconfigure(2, weight=1)
tree.rowconfigure(3, weight=1)
tree.rowconfigure(4, weight=1)
tree.rowconfigure(5, weight=1)
tree.rowconfigure(6, weight=1)
tree.rowconfigure(7, weight=1)
tree.rowconfigure(8, weight=1)
tree.rowconfigure(9, weight=1)
# changing the background window color
root.configure(background='#2F4F4F')

#function that is called whenever any row is selected
def selection(e):
    data_list=tree.item(tree.selection())['values']
    #clearing the previous data in the entry boxes
    reg_entry.delete(0, END)
    fname_entry.delete(0, END)
    mname_entry.delete(0, END)
    lname_entry.delete(0, END)
    college_entry.delete(0, END)
    schl_entry.delete(0, END)
    dpt_entry.delete(0, END)
    crse_entry.delete(0, END)
    year_entry.delete(0, END)
    gender_entry.delete(0, END)

    #inserting the new data
    reg_entry.insert(END, data_list[0])
    fname_entry.insert(END, data_list[1])
    mname_entry.insert(END, data_list[2])
    lname_entry.insert(END, data_list[3])
    college_entry.insert(END, data_list[4])
    schl_entry.insert(END, data_list[5])
    dpt_entry.insert(END, data_list[6])
    crse_entry.insert(END, data_list[7])
    year_entry.insert(END, data_list[8])
    gender_entry.insert(END, data_list[9])

# binding the selection function with the selection event
tree.bind('<<TreeviewSelect>>', selection)

#creating labels for data entry
label_bg = '#2F4F4F'
reg_label = Label(root, text='Reg No', font=('Helvetica', 13), background=label_bg)
reg_label.grid(row=2, column=0, pady=5, padx=5)
fname_label = Label(root, text='First Name:', font=('Helvetica', 13), background=label_bg)
fname_label.grid(row=2, column=2, pady=5, padx=5)
mname_label = Label(root, text='Middle name:', font=('Helvetica', 13), background=label_bg)
mname_label.grid(row=3, column=0, pady=5, padx=5)
lname_label = Label(root, text='Last Name:', font=('Helvetica', 13), background=label_bg)
lname_label.grid(row=3, column=2, pady=5, padx=5)
college_label = Label(root, text='College:', font=('Helvetica', 13), background=label_bg)
college_label.grid(row=4, column=0, pady=5, padx=5)
schl_label = Label(root, text='School:', font=('Helvetica', 13), background=label_bg)
schl_label.grid(row=4, column=2, pady=5, padx=5)
dprt_label = Label(root, text='Department:', font=('Helvetica', 13), background=label_bg)
dprt_label.grid(row=5, column=0, pady=5, padx=5)
crse_label = Label(root, text='Course', font=('Helvetica', 13), background=label_bg)
crse_label.grid(row=5, column=2, pady=5, padx=5)
year_label = Label(root, text='Year of Study', font=('Helvetica', 13), background=label_bg)
year_label.grid(row=2, column=4, padx=5, pady=5)
gender_label = Label(root, text='Gender: ', font=('Helvetica', 13), background=label_bg)
gender_label.grid(row=3, column=4)

#creating entry widgets for data capturing
entry_bg = 'silver'
reg_entry = Entry(root, width=20, font=('Helvetlica', 13), borderwidth=2)
reg_entry.grid(row=2, column=1, pady=5, padx=5)
fname_entry = Entry(root, width=20, font=('Helvetlica', 13), borderwidth=2)
fname_entry.grid(row=2, column=3, pady=5, padx=5)
mname_entry = Entry(root, width=20, font=('Helvetlica', 13), borderwidth=2)
mname_entry.grid(row=3, column=1, pady=5, padx=5)
lname_entry = Entry(root, width=20, font=('Helvetlica', 13), borderwidth=2)
lname_entry.grid(row=3, column=3, pady=5, padx=5)

#creating functions that will be used to narrow down lists into the specific categories
#creaing the school function
def school(clge_entry, s_entry, schl_list, event=None):
    if clge_entry.get()=='COPAS':
        schl_list=['SPS', 'SCIT', 'SMS', 'SBS']
    elif clge_entry.get()=='COETEC':
        schl_list=['SoMMME', 'SABS', 'SEEIE', 'SCEGE', 'SoBEE']
    elif clge_entry.get()=='COANRE':
        schl_list=['SOAES', 'SONRAS', 'SOFNUS']
    elif clge_entry.get()=='COHRED':
        schl_list=['School of Business', 'School of Entreprenuership, Procurement and Management', 'School of Communication and Development Studies']
    elif clge_entry.get()=='COHES':
        schl_list=['School of Nursing', 'School of Medicine', 'School of Pharmacy', 'School of Public Health', 'School of Biomedical Sciences']
    s_entry.delete(0, END)
    s_entry.config(value=schl_list)
 
def department(s_entry, d_entry, d_list, event=None):
    if s_entry.get()=='SPS':
        d_list = ['Physics', 'Chemistry']
    elif s_entry.get()=='SCIT':
        d_list = ['Computing', 'IT']
    elif s_entry.get()=='SMS':
        d_list = ['Dept.of Statistics and Actuarial Sciences', 'PAM']
    elif s_entry.get()=='SBS':
        d_list = ['Botany', 'Zoology']
    elif s_entry.get()=='SoMME':
        d_list = ['Mechatronic Engineering', 'Mechanical Engineering', 'Marine Engineering and Maritime Operations', 'Mining and mineral Processing Engineering']
    elif s_entry.get()=='SCEGE':
        d_list = ['Geomatic Engineering and Geospatial Information Systems', 'Civil Construction and Evironmental Engineering', 'SMARTEC']
    elif s_entry.get()=='SEEIE':
        d_list = ['Electrical and Electronic Engineering', 'Telecommunication and Information Engineering']
    elif s_entry.get()=='SoBEE':
        d_list = ['Agriculture and Biosystems Engineering', 'Soil Water and Environmental Engineering']
    elif s_entry.get()=='SOAES':
        d_list = ['Landscape and Environmental Sciences', 'Horticulture and Food Security', 'Agriculture and Resource Economics']
    elif s_entry.get()=='SONRAS':
        d_list = ['Animal Sciences', 'Land Resource Planning and Management']
    elif s_entry.get()=='SOFNUS':
        d_list = ['Human Nutrition Sciences', 'Food Science and Technology']
    elif s_entry.get()=='School of Business':
        d_list = ['Business Administration', 'Economics, Accounting and Finance']
    elif s_entry.get()=='School of Entreprenuership, Procurement and Management':
        d_list = ['Entreprenuership Technology Leadership Management', 'Procurement and Logistics']
    elif s_entry.get()=='School of Communication and Development Studies':
        d_list = ['Development Studies', 'Media Technology and Applied Communication', 'Centre of Foreign Language and Linguistics']
    elif s_entry.get()=='School of Nursing':
        d_list = ['Nursing']
    elif s_entry.get()=='School of Medicine':
        d_list = ['Dept.of Physiotherapy', 'Dept.of Clinical Medicine', 'Bachelor of Medicine and Bachelor of Surgery']
    elif s_entry.get()=='School of Pharmacy':
        d_list = ['Dept.of Pharmacy']
    elif s_entry.get()=='Schoool of Public Health':
        d_list = ['Dept.of Public Health']
    elif s_entry.get()=='School of Biomedical Sciences':
        d_list = ['Dept.of Biochemistry', 'Dept.of Medical Microbiology', 'Dept.of Medical Laboratory Sciences']
    d_entry.delete(0, END)
    d_entry.config(value=d_list)

def crse(d_entry, c_entry, c_list, event=None):
    if d_entry.get() == 'Physics':
        c_list = ['Control and Instrumentation', 'Geophysics', 'Renewable Energy and Environmental Physics']
    elif d_entry.get() == 'Chemistry':
        c_list = ['Bsc Chemistry', 'Bsc Analytical Chemistry', 'Bsc Industrial Chemistry']
    elif d_entry.get() == 'Computing':
        c_list = ['Bsc Computer science', 'BSc Computer Technology']
    elif d_entry.get() == 'IT':
        c_list = ['Bsc Information Technology']
    elif d_entry.get() == 'Dept.of Statistics and Actuarial Sciences':
        c_list = ['Bsc in Actuarial Sciences', 'Bsc in Financial Engineering', 'Bsc in Biostatistics', 'Bsc in Statistics', 'Ms Statistics', 'Ms Applied statistics']
    elif d_entry.get() == 'PAM':
        c_list = ['Bsc in Mathematics', 'Bachelor of Science(General)', 'Bsc Mathematics and Computer Science', 'Bsc Industrial Mathematics', 'Ms in Pure Mathematics', 'Ms in Applied Mathematics', 'Diploma in Pure Mathematic', 'Diploma in Mathematics', 'Phd Pure Mathematics', 'Phd Applied Mathematics']
    elif d_entry.get() == 'Zoology':
        c_list = ['Zoology', 'Applied Biology', 'Environmental Science']
    elif d_entry.get() == 'Botany':
        c_list = ['Bsc Microbiology', 'Bsc Biotechnology', '']
    elif d_entry.get() == 'Mechatronic Engineering':
        c_list = ['Bsc Mechatronic Engineering']
    elif d_entry.get() == 'Mechanical Engineering':
        c_list = ['Bsc Mechanical Engineering']
    elif d_entry.get() == 'Mechanical Engineering' :
        c_list = ['Bsc Mechanical Engineering']
    elif d_entry.get() == 'Marine Engineering and Maritime Operations':
        c_list = ['Bsc Marine Engineering and Maritime Operations']
    elif d_entry.get() == 'Mining and mineral Processing Engineering':
        c_list = ['Bsc Mining and mineral Processing Engineering']
    elif d_entry.get() == 'Geomatic Engineering and Geospatial Information Systems':
        c_list = ['Bsc Geomatic Engineering and Geospatial Information Systems']
    elif d_entry.get() == 'Civil Construction and Evironmental Engineering':
        c_list = ['Bsc Civil Engineering']
    elif d_entry.get() == 'SMARTEC':
        c_list = ['MSc. in Construction Engineering and Management', '']
    elif d_entry.get() == 'Electrical and Electronic Engineering':
        c_list = ['Bsc Electrical and Electronic Engineering']
    elif d_entry.get() == 'Telecommunication and Information Engineering':
        c_list = ['Bsc Telecommunication and Information Engineering']
    elif d_entry.get() == 'Agriculture and Biosystems Engineering':
        c_list = ['Bsc Agriculture and Biosysytems Engineering', 'Bsc Energy and Environmental Technology', 'Msc Agriculture and Processing Engineering']
    elif d_entry.get() == 'Soil Water and Environmental Engineering':
        c_list = ['Bsc Water and Environmental Management', 'Msc Water and soil Engineering', 'Msc Environmental Engineering and Management']
    elif d_entry.get() == 'Landscape and Environmental Sciences':
        c_list = ['Bsc Environmental Horticulture and Landscaping Technology']
    elif d_entry.get() == 'Horticulture and Food Security':
        c_list = ['Bsc Horticulture', 'Bsc Agriculture', 'Msc Plant Breeding', 'Bsc Environmental Horticulture', 'Msc Research Models']
    elif d_entry.get() == 'Agriculture and Resource Economics':
        c_list = ['Bsc Agriculture and Resource Economics']
    elif d_entry.get() == 'Animal Sciences':
        c_list = ['Bsc Animal Health and Production Processing']
    elif d_entry.get() == 'Land Resource Planning and Management':
        c_list = ['Bsc Land Resource Planning and Management']
    elif d_entry.get() == 'Human Nutrition Sciences':
        c_list = ['Bsc Human Nutrition and Dietetics', 'Bsc Food Science and Nutrition', 'Bsc Food service and Hospitality Management', 'Bsc Neutraceutical sciences', 'Msc Food Science and Nutrition']
    elif d_entry.get() == 'Food Science and Technology':
        c_list = ['Bsc Food Science and Technology']
    elif d_entry.get() == 'Business Administration':
        c_list = ['Bachelor of Commerce', 'Bachelor of Business Information Technology', '']
    elif d_entry.get() == 'Economics, Accounting and Finance':
        c_list = ['Bachelor of Science in Economics', 'Bachelor of science in Banking and Finance']
    elif d_entry.get() == 'Entreprenuership Technology Leadership Management':
        c_list = ['Bsc Entreprenuership Technology Leadership Management']
    elif d_entry.get() == 'Procurement and Logistics':
        c_list = ['Bsc Procurement and Logistics']
    elif d_entry.get() == 'Development Studies':
        c_list = ['Bsc Devlopment Studies']
    elif d_entry.get() == 'Media Technology and Applied Communication':
        c_list = ['Bachelor Mass Communication', 'Bachelor of Corporate Communication and Management', 'Bachelor of Journalism', 'Diploma in Mass communition', 'Diploma In Public Relations']
    elif d_entry.get() == 'Centre of Foreign Language and Linguistics':
        c_list = ['Certificate in Chinese Language', 'Certificate in Japanese Language']
    elif d_entry.get() == 'Nursing':
        c_list = ['Phd Nursing', 'Msc Nursing', 'Bsc Nursing']
    elif d_entry.get() == 'Dept.of Physiotherapy':
        c_list = ['Bsc Physiotherapy', 'Bsc Occupational Therapy']
    elif d_entry.get() == 'Dept.of Clinical Medicine':
        c_list = ['Bsc Clinical Medicine']
    elif d_entry.get() == 'Bachelor of Medicine and Bachelor of Surgery':
        c_list = ['Bachelor of Medicine and Surgery']
    elif d_entry.get() == 'Dept.of Pharmacy':
        c_list = ['Bsc Pharmacy']
    elif d_entry.get() == 'Dept.of Public Health':
        c_list = ['Bsc Public Health']
    elif d_entry.get() == 'Dept.of Biochemistry':
        c_list = ['BSc. in Biochemistry and Molecular Biology', 'BSc. in Biochemistry (Molecular Biology Option)', 'BSc in Medical Biochemistry', 'BSc. in Industrial Biotechnology', 'BSc in Applied Bioengineering']
    elif d_entry.get() == 'Dept.of Medical Microbiology':
        c_list = ['Msc INFECTIOUS DISEASES AND VACCINOLOGY', 'Msc MEDICAL MICROBIOLOGY', 'Msc MEDICAL VIROLOGY MEDICAL MYCOLOGY', 'Msc INFECTION BIOLOGY MEDICAL PARASITOLOGY']
    elif d_entry.get() == 'Dept.of Medical Laboratory Sciences':
        c_list = ['Bsc Medical Laboratory sciences', 'Bachelor of Radiography', 'Master of Medical Laborarory Sciences']
    c_entry.delete(0, END)
    c_entry.config(value = c_list)
# creating lists and variables for comboboxes for default data of the students
college_var = StringVar()
college_list = ['COPAS', 'COETEC', 'COANRE', 'COHRED', 'COHES']
schl_var = StringVar()
schl_list = []
dpt_var = StringVar()
dpt_list = []
crse_var = StringVar()
crse_list = ['Ian', 'Mark', 'Okeyo']
year_list = ['1st', '2nd', '4th', '5th', '6th', '7th']

#creating the comboboxes
college_entry = ttk.Combobox(root, value=college_list, width=21, font=('Helvetica', 14))
college_entry.grid(row=4, column=1, pady=5, padx=5)
college_entry.bind("<<ComboboxSelected>>", lambda event: school(college_entry, schl_entry, schl_list))
schl_entry = ttk.Combobox(root, value=schl_list, width=21, font=('Helvetica', 14))
schl_entry.grid(row=4, column=3, pady=5, padx=5)
schl_entry.bind("<<ComboboxSelected>>", lambda event: department(schl_entry, dpt_entry, dpt_list))
dpt_entry = ttk.Combobox(root, value=dpt_list, width=21, font=('Helvetica', 14))
dpt_entry.grid(row=5, column=1, pady=5, padx=5)
dpt_entry.bind("<<ComboboxSelected>>", lambda event: crse(dpt_entry, crse_entry, crse_list))
crse_entry = ttk.Combobox(root, value=crse_list, width=21, font=('Helvetica', 14))
crse_entry.grid(row=5, column=3, pady=5, padx=5)
year_entry = ttk.Combobox(root, value=year_list, width=11, font=('Helvetica', 14))
year_entry.grid(row=2, column=5)
gender_entry = ttk.Combobox(root, value=['M', 'F'], width=11, font=('Helvetica', 14))
gender_entry.grid(row=3, column=5)

#creating the database for the students
conn = sqlite3.connect('jkuat.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS Students(Reg_no TEXT, F_name TEXT, M_name TEXT, L_name TEXT, College TEXT, School TEXT, Department TEXT, Course TEXT, Year TEXT, Gender TEXT)')
conn.commit()
conn.close()

#function to pack any data into the treeview

def display(a_list):
    for y in tree.get_children(): #clearing the treeview to insert new filtered data
        tree.delete(y)
    for i in range(len(a_list)):
        if i%2==0:
            tree.insert('', END, values=(a_list[i][0], a_list[i][1], a_list[i][2], a_list[i][3], a_list[i][4], a_list[i][5], a_list[i][6], a_list[i][7], a_list[i][8], a_list[i][9]), tags=('evenrow',))
        else:
            tree.insert('', END, values=(a_list[i][0], a_list[i][1], a_list[i][2], a_list[i][3], a_list[i][4], a_list[i][5], a_list[i][6], a_list[i][7], a_list[i][8], a_list[i][9]), tags=('oddrow',))   

#inserting default values into the treeview
conn = sqlite3.connect('jkuat.db')
c = conn.cursor()
c.execute('SELECT * FROM Students')
data=c.fetchall()
conn.commit()
conn.close()
display(data)
# functions used to access the database
def display_window(category):
    global gnd_entry
    global school_entry
    global dept_entry
    global clge_entry
    global course_entry
    global yr_entry
    top = Tk()
    top.title('Display Category Window')
    if category=='college':
        clge_label = Label(top, text='Choose the college name')
        clge_label.grid(row=0, column=0, padx=5, pady=5)
        clge_entry = ttk.Combobox(top, values=['COPAS', 'COANRE', 'COETEC', 'COHES'])
        clge_entry.grid(row=0, column=1, padx=5, pady=5)
        yr_label = Label(top, text='Choose the year of study')
        yr_label.grid(row=1, column=0, padx=5, pady=5)
        yr_entry = ttk.Combobox(top, values=['All', '1st', '2nd', '3rd', '4th', '5th', '6th', '7th'])
        yr_entry.grid(row=1, column=1, padx=5, pady=5)
        gnd_label = Label(top, text='Choose the Gender')
        gnd_label.grid(row=2, column=0, padx=5, pady=5)
        gnd_entry = ttk.Combobox(top, values=['All', 'M', 'F'])
        gnd_entry.grid(row=2, column=1, padx=5, pady=5)
        def ok():
            conn = sqlite3.connect('jkuat.db')
            c = conn.cursor()
            data = []
            if yr_entry.get()=='All' and gnd_entry.get()=='All':
                c.execute(f'SELECT * FROM Students WHERE College = "{clge_entry.get()}"')
                data = c.fetchall()
            elif yr_entry.get()=='All' and gnd_entry.get() !='All':
                c.execute(f'SELECT * FROM Students WHERE College = "{clge_entry.get()}" AND Gender = "{gnd_entry.get()}"')
                data = c.fetchall()
            elif yr_entry.get() !='All' and gnd_entry.get()=='All':
                c.execute(f'SELECT * FROM Students WHERE College = "{clge_entry.get()}" AND Year = "{yr_entry.get()}"')
                data = c.fetchall()
            elif yr_entry.get() !='All' and gnd_entry.get()!='All':
                c.execute(f'SELECT * FROM Students WHERE College = "{clge_entry.get()}" AND Year = "{yr_entry.get()}" AND Gender = "{gnd_entry.get()}"')
                data = c.fetchall()
            else:
                messagebox.showerror(title='Data Not Found', message='There are no records that match the given categories')
            display(data)
            conn.commit()
            conn.close()
            top.destroy()
        ok_btn = Button(top, text='OK', command=ok, width=20)
        ok_btn.grid(row=3, column=0, columnspan=2, pady=10)
    if category=='school':
        clge_label = Label(top, text='Choose the college name')
        clge_label.grid(row=0, column=0, padx=5, pady=5)
        clge_entry = ttk.Combobox(top, values=['COPAS', 'COANRE', 'COETEC', 'COHES'])
        clge_entry.grid(row=0, column=1, padx=5, pady=5)
        clge_entry.bind("<<ComboboxSelected>>", lambda event: school(clge_entry, school_entry, schl_list))
        school_label = Label(top, text='Choose the school')
        school_label.grid(row=1, column=0, padx=5, pady=5)
        school_entry = ttk.Combobox(top, values=[])
        school_entry.grid(row=1, column=1, padx=5, pady=5)
        yr_label = Label(top, text='Choose the year of study')
        yr_label.grid(row=2, column=0, padx=5, pady=5)#
        yr_entry = ttk.Combobox(top, values=['All', '1st', '2nd', '3rd', '4th', '5th', '6th', '7th'])
        yr_entry.grid(row=2, column=1, padx=5, pady=5)
        gnd_label = Label(top, text='Choose the Gender')
        gnd_label.grid(row=3, column=0, padx=5, pady=5)#
        gnd_entry = ttk.Combobox(top, values=['All', 'M', 'F'])
        gnd_entry.grid(row=3, column=1, padx=5, pady=5)
        def ok():
            conn = sqlite3.connect('jkuat.db')
            c = conn.cursor()
            data = []
            if yr_entry.get()=='All' and gnd_entry.get()=='All':
                c.execute(f'SELECT * FROM Students WHERE School = "{school_entry.get()}"')
                data = c.fetchall()
            elif yr_entry.get()=='All' and gnd_entry.get() !='All':
                c.execute(f'SELECT * FROM Students WHERE School = "{school_entry.get()}" AND Gender = "{gnd_entry.get()}"')
                data = c.fetchall()
            elif yr_entry.get() !='All' and gnd_entry.get()=='All':
                c.execute(f'SELECT * FROM Students WHERE School = "{school_entry.get()}" AND Year = "{yr_entry.get()}"')
                data = c.fetchall()
            elif yr_entry.get() !='All' and gnd_entry.get()!='All':
                c.execute(f'SELECT * FROM Students WHERE School = "{school_entry.get()}" AND Year = "{yr_entry.get()}" AND Gender = "{gnd_entry.get()}"')
                data = c.fetchall()
            else:
                messagebox.showerror(title='Data Not Found', message='There are no records that match the given categories')
            display(data)
            conn.commit()
            conn.close()
            top.destroy()
        ok_btn = Button(top, text='OK', command=ok, width=20)
        ok_btn.grid(row=4, column=0, columnspan=2, pady=10)
    if category=='department':
        clge_label = Label(top, text='Choose the college name')
        clge_label.grid(row=0, column=0, padx=5, pady=5)
        clge_entry = ttk.Combobox(top, values=['COPAS', 'COANRE', 'COETEC', 'COHES'])
        clge_entry.bind("<<ComboboxSelected>>", lambda event: school(clge_entry, school_entry, schl_list))
        clge_entry.grid(row=0, column=1, padx=5, pady=5) 
        school_label = Label(top, text='Choose the school')
        school_label.grid(row=1, column=0, padx=5, pady=5)
        school_entry = ttk.Combobox(top, values=[])
        school_entry.bind("<<ComboboxSelected>>", lambda event: department(school_entry, dept_entry, dpt_list))
        school_entry.grid(row=1, column=1, padx=5, pady=5)
        dept_label = Label(top, text='Choose the department')
        dept_label.grid(row=2, column=0, padx=5, pady=5)
        dept_entry = ttk.Combobox(top, values=[])
        dept_entry.grid(row=2, column=1, padx=5, pady=5)
        yr_label = Label(top, text='Choose the year of study')
        yr_label.grid(row=3, column=0, padx=5, pady=5)
        yr_entry = ttk.Combobox(top, values=['All', '1st', '2nd', '3rd', '4th', '5th', '6th', '7th'])
        yr_entry.grid(row=3, column=1, padx=5, pady=5)
        gender_label = Label(top, text='Choose the Gender')
        gender_label.grid(row=4, column=0, padx=5, pady=5)
        gnd_entry = ttk.Combobox(top, values=['All', 'M', 'F'])
        gnd_entry.grid(row=4, column=1, padx=5, pady=5)
        def ok():
            conn = sqlite3.connect('jkuat.db')
            c = conn.cursor()
            data = []
            if yr_entry.get()=='All' and gnd_entry.get()=='All':
                c.execute(f'SELECT * FROM Students WHERE Department = "{dept_entry.get()}"')
                data = c.fetchall()
            elif yr_entry.get()=='All' and gnd_entry.get() !='All':
                c.execute(f'SELECT * FROM Students WHERE Department = "{dept_entry.get()}" AND Gender = "{gnd_entry.get()}"')
                data = c.fetchall()
            elif yr_entry.get() !='All' and gnd_entry.get()=='All':
                c.execute(f'SELECT * FROM Students WHERE Department = "{dept_entry.get()}" AND Year = "{yr_entry.get()}"')
                data = c.fetchall()
            elif yr_entry.get() !='All' and gnd_entry.get()!='All':
                c.execute(f'SELECT * FROM Students WHERE Department = "{dept_entry.get()}" AND Year = "{yr_entry.get()}" AND Gender = "{gnd_entry.get()}"')
                data = c.fetchall()
            else:
                messagebox.showerror(title='Data Not Found', message='There are no records that match the given categories')
            display(data)
            conn.commit()
            conn.close()
            top.destroy()
        ok_btn = Button(top, text='OK', command=ok, width=20)
        ok_btn.grid(row=3, column=0, columnspan=2, pady=10)
    if category=='course':
        clge_label = Label(top, text='Choose the college name')
        clge_label.grid(row=0, column=0, padx=5, pady=5)
        clge_entry = ttk.Combobox(top, values=['COPAS', 'COANRE', 'COETEC', 'COHES'])
        clge_entry.bind("<<ComboboxSelected>>", lambda event: school(clge_entry, school_entry, schl_list))
        clge_entry.grid(row=0, column=1, padx=5, pady=5) 
        school_label = Label(top, text='Choose the school')
        school_label.grid(row=1, column=0, padx=5, pady=5)
        school_entry = ttk.Combobox(top, values=[])
        school_entry.bind("<<ComboboxSelected>>", lambda event: department(school_entry, dept_entry, dpt_list))
        school_entry.grid(row=1, column=1, padx=5, pady=5)
        dept_label = Label(top, text='Choose the department')
        dept_label.grid(row=2, column=0, padx=5, pady=5)
        dept_entry = ttk.Combobox(top, values=[])
        dept_entry.bind("<<ComboboxSelected>>", lambda event: crse(dept_entry, course_entry, crse_list))
        dept_entry.grid(row=2, column=1, padx=5, pady=5)
        course_label = Label(top, text='Choose the course')
        course_label.grid(row=3, column=0, padx=5, pady=5)
        course_entry = ttk.Combobox(top, values=[])
        course_entry.grid(row=3, column=1, padx=5, pady=5)
        yr_label = Label(top, text='Choose the year of study')
        yr_label.grid(row=4, column=0, padx=5, pady=5)#
        yr_entry = ttk.Combobox(top, values=['All', '1st', '2nd', '3rd', '4th', '5th', '6th', '7th'])
        yr_entry.grid(row=4, column=1, padx=5, pady=5)
        gender_label = Label(top, text='Choose the Gender')
        gender_label.grid(row=5, column=0, padx=5, pady=5)#
        gnd_entry = ttk.Combobox(top, values=['All', 'M', 'F'])
        gnd_entry.grid(row=5, column=1, padx=5, pady=5)
        def ok():
            conn = sqlite3.connect('jkuat.db')
            c = conn.cursor()
            data=[]
            if yr_entry.get()=='All' and gnd_entry.get() =='All':
                c.execute(f'SELECT * FROM Students WHERE Course = "{course_entry.get()}"')
                data = c.fetchall()
            elif yr_entry.get()=='All' and gnd_entry.get() !='All':
                c.execute(f'SELECT * FROM Students WHERE Course = "{course_entry.get()}" AND Gender = "{gnd_entry.get()}"')
                data = c.fetchall()
            elif yr_entry.get() !='All' and gnd_entry.get()=='All':
                c.execute(f'SELECT * FROM Students WHERE Course = "{course_entry.get()}" AND Year = "{yr_entry.get()}"')
                data = c.fetchall()
            elif yr_entry.get() !='All' and gnd_entry.get()!='All':
                c.execute(f'SELECT * FROM Students WHERE Course = "{course_entry.get()}" AND Year = "{yr_entry.get()}" AND Gender = "{gnd_entry.get()}"')
                data = c.fetchall()
            else:
                messagebox.showerror(title='Data Not Found', message='There are no records that match the given categories')
            display(data)
            conn.commit()
            conn.close()
            top.destroy()
        ok_btn = Button(top, text='OK', command=ok, width=20)
        ok_btn.grid(row=6, column=0, columnspan=2, pady=10)
    if category=='year':        
        yr_label = Label(top, text='Choose the year of study')
        yr_label.grid(row=0, column=0, padx=5, pady=5)
        yr_entry = ttk.Combobox(top, values=['1st', '2nd', '3rd', '4th', '5th', '6th', '7th'])
        yr_entry.grid(row=0, column=1, padx=5, pady=5)
        def ok():
            conn = sqlite3.connect('jkuat.db')
            c = conn.cursor()
            c.execute(f'SELECT * FROM Students WHERE Year = "{yr_entry.get()}"')
            data=c.fetchall()
            conn.commit()
            conn.close()
            display(data)
            top.destroy()
        ok_btn = Button(top, text='OK', command=ok, width=20)
        ok_btn.grid(row=1, column=0, columnspan=2, pady=10)
    if category == 'gender':
        gender_label = Label(top, text='Choose the Gender')
        gender_label.grid(row=0, column=0, padx=5, pady=5)#
        gnd_entry = ttk.Combobox(top, values=['M', 'F'])
        gnd_entry.grid(row=0, column=1, padx=5, pady=5)
        def ok():
            conn = sqlite3.connect('jkuat.db')
            c = conn.cursor()
            c.execute(f'SELECT * FROM Students WHERE Gender = "{gnd_entry.get()}"')
            data=c.fetchall()
            conn.commit()
            conn.close()
            display(data)
            top.destroy()
        ok_button = Button(top, text='OK', command=ok, width=20)
        ok_button.grid(row=1, column=0, columnspan=2, pady=10)
    top.mainloop()

conn = sqlite3.connect('jkuat.db')
c = conn.cursor()
c.execute('SELECT * FROM Students')
data = c.fetchall()
conn.commit()
conn.close()
#1.function to display the records from the database
def display_records(event):
    pop_menu = Menu(root, tearoff=2)
    pop_menu.add_command(label='Display all', command=lambda:display(data))
    pop_menu.add_separator()
    pop_menu.add_command(label='Display data from a College', command=lambda:display_window('college'))
    pop_menu.add_separator()
    pop_menu.add_command(label='Display data from a School', command=lambda:display_window('school'))
    pop_menu.add_separator()
    pop_menu.add_command(label='Display data from a Department', command=lambda:display_window('department'))
    pop_menu.add_separator()
    pop_menu.add_command(label='Display data from a Course', command=lambda:display_window('course'))
    pop_menu.add_separator()
    pop_menu.add_command(label='Display data from a Year of study', command=lambda:display_window('year'))
    pop_menu.add_separator()
    pop_menu.add_command(label='Display data from a Gender', command=lambda:display_window('gender'))
    pop_menu.add_separator()
    pop_menu.add_command(label='Exit', command=pop_menu.destroy)

    try:
        pop_menu.tk_popup(event.x_root, event.y_root)
    finally:
        pop_menu.grab_release()


#2.function to add a new record to the database
def add_record():
    conn = sqlite3.connect('jkuat.db')
    c = conn.cursor()
    # to prevent duplicates, we have to make sure there are no similar reg nos for different students:
    reg_no_list=[] #creating a list that will store all registration numbers in the db and will be used to check for duplicates
    c.execute('SELECT * FROM Students') #fetching all the data for duplicates check up
    data = c.fetchall() #data is a list of tuples that stores all the data in the database
    for student in data:# inserting all the reg nos into the reg_no_list
        reg_no_list.insert(0, student[0])
    if str(reg_entry.get()).upper() in reg_no_list:# checking for the duplicates
        messagebox.showerror(title='Duplicates detected', message='The registration number already exists')
    elif reg_entry.get()=='' or fname_entry.get()=='' or lname_entry.get()=='' or college_entry.get()=='' or schl_entry.get()=='' or dpt_entry.get()=='' or crse_entry.get()=='' or year_entry.get()=='' or gender_entry.get()=='':
        messagebox.showerror(title='Missing Values', message='Please enter all the required data. Only middle name can be given a null value')
    else:
        c.execute("INSERT INTO Students VALUES(:reg_no, :f_name, :m_name, :l_name, :college, :school, :dept, :crse, :year, :gender)",
            {
                'reg_no': str(reg_entry.get()).upper(),
                'f_name': str(fname_entry.get()),
                'm_name': str(mname_entry.get()),
                'l_name': str(lname_entry.get()),
                'college': str(college_entry.get()),
                'school': str(schl_entry.get()),
                'dept': str(dpt_entry.get()),
                'crse': str(crse_entry.get()),
                'year': str(year_entry.get()),
                'gender': str(gender_entry.get())
            })
        tree.insert('', END, values=(reg_entry.get(), fname_entry.get(), mname_entry.get(), lname_entry.get(), college_entry.get(), schl_entry.get(), dpt_entry.get(), crse_entry.get(), year_entry.get(), gender_entry.get()), tags=('evenrow',))
        messagebox.showinfo(title='', message='Record added successfully')
    conn.commit()
    conn.close()
#3.function to update a record in the database
def update():
    conn = sqlite3.connect('jkuat.db')
    c = conn.cursor()
    reg_no_list=[] #creating a list that will store all registration numbers in the db and will be used to check if the reocord to be updated already exists in the database
    c.execute('SELECT * FROM Students') #fetching all the data for duplicates check up
    data = c.fetchall() #data is a list of tuples that stores all the data in the database
    for student in data:# inserting all the reg nos into the reg_no_list
        reg_no_list.insert(0, student[0])
    if reg_entry.get() in reg_no_list:
        c.execute("""UPDATE Students SET
                Reg_no = :reg_no,
                F_name = :f_name,
                M_name = :m_name,
                L_name= :l_name,
                College= :college,
                School= :school,
                Department= :dept,
                Course= :crse,
                Year= :year,
                Gender= :gender
                WHERE Reg_no = :r""",
                {
                    'reg_no': reg_entry.get(),
                    'f_name': fname_entry.get(),
                    'm_name': mname_entry.get(),
                    'l_name': lname_entry.get(),
                    'college': college_entry.get(),
                    'school':schl_entry.get(),
                    'dept': dpt_entry.get(),
                    'crse': crse_entry.get(),
                    'year': year_entry.get(),
                    'gender': gender_entry.get(),
                    'r': reg_entry.get(),
                })
    else:
        messagebox.showinfo(title='Missing Record',  message='The given registration number does not exist')
    c.execute('SELECT * FROM Students')
    data = c.fetchall()
    display(data)
    conn.commit()
    conn.close()

#4.function to delete a record from the database
def delete_record():
    conn = sqlite3.connect('jkuat.db')
    c = conn.cursor()
    reg_no_list=[] #creating a list that will store all registration numbers in the db and will be used to check for duplicates
    c.execute('SELECT * FROM Students') #fetching all the data for duplicates check up
    data = c.fetchall() #data is a list of tuples that stores all the data in the database
    for student in data:# inserting all the reg nos into the reg_no_list
        reg_no_list.insert(0, student[0])
    if reg_entry.get() in reg_no_list:
        c.execute(f'DELETE FROM Students WHERE Reg_no="{reg_entry.get()}"')
        conn.commit()
        conn.close()
        selected_item = tree.selection()[0]#getting the selected item
        tree.delete(selected_item)#removing the selected item from the treeview
        messagebox.showinfo(message='The record has been deleted successfully')
    else:
        messagebox.showinfo(title='Missing Record',  message='The given registration number does not exist')
#5. function to search for a record
def search():
    top = Tk()
    top.title('Search window')
    search_label = Label(top, text='Enter the Reg No')
    search_label.grid(row=0, column=0, padx=10, pady=10)
    search_entry = Entry(top, width=30, font=('Helvetica', 15))
    search_entry.grid(row=0, column=1, padx=10, pady=10)
    def ok1():
        conn = sqlite3.connect('jkuat.db')
        c = conn.cursor()
        c.execute(f'SELECT * FROM Students WHERE Reg_no="{search_entry.get().upper()}"')
        data = c.fetchall()
        if len(data)>0:
            ok_btn.destroy()
            name_label = Label(top, text='Name: ')
            name_label.grid(row=1, column=0)
            name = Label(top, text=f'{data[0][3]} {data[0][1]} {data[0][2]}')
            name.grid(row=1, column=1, padx=10, pady=10)
            clge_label = Label(top, text='College')
            clge_label.grid(row=2, column=0, padx=10, pady=10)
            college = Label(top, text=data[0][4])
            college.grid(row=2, column=1, padx=10, pady=10)
            school_label = Label(top, text='School: ')
            school_label.grid(row=3, column=0)
            school = Label(top, text=data[0][5])
            school.grid(column=1, row=3, padx=10, pady=10)
            depart_label = Label(top, text='Department')
            depart_label.grid(row=4, column=0, padx=10, pady=10)
            depart = Label(top, text=data[0][6])
            depart.grid(row=4, column=1, padx=10, pady=10)
            course_label = Label(top, text='Course: ')
            course_label.grid(row=5, column=0, padx=10, pady=10)
            course = Label(top, text=data[0][7])
            course.grid(row=5, column=1, padx=10, pady=10)
            yr_label = Label(top, text='Year')
            yr_label.grid(row=6, column=0, padx=10, pady=10)
            year = Label(top, text=data[0][8])
            year.grid(row=6, column=1, padx=10, pady=10)
            gend_label = Label(top, text='Gender: ')
            gend_label.grid(row=7, column=0, padx=10, pady=10)
            gender = Label(top, text=data[0][9])
            gender.grid(row=7, column=1, padx=10, pady=10)
        else:
            top.destroy()
            messagebox.showinfo(title='No record Found', message='There is no record that matches the given Registration Number')
        conn.commit()
        conn.close()
    ok_btn = Button(top, text='OK', width=30, command=ok1)
    ok_btn.grid(row=1, column=0, columnspan=2)
    top.mainloop()
# creating buttons that are used to access the database by the end user
add_btn = Button(root, text='ADD RECORD', width=31, command=add_record, fg='#006400', bg='#5F9EA0')
add_btn.grid(row=4, column=4, padx=5, pady=5, columnspan=2)
update_btn = Button(root, text='UPDATE RECORD',width=31, command=update, fg='#006400', bg='#5F9EA0')
update_btn.grid(row=5, column=4, padx=5, pady=5, columnspan=2)
search_btn = Button(root, text='SEARCH', width=31, command=search, fg='#006400', bg='#5F9EA0')
search_btn.grid(row=2, column=6, padx=5, pady=5)
delete_btn = Button(root, text='DELETE RECORD', width=31, command=delete_record, fg='#006400', bg='#5F9EA0')
delete_btn.grid(row=3, column=6, padx=5, pady=5)
display_btn = Button(root, text='DISPLAY RECORD', width=31, fg='#006400', bg='#5F9EA0')
display_btn.grid(row=4, column=6, padx=5, pady=5)
exit_btn = Button(root, text='EXIT', width=36, command=root.destroy, fg='#800000', bg='#5F9EA0', font=('Helvetica', 10))
exit_btn.grid(row=5, column=6, padx=5, pady=5)

display_btn.bind('<Button-1>', display_records)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.columnconfigure(4, weight=1)
root.columnconfigure(6, weight=1)
root.columnconfigure(7, weight=1)

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)
root.rowconfigure(5, weight=1)
root.rowconfigure(6, weight=1)

root.mainloop()

#this code is written by Ian Mark Okeyo...contact for more details if you happen not to understand any line in this code