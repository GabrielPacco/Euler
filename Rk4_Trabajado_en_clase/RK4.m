function y=RK4(x,f,y0)
    n=length(x);
    y=zeros(1,n);
    y(1)=y0;
    
    for i=1:n-1
        h = x(i+1)-x(i);
        p = f(x(i),y(i))*h;
        q = f(x(i)+h/2,y(i)+p/2)*h;
        r = f(x(i)+h/2, y(i)+q/2)*h;
        s = f(x(i)+h, y(i)+r)*h;
    
        y(i+1)=y(i)+(p+2*q+2*r+s)/6;
    end