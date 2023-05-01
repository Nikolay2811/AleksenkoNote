import os
import time


def PrintMenu():
    print("\n1) создать заметку\n2) список заметок\n3) показать тект заметок\n4) редактировать заметку\n5) удалить заметку\n6) выход")
    
def CreateNote():
    # допускается повторение имен заметок, т.к. идентификатором является дата и время
    name = input("Введите имя заметки => ")
    t = time.localtime()
    id =f"{t.tm_mday}{t.tm_mon}{t.tm_year}{t.tm_hour}{t.tm_min}{t.tm_sec}_"
    with open ("names.txt", "a") as note_names:
        note_names.write(id + name + ".txt\n")
    with open (id + name + ".txt", "w") as file: # note_02032023104534999{datetime}_name.txt
        # file.write(input("Введите текст заметки"))
        note = ""
        while True:
            print("Введите текст нового абзаца заметки и нажмите ENTER. Если хотите Сохранить и Выйти, то введите 0.")
            t = input()
            if t != "0":
                note = note + t + '\n'
            else:
                break
        file.write(note)
        

def Spisok():
    with open("names.txt", "r") as notes_names:
        i=1
        for line in notes_names.readlines():
            print(i,") ",line, end="")
            i=i+1



def ShowNote():
    with open("names.txt", "r") as notes_names:
        spisok=notes_names.readlines()
    Spisok()
    try:
     number =int(input("Ведите номер заметки => "))
     if number > 0 and number <= len(spisok):
            call=spisok[number-1].strip()
   
            with open(call, "r") as file:
                i=1
                for line in file:
                    print(i,"->", line, end="")
                    i=+i+1
     else:
         print("Нет такой заметки")
         
    except ValueError as ve:
        print("Введено не число ")



def Delete():
    Spisok()
    with open("names.txt", "r") as notes_names:
        spisok=notes_names.readlines()
    
    try:
        number = int(input("Введите номер заметки  для удаления => "))
        if number > 0 and number <= len(spisok):
            print("удалить файл " + spisok[number-1] +"[y/n]?")
            if input() == "y":
                call=spisok[number-1].strip()
                print(os.path.abspath(os.curdir)+"\\"+call)
                if os.path.isfile(os.path.abspath(os.curdir)+"\\"+call):                    
                        os.remove(os.curdir+"\\"+call)                  
                del spisok[number-1]
            else:
                
                pass 
        else:
            print("Нет  такой заметки")
            pass 
    except ValueError as ve:
        print("Введено не число, пожалуйста введите число")
    with open ("names.txt","w") as f:
        for line in spisok:
            f.write(line)


def NotesList(n):
    with open("names.txt", "r") as notes_names:
        spisok=notes_names.readlines()
    print("Выберите заметку: ")
    Spisok()
    try:
        number2 = int(input("Ведите номер заметки  или 0 для выхода в меню=> "))
        if number2 > 0 and number2 <= len(spisok):
            call=spisok[number2-1].strip()
            with open(call, n) as newStr:
                    while True:
                        print("Введите текст нового абзаца заметки и нажмите ENTER. Если хотите Сохранить и Выйти, то введите 0.")
                        t = input()
                        if t != "0":
                            newStr.write('n'+t)
                        else:
                            break
        elif number2==0:
            pass
        else:
            print("Нет такой заметки")

    except ValueError as ve:
        print("Введено не число, пожалуйста введите число")

def readactor():
    with open("names.txt", "r") as notes_names:
        spisok=notes_names.readlines()
    print("Выберите:\n1) добавить новые строки в заметку \n2) Редактировать строки в заметке \n3) Перезаписать заметку \n4) Выход в меню")
    number = input("=> ")
    if number =="1":
        NotesList("a")            
    elif number =="2":
        print("Выберите заметку: ")
        Spisok()
        try:
            number2 = int(input("Ведите номер заметки для перезаписи строк строк => "))
            if number2 > 0 and number2 <= len(spisok):
                call=spisok[number2-1].strip()
                print
                with open(call, "r") as notes_text:
                    text=notes_text.readlines()
                while True:
                    for i in range(0, len(text)):
                        print(i+1,"->",text[i], end="")
                    str = int(input("\nВедите номер строки для перезаписи  или 0 для сохранения и выхода в меню=> "))
                    
                    if str > 0 and str <= len(text):
                        print(text[str-1])
                        newstr =input("Новый текст строки => ")
                        yes =input("Вы точно хотите переписать cтроку? [y/n] => ")
                        if yes =="y":
                            text[str-1]=newstr+'\n'
                        else:
                         pass
                    elif str ==0:
                        with open (call,"w") as f:
                            for line in text:
                                f.write(line )
                        break
                    else:
                        print("Нет таой строки")
            else:
                print("Нет такой заметки")   
        except ValueError as ve:
            print("Введено не число")    
    elif number =="3":
        NotesList("w")
    elif number == "4":
        pass

    else:
        print("Не коректный ввод. Видите число от 1 до 4")         
             
         

        
          

    
 



if __name__ == "__main__":
    print("Ну что народ, погнали!!!")  
    while True:
        PrintMenu()
        menu = input("Выберите действие => ")
        if menu == "1":
            CreateNote()
        elif menu == "2":
            Spisok()  
        elif menu == "3":
            
            ShowNote()

            pass   
        elif menu == "4":
            
            readactor()

            pass   
        elif menu == "5":
            
            Delete()
            pass
        elif menu == "6":
            exit(0)
        else:
            print("Не корректная команда. Введите команду от 1 до 6")
    
