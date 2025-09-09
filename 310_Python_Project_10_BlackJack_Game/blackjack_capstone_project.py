import random as rd

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def deal_card(input_list):
    if len(input_list) <= 1:
        val1 = rd.choice(cards)
        val2 = rd.choice(cards)
        input_list.extend([val1,val2])
    else:
        val = rd.choice(cards)
        input_list.append(val)
    return input_list

#TODO- 1

comp_cards =[]
user_cards =[]

deal_card(comp_cards)
deal_card(user_cards)

def check(input_list, score):
    output_list = []  # Create a new list to store modified values
    for elem in input_list:
        if elem == 11 and (score + 11) > 21:
            output_list.append(1)  # Replace 11 with 1 if condition is met
        else:
            output_list.append(elem)  # Keep original value otherwise
    return output_list

def calculate_score(input_list):
    output_list = []
    if sum(input_list) == 21:
        return 0
    else:
        score = sum(input_list)
        return score
    

comp_score = calculate_score(comp_cards)
print(comp_cards,comp_score)

