

mevalar = {}

for _ in range(5):
    nomi = input("Meva nomini kiriting: ")
    narxi = int(input(f"{nomi} narxini kiriting: "))
    mevalar[nomi] = narxi

print(mevalar) 

mevalar = {'olma': 12000, 'banan': 25000, 'gilos': 20000, 'shaftoli': 16000, 'uzum': 23000}

meva_nomi = input("Meva nomini kiriting: ")

if meva_nomi in mevalar:
    print(mevalar[meva_nomi]) 
else:
    print("Bunday meva yo'q.")

oquvchilar = {
    'Ali': 'Aliyev',
    'Oygul': 'Rahmonova',
    'Rustam': 'Asqarov',
    'Gulnora': 'Toshbekova',
    'Sarvar': 'Khamidov'
}

ism = input("O'quvchining ismini kiriting: ")

if ism in oquvchilar:
    del oquvchilar[ism]
    print(f"{ism} o'chirildi.")
else:
    print("Bunday ismli o'quvchi yo'q.")
