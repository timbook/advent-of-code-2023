import math

times = [51, 69, 98, 78]
dists = [377, 1171, 1224, 1505]

def quad_func(T, D):
    tol = 1e-9
    L = (T - math.sqrt(T**2 - 4*D)) / 2 + 1e-9
    R = (T + math.sqrt(T**2 - 4*D)) / 2 - 1e-9
    return math.floor(R) - math.ceil(L) + 1

sol = 1
for T, D in zip(times, dists):
    sol *= quad_func(T, D)

print(f"A ::: {sol}")

T = 51699878
D = 377117112241505

sol = quad_func(T, D)
print(f"B ::: {sol}")
