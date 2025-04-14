# PERULANGAN (LOOP)

# For-loop
# For-kondisi:
#   aksi

a = 0
a += 1 # a = a + 1
print(a)
a += 1 
print(a)
a += 1 
print(a)

angka_list = [0,1,4,8,10]
for i in angka_list:
    print(f"i sekaranng -> {i}")

print("ini akhir for 1 \n")


# perulangan dengan range
angka_range = range(5) # diulang 5 kali
for i in angka_range:
    print(f"i sekarang -> {i}")

print("ini akhir for 2 \n")

angka_range1 = range(1,10)
for i in angka_range1:
    print(f"i sekarang -> {i}")

print("ini akhir for 3 \n")

data_str = "Pendidikan Mandalika"
for huruf in data_str:
    print(huruf)

print("ini perulangan string\n")