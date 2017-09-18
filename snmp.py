from Tkinter import *
from easysnmp import Session
import os
import time
import sys
import nmap 

class up_hosts(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.geometry("250x300")
        self.net_label = Label(self, text = "specify network with mask\n example: 192.168.1.0/24")
        self.net_label.pack(fill=BOTH)
        
        self.net_entry = Entry(self)
        self.net_entry.pack(fill=BOTH)
        
        self.button1 = Button(self, text="go!", command=self.nmap_net)
        self.button1.pack(fill=Y)
        self.space1_label = Label(self, text = " ")
        self.space1_label.pack(fill=BOTH)
        
    


    def nmap_net(self):
        hosty = self.net_entry.get()
        nm = nmap.PortScanner()
        nm.scan(hosts='192.168.1.0/24', arguments='-n -sP -PE -PA21,23,80,3389')
        hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
        listbox = Listbox(self)
        for host, status in hosts_list:
            print('{0}:{1}'.format(host, status))
                
   
            listbox.insert(END,host +" "+ status)
        listbox.pack(fill=BOTH)

        
             
     
class ping(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.geometry("340x300")
        
        self.host_label = Label(self, text = "host ip:")
        self.host_label.pack(fill=BOTH)
        self.host_entry = Entry(self)
        self.host_entry.pack(fill=BOTH)
        self.button1 = Button(self, text="PING!", command=self.pi)
        self.button1.pack(fill=Y)
        self.space1_label = Label(self, text = " ")
        self.space1_label.pack(fill=BOTH)

    


    def pi(self):
        hosty = self.host_entry.get()
        response = os.system("ping -c 3 " + hosty)
        
        if response == 0: 
           self.oid_label = Label(self, text ="at "+time.asctime( time.localtime(time.time()) )+ "host: "+ hosty+" is up!")
           self.oid_label.pack(fill=BOTH)
             
        else:
            self.oid_label = Label(self, text = "at "+time.asctime( time.localtime(time.time()) )+" host: "+ hosty+"is down!")
            self.oid_label.pack(fill=BOTH)      
        
        
#create set,get,walk,traps window
class create_details(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.geometry("400x500")
        #get
        self.oid_label = Label(self, text = "get oid:")
        self.oid_label.pack(fill=BOTH)
        self.oid_entry = Entry(self)
        self.oid_entry.pack(fill=BOTH)
        
        self.button1 = Button(self, text="Get", command=self.on_button_get)
        self.button1.pack(fill=Y)
        self.space1_label = Label(self, text = " ")
        self.space1_label.pack(fill=BOTH)



        #set
        self.oid2_label = Label(self, text = "set oid:")
        self.oid2_label.pack(fill=BOTH)
        self.oid2_entry = Entry(self)
        self.oid2_entry.pack(fill=BOTH)

        self.oid2_value_label = Label(self, text = "Value:")
        self.oid2_value_label.pack(fill=BOTH)
        self.oid2_value_entry = Entry(self)
        self.oid2_value_entry.pack(fill=BOTH) 
        self.button2 = Button(self, text="Set", command=self.on_button_set)
        self.button2.pack(fill=Y)
        self.space2_label = Label(self, text = " ")
        self.space2_label.pack(fill=BOTH)



        #walk
        self.oid3_label = Label(self, text = "walk oid:")
        self.oid3_label.pack(fill=BOTH)
        self.oid3_entry = Entry(self)
        self.oid3_entry.pack(fill=BOTH)
        self.button3 = Button(self, text="walk now!",command=self.on_button_walk)
        self.button3.pack(fill=Y)
        self.space3_label = Label(self, text = " ")
        self.space3_label.pack(fill=BOTH)

        #traps
        self.oid3_label = Label(self, text = "traps:")
        self.oid3_label.pack(fill=BOTH)
        listbox = Listbox(self)
        for a in range (1,100):
               listbox.insert(END, a)
        listbox.pack(fill=BOTH)


    #get operation
    def on_button_get(self):
        snmp_get = session.get(self.oid_entry.get())
        result = snmp_get.value.encode("ascii")
        print ("the result" +result)
        window_1 = Toplevel(self)
        window_1.geometry("250x100")
        self.res_label = Label(window_1, text ="The result of ("+self.oid_entry.get() +") is : \n"+ result)
        self.res_label.pack(fill=BOTH)
        button_done = Button(window_1, text="Done!",command=window_1.destroy)
        button_done.pack(fill=Y)

        

    #set operation
    def on_button_set(self):
        snmp_set = session.set(self.oid2_entry.get(),self.oid2_value_entry.get())
        print "\n Done, check the device %s" %host 
        window_1 = Toplevel(self)
        window_1.geometry("250x150")
        self.res_label = Label(window_1, text ="Done, check the device with ip : \n"+host)
        self.res_label.pack(fill=BOTH)
        button_done = Button(window_1, text="Done!",command=window_1.destroy)
        button_done.pack(fill=Y)


    #walk operation
    def on_button_walk(self):
        snmp_walk = session.walk(self.oid3_entry.get())       
        
        print "\n the result of snmp walk on %s is " %self.oid3_entry.get()
          
            
        window_1 = Toplevel(self)
        window_1.geometry("250x300")
        self.res_label = Label(window_1, text ="walk result:")
        self.res_label.pack(fill=BOTH)
        listbox = Listbox(window_1)
        for obj in snmp_walk:
            listbox.insert(END,obj.oid.encode('ascii') +" :"+ obj.value.encode('ascii'))
        listbox.pack(fill=BOTH)
        button_done = Button(window_1, text="Done!",command=window_1.destroy)
        button_done.pack(fill=Y)

#create main window and connect to the host 
class create_session(Tk):


    def create_about_window(self):
        window = Toplevel(self)
        label = Label(window, text="welcome to our program .... \n you can use it for free .. \n  ")
        label.grid(row=1, column=1) 

    def create_contact_us_window(self):
        window = Toplevel(self)
        label = Label(window, text="welcome to our program .... \n you can use it for free .. \n if you have any questions or suggestion \n"

                                "you can E-mail me :p \n  doaa.assaf@hotmail.com")
        label.grid(row=1, column=1)
    
    def create_MIB_tree_window(self):
        window = Toplevel(self)
        window.geometry("250x300")
        self.res_label = Label(window, text ="Here is MIB tree:")
        self.res_label.pack(fill=BOTH)
        listbox = Listbox(window,width=30,height=15)

        file = open('newfile.txt', 'r')
        
        for line in file:
            listbox.insert(END,line)
        listbox.pack(fill=BOTH)
        button_done = Button(window, text="Done!",command=window.destroy)
        button_done.pack(fill=Y)     
 
    def create_OIDs_tree_window(self):
        window = Toplevel(self)
        window.geometry("250x300")
        window.res_label = Label(window, text ="Here is the most famous OIDs:")
        window.res_label.pack(fill=BOTH)
        listbox = Listbox(window,width=30,height=15)

        oids = open('oids.txt', 'r')
        
        for line in oids:
            listbox.insert(END,line)
        listbox.pack(fill=BOTH)
        button_done = Button(window, text="Done!",command=window.destroy)
        button_done.pack(fill=Y) 
   
    
         
    def up_hosts(self,w,ii):
        listbox = Listbox(w)
        for ip in range(1,10):
              
             hostname = str(ii)+str(ip) 
             response = os.system("ping -c 1 " + hostname)
             if response == 0:
                listbox.insert(END,hostname+" is up")            
        
        button_done = Button(w, text="Done!",command=w.destroy)
        button_done.pack(fill=Y)
        listbox.pack(fill=BOTH)

    def show_up_hosts(self):
        w6=up_hosts()
        
    def ping_to_host(self):
        w3=ping()     
        
 
    def __init__(self):
        Tk.__init__(self)
        self.geometry("325x300")
        menu = Menu(self)
        self.config(menu=menu)
        # create file sub menu
        submenu = Menu(menu)  # create submenu
        menu.add_cascade(label="file", menu=submenu)  ##dropdown functionality
        submenu.add_command(label="exit", command=self.destroy)
        # create about submenu
        submenu3 = Menu(menu)  # create submenu
        menu.add_cascade(label="Help", menu=submenu3)  ##dropdown functionality
        submenu3.add_command(label="about", command=self.create_about_window)
        submenu3.add_command(label="contact us", command=self.create_contact_us_window)
        
        # create view submenu
        submenu4 = Menu(menu)  # create submenu
        menu.add_cascade(label="Tools", menu=submenu4)  ##dropdown functionality
        submenu4.add_command(label="All MIB tree", command=self.create_MIB_tree_window)
        submenu4.add_command(label="famous OIDs", command=self.create_OIDs_tree_window)
        submenu4.add_command(label="up hosts", command=self.show_up_hosts)
        submenu4.add_command(label="ping to host", command=self.ping_to_host)
        self.ip_label = Label(self, text = "IP:")
        self.ip_label.pack(fill=BOTH) 
        self.ip_entry = Entry(self)
        self.ip_entry.pack(fill=BOTH)
        
        self.community_label = Label(self, text = "Community:")
        self.community_label.pack(fill=BOTH)
        self.community_entry = Entry(self)
        self.community_entry.pack(fill=BOTH)
        global var
        var=  IntVar()
        self.R1 = Radiobutton(self, text="version 1", variable=var, value=1,
                  command=self.sel)
        self.R1.pack( anchor = W )

        self.R2 = Radiobutton(self, text="version 2", variable=var, value=2,
                  command=self.sel)
        self.R2.pack( anchor = W )

        self.R3 = Radiobutton(self, text="version 3", variable=var, value=3,
                  command=self.sel)
        self.R3.pack( anchor = W)


        self.button = Button(self, text="connect", command=self.on_button)
        self.button.pack(fill=Y)
        self.labels = Label(self)
        self.labels.pack()


    def on_button(self):
        print(self.ip_entry.get())
        global host
        host=self.ip_entry.get()
        print(self.community_entry.get())
        global comm
        comm=self.community_entry.get()
        global session
        if var.get() == 2 :
          
          session = Session(hostname =host,community=comm,version = 2)
          w2=create_details()
        elif var.get() == 1 :  
         
          session = Session(hostname =host,community=comm,version = 1)
          w2=create_details()
        else  :  
         
          session = Session(hostname =host,community=comm,version = 3)
          w2=create_details()


        #w2 = Toplevel(self)
    def sel(self):
     
        
        selection = "You selected the option " + str(var.get())
        self.labels = Label(self, text = selection)
        print("selecrion = "+ str(var.get()))
        
w1 = create_session()
w1.mainloop()
