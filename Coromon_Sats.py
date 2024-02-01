import random
 
f = open("CoromonDataset.csv", "r")


Lines = f.readlines()


Type_dict = {}
H_points = {}
A_points = {}
S_Attack = {}
Defense_dict = {} 
S_Defense = {}
Speed_dict = {}
St_Points = {}

print("Total number of Coromons: ", len(Lines[1: ]))


random_char = random.choice(Lines[1: ]).strip().split(",")

print("Name: ", random_char[0])
print("Type: ", random_char[1])
print("Health Points: ", random_char[2])
print("Attack: ", random_char[3])
print("Special Attack: ", random_char[4])
print("Defense: ", random_char[5])
print("Special Defense: ", random_char[6])
print("Speed: ", random_char[7])
print("Stamina Points: ", random_char[8],'\n')

for line in Lines[1: ]:
    line = line.strip().split(",")
    Name = line[0]
    Type = line[1]
    Health_Points = int(line[2])
    Attack = int(line[3])
    Special_Attack = int(line[4])
    Defense = int(line[5])
    Special_Defense = int(line[6])
    Speed = int(line[7])
    Stamina_Points = int(line[8])
    if Type not in Type_dict:
        Type_dict[Type] = 1
        H_points[Type] = Health_Points
        A_points[Type] = Attack
        S_Attack[Type] = Special_Attack
        Defense_dict[Type] = Defense
        S_Defense[Type] = Special_Defense
        Speed_dict[Type] = Speed
        St_Points[Type] = Stamina_Points
    else:
        Type_dict[Type] += 1
        H_points[Type] += Health_Points
        A_points[Type] += Attack
        S_Attack[Type] += Special_Attack
        Defense_dict[Type] += Defense
        S_Defense[Type] += Special_Defense
        Speed_dict[Type] += Speed
        St_Points[Type] += Stamina_Points

for k,v in Type_dict.items():
    H_points[k] //= v
    A_points[k] //= v
    S_Attack[k] //= v
    Defense_dict[k] //= v
    S_Defense[k] //= v
    Speed_dict[k] //= v
    St_Points[k] //= v

print("Average Health Points: ", H_points)
print("Average Attack Points: ", A_points)
print("Average Special Attack Points: ", S_Attack)
print("Average Defense Points: ", Defense_dict)
print("Average Special Defense Points: ", S_Defense)
print("Average Speed Points: ", Speed_dict)
print("Average Stamina Points: ", St_Points)

print("Different Types of Coromon:",list(Type_dict.keys()))

def max_coromon(dictionary):
    max_val = 0
    max_items = []
    for k,v in dictionary.items():
        if v > max_val:
            max_val = v
            max_items.clear()
            max_items.append(k)
        elif v == max_val:
            max_items.append(k)
    return max_items

def min_coromon(dictionary):
    min_val = 1000000
    min_items = []
    for k,v in dictionary.items():
        if v < min_val:
            min_val = v
            min_items.clear()
            min_items.append(k)
        elif v == min_val:
            min_items.append(k)
    return min_items

print(max_coromon(Speed_dict),'\n')

print("Max Average Health Points:", max_coromon(H_points))
print("Min Average Health Points:", min_coromon(H_points))
print("Max Average Attack Points:", max_coromon(A_points))
print("Min Average Attack Points:", min_coromon(A_points))
print("Max Average Special Attack Points:", max_coromon(S_Attack))
print("Min Average Special Attack Points:", min_coromon(S_Attack))
print("Max Average Defense Points:", max_coromon(Defense_dict))
print("Min Average Defense Points:", min_coromon(Defense_dict))
print("Max Average Special Defense Points:", max_coromon(S_Defense))
print("Min Average Special Defense Points:", min_coromon(S_Defense))
print("Max Average Speed Points:", max_coromon(Speed_dict))
print("Min Average Speed Points:", min_coromon(Speed_dict))
print("Max Average Stamina Points:", max_coromon(St_Points))
print("Min Average Stamina Points:", min_coromon(St_Points))



