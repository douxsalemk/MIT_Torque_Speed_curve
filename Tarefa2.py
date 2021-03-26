import Tarefa1 as T1
import math
import matplotlib.pyplot


# Curva do torque x velocidade


"""
Dados decorrente da tarefa 1

R1 = Resistência do estator
X1 = Reatância do estator
R2 = Resistência do rotor
X2 = Reatância do rotor
Xm = Reatância do ramo de magnetização
V_phase = Tensão de fase
N_sync = Velocidade síncrona (rpm)
W_sync = Velocidade síncrona (rad/s)
Nm = Velocidade mecânica
"""

V_phase = T1.Vbl/math.sqrt(3) 
N_sync = 1800
W_sync = 188.5

# Calculo da tensão e da impedância de Thévenin

V_th = V_phase*(T1.Xm/math.sqrt(T1.R1**2+(T1.X1 + T1.Xm)**2))
Z_th = ((1j*T1.Xm)*(T1.R1 + 1j*T1.X1))/(T1.R1 + 1j*(T1.X1+T1.Xm))
R_th = Z_th.real
X_th = Z_th.imag

# Calculo das característica de conjugado X velocidade para diversos S.
acc = list(range(1,51))

S = [x/50 for x in acc] 
print(S)
S[1] = 0.001

Nm = [(1-x)*N_sync for x in S]

# Calculo do conjugado para resistência de rotor original



T_ind1 = [(3*(V_th**2)*(T1.R2/S[i]))/(W_sync*((R_th+T1.R2/S[i])**2+(X_th+T1.X2)**2)) for i in range(0,50)]

# Calcule do conjugado para a resistência de rotor dobrada


T_ind2 = [3*(V_th**2)*(2*T1.R2/S[i])/(W_sync*((R_th+2*T1.R2/S[i])**2+(X_th+T1.X2)**2)) for i in range(0,50)]


# Plote a curva de conjugado X velocidade

matplotlib.pyplot.plot(Nm, T_ind1)
matplotlib.pyplot.title("1) Torque X Velocidade")
matplotlib.pyplot.xlabel("Velocidade Mecanica")
matplotlib.pyplot.ylabel("Conjugado induzido em porc. da carga plena")
matplotlib.pyplot.ylim(0, 10)
matplotlib.pyplot.show()



matplotlib.pyplot.plot(Nm, T_ind2)
matplotlib.pyplot.title("2) Torque X Velocidade")
matplotlib.pyplot.xlabel("Velocidade Mecanica")
matplotlib.pyplot.ylabel("Conjugado induzido em porc. da carga plena")
matplotlib.pyplot.show()


"""
plot(nm,t_ind1,'Color','b','LineWidth',2.0);
hold on;
plot(nm,t_ind2,'Color','k','LineWidth',2.0,'LineStyle','-.');
xlabel('\bf\itn_{m}');
ylabel('\bf\tau_{ind}');
title ('\bfCaracterística de conjugado versus velocidade do motor de indução');
legend ('R_{2} Original','R_{2} Dobrada');
grid on;
hold off;
"""