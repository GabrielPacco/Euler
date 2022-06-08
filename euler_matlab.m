a=0;
b=2;
c=1;
f=@(y,t)y+t;
n=101; % Nro de puntos equiespaciados
% Solución Exacta
    Y=@(t)2*exp(t)-t-1;

h=(b-a)/(n-1);
t=zeros(1,n);
y=zeros(1,n);
y(1)=c;
t(1)=a;
for i=2:n
    t(i)=t(i-1)+h;
    y(i)=y(i-1)+h*f(y(i-1),t(i-1));
end

% Graficando
grid on
plot(t,y,'*')
hold on
tt=a:0.1:b;
yy=Y(tt);
plot(tt,yy,'r')
