#HENDRA USMAN (D0221079)

#wadah matriks 3x3
b = [[1,2,2],
     [-2,1,0],
     [7,-9,3]]
    
#kalkulasi determinan matriks 3x3
x = ((b[0][0]*b[1][1]*b[2][2]) + (b[0][1]*b[1][2]*b[2][0]) + (b[0][2]*b[1][0]*b[2][1]))
y = ((b[2][0]*b[1][1]*b[0][2]) + (b[2][1]*b[1][2]*b[0][0]) + (b[2][2]*b[1][0]*b[0][1]))
hasil= x - y

#hasil
print(f"Hasil Determinan Matriks 3x3 adalah: {hasil}")