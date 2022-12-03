row1 = [1, 2, 3]
row2 = [2, 8, 7]
row3 = [1, 5, 6]

print(row1)
print(row2)
print(row3)

det = (row1[0]*row2[1]*row3[2]+
       row1[1]*row2[2]*row3[0]+
       row1[2]*row2[0]*row3[1]-
       row1[2]*row2[1]*row3[0]-
       row1[0]*row2[2]*row3[1]-
       row1[1]*row2[0]*row3[2])
print("Determinan Matriks: ", det)

a11 = row2[1]*row3[2]-row2[2]*row3[1]
a12 = (-1*((row2[0]*row3[2])-(row2[2]*row3[0])))
a13 = row2[0]*row3[1]-row2[1]*row3[0]

a21 = (-1*((row1[1]*row3[2])-(row1[2]*row3[1])))
a22 = row1[0]*row3[2]-row1[2]*row3[0]
a23 = (-1*((row1[0]*row3[1])-(row1[1]*row3[0])))

a31 = row1[1]*row2[2]-row1[2]*row2[1]
a32 = (-1*((row1[0]*row2[2])-(row1[2]*row2[0])))
a33 = row1[0]*row2[1]-row1[1]*row2[0]

print("\nKofaktor Matriks: ")
print("|", a11, a12, a13, "|")
print("|", a21, a22, a23, "|")
print("|", a31, a32, a33, "|")

print("\nAdjoin Matriks: ")
print("|", a11, a21, a31, "|")
print("|", a12, a22, a32, "|")
print("|", a13, a23, a33, "|")

print("\nInvers Matriks: ")
print("|", round(1/det*a11, 2), round(1/det*a21, 2), round(1/det*a31, 2), "|")
print("|", round(1/det*a12, 2), round(1/det*a22, 2), round(1/det*a32, 2), "|")
print("|", round(1/det*a13, 2), round(1/det*a23, 2), round(1/det*a33, 2), "|")

# TANPA PEMBULATAN
# print("\nInvers Matriks: ")
# print("|", 1/det*a11, 1/det*a21, 1/det*a31, "|")
# print("|", 1/det*a12, 1/det*a22, 1/det*a32, "|")
# print("|", 1/det*a13, 1/det*a23, 1/det*a33, "|")