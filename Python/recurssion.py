def double(x):
    y = x* 2
    print(y)
    if y < 1000:
        double(y)
    
double(1)

def CountDown(x):
    if x<= 0:
        return 
    else:
        print(x)
        CountDown(x-1)
        
CountDown(10)    
