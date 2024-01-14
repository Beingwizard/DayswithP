#Tine Complexities
# o > - big O Notation for the worst case
# omega > - omega Notation for the best case
# theta >- thera Notation for the average case

# for (int i= 0, i<n;i++)
# -> o(n)

# for(int i = n, i<n, i--)
# -> 0(n)

# for (int i, i=0, i<n, i+=2)
# -> stmt -> n -> i++
# -> O(n/2) -> o(n)

# for (int i=0, i<n, i++):
#     for (int, j =0 j<n, j++)
# -> o(n^2)

int p=0
for (int i=1;p<=n;i++):
    p=p+i

i   p
1   0+1
2   1+2
3   3+3
....

k   1+2+3+.....k

Assume p>n 
sum of k terms = k(k+1)/2
p=k(k=1)/2
k(k+1)/2>n 
k^2<n 
n> sqrt(n)
0(sqrt(n))
####

for(int i=1, i<n,i=i*2)
O(log n)

###########3
for(int i = n, i<n, i--)
-> 0(n)
for(int i = n, i<n, i--)
-> 0(n)
Final Complexities will be o(n+n) -> o(2n) -> O(n)

int p=0
for(int i=1, i<n,i=i*2):
    p++ -> log2 n
-> O(log2 n)
for(int j=1,j<p,j*2)
-> O(log2 p)

final Complexities : O(log2 n(log2 n))

for(int i=0, i<n, i++):
    for(int j=1, j<n, j=j*2)
Final Complexities : O(n log2 n)

for(int i=1, i<n,i=I*3)
-> O(log3 n)

while(i<n):
    i++
>- O(n)

while(a<b):
    //stmt
    a=a*2
-> O(log2 n)

while(k<n):
    k=k+i,
    i++
-> O(sqrt n)

#Linear Search
def solve(int arr[], int x):
    for (i=0,i<n):
        i=i+1
        if(a[i]==x):
            return true;return 1;
            return i;
    return -1

solve()