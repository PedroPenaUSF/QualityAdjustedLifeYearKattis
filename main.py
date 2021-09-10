# Step 1 accept user input as n, n is how many times we will need to accept further user input
# also initialize QALY value
n = int(input())
i = 0
qaly = 0
# Step 2 loop n times accepting user input
while i < n:
    # Step 3 accept user input, split values with first element q as quality of life and y as number of years
    qy = input().split(' ')
    q = float(qy[0])
    y = float(qy[1])
    # Step 4 multiply q and y and add product to qaly
    qaly = q*y + qaly
    i += 1
print(format(qaly, ".3f"))
