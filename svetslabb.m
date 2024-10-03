clear
clc
% Reservera minne för plottning
x1 = zeros(1,145);
y1 = zeros(1,145);
y2 = zeros(1,145);
y3 = zeros(1,145);
% Indata
h0=1.5; % Plåttjocklek innan valsning, mm
h1=0.5; % Plåttjocklek efter valsning, mm (önskat värde)
sigmaf=50; % Materialets flytspänning i N/mm2
b0=27; % Plåtens bredd före valsning, 27 mm
m=0.5; % Friktionsfaktor, varierar mellan 0 och 1
n=141; % Valsarnas varvtal, varv/min
verkningsgrad=0.8; % Drivlinans verkningsgrad, 80 %
omega=2*pi*n/60; % Vinkelhastighet, rad/s
% Motoreffektgräns
Pmotor_max = 2000; % Max motoreffekt i W
% Startvärde för valsens radie
R = 94/2; % Initial valsradie, mm
% Sätt en mycket liten minskningsfaktor
delta_R = 0.1; % Minskning av radie för varje iteration
% Effektberäkning i en while-loop tills motoreffekten är under 2000 W
Pmotor = inf; % Startvärde för motoreffekten (infinit)
ii = 1;
while Pmotor > Pmotor_max && R > 0
    deltah = h0 - h1;
    hmedel = (h0 + h1)/2;
    L = sqrt(R * deltah);
    F = (1/sqrt(3)) * sigmaf * L * b0 * (2 + m * L / hmedel);
    Mv = F * L;
    Pvals = Mv * omega * 0.001; % Omvandla Nmm till Nm för effektberäkning
    Pmotor = Pvals / verkningsgrad;
    
    % Spara värden för plottning
    x1(ii) = R;
    y1(ii) = Pmotor;
    y2(ii) = L;
    y3(ii) = F;
    
    % Minska radien
    R = R - delta_R;
    ii = ii + 1;
end
% Plotting the results
figure;
subplot(1,3,1);
plot(x1(1:ii-1), y1(1:ii-1));
grid;
title('Motoreffekt');
xlabel('Valsradie R [mm]'); ylabel('Motoreffekt [W]');
subplot(1,3,2);
plot(x1(1:ii-1), y2(1:ii-1));
grid;
title('Kontaktlängd');
xlabel('Valsradie R [mm]'); ylabel('Kontaktlängd [mm]');
subplot(1,3,3);
plot(x1(1:ii-1), y3(1:ii-1));
grid;
title('Valskraft');
xlabel('Valsradie R [mm]'); ylabel('Valskraft [N]');
% Skriv ut resultat
fprintf('Minsta valsradie som ger en motoreffekt under 2000 W: %.2f mm\n', R + delta_R);
