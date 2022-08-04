function s=serieSen(x,N)
    s=0;
    for n=0:N
        s=s+(-1)^n*x.^(2*n+1)/factorial(2*n+1);
    end
end