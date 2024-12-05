% MATLAB Code to Analyze the Open-Loop and Closed-Loop System
clc;
clear;

% Define the open-loop transfer function
K = 1; % Proportional controller gain
num = K * [1.9]; % Numerator of G(s)
den = [8, 86, 40, 0]; % Denominator of G(s)
open_loop_tf = tf(num, den); % Open-loop transfer function

% Bode plot for open-loop system
figure;
bode(open_loop_tf);
grid on;
title('Bode Plot of Open-Loop System');

% Calculate gain crossover frequency and phase margin
[gm, pm, wcg, wcp] = margin(open_loop_tf); % gm = gain margin, pm = phase margin
disp('Open-Loop Analysis:');
disp(['Crossover Frequency (rad/s): ', num2str(wcp)]);
disp(['Phase Margin (degrees): ', num2str(pm)]);

% Closed-loop transfer function
closed_loop_tf = feedback(open_loop_tf, 1); % Closed-loop system with unity feedback

% Bode plot for closed-loop system
figure;
bode(closed_loop_tf);
grid on;
title('Bode Plot of Closed-Loop System');

% Calculate closed-loop bandwidth
[mag, phase, w] = bode(closed_loop_tf); % Get magnitude and phase
mag_db = 20*log10(squeeze(mag)); % Convert magnitude to dB
bandwidth_idx = find(mag_db <= -3, 1, 'first'); % Find frequency at -3 dB
bandwidth = w(bandwidth_idx); % Bandwidth frequency
disp(['Closed-Loop Bandwidth (rad/s): ', num2str(bandwidth)]);

% Summary of Results
disp('Results Summary:');
disp(['Crossover Frequency (rad/s): ', num2str(wcp)]);
disp(['Phase Margin (degrees): ', num2str(pm)]);
disp(['Closed-Loop Bandwidth (rad/s): ', num2str(bandwidth)]);
