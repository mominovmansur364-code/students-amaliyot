#Azizjon

with open("sudents.txt", "r", encoding="utf-8") as fayl:
    talabalar = fayl.readlines()

print("-" * 35)
print("       O'QUVCHILAR RO'YXATI          ")
print("-" * 35)

for raqam, talaba in enumerate(talabalar, 1):
    ism_familiya = talaba.strip().split()

    if len(ism_familiya) >= 2:
        ism = ism_familiya[0]
        familiya = " ".join(ism_familiya[1:])

        print(f"{raqam}. Ismi: {ism}")
        print(f"   Familiyasi: {familiya}")
        print("-" * 35)

print(f"Jami o'quvchilar soni: {len(talabalar)} ta")