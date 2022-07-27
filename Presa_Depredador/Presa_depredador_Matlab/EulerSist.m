function [y,z]=EulerSist(x,f,g,y0,z0)
    n=length(x);
    y=zeros(1,n);
    z=zeros(1,n);
    y(1)=y0;
    z(1)=z0;
    for i=1:n-1
        h=x(i+1)-x(i);
        y(i+1)=y(i)+h*f(x(i),y(i),z(i));
        z(i+1)=z(i)+h*g(x(i),y(i),z(i));
    end
    