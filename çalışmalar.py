"""
Problem 1
Elinizde bir dikdörtgenin kenarlarını ifade eden sayı çiftlerinin bulunduğu bir liste olsun.

         [(3,4),(10,3),(5,6),(1,9)]

Şimdi kenar uzunluklarına göre dikdörtgenin alanını hesaplayan bir fonksiyon yazın ve bu listenin her bir elemanına bu fonksiyonu uygulayarak ekrana şöyle bir liste yazdırın.

         [12, 30, 30, 9]

Not : map() fonksiyonunu kullanmaya çalışın.

Problem 2
Elinizden her bir elemanı 3'lü bir demet olan bir liste olsun.

     [(3,4,5),(6,8,10),(3,10,7)]

Şimdi kenar uzunluklarına göre bu kenarların bir üçgen olup olmadığını dönen bir fonksiyon yazın ve sadece üçgen belirten kenarları bulunduran listeyi ekrana yazdırın.

     [(3, 4, 5), (6, 8, 10)]

Not: filter() fonksiyonunu kullanmaya çalışın.

Problem 3
Elinizde şöyle bir liste bulunsun.

    [1,2,3,4,5,6,7,8,9,10]

Bu listenin içindeki çift sayıların toplamını ekrana yazdıran bir fonksiyon yazın.

Not: İlk önce filter() fonksiyonu ile çift sayıları ayıklayın. Daha sonra reduce() fonksiyonunu kullanın.

Problem 4
Elinizde isimlerin ve soyisimlerin bulunduğu iki tane liste olsun.

        isimler -----> ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]

        soyisimler -----> ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

Bu isimleri ve soyisimleri sırasıyla eşleştirin ve ekrana alt alta isimleri ve soyisimleri yazdırın.

Not: zip() fonksiyonunu kullanmaya çalışın.

#problem1
liste = [(3,4),(10,3),(5,6),(1,9)]
liste2 = []
def alan_hesaplama():
    for x,y in liste:
        liste2.append(x*y)
    print(liste2)


#problem2
alan_hesaplama()

liste = [(3,4,5),(6,8,10),(3,10,7)]

def triangle(tuple):
    if tuple[2]-tuple[0]<tuple[1]<tuple[2]+tuple[0]:
        return True
    else:
        return False

print(list(filter(triangle,liste)))



#problem3

from functools import reduce

liste = [1,2,3,4,5,6,7,8,9,10]

filter_double = list(filter(lambda x: x % 2 == 0,liste))

print(reduce(lambda x,y:x+y,filter_double))



#problem4


isimler = ["Kerim", "Tarık", "Ezgi", "Kemal", "İlkay", "Şükran", "Merve"]

soyisimler = ["Yılmaz", "Öztürk", "Dağdeviren", "Atatürk", "Dikmen", "Kaya", "Polat"]

for i,x in zip(isimler,soyisimler):
    print(i,x)




karmaşık = "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"

liste = dict()

for i in karmaşık:
    if i in liste:
        liste[i] += 1
    else:
        liste[i] = 1

for i,z in liste.items():
    print("{}-----> {}".format(i,z))







with open("şiir.txt","r",encoding="utf-8") as file:
    baş_harfler = ""
    for i in file:

        baş_harfler += i.split()[0][0]

print(baş_harfler)





with open("email.txt","r",encoding="utf-8") as file:


    for i in file:

        if i.endswith(".com\n") and i.find("@") != -1:
            print(i)


isim =["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]

soyisim = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]



list = list(zip(isim,soyisim))

list.sort()
for i,j in list:
    print(i,j)
"""






















