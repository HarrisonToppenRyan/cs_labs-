firstInput = int(input("Please enter the first integer: "))
secondInput = int(input("Please enter a second integer: "))
a1 = firstInput // 10
a2 = firstInput % a1 * 0.1
a3 = a1 + a2
int1 = a3
div1 = int1 // 10
mod1 = int1 % div1
res1 = int1 - mod1
mod1pt1 = mod1 * 10

b1 = firstInput // 10
b2 = firstInput % b1 * 0.1
b3 = b1 + b2
int2 = b3 
div2 = int2 // 10
mod2 = int2 % div2
res2 = int2 - mod2
mod2pt1 = mod2 * 10


res = (res1 * res2) + (res1 * mod2pt1 * 0.1) + (res2 * mod1pt1 * 0.1) + (mod1pt1 * mod1pt1 * 0.01)

print(res)