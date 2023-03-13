# DONE: Python'da Veri Tiplerini araştırınız, her bir veri tipi için kendi cümlelerinizle açıklamalar yazınız.
# TODO: Kodlama.io sitesinde değişken olarak kullanıldığını düşündüğünüz verileri, veri tipleriyle birlikte örneklendiriniz.
# TODO: Kodlama.io sitesinde şart blokları kullanıldığını düşündüğünüz kısımları örneklendiriniz ve Python dilinde bu örnekleri koda dökünüz.

#String (str) : Metinsel ifadeler.
#Int : Tam sayili ifadeler.
#Float : Ondalikli sayili ifadeler.
#Bool : Mantiksal ifadeler (True/False)
#List : Birdne cok veriyi tutabilen veri tipi.
#Dictionary : Key value iliskisini kullanan veri tipi.

#"Bitir ve devam et , onceki ders, bitir ve devamet" butonlari bool veri tipine ornektir.
#Anasayfadaki kategori ve egitmen birer listedir.



Email = 'ayk123@gmail.com'
Pass = '1234'

EnterMail = input('Mail adresiniz: ')
EnterPass = input('Sifreniz : ')

if (EnterMail == Email and EnterPass == Pass):
    print('Giris basarili')
else:
    print("Hatali sifre veya mail lutfen tekrar deneyiniz")