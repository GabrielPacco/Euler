f=@(t,y,z)z;
g=@(t,y,z)-sin(t);
a=0;
b=4;
y0=0;
z0=1;
N=10; % Numero de intervalos

y1=@(t)sin(t); % Solución exacta del problema y' = f(x,y), y(a)=y0


%% Construyendo los nodos
h=(b-a)/N
tv=zeros(1,N+1);
tv(1)=a;
for i=2:N+1
    tv(i)=tv(i-1)+h;
end




% método de euler para sistemas de ecuaciones

    yv=EulerSist(tv,f,g,y0,z0);
    plot(tv,yv,'*r')
    grid on


% Solución exacta
tt=linspace(a,b,0.1);
yy=y1(tt);
hold on          % Directiva para graficar sobre la grafica que ya se tiene
plot(tt, yy)
grid on