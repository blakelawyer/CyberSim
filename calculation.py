from scipy.optimize import linprog

lumber = 0
nuclear = 0
agriculture = 0
chemical = 0
mining = 0

energy_drinks = 0
corn_flakes = 0
TVs = 0
computers = 0
bicycles = 0
roller_skates = 0
vitamins = 0
pet_food = 0
mattresses = 0
yo_yos = 0

lumber_workers = 5
nuclear_workers = 5
agriculture_workers = 5
chemical_workers = 5
mining_workers = 5

lumber_hours = 8
nuclear_hours = 8
agriculture_hours = 8
chemical_hours = 8
mining_hours = 8

lumber_days = [0, 1, 2, 3, 4]
nuclear_days = [0, 1, 2, 3, 4]
agriculture_days = [0, 1, 2, 3, 4]
chemical_days = [0, 1, 2, 3, 4]
mining_days = [0, 1, 2, 3, 4]

input_output_table_0 = [[5, 0, 5, 0, 1],
                        [2, 1, 1, 3, 2],
                        [15, 10, 20, 10, 25],
                        [0, 5, 3, 15, 1],
                        [2, 2, 1, 5, 2],
                        [25, 15, 100, 40, 20]]

demand_0 = [100000, 100000, 100000, 100000, 100000]


def make_energy_drink():
    global lumber, nuclear, agriculture, chemical, mining, energy_drinks
    energy_drinks += 1
    nuclear -= 10
    chemical -= 50
    mining -= 20


def make_corn_flakes():
    global lumber, nuclear, agriculture, chemical, mining, corn_flakes
    corn_flakes += 1
    lumber -= 10
    agriculture -= 50
    mining -= 10


def make_TV():
    global lumber, nuclear, agriculture, chemical, mining, TVs
    TVs += 1
    lumber -= 10
    nuclear -= 20
    chemical -= 10
    mining -= 30


def make_computer():
    global lumber, nuclear, agriculture, chemical, mining, computers
    computers += 1
    nuclear -= 30
    chemical -= 20
    mining -= 40


def make_bicycle():
    global lumber, nuclear, agriculture, chemical, mining, bicycles
    bicycles += 1
    lumber -= 20
    mining -= 40


def make_roller_skates():
    global lumber, nuclear, agriculture, chemical, mining, roller_skates
    roller_skates += 1
    lumber -= 10
    mining -= 20


def make_vitamins():
    global lumber, nuclear, agriculture, chemical, mining, vitamins
    vitamins += 1
    agriculture -= 10
    chemical -= 30


def make_pet_food():
    global lumber, nuclear, agriculture, chemical, mining, pet_food
    pet_food += 1
    agriculture -= 30
    chemical -= 10


def make_mattress():
    global lumber, nuclear, agriculture, chemical, mining, mattresses
    mattresses += 1
    lumber -= 30
    agriculture -= 30
    mining -= 10


def make_yo_yo():
    global lumber, nuclear, agriculture, chemical, mining, yo_yos
    yo_yos += 1
    lumber -= 10
    agriculture -= 10


def net_lumber_calc():
    return (25 * lumber_workers * lumber_hours * len(lumber_days) * 4) - (
            5 * lumber_workers * lumber_hours * len(lumber_days) * 4) - (
                   5 * agriculture_workers * agriculture_hours * len(agriculture_days) * 4) - (
                   1 * mining_workers * mining_hours * len(mining_days) * 4)


def net_nuclear_calc():
    return (15 * nuclear_workers * nuclear_hours * len(nuclear_days) * 4) - (
            2 * lumber_workers * lumber_hours * len(lumber_days) * 4) - (
                   1 * nuclear_workers * nuclear_hours * len(nuclear_days) * 4) - (
                   1 * agriculture_workers * agriculture_hours * len(agriculture_days) * 4) - (
                   3 * chemical_workers * chemical_hours * len(chemical_days) * 4) - (
                   2 * mining_workers * mining_hours * len(mining_days) * 4)


def net_agriculture_calc():
    return (100 * agriculture_workers * agriculture_hours * len(agriculture_days) * 4) - (
            15 * lumber_workers * lumber_hours * len(lumber_days) * 4) - (
                   10 * nuclear_workers * nuclear_hours * len(nuclear_days) * 4) - (
                   20 * agriculture_workers * agriculture_hours * len(agriculture_days) * 4) - (
                   10 * chemical_workers * chemical_hours * len(chemical_days) * 4) - (
                   25 * mining_workers * mining_hours * len(mining_days) * 4)


def net_chemical_calc():
    return (40 * chemical_workers * chemical_hours * len(chemical_days) * 4) - (
            5 * nuclear_workers * nuclear_hours * len(nuclear_days) * 4) - (
                   3 * agriculture_workers * agriculture_hours * len(agriculture_days) * 4) - (
                   15 * chemical_workers * chemical_hours * len(chemical_days) * 4) - (
                   1 * mining_workers * mining_hours * len(mining_days) * 4)


def net_mining_calc():
    return (20 * mining_workers * mining_hours * len(mining_days) * 4) - (
            2 * lumber_workers * lumber_hours * len(lumber_days) * 4) - (
                   2 * nuclear_workers * nuclear_hours * len(nuclear_days) * 4) - (
                   1 * agriculture_workers * agriculture_hours * len(agriculture_days) * 4) - (
                   5 * chemical_workers * chemical_hours * len(chemical_days) * 4) - (
                   2 * mining_workers * mining_hours * len(mining_days) * 4)


def lumber_hour():
    global lumber, nuclear, agriculture, chemical, mining
    lumber = lumber - 5
    nuclear = nuclear - 2
    agriculture = agriculture - 15
    chemical = chemical - 0
    mining = mining - 2
    lumber = lumber + 25


def nuclear_hour():
    global lumber, nuclear, agriculture, chemical, mining
    lumber = lumber - 0
    nuclear = nuclear - 1
    agriculture = agriculture - 10
    chemical = chemical - 5
    mining = mining - 2
    nuclear = nuclear + 15


def agriculture_hour():
    global lumber, nuclear, agriculture, chemical, mining
    lumber = lumber - 5
    nuclear = nuclear - 1
    agriculture = agriculture - 20
    chemical = chemical - 3
    mining = mining - 1
    agriculture = agriculture + 100


def chemical_hour():
    global lumber, nuclear, agriculture, chemical, mining
    lumber = lumber - 0
    nuclear = nuclear - 3
    agriculture = agriculture - 10
    chemical = chemical - 15
    mining = mining - 5
    chemical = chemical + 40


def mining_hour():
    global lumber, nuclear, agriculture, chemical, mining
    lumber = lumber - 1
    nuclear = nuclear - 2
    agriculture = agriculture - 25
    chemical = chemical - 1
    mining = mining - 2
    mining = mining + 20


def linear_programming():

    obj = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]

    lhs_ineq = [[0, 10, 10, 0, 20, 10, 0, 0, 30, 10],
                [10, 0, 20, 30, 0, 0, 0, 0, 0, 0],
                [0, 50, 0, 0, 0, 0, 10, 30, 30, 10],
                [50, 0, 10, 20, 0, 0, 30, 10, 0, 0],
                [20, 10, 30, 40, 40, 20, 0, 0, 10, 0]]

    rhs_ineq = [[net_lumber_calc()],
                [net_nuclear_calc()],
                [net_agriculture_calc()],
                [net_chemical_calc()],
                [net_mining_calc()]]

    bnd = [(0, float("inf")),  # Energy Drinks
           (0, float("inf")),  # Corn Flakes
           (0, float("inf")),  # TV
           (0, float("inf")),  # Computer
           (0, float("inf")),  # Bicycle
           (0, float("inf")),  # Roller Skates
           (0, float("inf")),  # Vitamins
           (0, float("inf")),  # Pet Food
           (0, float("inf")),  # Mattresses
           (0, float("inf"))  # Yo-yos
           ]

    opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,
                  bounds=bnd,
                  method="revised simplex")

    print(opt)