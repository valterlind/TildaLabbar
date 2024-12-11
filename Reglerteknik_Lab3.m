clear;
clc;
%% Assignment 1

% Definera variabler
PersonalNumber = 020711;

num = 1.9;
den = [8, 86, 40, 0];
G = tf(num, den);


%Anropar funktioner
[J,umax] = lab3robot(PersonalNumber);
%lab3robot(G, PersonalNumber);

%% Assignment 2

% Definera P-contoller
Kp = 5.1;
F = tf(Kp);

% Open loop system
FG = F*G;

% Closed-loop system
T = feedback(F * G, 1);

% Simulera stegsvar
step(T);

grid on;
title('Stegsvar för P-regulator')

%lab3robot(G,Kp,[],[],[],[],[],[],PersonalNumber)

%% Assignment 3

% Calculate the cross-over frequency and phase-margin for the open loop system

[gm, pm, wcg, wcp] = margin(FG); % gm = gain margin, pm = phase margin
disp('Open-Loop Analysis:');
disp(['Crossover Frequency (rad/s): ', num2str(wcp)]);
disp(['Phase Margin (degrees): ', num2str(pm)]);

% Calculate the closed-loop bandwidth
[mag, phase, w] = bode(T); % Get magnitude and phase
mag_db = 20*log10(squeeze(mag)); % Convert magnitude to dB
bandwidth_idx = find(mag_db <= -3, 1, 'first'); % Find frequency at -3 dB
bandwidth = w(bandwidth_idx); % Bandwidth frequency
disp('Closed-Loop Analysis:');
disp(['Closed-Loop Bandwidth (rad/s): ', num2str(bandwidth)]);

% Bode diagram open-loop
figure;
bode(FG);
grid on;
title('Bode Plot of Open-Loop System');

% Bode diagram closed-loop
figure;
bode(T);
grid on;
title('Bode Plot of Closed-Loop System');

%% LEAD-LAG
% Parametrar för lead-lag-länken
K_v = 15.4; % Förstärkningsfaktor
Td = 2.84; % Tidskonstant för lead-delen
B = 0.16; % Förhållande mellan nollställe och pol för lead-delen
Ti = 13.6; % Tidskonstant för lag-delen
gamma = 0.036; % Faktor för lag-delen

% Lead-del: (T_d s + 1) / (B T_d s + 1)
lead_numerator = [Td, 1]; % T_d s + 1
lead_denominator = [B * Td, 1]; % B T_d s + 1
C_lead = tf(lead_numerator, lead_denominator);

% Lag-del: (T_i s + 1) / (T_i s + gamma)
lag_numerator = [Ti, 1]; % T_i s + 1
lag_denominator = [Ti, gamma]; % T_i s + gamma
C_lag = tf(lag_numerator, lag_denominator);

% Kombinera lead och lag med förstärkning K
F_ll = K_v * C_lead * C_lag;

% T_open
L_open = F_ll * G;

% T_closed
L_closed = feedback(L_open, 1);

%% U_max

% Visa överföringsfunktionen
disp('Lead-lag-kompensatorn C(s):');

% Rita Bodediagram
figure;
bode(F_ll);
grid on;
title('Bodeplot för Lead-Lag-Kompensator');

figure;
step(L_closed);
grid on;
title('Stegsvar för leadlag')

% U max
% Tidsvektor
t = 0:0.01:10;  % Tid från 0 till 10 sekunder med steg på 0.01 sekunder

% Definiera referenssignalen r(t) som ett enhetssteg
r = ones(length(t), 1);  % Gör r till en kolumnvektor med samma längd somt

% Beräkna utsignalen y(t) för enhetssteget
[y, t] = step(L_closed, t);  % Säkerställ att y och t är samma längd som r

% Omvandla y till en kolumnvektor om det behövs
y = y(:);

% Beräkna insignalen u(t) = C * (r(t) - y(t))
u = lsim(F_ll, r - y, t);

% Beräkna det maximala värdet av u(t)
u_max = max(u);

% Plot av insignalen u(t)
figure;
plot(t, u, 'b', 'LineWidth', 1.5);
grid on;
xlabel('Tid [s]');
ylabel('Insignal u(t)');
title('Insignal u(t) för enhetssteg i referenssignalen r(t)');

% Visa det maximala värdet av u(t)
fprintf('Maximalt värde av u(t): %.4f\n', u_max);

%% Tester

% REQUIREMENT 4: Error < 0.05
s = tf('s');
ramp = 1 / s;
ramperror = dcgain(ramp - (L_closed/s));
disp('Ramp error = ')
disp(ramperror)

%% Assignment 8

% Funktioner
S1 = 1 / (1 + FG);
S2 = 1 / (1 + L_open);

% Plot
bodemag(S1, S2);

%% Assignment 9

% Funktioner
dG1 = (s + 10) / 40;
dG2 = (s + 10) / (4*(s + 0.01));
T2 = 1 - S2;
%T2 = feedback(L_open, 1);

bodemag(T2, 1/dG1, 1/dG2);

%% Assignment 10

A = [0, 1/20, 0 ; 0, -0.25, 9.5 ;0 , -0.25, -10.5];
B = [0; 0; 0.5];
C = [1,0,0];

%% Assignment 12

desired_poles = [-2.1+2.1i, -2.1-2.1i, -2.1];
L = place(A, B, desired_poles);

%L0 = -inv(C / (A-B*L) * B)
L0 = L(1);

%% Test
lab3robot(G,Kp,F_ll,A,B,C,L,L0,PersonalNumber);
