from googletrans import Translator
import argparse

translator = Translator(service_urls=[
      'translate.google.com',
      'translate.google.com.tr',
    ])

class Dosya():

    def __init__(self, file_name):
        """at beginning, open file and returns simplified words list"""

        with open(file_name,"r",encoding="utf-8") as file: #okunacak dosyamızı açtık.

            dosya_icerigi = file.read()#dosya içeriğini okuduk ve bir değişkene attık.

            kelimeler = dosya_icerigi.split()#içerikteki metinde geçen kelimelerin hepsini ayrı ayrı alabilmek için
                                             #boşluk filtresini kullandık ve her bir kelimeyi dizeye attık.
                                            #hiçbir şey vermediğimiz içim boşluğa göre ayıracak.


            self.sade_kelime_list = list() #kelimeleri sadeleştirdikten sonra bu listeye atacağız.
            self.kelime_set = set() #sade_kelimeler üzerinde gezinip elemanları kümeye atacağız. Böylece birden fazla olan
                                     #elemanlar yazılmayacak.
            self.kelime_frekans_dict= dict()  #kelimeler ve tekrarlanma sayılarını birlikte girmek için bir sözlük oluşturduk.
            self.frekans_sort_list = list()  # sıralama için en son kelime ve tekrarlanma sayılarını buraya atacağız.


            for i in kelimeler:

                #sadeleştirmeler
                i=i.strip("\n") #strip baştan ve sondan bu karakteri siler.

                i = i.strip(" ")

                i = i.strip(".")

                i = i.strip(",")

                i = i.strip('“')

                i= i.strip('”')

                i= i.strip('?')

                i= i.lower()

                self.sade_kelime_list.append(i)


    def tum_kelimeler(self):
        """Get the simplified list and returns the set of words """

        for i in self.sade_kelime_list:

            self.kelime_set.add(i) #sade_kelimeler listesinde gezinerek tüm elemanları kümeye atıyoruz. Aynı olanlar atılmıyor.



    def kelime_frekansi(self):
        """Get the simplified list and returns the frequency list of words """

        for i in self.sade_kelime_list:

            if (i in self.kelime_frekans_dict): #i kelimesi kelime_sozluk'te var mı varsa değeri 1 arttır.

                self.kelime_frekans_dict[i] += 1

            else:
                self.kelime_frekans_dict[i] = 1 #eğer yoksa o kelimeyi ekle ve değerini 1 olarak ata.


    def en_fazla_kelime(self):
        """Get the frequency list of words and returns the most used word """

        self.kelime_frekansi()

        kelime_sozluk_deger = list(self.kelime_frekans_dict.items())#kelime_sozluk sözlüğündeki her 2 parametreyi 2 parametre
                                                                #1  demet olması ve her demet de liste oluşturması için
                                                                #listeye dönüştürüyoruz.


        for j in range(1,len(kelime_sozluk_deger)):#kelime tekrarlanma sayılarını sıralamak için liste boyutu kadar döngüye
                                                    #sokuyoruz. Böylece tüm elemanlar birbiriyle karşılaştırılacak.

            enbuyukindis = 0 # en büyük indisi tutacak.

            for i in range(1,len(kelime_sozluk_deger)):#her bir eleman bir demek demiştik. Burada kaç tane demek varsa
                                                    # ,ki bu da liste boyutuna eşit, 1.indislerini karşışatırıyoruz.

                a=int(kelime_sozluk_deger[i][1])#her el yeni indisli elemanı tutacak.
                b=int(kelime_sozluk_deger[enbuyukindis][1])#her el büyük indisli tutacak
                if a > b:
                    enbuyukindis = i
                else:
                    enbuyukindis = enbuyukindis


            self.frekans_sort_list.append((kelime_sozluk_deger[enbuyukindis][0],kelime_sozluk_deger[enbuyukindis][1]))
            #en büyük indisi ve o kelimeyi bir listeye   atar. Böylece en çok tekrarlanan kelime ile tekrarlanma sayısı
            #listeye bir atılır.

            kelime_sozluk_deger.pop(enbuyukindis)#en büyüğü bulduktan sonra listeden çıkartılır ve yeni listedeki en
            #büyük bulunur. Böylece listede hiç eleman kalmayıncaya kadar tüm elemanları büyükten küçüğe sıralar.


    def kelime_varmi(self,word):
        """checks whether the given word is mentioned in the text or not"""

        #girilen = input("Lütfen aramak istediğiniz kelimeyi yazın: ")
        girilen = word

        adet = 0

        for i in self.sade_kelime_list:

            if i == girilen:
                adet += 1

        if adet == 0:
            print("Girlien kelime dosyada geçmiyor....")
        else:
            print("Girilen kelime '{}' dosyada {} defa geçer..".format(girilen, adet))


ap = argparse.ArgumentParser()
ap.add_argument("-fr", "--frequency", required=False, help="tpye 'frekans' and enter")
ap.add_argument("-w", "--word", required=False, help="Enter a word")
ap.add_argument("-f", "--file", required=False, help="Enter txt file")

args = vars(ap.parse_args())

if args["file"]:
    file_name_txt = args["file"]
    file_name_split = file_name_txt.split(".")
    if len(file_name_split) > 1 and file_name_split[2] == "txt":
        file_name = file_name_split[0]
    elif len(file_name_split) == 1:
        file_name = file_name_txt
        file_name_txt = file_name_txt + '.txt'
    else:
        print("Maalesef dosya tipi geçersiz...")
        exit()
else:
    file_name_txt = "ing1.txt"
    file_name = "ing1"


dosya = Dosya(file_name_txt)
#print("********************************************************")
#print("Sade Kelimeler: ",dosya.sade_kelime_list)
#print("********************************************************")
dosya.tum_kelimeler()
#print("Kelimeler Kumesi: ",dosya.kelime_set)
#print("********************************************************")
dosya.kelime_frekansi()
#print("Kelime Frekans Sözlük: ",dosya.kelime_frekans_dict)
#print("********************************************************")
dosya.en_fazla_kelime()
#print("Sıralanmış Kelime Frekans Sözlük: ",dosya.frekans_sort_list)
#print("********************************************************")

if args["frequency"] == "frekans":
    for i in dosya.frekans_sort_list:
        print(i)
    exit()

if args["word"]:
    dosya.kelime_varmi(args["word"])
    exit()



word_frequency_file = file_name + '_word_frequency.txt'
word_frequency = open(word_frequency_file, "w")
word_frequency.write(
    "Sade Kelimeler:\n" + str(dosya.sade_kelime_list)
    + "\nKelimeler Kumesi:\n" + str(dosya.kelime_set)
    + "\nKelime Frekans Sözlük:\n" + str(dosya.kelime_frekans_dict)
    + "\nSıralanmış Kelime Frekans Sözlük:\n" + str(dosya.frekans_sort_list)
)
word_frequency.close()

print("Bilgiler word_frequency.txt dosyasına yazıldı... ")
print("")
print("İsterseniz -h yazarak kullanılabilen argümanları görebilirsiniz. ")
print("")
print("Kelimeler Türkçeye çevriliyor... ")


transliste = list(dosya.kelime_set)

translations = translator.translate(transliste, dest='tr')

#for translation in translations:
#	print(translation.origin, ' -> ', translation.text)

word_translate_file = file_name + '_word_translate.txt'
word_translate = open(word_translate_file, "w")
for translation in translations:
    word_translate.write(translation.origin + ' -> ' + translation.text + '\n')
word_translate.close()

print("")
print(" Kelimelerin türkçe anlamları word_translate.txt dosyasına yazıldı... ")
