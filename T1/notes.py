""" Реализовать консольное приложение заметки, с сохранением, чтением,
добавлением, редактированием и удалением заметок. Заметка должна
содержать идентификатор, заголовок, тело заметки и дату/время создания или
последнего изменения заметки. Сохранение заметок необходимо сделать в
формате json или csv формат (разделение полей рекомендуется делать через
точку с запятой). Реализацию пользовательского интерфейса студент может
делать как ему удобнее, можно делать как параметры запуска программы
(команда, данные), можно делать как запрос команды с консоли и
последующим вводом данных, как-то ещё, на усмотрение студента 

1. Вывести список заметок +
2. Прочитать запись +
3. Добавить запись +
4. редактировать запись+
5. удалить заметку. + 


"""

from datetime import datetime
import os
import csv

def input_header():
    return input("Введите название заметки : ")

def input_body():
    return input("Введите тело: ")

def input_param():
    return input("Введите номер  заметки: ")



def print_data():
    with open('notes.csv', 'r', newline='') as f:
        reader = csv.DictReader(f)

        # Печатаем заголовки только для полей 'id' и 'header'
        print("ID\tHeader")
        print("------------------------")
        for row in reader:
            print(f"{row['ID']}\t{row['Head']}")

def add_note(count):
    with open('notes.csv', 'a', newline='') as f:
     writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
     writer.writerow([count,input_header(),input_body(),datetime.now().strftime("%Y-%m-%d %H:%M:%S")])
       
            
def read_note(read_num):
    #row_to_read = note_num
    with open('notes.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
    # Ищем строку с указанным номером ID
        for row in reader:
            if row['ID'] == read_num:
                print("ID:", row['ID'])
                print("\tHead:", row['Head'])
                print("\tBody:", row['Body'])
                print("\t_________________________")
                print("\tDate:", row['Date'])
                

def delete_note(num_to_delete):
    #row_to_delete = num_to_delete
    data = []
    with open('notes.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            if (row['ID'] != num_to_delete):
               # print(row['ID'])
                data.append(row)

    # Перезаписываем исходный файл CSV данными из списка
    fieldnames = ['ID', 'Head', 'Body', 'Date']
    with open('notes.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def edit_note(edit_num):
   delete_note(edit_num)
   add_note(edit_num)




def interface():
    if not os.path.exists('notes.csv'):
        with open('notes.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Head', 'Body', 'Date'])
            count = 1
    else:
        with open('notes.csv', 'r', newline='') as csvfile:
            # Считаем количество строк в файле
            count = sum(1 for _ in csvfile)
    command = ""
    os.system('cls')
    while command != "6":
        print("Меню пользователя: \n"
                "1. Вывести список заметок.\n"
                "2. Прочитать заметку.\n"
                "3. Добавить заметку.\n"
                "4. Редактировать заметку.\n"
                "5. Удалить заметку.\n" 
                "6. Вывод.\n" )
        command =  input("Выберите пункт меню: ")

        while command not in ("1","2","3","4","5","6"):
            print("Некорректный ввод, повторите запрос")
            command =  input("Выберите пункт меню: ")

        match command:
            case "1":
                print_data()
            case "2":
                read_note(input_param())
            case "3":
                add_note(count)
                count += 1
            case "4":
                edit_note(input_param())    
            case "5":
                delete_note(input_param())
            case "6":
                print("Завершение программы.")
        print()

if __name__ == "__main__":
    interface()