import timeit

#iteratif
def iter_fibo(n):
    a, b = 1, 1
    for i in range(1, n):
        a, b = b, a + b
    return a 

#rekursif
def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))
print(" ")
print("==========Iteratif==========")
print(" ")
for i in range(1,101):
    start = timeit.default_timer()
    nilai = iter_fibo(i)
    end = timeit.default_timer()
    print("waktu untuk nilai ke-",i,nilai,"dengan iteratif adalah",end-start)    
print(" ")
print("==========Rekursif==========")
print(" ")
for j in range(1,101):
    start = timeit.default_timer()
    nilai = recur_fibo(j)
    end = timeit.default_timer()
    print("waktu untuk nilai ke-",j,nilai,"dengan rekursif adalah",end-start)   