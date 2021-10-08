def bouncing_ball(h, bounce, window):
    if h <= 0 or bounce <= 0 or bounce >= 1 or window >= h:
        return -1
    t = 1
    h = h * bounce
    while h > window:
        t += 2
        h = h * bounce
    return t


pass

height = float(input("Give me the height of the floor\n"))
b = float(input("Give me the bounce of the ball\n"))
w = float(input("Give me the height of the window(NOTE:It must be less than the floor's height\n"))
times = bouncing_ball(height, b, w)
print(times)
