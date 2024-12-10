% Tidsvektor
t = 0:0.01:10;  % Tid från 0 till 10 sekunder med steg på 0.01 sekunder

% Definiera referenssignalen r(t) som ett enhetssteg
r = ones(length(t), 1);  % Gör r till en kolumnvektor med samma längd som t

% Antag en överföringsfunktion för kompensatorn C(s) och systemet G(s)
% Exempel på kompensator och system (ersätt med dina egna värden)
K = 15.4;         % Förstärkningsfaktor
Td = 2.84;        % Tidskonstant för lead-delen
B = 0.16;         % Förhållande mellan nollställe och pol för lead-delen
Ti = 11.36;       % Tidskonstant för lag-delen
gamma = 1;        % Faktor för lag-delen

% Lead-del: (T_d s + 1) / (B T_d s + 1)
lead_numerator = [Td, 1];
lead_denominator = [B * Td, 1];
C_lead = tf(lead_numerator, lead_denominator);

% Lag-del: (T_i s + 1) / (T_i s + gamma)
lag_numerator = [Ti, 1];
lag_denominator = [Ti, gamma];
C_lag = tf(lag_numerator, lag_denominator);

% Kombinera lead och lag med förstärkning K
C = K * C_lead * C_lag;

% Antag att G(s) är ditt system, här är ett exempel
G = tf(1.9, [8, 86, 40, 0]);  % Exempel på G(s) (ersätt med ditt eget system)

% Öppen styrslinga
L = C * G;

% Sluten styrslinga
T_closed = feedback(L, 1);

% Beräkna utsignalen y(t) för enhetssteget
[y, t] = step(T_closed, t);  % Säkerställ att y och t är samma längd som r

% Omvandla y till en kolumnvektor om det behövs
y = y(:);

% Beräkna insignalen u(t) = C * (r(t) - y(t))
u = lsim(C, r - y, t);

% Beräkna det maximala värdet av u(t)
umax = max(u);

% Plot av insignalen u(t)
figure;
plot(t, u, 'b', 'LineWidth', 1.5);
grid on;
xlabel('Tid [s]');
ylabel('Insignal u(t)');
title('Insignal u(t) för enhetssteg i referenssignalen r(t)');

% Visa det maximala värdet av u(t)
fprintf('Maximalt värde av u(t): %.4f\n', umax);
