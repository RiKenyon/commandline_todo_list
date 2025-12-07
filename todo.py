import cmd
import os

from datetime import datetime

class MyCLI(cmd.Cmd):
    prompt = 'Todo List>> '
    intro = 'Welcome to your todo list'
    def __init__(self):
        super().__init__()
        self.current_directory = os.getcwd()
        
    def do_hello(self, line):
        print("hello woorld")
        
    def do_list(self, line):
        files_and_dirs = os.listdir(self.current_directory)
        for item in files_and_dirs:
            print(item)
            
    def do_change_dir(self, directory):
        new_dir = os.path.join(self.current_directory,directory)
        if os.path.exists(new_dir) and os.path.isdir(new_dir):
            self.current_directory = new_dir
            print("Current directory changed to " + self.current_directory)
        else:
            print("Directory" + directory + " does not exist.")
            
    def do_create_list(self, filename):
        file_path = os.path.join(self.current_directory, filename)
        try:
            with open(file_path, 'w') as new_file:
                print(f"File {filename} created in {self.current_directory}")
                todo_list = []
                number = 1
                while True:
                    userList = input(f"List {number}: ")
                    
                    if userList.lower() == "q":
                        print("Exiting..")
                        break
                    
                    todo_list.append(userList)
                    number += 1
                    
                print(f"Your list has been added: {todo_list}")
                now = datetime.now()
                formatted = now.strftime("%d/%m/%Y %H:%M:%S")
                new_file.write(f"This is todo list on: {formatted}")
                for i in todo_list:
                    new_file.write(f"\n>>> {i}")
                
                    

        except Exception as e:
            print(f"Error: {e}")
            
    def do_read_file(self, filename):
        file_path = os.path.join(self.current_directory, filename)
        try:
            with open(file_path, 'r') as existing_file:
                print(existing_file.read())
        except FileNotFoundError:
            print(f"File {filename} not found")
        except Exception as e:
            print(f"Error: {e}")
        
    def do_quit(self, line):
        return True
    def postcmd(self, stop, line):
        print("----------------------------------")
        return stop

if __name__ == '__main__':
    MyCLI().cmdloop()