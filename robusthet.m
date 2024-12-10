% Definiera kompenseringslänken F(s)
K = 15.4;
Td = 2.84;
B = 0.16;
Ti = 13.6;
gamma = 0.036;

lead = tf([Td 1], [B*Td 1]);
lag = tf([Ti 1], [Ti gamma]);
F = K * lead * lag;

% Definiera systemet G(s)
G = tf(1.9, [8 86 40]);

% Beräkna T(s)
T = feedback(F * G, 1);

% Definiera modellfelen Delta G1 och Delta G2
DeltaG1 = tf([1 10], 40);
DeltaG2 = tf([1 10], [4 0.04]);

% Invertera Delta G1 och Delta G2 för att få 1/Delta G
inv_DeltaG1 = 1 / DeltaG1;
inv_DeltaG2 = 1 / DeltaG2;

% Rita Bode-diagram för T(s), 1/DeltaG1 och 1/DeltaG2
figure;
bodemag(T, inv_DeltaG1, inv_DeltaG2);
legend('T(s)', '1/\DeltaG1(s)', '1/\DeltaG2(s)');
grid on;
title('Bode Diagram för T(s) och 1/\DeltaG');
