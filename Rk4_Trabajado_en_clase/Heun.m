% Código para Euler mejorado

function y=Heun(x,f,y0)
n=length(x);
y=zeros(1,n);
y(1)=y0;
for i=1:n-1
    h=x(i+1)-x(i);
    z=y(i)+h*f(x(i),y(i));
    y(i+1)=y(i)+h*(f(x(i), y(i))+f(x(i),z))/2;
end