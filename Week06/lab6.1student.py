

def display_menu():
    print ("What would you like to do?")
    print ("\t(a) Add new student")
    print ("\t(v) View student")
    print ("\t(q) Quit")
    choice = input ("Type one letter (a/v/q): ").strip()
         
    return choice
        
    
#def do_add():
#    print ("adding ")

#def do_view():
#    print ("view ") 

choice = display_menu()
print (f'you chose {choice}')
while (choice != "q"):
    if (choice == "a"):
        do_add()
    elif (choice == "v"):
        do_view()
    elif (choice != "q"):
        print ("\n\nplease select either a, v,or q")
    choice = display_menu()


    
