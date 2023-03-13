%% Part 1 - Inverse Kinematics
% Define the length of each link
L1 = .07; % Length of link 1
L2 = .13; % Length of link 2

x = -0.0635:0.0025:0.0635;
y = [-0.16 -0.15537636169249588 -0.15147173554992632 -0.14823555474220548 -0.14561725243924759 -0.14356626181096674 -0.14203201602727722...
    -0.1409639482580931 -0.14031149167332865 -0.14002407944289802 -0.14001248063218968 -0.14008730805390868 -0.14022673712192113 -0.1404273855510808...
    -0.14068587105624145 -0.14099881135225678 -0.14136282415398058 -0.14177452717626657 -0.1422305381339685 -0.1427274747419401 -0.14326195471503517...
    -0.1438305957681074 -0.14443001561601054 -0.14505683197359837 -0.14570766255572457 -0.14637912507724296 -0.14706783725300723 -0.14777041679787117...
    -0.1484834814266885 -0.14920364885431292 -0.14992753679559825 -0.15065176296539826 -0.15137294507856655 -0.152087700849957 -0.15279264799442333...
    -0.15348440422681925 -0.1541595872619985 -0.15481481481481485 -0.15544670460012203 -0.15605187433277382 -0.15662694172762393 -0.15716852449952612...
    -0.1576732403633341 -0.15813770703390168 -0.15855854222608257 -0.1589323636547305 -0.15925578903469922 -0.1595254360808425 -0.15973792250801405...
    -0.15988986603106767 -0.15997788436485705];

% Define the target point coordinates (as an array of x and y values)
targetPoints = [x;y];

theta2 = zeros(1,length(targetPoints));
theta1 = zeros(1,length(targetPoints));

% Loop through each target point and calculate the joint angles
for i = 1:length(targetPoints)
    X = targetPoints(1, i); % Target x-coordinate
    Y = targetPoints(2, i); % Target y-coordinate

    % Calculate the inverse kinematics
    r = sqrt(X^2 + Y^2);
    theta2(i) = acos((r^2 - L1^2 - L2^2) / (2 * L1 * L2));
    theta1(i) = atan2(Y, X) - atan2((L2 * sin(theta2(i))), (L1 + L2 * cos(theta2(i))));
end

theta1 = rad2deg(theta1);
theta1 = theta1+180;
theta2 = rad2deg(theta2);

figure
testX = L1*cosd(theta1) + L2*cosd(theta1+theta2);
testY = L1*sind(theta1) + L2*sind(theta1+theta2);
scatter(testX,testY)
xlabel("X Position (m)")
ylabel("Y Position (m)")
title("Test of Calculated Path")

time = 0:1:(length(targetPoints)-1);
figure
scatter(time, testX)
xlabel("Time (Unit Time)")
ylabel("X Position (m)")
title("Test of Calculated X Path Over Unit Time")

figure
scatter(time, testY)
xlabel("Time (Unit Time)")
ylabel("Y Position (m)")
title("Test of Calculated Y Path Over Unit Time")

%% Part 2 - Transfer Function

file = readmatrix("motorsv50_2.csv");
time = file(1,:);
time = time(2:end);

angle = file(2,:);
angle = angle(2:end);

