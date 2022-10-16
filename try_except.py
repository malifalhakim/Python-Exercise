input_user_benar = False

while not input_user_benar:
    try:
        input_user = int(input("Enter integer : "))
        input_user_benar = True
        print(input_user)
    except ValueError :
        print("Input ada yang salah")
    except KeyboardInterrupt :
        print()
        print("Ada interupsi keyboards")
        break