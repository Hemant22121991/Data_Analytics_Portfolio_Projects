def calculate_love_score(name1,name2):

    name = name1+name2

    name = name.upper()

    check_list1 = list('TRUE')

    check_list2 = list('LOVE')

    i = 0

    j = 0

    for char1 in check_list1:
        counter = name.count(char1)
        i = i + counter
        # print(f"\n{char1} occures {counter} times!")

    for char2 in check_list2:
        counter = name.count(char2)
        j = j + counter
        # print(f"\n{char2} occures {counter} times!")

    i = str(i)
    j = str(j)

    final_num = i + j

    final_num = int(final_num)

    print(f"\n{name1} and {name2} love score is {final_num}!\n")

calculate_love_score('Hemant','Mandge')

calculate_love_score('Jack Bauer','Angela Yu')

calculate_love_score('Mayuri','Hemant')

calculate_love_score('Hemant','Dhanashree')

calculate_love_score("Kanye West", "Kim Kardashian")