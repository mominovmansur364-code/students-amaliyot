#Muhammadbilol
qidiruv=input("Talaba ID sini kiriting: ")

with open("students.txt","r") as f:
    data=f.readlines()

    for i in data:
        i = i.split(",")
        if i[0]==qidiruv:
            print(f"ID {i[0]} {i[1]}")
            break
    else:
        print("Bunday ID li talaba mavjud emas!")