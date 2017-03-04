def deboor(myu,point,u,l,j,i,k):
        if l==0:
            return point[0][j+1],point[1][j+1]
        a_dividend=(u-myu[j+l])
        a_divisor=myu[j+k+1]-myu[j+l]
        
        if a_divisor<1e-10 and  a_dividend<1e-10:
            alj=0
        else:
            alj=a_dividend/a_divisor
#######
        ab1,cd1=deboor(myu,point,u,l-1,j,i,k)
        ab2,cd2=deboor(myu,point,u,l-1,j+1,i,k)        
        return ((1-alj)*ab1+alj*ab2),((1-alj)*cd1+alj*cd2)
