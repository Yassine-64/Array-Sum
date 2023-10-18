N = int(input("veuillez entrez la taille des tableaux: "))

T1 = [0] * N
T2 = [0] * N
TS = [0] * N

for i in range(N):
    T1[i] = int(input("veuiller entrer la valeur de T1:"))
for j in range(N):
    T2[j] = int(input("veuiller entrer la valeur de T2:"))

for i in range (N):
    TS[i] = T1[i] + T2[j]

print("le tableau TS a la somme:", TS)