# OOP
class Student:
    def __init__(self, name, surname, email, phone, code):
        self.telebead=name.capitalize()
        self.telebesoyad=surname.capitalize()
        self.telebemail=email.capitalize()
        self.telebetelefon=phone
        self.telebekod=code

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
# FUNCTIONS

# Main functions of program
# Koda uyğun məlumatı silmək
def KodaGoreSil(silkod):
    KodaGoreSilVar=False
    for i in students:
        if i.telebekod==silkod:
            students.remove(i)
            KodaGoreSilVar=True
    if not KodaGoreSilVar:
        print("Belə bir tələbə yoxdur !")
# Koda uyğun məlumatı dəyişmək
def KodaGoreDeyis(deyiskod):
    deyisKodVar=True
    for i in students:
        if i.telebekod==deyiskod:
            name=input("Tələbə adı : ").lower()
            name=BosluqlariDoldur(name)
            name=UzunluguYoxla(name, 2)
            name=HerfleriYoxla(name, "ad")
            surname=input("Tələbə soyadı : ").lower()
            surname=BosluqlariDoldur(surname)
            surname=UzunluguYoxla(surname, 2)
            surname=HerfleriYoxla(surname, "soyad")
            email=input("Tələbə e-poçtu : ").lower()
            email=BosluqlariDoldur(email)
            email=UzunluguYoxla(email, 3)
            email=EmailYoxla(email)
            phone=input("Tələbə telefon nömrəsi : ")
            phone=BosluqlariDoldur(phone)
            phone=TelefonNomresiYoxla(phone)
            i.telebead = name.capitalize()
            i.telebesoyad = surname.capitalize()
            i.telebemail = email.capitalize()
            i.telebetelefon = phone
            break
        else:
            deyisKodVar=False
    if not deyisKodVar :
        print("Belə bir tələbə mövcud deyil")
#Ada uyğun məlumat göndərmək
def AdaGoreGoster(gosterad):
    AdaGoreGosterVar=False
    for i in students:
        AdaGoreGosterVar=True
        if i.telebead==gosterad.capitalize():
            print('''Tələbə Adı : {}
Tələbə Soyadı : {} 
Tələbə e-poçtu : {}
Tələbə telefon nömrəsi : {}
Tələbə kodu : {}'''.format(i.telebead, i.telebesoyad, i.telebemail, i.telebetelefon, i.telebekod))
    if AdaGoreGosterVar==False:
        print("Bu adlı bir tələbə yoxdur")
# Bütün məlumatları göstərmək
def ButunGoster():
    for i in students:
        print('''{} kodlu tələbə haqqında məlumatlar : 
Tələbə Adı : {}
Tələbə Soyadı : {} 
Tələbə e-poçtu : {}
Tələbə telefon nömrəsi : {}
Tələbə kodu : {}'''.format(i.telebekod, i.telebead, i.telebesoyad, i.telebemail, i.telebetelefon, i.telebekod))

# Common functions
def MuracietDaxilEtmek():
    global operation
    operation=input('''Nə etmək istəyirsiniz?
Açar sözlər haqqında ətraflı məlumat üçün "məlumat" daxil edin : ''').lower()
# Açar sözlər haqqında ətraflı məlumat
def EtrafliMuraciet():
    global operation
    operation=input('''Əgər tələbə əlavə edəcəksinizsə, "əlavə",
Əgər xüsusi tələbə məlumatlarını siləcəksinizsə, "sil",
Əgər xüsusi tələbə məlumatlarını dəyişəcəksinizsə, "dəyiş" ,
Əgər xüsusi tələbə məlumatlarını görmək istəyirsinizsə, "tələbə",
Əgər bütün tələbələrin məlumatlarını görmək istəyirsinizsə,"bütün", 
Əgər proqramı ləğv etmək istəyirsinizsə, "çıx",
açar sözlərindən birini daxil edin : ''').lower()
# Input validation
# Daxil olunan dəyərin boş olub-olmadığını yoxlayır
def BosluqlariDoldur(x):
    while not x:
        x=input("Zəhmət olmasa boşluqları doldurun : ")
    return x
# Daxil olunan tələbə kodunun düzgünlüyünü yoxlayır
def TelebeKodunuYoxla(x):
    for i in students:
         if x==i.studentcode:
            x=input("This ID is already taken. Enter new ID : ")
    while not x.isdigit() or len(x) != 3:
        x = input("Please enter 3 digits of positive number : ")
    else:
        print("You added a new student successfully !")
    return x
# Daxil olunan email adresi yoxlayır
def EmailYoxla(x):
    EmailIsaresi=False
    for i in x[1:]:
        if i=="@":
            EmailIsaresi=True
            break
    while not EmailIsaresi:
        x=input("Zəhmət olmasa düzgün e-poçt daxil edin : ")
        BosluqlariDoldur(x)
        UzunluguYoxla(x, 3)
        EmailIsaresi=False
        for i in x:
            if i=="@":
                EmailIsaresi=True
                break
    return x
# Daxil olunan telefon nömrəsini yoxlayır
def TelefonNomresiYoxla(x):
    x="".join(x.split(" "))
    while len(x)!=13 and x[:4]!="+994" and not x[1:].isdigit():
        x=input("Zəhmət olmasa düzgün Azərbaycan nömrəsi daxil edin : ")
        x="".join(x.split(" "))
    return x
# Daxil olunan dəyərlərin uzunluğunu yoxlayır
def UzunluguYoxla(x, uzunluqlimiti):
    while len(x)<uzunluqlimiti:
        x=input("Məlumatı tam daxil edin : ")
        BosluqlariDoldur(x)
    return x
# Daxil olunan dəyərin yalnız hərflərdən ibarət olub-olmadığını yoxlayır
def HerfleriYoxla(x, str):
    while not x.isalpha():
        x=input("Zəhmət olmasa düzgün {} daxil edin : ".format(str))
    return x
# THE PROCESS

# Entry point
students=[]
print("Tələbə idarəetmə proqramına xoş gəlmişsiniz.")
MuracietDaxilEtmek()

# Workflow of program
while operation!="cix" and operation!="çıx":
    if operation=="elave" or operation=="əlavə":
        print("Yeni bir tələbə əlavə etmək üçün aşağıdakı boşluqları doldurun.")
        name=input("Tələbə adı : ").lower()
        name=BosluqlariDoldur(name)
        name=UzunluguYoxla(name, 2)
        name=HerfleriYoxla(name, "ad")
        surname=input("Tələbə soyadı : ").lower()
        surname=BosluqlariDoldur(surname)
        surname=UzunluguYoxla(surname, 2)
        surname=HerfleriYoxla(surname, "soyad")
        email=input("Tələbə e-poçtu : ")
        email=BosluqlariDoldur(email)
        email=UzunluguYoxla(email, 3)
        email=EmailYoxla(email)
        phone=input("Tələbə telefon nömrəsi : ")
        phone=BosluqlariDoldur(phone)
        phone=TelefonNomresiYoxla(phone)
        code=input("Tələbə kodu(3 rəqəmli bir ədəd olmalıdır) : ")
        code=BosluqlariDoldur(code)
        code=TelebeKodunuYoxla(code)
        student=Student(name, surname, email, phone, code)
        students.append(student)
        MuracietDaxilEtmek()
    elif operation=="sil":
        silkod=input()
        KodaGoreSil(silkod)
        MuracietDaxilEtmek()
    elif operation=="deyis" or operation=="dəyiş":
        deyiskod=input("Məlumatlarını dəyişmək istədiyiniz tələbənin kodunu daxil edin : ")
        KodaGoreDeyis(deyiskod)
        MuracietDaxilEtmek()
    elif operation=="telebe" or operation=="tələbə":
        gosterad=input("Məlumatını görmək istədiyiniz tələbənin adını daxil edin : ").lower()
        AdaGoreGoster(gosterad)
        MuracietDaxilEtmek()
    elif operation=="butun" or operation=="bütün":
        ButunGoster()
        MuracietDaxilEtmek()
    elif operation=="melumat" or operation=="məlumat":
        EtrafliMuraciet()
    else:
        operation=input("Doğru açar söz daxil edin : ").lower()
else:
    print("Tələbə idarəetmə proqramını işlətdiyiniz üçün təşəkkürlər")
    pass


