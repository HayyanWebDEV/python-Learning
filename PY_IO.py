with open("progect pdf\\hayyan.pdf", "w") as file1:
    file1.write("This is true meow meow! hahahhahahaha"
                "bho bha bbum ba fihjsgahjgfhldgsalhfgdlas ")

with open("progect pdf\\hayyan2.pdf", "w") as file2:
    file2.write("This is true meow meow! hahahhahahaha"
                "bho bha bbum ba fihjsgahjgfhldgsalhfgdlas ")

with open("progect pdf\\hayyan.pdf", "r") as file1,\
     open("progect pdf\\hayyan2.pdf", "r") as file2:

       if (file1.read() == file2.read()):
        print("both pdfs are same")
       else:
         print("both pdfs are different")