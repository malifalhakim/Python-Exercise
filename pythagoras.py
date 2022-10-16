for a in range(1,50):
    for b in range(a + 1 , 50):
        for c in range(b + 1,50):
            if (a**2 + b**2) == c**2:
                print(a,b,c)