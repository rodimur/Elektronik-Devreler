# ************************
# ************************
# FED ac yükseltec hesapları için modül
# ************************

print("Bu Program , bir JFED veya Kanal Ayarlamalı  MOSFET ")
print("İçin dc öngerilim hesalarını ve ")
print("Şekil 10.23 ' teki gibi bir devre için ")
print("")
print("Aşağıdaki devre bilgilerini giriniz : ")
R1 = float(input("(Açık devre ise 1E30 kullanınız) RG1 = "))
R2 = float(input("RG2 = "))
RS = float(input("Toplam Kaynak Direnci , RS = "))
RD = float(input("RD = "))
print("")
DD = (float(input("BEsleme Gerilimi , VDD = ")))
print("Aşağıdaki eleman bilgilerini giriniz : ")
SS = float(input("Akaç-Kaynak doyma akımı , IDSS = "))
VP = float(input("Geçit-Kaynak kısmına gerilimi , VP = "))
print("")
# FET dc öngerilim hesaplamarı için modül 
GG = (R2 / (R1 + R2)) * DD
A = SS * RS / (VP * VP)
B = 1-(2 * SS * RS / VP)
C = (SS * RS) - GG
D = (B * B) - (4 * A * C)
if D < 0 :
    print("Çözüm Yok !!!")
import math
V1 = (-B + math.sqrt(D)) / (2 * A)
V2 = (-B - math.sqrt(D)) / (2 * A)
if abs(V1) > abs(VP):
    GS = V2
if abs(V2) > abs(VP):
    GS = V1
ID = SS * (1 - ((GS / VP) * (GS / VP)))
VS = ID * RS
VG = GG
VD = DD - (ID * RD)
DS = VD - VS
# Şimdi ön gerilim hesaplamarını yapalım 
print("Öngerilim Akımı , ID = " + str(ID * 1000) + " mA")
print("Öngerilimler : ")
print("VGS = " + str(GS) + " Volt")
print("VD = " + str(VD) + " Volt")
print("VS = " + str(VS) + " Volt")
print("VDS = " + str(DS) + " Volt")
print("")
print("Şimdi de ac yükselteç verilerini alalım : ")
print("")
RL = float(input("Yük Direnci (Yok ise IE30 alın) , RL = "))
VA = float(input("Kaynak Gerilimi , Vs = "))
RA = float(input("Kaynak Direnci , Rs = "))
S1 = float(input("Köprülenmiş Kaynak Direnci , RS1 = "))
# Module to do FET amplifier ac calculations
G0 = (2 * SS) / abs(VP)
GM = G0 * (1 - (GS / VP))
RM = 1 / GM
AV = -RD / (RM + S1)
RI = (R1 * R2) / (R1 + R2)
R0 = RD
VI = (RI * VA) / (RA + RI)
VL = (AV * VI) * (RL / (R0 + RL))
# Şimdi FET ac hesaplamarını Yapalım
print("")
print("Yükselteçin Gerilim kazancı , Av = " + str(AV))
print("Yük üzerindeki çıkış gerilimi = " + str(VL * 1000) + " mV")
print("")
print("Yükselteç katının giriş direnci , Ri = " + str(RI / 1000) + " Kiloohm")
print("Yükselteç katı çıkış direnci , Ro = " + str(R0 / 1000) + " Kiloohm")























