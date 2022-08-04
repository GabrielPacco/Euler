x=linspace(0,4*pi,2000);
for N=4:4:16
    y=serieSen(x,N);
    hold on
    plot(x,y,'g')
    grid on
end
y=sin(x);
hold on
plot(x,y,'r')
grid on
axis([0,4*pi, -1,1])