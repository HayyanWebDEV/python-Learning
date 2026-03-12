import os

def file_searcher(directoryname):
    def list_files(d):
         nonlocal tabstop
         files = os.listdir(d)
         for f in files:
            current_dir = os.path.join(d, f)
            if os.path.isdir(current_dir):
                print('\t'*tabstop + "directory: " + current_dir)
                tabstop += 1
                list_files(current_dir)
                tabstop -= 1
            else:
                print('\t' * tabstop + "file: " + current_dir)
    tabstop = 0
    if os.path.exists(directoryname):
        print("Searching inside " + directoryname)
        list_files(directoryname)
    else:
        print(f"File {directoryname} does not exist")


file_searcher(r"C:\Users\PC\downloads")
