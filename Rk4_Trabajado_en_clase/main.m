f=@(x,y)x+y;
a=0;
b=2;
y0=1;
N=20; % Numero de intervalos

y1=@(x)-1-x+2*exp(x); % Solución exacta del problema y' = f(x,y), y(a)=y0

h=(b-a)/N
xv=zeros(1,N+1);
xv(1)=a;
for i=2:N+1
    xv(i)=xv(i-1)+h;
end

% método de euler tradicional
% Con estrellitas de color Rojo

    yv=Euler(xv,f,y0);
    plot(xv,yv,'*r')
    grid on

% Metodo de euler mejorado
% Con estrellitas de color azul

    yv=Heun(xv, f, y0);
    hold on
    plot(xv, yv, '*b')
    grid on


% Metodo de Runge-Kutta de cuarto orden
% Con estrellitas de color negro
    yv=RK4(xv, f, y0);
    hold on
    plot(xv, yv, '*k')
    grid on


% Solución exacta
xx=linspace(a,b,200);
yy=y1(xx);
hold on          % Directiva para graficar sobre la grafica que ya se tiene
plot(xx, yy)




