class Phone_directory:
    def __init__(self):
        self.contact={}
        self.menu()
        
    def create(self):
        name=input("Enter your name : ")
        phone=int(input("Enter your phone number : "))
        email=input("Enter your email address : ")
        self.contact.update({name:[name,phone,email]})
        print("Congratulations Arked Contact created successfully...")
        
        self.menu()
    
    def update(self):
        name=input("Enter the name you want to update the details : ")
        if name in self.contact:
            new_name=input("Enter new name to update : ")
            new_phone=int(input("Enter new phone number to update : "))
            new_email=input("Enter new email to update : ")
            self.contact.update({new_name:[new_name,new_phone,new_email]})
            self.contact.pop(name)
        else:
            print("Sorry entered name is not exists...")
            
        self.menu()
        
        
    def delete(self):
        name=input("Enter name  to delete phone record : ")
        if name in self.contact(name):
            self.contac.pop(name)
        else:
            print("Sorry Entered name not found..")
            
        self.menu()
        
        
    def search(self):
        name=input("Enter the name to search : ")
        if name in self.contact(name):
            print(self.contact[name])
        else:
            print("Sorry given name is not present is directory..")
            
        self.menu()
        
    def show(self):
        print(self.contact)
        
        self.menu()
        
        
    def exit(self):
        print("Exit successfully")
        
        
    def menu(self):
        print("Enter your choice ....")
        print(''' Enter 1. Create contact
              2. Update contact
              3. Delete contact
              4. Search contact
              5. Show contact list
              6. Exit from directory''')
        choice=int(input())
        if choice == 1:
            self.create()
        elif choice == 2:
            self.update()
        elif choice == 3:
            self.delete()
        elif choice == 4:
            self.search()
        elif choice == 5:
            self.show()
        elif choice == 6:
            self.exit()
        else:
            print("Sorry you selected wrong choice")
            
            
Contact1=Phone_directory()
        
        
        
        
        
            
            
        
        