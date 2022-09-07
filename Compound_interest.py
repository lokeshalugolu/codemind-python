p,r,t=map(int,input().split())
G=p*((1+r/100)**t)
print('%0.2f'%G)