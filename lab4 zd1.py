# przedzial
start = -1.0
end = 1.0

length = end - start


# liczba punktow
n = 21

length2 = length / (n-1)

result_x = []
result_fx = []

for i in range(n):
    x = round(start + (i * length2), 1)

    denominator = pow(x, 2)
    denominator *= 25
    denominator += 1
    y = 1 / denominator

    print("nr", i+1, "x =", x, "y =", y)