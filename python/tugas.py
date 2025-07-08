# Variabel & Tipe Data
name = "Haikal"
age = 16
height = 1.75
is_student = True
print(f"Nama: {name}, Umur: {age}, Tinggi: {height}, Siswa: {is_student}")

# Input & Output
user_input = input("Masukkan nama Anda: ")
print("Halo, " + user_input)

# Operasi Aritmatika
x, y = 10, 3
print(f"Penjumlahan: {x + y}, Pangkat: {x ** y}, Modulus: {x % y}")

# Percabangan
if age >= 18:
    print("Anda sudah dewasa.")
else:
    print("Anda masih remaja.")

# Looping
for i in range(1, 6):
    print(f"Perulangan ke-{i}")

i = 1
while i <= 5:
    print(f"While Loop ke-{i}")
    i += 1

# List, Tuple, Dictionary
data_list = ["Python", "C++", "Java"]
data_tuple = (10, 20, 30)
data_dict = {"nama": "Haikal", "umur": 16}
print(data_list[0], data_tuple[1], data_dict["nama"])

# Fungsi & Rekursi
def faktorial(n):
    return 1 if n == 0 else n * faktorial(n - 1)
print(f"Faktorial 5: {faktorial(5)}")

# OOP (Class & Object)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        return f"Halo, nama saya {self.name} dan saya {self.age} tahun."
haikal = Person("Haikal", 16)
print(haikal.greet())

# Exception Handling
try:
    num = int(input("Masukkan angka: "))
    print(f"Angka yang dimasukkan: {num}")
except ValueError:
    print("Harap masukkan angka valid!")

# File Handling
with open("sample.txt", "w") as file:
    file.write("Belajar Python itu seru!")
with open("sample.txt", "r") as file:
    print(file.read())

# Bitwise Operator
a, b = 5, 3
print(f"AND: {a & b}, OR: {a | b}, XOR: {a ^ b}, Shift Left: {a << 1}")

# Compile ke .pyc
import py_compile
py_compile.compile("your_script.py")
