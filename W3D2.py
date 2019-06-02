 #Chris Scott part 1
 Hours = int(input("hour many hours do you work:"))
    ...: print("YOur worked hours are: ", Hours)
    ...: type(Hours)
    ...: RPH = int(input("what is your pay rate?: "))
    ...: print ("your rate is: ", RPH)
    ...: type(RPH)
    ...: pay = Hours*RPH
    ...: print ("your pay is: ", pay)
    ...: def computepay(a=6,b=7):
    ...:  c=a+b
    ...:  return c
    ...: 
hour many hours do you work:40 
YOur worked hours are:  40
what is your pay rate?: 5
your rate is:  5
your pay is:  200

 
 #Chris Scott part 2
 ...: def computepay(a,b):
    ...:     pay=a*b
    ...:     if pay>40:
    ...:         return pay*1.5
    ...:     else:
    ...:         return pay
    ...: computepay(10,6)
    ...: 
    ...: 
    ...: 
Out[30]: 90.0

#Chris Scott part 3
    ...:     ...: t= arange(0,1,0.01)
    ...:     ...: y =2*sin(2*pi*t)
    ...:     ...: N= len(y)
    ...:     ...: y_sat= zeros(N)
    ...:     ...: for i in range(N):
    ...:     ...:     y_i=y[i]
    ...:     ...:     if y_i <.5:
    ...:     ...:      y_sat[i]=.5
    ...:     ...:     else:
    ...:     ...:      y_sat[i]=y_i +1
    ...:     ...: figure(1)
    ...:     ...: clf()
    ...:     ...: plot(t,y,'r--')
    ...:     ...: plot(t,y_sat,label='$y(t)$',linewidth=2.0)
    ...:     ...: ylabel('$y(t)$')
    ...:     ...: xlabel('Time(sec)')
    ...:     ...: legend(loc=1)
    ...: show()
