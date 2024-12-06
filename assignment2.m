clear;
clc;

% Definera variabler
PersonalNumber = 020711;

%open_num = 38;
%open_den = [200, 2100, 0];

%open_loop_tf = tf(open_num, open_den);

num = 1.9;
den = [8, 86, 40, 0];
G = tf(num, den);


%Anropar funktioner
[J,umax] = lab3robot(PersonalNumber);
%lab3robot(G, PersonalNumber);


%%
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

%%
% Assignment 3

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
K = 1; % Förstärkningsfaktor
Td = 0.1; % Tidskonstant för lead-delen
B = 10; % Förhållande mellan nollställe och pol för lead-delen
Ti = 0.5; % Tidskonstant för lag-delen
gamma = 0.1; % Faktor för lag-delen

% Lead-del: (T_d s + 1) / (B T_d s + 1)
lead_numerator = [Td, 1]; % T_d s + 1
lead_denominator = [B * Td, 1]; % B T_d s + 1
C_lead = tf(lead_numerator, lead_denominator);

% Lag-del: (T_i s + 1) / (T_i s + gamma)
lag_numerator = [Ti, 1]; % T_i s + 1
lag_denominator = [Ti, gamma]; % T_i s + gamma
C_lag = tf(lag_numerator, lag_denominator);

% Kombinera lead och lag med förstärkning K
C = K * C_lead * C_lag;

