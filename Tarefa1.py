import math
print("\n\n#=============================Enunciado=========================================")

print("\n\nDados um motor de indução trifásico de 6 polos, ")
print("60 Hz e 25 hp passou pelos seus ensaios tradicionais  e ")
print(" deles foram obtidos os seguintes dados: ")

p = 6
f = 60
pmec = 25

print(" - Ensaio de corrente contínua: 13,5 V e 64 A;")
print(" - Ensaio de Rotor Bloqueado: 24,6 V a 15 Hz, 64 A e 2200 W;")
print(" - Ensaio a Vazio: 208 V, 24 A e 1400 W.") 
print()
Vcc = 13.5
Icc = 64

Vbl = 24.6
fbl = 15
Ibl = 64
Pbl = 2200


Vz = 208
Iz = 24
Pz = 1400


print()
print("#==============================ENSAIO CC========================================")
print("\nEnsaio a CC")

print("\nO valor de Vcc =", Vcc)
print("O valor de Icc =", Icc)

print("\nValores calculados" )

R1= Vcc/(2*Icc)
print("\nO valor de R1 = ", R1)



print()
print("\n\n#========================ENSAIO  ROTOR BLOQUEADO================================")
print("\n\nEnsaio a rotor Bloqueado")

print("O valor de Vbl =", Vbl)
print("O valor de fbl =", fbl)
print("O valor de Ibl =", Ibl)
print("O valor de Pbl =", Pbl)

print("\n\nValores calculados" )

Sbl = math.sqrt(3)*Vbl*Ibl
print("\nO valor de Sbl = ", Sbl)

Qbl = math.sqrt((Sbl*2)-(Pbl*2))
print("O valor de Qbl = ", Qbl)

Rbl = Pbl/(3*(Ibl**2))
print("O valor de Rbl = ", Rbl)

R2 = Rbl-R1
print("O valor de R2 = ", R2)

Xbl = Qbl/(3*(Ibl**2))
print("O valor de Xbl = ", Xbl)

Xt = Xbl*(f/fbl)
print("X1+X2 = Xt =  ", Xt)

X1 = Xt/2
X2 = X1

print("\nClasse A => X1 = X2 =", X2)
print("\n\n\n#==============================ENSAIO A VAZIO===================================")
print("\n\nEnsaio a vazio")

print("O valor de Vz =", Vz)
print("O valor de Iz =", Iz)
print("O valor de Pz =", Pz)

print("\n\nValores calculados" )

Pr1 = 3*R1*(Iz**2)
print("\nO valor de Pr1 = ", Pr1)

Prc = Pz-Pr1
print("O valor de Prc (P do nucleo) = ", Prc)

Rc = 3*((Vz**2)/Prc)
print("O valor de Rc =  ",Rc)

print("\nXm << Rc")
Xm = (Vz/Iz)-X1
print("O valor de Xm =  ", Xm)

print("\n\n\n")