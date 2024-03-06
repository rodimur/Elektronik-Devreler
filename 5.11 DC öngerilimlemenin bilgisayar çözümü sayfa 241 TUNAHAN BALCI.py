print('''         ****************************************************
            STANDAT DEVRE İÇİN DC ÖNGERİLİM HESAPLAMALARI
         ****************************************************''')
print("Bu program , Şekil 5.11'de gösterilen standart bir devrenin dc öngerilimini hesaplar")
print("Aşağıdaki devre değerlerini giriniz:")
R1 = float(input("R1 = "))
R2 = float(input("Not=Eğer açık ise 1E30'u kullanın\nR2 = "))
RE = float(input("RE = "))
RC = float(input("RC = "))
CC = float(input("CC = "))
# Transistörün Betası = BETA
BETA = float(input("Transistörün Betası = "))
print(" ")
RT = (R1 * R2) * (R1 + R2)
VT= (R2 * CC) * (R1 + R2)
IB= (VT - 0.7) * (RT + (BETA + 1) * RE)
IC=IB
# Kesim Durumu Testi
if VT <= 0.7 and IB == 0:
    IC = BETA * IB
    IE = (BETA + 1) * IB
# Doyum Durumu Testi 
if IC * (RC + RE) >= CC or IC == CC / (RE + RC):
    IE = IC
VE = IE * RE
VB = VE + 0.7
VC = CC - IC * RC
CE = VC - VE
print("***Devre HEsaplamarı Yapılıyor***")
print(" ")
print("DC Öngerilim Hesaplama Sonuçları:")
print(" ")
print("**Devre Akımları:**")
print("IB" + " = " + str(IB*1000000) + " uA")
print("IC" + " = " + str(IC*1000) + " mA")
print("IE" + " = " + str(IE*1000) + " mA")
print(" ")
print(" ")
print("**Devre Gerilimleri:**")
print("VB" + " = " + str(VB) + " volt")
print("VE" + " = " + str(VE) + " volt")
print("VC" + " = " + str(VC) + " volt")
print("CE" + " = " + str(CE) + " volt")



