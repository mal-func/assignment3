def func(m1,m2,m3,m4):

  tot=0
  try:

    for x in [m1,m2,m3,m4]:
      if x<0 or x>100:
        raise Exception("OutOfRange")
      tot=tot+x
    perc=tot/4
    return perc

  except:
    
    print("Out_of_range")
    return("try again")


lst=[]
for x in range(4):
  m=float(input(f'enter no. {x+1}: '))
  lst.append(m)

x=func(lst[0],lst[1],lst[2],lst[3])
print(x)


