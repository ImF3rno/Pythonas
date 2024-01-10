# petriuko pazymiai, suvedam, atspausdinam, apskaiciuojame vidurki, mamai rodome didesnius uz 3, teciui didesnius uz 5
# gavome uzsakyma visai klasei padaryti

MAMA=4
TETIS=6
# =============================== Pazymiu kiekis =================================================
def numbersofGrades(name):
    numbersGrades=int(input(f'Kiek {name} turi pazymiu...'))
    return numbersGrades
# =================================================================================================

# =============================== Pazymiu grazinims ===============================================
def getGrades(numbersGrades,name):
    grades=[]
    i=0
    while i<numbersGrades:
        grade=int(input(f'Iveskite {name} {i+1}-aji pazymi...'))
        if 1<=grade<=10:
            grades.append(grade)
            i=i+1
        else:
            print('Blogas pazimys. Veskite kita')
    return grades
# ================================================================================================

# =============================== Vidurkis =======================================================
def averages(grades):
    if len(grades)==0:
        return 0
    else:
        return sum(grades)/len(grades)
# =================================================================================================

# =============================== Pazymiai tevams =======================================================
def parents(grades,critiks):
    parentsGrades=[]
    for i in grades:
        if i>=critiks:
            parentsGrades.append(i)
    return parentsGrades
# =================================================================================================

# =============================== Vidurkis =======================================================
def results(name):
    grades=getGrades(numbersofGrades(name),name)
    pazM=parents(grades,MAMA)
    pazTec=parents(grades,TETIS)
    print(f'{name} pazymiai yra {grades}, vidurkis {averages(grades)}')
    print(f'{name} mamai pazymiai yra{pazM}, vidurkis {averages(pazM)}')
    print(f'{name} teciui pazymiai yra {pazTec}, vidurkis {averages(pazTec)}')
# =================================================================================================

klase=['Petras','Antanas','Jonas','Martynas','Stasys','Maryte','Ona']
for i in klase:
    results(i)