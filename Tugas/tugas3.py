def fibonacci(n):
    a, b = 0, 1
    hasil = []
    for _ in range(n):
        hasil.append(b)
        a, b = b, a + b
    return hasil

# Contoh penggunaan
jumlah = int(input("Masukkan jumlah deret Fibonacci: "))
deret = fibonacci(jumlah)
print("Deret Fibonacci:", ', '.join(map(str,deret)))