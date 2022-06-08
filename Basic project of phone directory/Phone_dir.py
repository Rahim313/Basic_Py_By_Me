class Phone_dir:
    def __init__(self):
        self.contact={}  #initialize null dictionary
        self.menu()
        
        
    #function to show menu
    def menu(self):
        print("Enter your choice : ")
        print(''' Press Number to select your choice..
              1. Create Contact
              2. Update Contact
              3. Search Contact
              4. Delete Contact
              5. Show all contacts
              6. Exit from Directory''')
        choice =int(input())
        if choice == 1:
            self.Create()
        elif choice == 2:
            self.Update()
        elif choice == 3:
            self.Search()
        elif choice == 4:
            self.Delete()
        elif choice == 5:
            self.Show_all()
        elif choice == 6:
            self.Exit()
        else:
            print("Your entered a wrong choice")
            
            
    # function to add contact details
    def Create(self):
        name=input("Enter your name : ")
        phone=int(input("Enter your phone number : "))
        email=input("Enter your email : ")
        self.contact.Update({name:[name,phone,email]})
        print("******************** Contact Successfully Created ***************************")
        self.menu()
    
    # function to update contact details 
    def Update(self):
        name=input("Enter the name you want to update : ")
        if name in self.contact:
            new_name=input("Enter a new name : ")
            new_phone=int(input("Enter new phone number : "))
            new_email=input("Enter new email : ")
            self.contact.Update({new_name:[new_name,new_phone,new_email]})
            self.contact.pop(name)
            print("*********************    New  Contact Update    ***************")
        else:
            print("**********************   Searched name not exist  *****************")
            
        self.menu()
        
        
        
        
    # Function to delete contact details
    def Delete(self):
        name=input("Enter name your want to delete : ")
        if name in self.contact:
            self.contact.pop(name)
        else:
            print("************** Give name not exist *****************")
        self.menu()
        
        
        
    # function to search specific contact
    def Search(self):
        name=input("Enter name you want to search : ")
        if name in self.contact:
            print(self.contact[name])
        else:
            print("********************  Given name is not in phone directory *************")
        self.menu()
        
        
        
    # function to show all stored contact details
    def Show(self):
        print(self.contact)
        
        self.menu()
        
    # function to exit from phone_directory
    def Exit(self):
        print("*************************   Exited successfully ********************")
        
    # Calling phone directory calss to run above code
    
Phone_dir()
    
    
    
    
    