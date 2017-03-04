def Basis(myu,u,i,k):
    if k==0:
        if myu[i]<=u<myu[i+1]:
            return 1
        else:
            return 0

    a_dividend=u-myu[i]
    a_divisor=myu[i+k]-myu[i]
    if a_divisor==0 and a_divisor==0:
        a=0
    else:
        a=a_dividend/a_divisor
    b_dividend=myu[i+k+1]-u
    b_divisor=myu[i+k+1]-myu[i+1]
    if b_divisor==0 and b_divisor==0:
        b=0
    else:
        b=b_dividend/b_divisor  
    return a*Basis(myu,u,i,k-1)+b*Basis(myu,u,i+1,k-1)
        