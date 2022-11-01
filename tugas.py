#wadah matriks 3x3
b = [[0,0,0],
     [0,0,0],
     [0,0,0]]

#user input
for i in range(len(b)):
    for j in range(len(b)):
        b[i][j] = int(input(f"Masukkan Nilai Untuk Matriks Posisi {i+1}, {j+1}: "))

#output matriks 3x3
print("Matriks: ")
for h in b:
    print(h)
    
#kalkulasi determinan matriks 3x3
x = ((b[0][0]*b[1][1]*b[2][2]) + (b[0][1]*b[1][2]*b[2][0]) + (b[0][2]*b[1][0]*b[2][1]))
y = ((b[2][0]*b[1][1]*b[0][2]) + (b[2][1]*b[1][2]*b[0][0]) + (b[2][2]*b[1][0]*b[0][1]))
hasil= x - y

#hasil
print(f"Hasil Determinan Matriks 3x3 adalah: {hasil}")