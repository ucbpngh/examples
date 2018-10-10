function [ result ] = fibonacci_r( n )


if n==0||n==1
    result = 1;

else
    result = fibonacci_r(n-2) + fibonacci_r(n-1);
end

end