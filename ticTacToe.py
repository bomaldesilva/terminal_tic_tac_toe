print("Welcome to our tic tac toe game.")
player_1 = input("Enter First Player's Name : ")
player_2 = input("Enter Second Player's Name : ")
print("\t   |   |   ")
print("\t---|---|---")
print("\t   |   |   ")
print("\t---|---|---")
print("\t   |   |   ")
print("\n")
print(player_1+" vs "+player_2)
print(player_1+"'s sign will be - X")
print(player_2+"'s sign will be - O")
print("*instructions:\n1. Insert the spot number(1-9) to put your sign\n2. Second player will go first\n3. If you are entered not a number program will be execute")
print("\t {0} | {1} | {2}  ".format("1","2","3"))
print("\t---|---|---")
print("\t {0} | {1} | {2}  ".format("4","5","6"))
print("\t---|---|---")
print("\t {0} | {1} | {2}  ".format("7","8","9"))
print("\nIndex Structure in below\n")
track_list_format=[" "]*9
print("\t {0} | {1} | {2}  ".format(track_list_format[0],track_list_format[1],track_list_format[2]))
print("\t---|---|---")
print("\t {0} | {1} | {2}  ".format(track_list_format[3],track_list_format[4],track_list_format[5]))
print("\t---|---|---")
print("\t {0} | {1} | {2}  ".format(track_list_format[6],track_list_format[7],track_list_format[8]))
print("Start Now\n")
track_list=[None]*9
player_id=None
final_break=False
input_index=[None]*9
for i in range(9):
    if(i%2):
        try:
            index=int(input(player_1+": "))
            while (index>9 or index<1 or index in input_index):
                print("Enter Valid Index : ")
                index = int(input(player_1 + ": "))
            player_id = 1
            track_list_format[index-1]="X"
            input_index[index-1]=index
        except ValueError:
            print("Enter Valid Number :)\nTry Again!")
            final_break=True
        if (final_break):
            break
    else:
        try:
            index=int(input(player_2 + ": "))
            while (index > 9 or index < 1 or index in input_index):
                print("Enter Valid Index : ")
                index = int(input(player_2 + ": "))
            player_id = 0
            track_list_format[index - 1] = "O"
            input_index[index - 1] = index
        except ValueError:
            print("Enter Valid Number :)\n Try Again!")
            final_break = True
        if (final_break):
            break

    print("\t {0} | {1} | {2}  ".format(track_list_format[0], track_list_format[1], track_list_format[2]))
    print("\t---|---|---")
    print("\t {0} | {1} | {2}  ".format(track_list_format[3], track_list_format[4], track_list_format[5]))
    print("\t---|---|---")
    print("\t {0} | {1} | {2}  ".format(track_list_format[6], track_list_format[7], track_list_format[8]))

    try:
        print(player_id)
        track_list[index-1]=player_id
    except:
        print("Error :)")
        i=8
    found=False
    for i in range(2):
        j = 0
        k = 1
        m = 2
        for l in range(3):
            # print(m)
            if(track_list[j]==i and track_list[k]==i and track_list[m]==i):
                if (i==0):
                    print('Congratulations '+player_1+"! You Won The Game.!")
                    found = True
                    final_break = True
                    break
                else:
                    print('Congratulations ' + player_2 + "! You Won The Game.!")
                    found = True
                    final_break = True
                    break
            j += 3
            k += 3
            m += 3
        if (found):
            break

    found=False
    for i in range(2):
        j = 0
        k = 3
        m = 6
        for l in range(3):
            if(track_list[j]==i and track_list[k]==i and track_list[m]==i):
                if (i==0):
                    print('Congratulations ' + player_1 + "! You Won The Game.!")
                    found = True
                    final_break = True
                    break
                else:
                    print('Congratulations ' + player_2 + "! You Won The Game.!")
                    found = True
                    final_break = True
                    break
            j += 1
            k += 1
            m += 1
        if (found):
            break

    found=False
    for i in range(2):
        j = 0
        k = 4
        m = 8
        for l in range(2):
            if(track_list[j]==i and track_list[k]==i and track_list[m]==i):
                if (i==0):
                    print('Congratulations ' + player_1 + "! You Won The Game.!")
                    found=True
                    final_break = True
                    break
                else:
                    print('Congratulations ' + player_2 + "! You Won The Game.!")
                    final_break=True
                    found = True
                    break
            j += 2
            m -= 2
        if(found):
            break
    if(final_break):
        break
print("Thank you both for joining.")
print("Play Again")