import numpy as np

lumber = 0
nuclear = 0
agriculture = 0
chemical = 0
mining = 0

input_output_table_0 = [[5, 0, 5, 0, 1],
                      [2, 1, 1, 3, 2],
                      [15, 10, 20, 10, 25],
                      [0, 5, 3, 15, 1],
                      [2, 2, 1, 5, 2],
                      [25, 15, 100, 40, 20]]

demand_0 = [100000, 100000, 100000, 100000, 100000]


def labor_calculation(input_output_table, demand):

    output_table = input_output_table[-1]
    input_table = input_output_table[:len(input_output_table) - 1]
    A = np.zeros((len(input_table), len(input_table[0])))

    for row in range(len(input_table)):
        for column in range(len(input_table[0])):
            A[row][column] = input_output_table[row][column] / output_table[column]

    d = np.zeros((1, len(demand)))

    for goal in range(len(demand)):
        d[0][goal] = demand[goal] / output_table[goal]

    d = np.transpose(d)
    I = np.identity(len(input_table[0]))
    x = np.dot(np.linalg.inv(np.subtract(I, A)), d)

    print(x)


#labor_calculation(input_output_table_0, demand_0)


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






