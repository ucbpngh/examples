function [  ] = complexFunction(  )
%This is a function with no arguments - it simply calls another function.

[list sum] = powerList(10);

list(1);

for i=1:5
    if i==1
        fprintf('The %dst power is %d.\n',i,list(i)); % d = decimal
    else
        fprintf('The %dth power is %d.\n',i,list(i));
    end
end

end

