contact_book={}
def display_contact():
    print("name\t\tcontact number")
    for key in contact_book:
        print("{}\t\t{}.format(key,contact_book.get(key))")
while True:
     choice=int(input('1.Add new contaxt\n 2.Search contact\n 3.Display contact\n 4.Edit contact\n 5.Delete contact\n 6.Exit\n'))
     if choice==1:
         name=input('enter the contact name:')
         phone_no=input('enter the mobile number:')
         contact_book[name]=phone_no
     elif choice==2:
        search_name=input('enter the name:')
        if search_name in contact_book:
            print(search_name,"contact number is",contact_book[search_name])
        else:
            print("Contact not found!")
     elif choice ==3:
         if not contact_book:
             print("empty contact book")
         else:
            display_contact()
     elif choice==4:
         edit_contact_book=input("enter the contact to be edited:")
         if edit_contact_book in contact_book:
             phone_no=input("enter the phone num:")
             contact_book[edit_contact_book]=phone_no
             print('contact updated')
         else:
             print("name isn't found")
     elif choice==5:
         delete_contact=input('enter the name to be deleted:')
         if delete_contact in contact_book:
             confirm=input('Do you want to delete the contact Y/N?')
             if confirm==1:
                 contact_book.pop(delete_contact)
                 display_contact()
             else:
                 print("name isn't found")
     else:
         break
        
         
