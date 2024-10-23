def Temperatur (Value, Unit):
    if Unit == 'C':
        return (Value * 9/5) + 32 
    elif Unit == 'F':
        return (Value - 32) * 5/9  
    else:
        return "Satuan tidak valid. Gunakan 'C' untuk Celsius atau 'F' untuk Fahrenheit."
    
NilaiSuhu = float(input("Masukan nilai suhu:"))
satuanSuhu= input("Masukan unit suhu ('C' untuk Celcius, 'F' untuk Fahrenheit):")

Hasiltemperatur =Temperatur(NilaiSuhu, satuanSuhu)
print("Hasil Temperatur suhu: ", Hasiltemperatur)



import math

# Fungsi lambda untuk menghitung luas lingkaran menggunakan math.pi
luas_lingkaran = lambda jarijari: math.pi * jarijari ** 2

# Menerima input dari pengguna
jarijari = float(input("Masukkan jari-jari lingkaran: "))

# Menghitung dan menampilkan hasil luas
luas = luas_lingkaran(jarijari)
print("Luas lingkaran dengan jari-jari", jarijari, "adalah:", luas)
