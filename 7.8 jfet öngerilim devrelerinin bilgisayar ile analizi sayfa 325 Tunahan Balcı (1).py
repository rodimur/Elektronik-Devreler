print('''         ***************************************
            FET dc Ongerilim Hesaplama Modulu
         ***************************************''')
print("Bu program , sekil 7.43'deki gibi ")
print("JFET veya kanal ayarlamali MOSFET devresi icin dc ongerilimini hesaplar")
print()
print("Asagidaki devre degerlerini giriniz:")
R1 = float(input("Not = Eger acik ise 1E30'u kullanin\nR1 = "))
R2 = float(input("R2 = "))
RS = float(input("RS = "))
RD = float(input("RD = "))
print()
DD = float(input("Kaynak Gerilimi = "))
print()
print("Asagidaki transistor degerlerini giriniz : ")
SS = float(input("Akac - Kaynak doyma akimmi = "))
VP = float(input("Kapi - Kaynak kisma gerilimi = "))
print()
# FET dc Ongerilim Hesaplama Modulu
GG = (R2 / (R1 + R2)) + DD
A = SS * RS / (VP * VP) 
B = 1 - 2 * SS * RS / VP
C = SS * RS - GG
D = (B * B) - 4 * A * C
if D < 0 :
    print("Cozum yok !!!")
import math
V1 = (- B + math.sqrt(D)) / (2 * A)
V2 = (- B - math.sqrt(D)) / (2 * A)
if abs(V1) > abs(VP):    
    GS = V2
if abs(V2) > abs(VP):    
    GS = V1
ID = SS * (1 - GS / VP) * (1 - GS / VP)
VS = ID * RS
VG = GG
VD = DD - ID * RD
DS = VD - VS

print("Ongerilim akimi ID = " + str(ID*1000) + " mA")
print("Ongerilim voltaj degerleri :")
print("VGS = " + str(GS) + " volt")
print("VD = " + str(VD) + " volt")
print("VS = " + str(VS) + " volt")
print("VDS = " + str(DS) + " volt")