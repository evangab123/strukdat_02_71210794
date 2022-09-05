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
list_iteratif = list()
for i in range(1,101):
    start = timeit.default_timer()
    nilai = iter_fibo(i)
    end = timeit.default_timer()
    start2 = timeit.default_timer()
    nilai = recur_fibo(i)
    end2 = timeit.default_timer()
    print("n=",i,",","iteratif",end-start,"detik",",","Rekursif",end2-start2,"detik")