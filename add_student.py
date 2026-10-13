with open("students.txt", 'a') as file:
    ism = input("Ism: ")
    id = input("ID: ")
    
    file.write(f"ism: {ism}\n")
    file.write(f"ID: {id}\n")