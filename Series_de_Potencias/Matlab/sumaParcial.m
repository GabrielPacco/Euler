function s=sumaParcial(N,p)
    s=0;
    for n=1:N
        s=s+1/n^p;
    end
end