myCharDict = {"Name": "none", "Class": "none", "Weapon": "none"}
def menu():
     print "A) Name"
     print "B) Class"
     print "C) Weapon"
     option = raw_input("Choose a letter: ")
     if option == "A" or option == "a":
         optionName = raw_input("Enter name: ")
         myCharDict["Name"] = optionName
         menu()
     if option == "B" or option == "b":
        print "A) Warrior"
        print "B) Magician"
        print "C) Rogue"
        print "D) College Student"
        optionClass = raw_input("Choose a class: ")
        if optionClass == "Warrior" or optionClass == "warrior" or optionClass == "A" or optionClass == "a":
            myCharDict["Name"] = optionClass
            menu()
        if optionClass == "Magician" or optionClass == "magician" or optionClass == "B" or optionClass == "b":
            myCharDict["Name"] = optionClass
            menu()
        if optionClass == "Rogue" or optionClass == "rogue" or optionClass == "C" or optionClass == "c":
            myCharDict["Name"] = optionClass
            menu()
        if optionClass == "College Student" or optionClass == "college student" or optionClass == "D" or optionClass == "d":
            myCharDict["Name"] = optionClass
            menu()  
        else:
            raw_input("Sorry, you must choose a provided class.: ")
     if option == "C" or option == "c":
        print "A) Sword"
        print "B) Staff"
        print "C) Knife"
        print "D) Battleaxe"
        print "E) Spear"
        print "F) Cellphone"
        optionWeapon = raw_input("Choose a weapon: ")
        if optionWeapon == "Sword" or optionWeapon == "sword" or optionWeapon == "A" or optionWeapon == "a":
            myCharDict["Name"] = optionWeapon
            menu()
        if optionWeapon == "Staff" or optionWeapon == "staff" or optionWeapon == "B" or optionWeapon == "b":
            myCharDict["Name"] = optionWeapon
            menu()
        if optionWeapon == "Knife" or optionWeapon == "knife" or optionWeapon == "C" or optionWeapon == "c":
            myCharDict["Name"] = optionWeapon
            menu()
        if optionWeapon == "Battleaxe" or optionWeapon == "battleaxe" or optionWeapon == "D" or optionWeapon == "d":
            myCharDict["Name"] = optionWeapon
            menu()
        if optionWeapon == "Spear" or optionWeapon == "spear" or optionWeapon == "E" or optionWeapon == "e":
            myCharDict["Name"] = optionWeapon
            menu()
        if optionWeapon == "Cellphone" or optionWeapon == "cellphone" or optionWeapon == "F" or optionWeapon == "f":
            myCharDict["Name"] = optionWeapon
            menu()
        if myCharDict["Name"] <> "none" and myCharDict["Class"] <> "none" and myCharDict["Weapon"] <> "none":
            finalizeChar()
        else:
            raw_input("Sorry, you must choose a provided weapon.: ")
def finalizeChar():
     finalize = raw_input("Are you good with these choices?: ")
     print ("Name: %(Name)s \nClass:%(Class)s \nWeapon: %(Weapon)s" % (myCharDict))
     if finalize == "Yes" or finalize == "yes":
         print "Very well. Enjoy the adventure."
     if finalize == "No" or finalize == "no":
         menu()
     else:
         print "You need to do SOMETHING."

menu()
finalizeChar()