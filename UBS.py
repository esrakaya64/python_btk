import sqlite3 as sql
from ubsUi import UI
import json
from tabulate import tabulate 
import os

#Böyle bir veritabanı varsa erişir, yoksa oluşturur.
vt = sql.connect("/Users/esrakaya/Desktop/Btk Python/project.db" )
#Bir imleç tanımlayalım.
im = vt.cursor() 

#yeni tablo oluşturalım
im.execute("CREATE TABLE IF NOT EXISTS sis(id,studentId,name,surname,lesson,midterm, final)")

def addFromJSON():
    
#Path: /Users/esrakaya/Desktop/Btk Python/project2.json
    file_path = input("Enter the JSON file path: ")
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            for student in data:
                studentId = student["studentId"]
                name = student["name"]
                surname = student["surname"]
                lesson = student["lesson"]
                midterm = student["midterm"]
                final = student["final"]

                im.execute("INSERT INTO sis(studentId, name, surname, lesson, midterm, final) VALUES (?, ?, ?, ?, ?, ?)",
                           (studentId, name, surname, lesson, midterm, final))
            
            vt.commit()  # Veritabanındaki değişiklikleri kaydet
            print("Students added successfully from JSON!")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)


def addStudent():

        studentId= int(input("ID: "))
        name = input("NAME: ")
        surname = input("SURNAME: ")
        lesson = input("LESSON: ")
        midterm = input("MIDTERM: ")
        final = input("FINAL: ")

        im.execute("INSERT INTO sis(studentId,name, surname, lesson, midterm, final) VALUES (?,?, ?, ?, ?, ?)",
                  (studentId, name, surname, lesson, midterm, final))

        vt.commit()
        print("Student added successfully!")


#Bir öğrencinin tüm notlarını görüntüleme.
def showAllGrades():
    
    studentId=int(input("Enter the student id: "))
    im.execute('SELECT * FROM sis WHERE studentId = ?', (studentId,))
    rows = im.fetchall()
    if rows:
        headers = ["ID", "Student ID", "Name", "Surname", "Lesson", "Midterm", "Final"]
        print(tabulate(rows, headers=headers, tablefmt="grid"))
    else:
        print("No data found for the student ID:", studentId)

#Bir ööğrencinin belli bir ders bilgisini görünütleme:
def showLesson():
    
    studentId = int(input("Enter the student id: "))
    lesson = input("Enter the lesson: ").lower()  # Ders adını küçük harfe çevir
    im.execute('SELECT * FROM sis WHERE studentId = ? AND LOWER(lesson) = ?', (studentId, lesson))
    row = im.fetchone()
    if row:
        headers = ["ID", "Student ID", "Name", "Surname", "Lesson", "Midterm", "Final"]
        print(tabulate([row], headers=headers, tablefmt="grid"))
        midterm = row[5]
        final = row[6]
        print("Average of this lesson:", getAverage(midterm, final))
        print("Status:", isPass(getAverage(midterm, final)))
    else:
        print("No data found for the given student ID and lesson.")


def getAverage(midterm, final):
    avarage= (midterm*0.4) + (final*0.6)
    return avarage

def isPass(avarage):
    if avarage>59:
        print("SUCCESSFULL! :)")
    else:
        print("UNSUCCESSFULL :()")
    
def deleteInformation():
    studentId=input("STUDENT ID: ")
    lesson=input("LESSON: ").lower()  # Ders adını küçük harfe çevir
    deleting=im.execute('DELETE from sis WHERE studentID = ? AND LOWER(lesson) = ?', (studentId, lesson))
    if deleting.rowcount>0:
        print("DELETED...")
    else:
        print("Information not found for the given student ID and lesson.")

    vt.commit()
    
def saveToTextFile():
    try:
        # Default olarak projenin bulunduğu dizine kaydedilecek dosyanın adı
        file_name = "sis_data.txt"
        file_path = os.path.join(os.getcwd(), file_name)  # Dosya yolunu oluştur
        with open(file_path, 'w') as file:
            im.execute("SELECT * FROM sis")
            rows = im.fetchall()
            if rows:
                headers = ["ID", "Student ID", "Name", "Surname", "Lesson", "Midterm", "Final"]
                file.write(tabulate(rows, headers=headers, tablefmt="grid"))
                print("Data saved to", file_path)
            else:
                print("No data found in the database.")
    except Exception as e:
        print("An error occurred:", e)

menu=UI(["Add New Data.", "Show All Grades.", "Show Lesson Information", "Delete the information", "Add from JSON", "Save to Text File", "Exit"])

while True:
    menu.ShowMenu()
    choice = menu.GetChoise()
    if choice == 1:
        addStudent()
    elif choice == 2:
        showAllGrades()
    elif choice == 3:
        showLesson()
    elif choice == 4:
        deleteInformation()
    elif choice == 5:
        addFromJSON()
    elif choice == 6:
        saveToTextFile()
    elif choice == 7:
        break

