# DONE:Bir öğrenci kayıt sistemi yazdığımızı düşünelim. Sistemimizdeki öğrencileri bir listede sadece ad soyad olacak şekilde tutalım.
# DONE:Bu öğrenci kayıt sistemine;
# DONE:Aldığı isim soy isim ile listeye öğrenci ekleyen
# DONE:Aldığı isim soy isim ile eşleşen değeri listeden kaldıran
# DONE:Listeye birden fazla öğrenci eklemeyi mümkün kılan
# DONE:Listedeki tüm öğrencileri tek tek ekrana yazdıran
# DONE:Öğrencinin listedeki index numarası öğrenci numarası olarak kabul edildiğini düşünerek öğrencinin numarasını öğrenmeyi mümkün kılan
# DONE:Listeden birden fazla öğrenci silmeyi mümkün kılan (döngü kullanınız)
# DONE:fonksiyonları geliştiriniz ve her bir fonksiyonu en az bir kere çağırarak konsolda test ediniz.
# DONE:Ödevde kullanacağınız döngülerin bir tanesi for bir tanesi while döngüsü olması istenmektedir.


students = []

def add_student(name):
    print("----------####----------")
    students.append(name.capitalize())
    print(name.capitalize(), "Listeye eklendi. ")

def delete_student(name):
    print("----------####----------")
    if name in students:
        students.remove(name)
        print(name.capitalize(), "Listeden silindi. ")
    else:
        print(name.capitalize(), "ismindeki ogrenci listede bulunamadi. ")


def add_multi_student():
    print("----------####----------")
    while True :
        names = input("Lutfen eklemek istediginiz ogrenci isminini giriniz. (Cikis yapmak istiyorsaniz 'N' tusuna basip cikis yapiniz): ")
        if names.lower() == 'n':
            break
        else:
            add_student(names.capitalize())
            print(names.capitalize(), "Basariyla eklendi. ")

def delete_multi_student():
    print("----------####----------")
    while True:
        names = input("Lutfen silmek istediginiz ogrenci isminini giriniz. (Cikis yapmak istiyorsaniz 'N' tusuna basip cikis yapiniz): ")
        if names.lower() == 'n':
            break
        else:
            delete_student(names)

def print_list():
    print("----------####----------")
    for student in students:
        print(student.capitalize())


def print_student_no(student):
    print("----------####----------")
    if student in students:
        no = student.index(student) + 1
        print(f"{student} isimli ogrencinin numarasi: {no}. ")
    else:
        print(f"{student} isimli ogrenci listede bulunamadi. ")




add_student("hasan kilic")
add_student("Nazli aslan")
add_student("Ahmet hakan")
print_list()
delete_student("hasan kilic")
add_multi_student()
print_list()
print_student_no("hasan hepi")