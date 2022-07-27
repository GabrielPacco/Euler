alpha = 0.8;
betha = 0.4;
delta = 0.3;
gamma = 0.6;

f=@(t,x,y) x*(alpha-betha*y);
g=@(t,x,y) y*(delta*x-gamma);
a=0;
b=40;
x0=15; % Cantidad inicial de presas
y0=4; % Cantidad inicial de depredadores
N = 4000; % Numero de intervalos

%y1=@(t)sin(t);  % Funcion de la solucion analitica

%% Construyendo los nodos
h=(b-a)/N;
tv=zeros(1,N+1);
tv(1)=a;
for i=2:N+1
    tv(i)=tv(i-1)+h;
end

% Método de Euler para sistemas de ecuaciones diferenciales
    [xv,yv]=EulerSist(tv,f,g,x0,y0);
    plot(tv,xv,'*b')
    hold on
    plot(tv,yv,'*r')
    grid on

% Solucion analitica (Exacta)
% tt=linspace(a,b,200);
% yy=y1(tt);
% hold on;
% plot(tt,yy);