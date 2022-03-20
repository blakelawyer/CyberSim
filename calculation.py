lumber = 0
nuclear = 0
agriculture = 0
chemical = 0
mining = 0

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

# if self.day % 7 == 0:
# print("Monday")
# if self.day % 7 == 1:
# print("Tuesday")
# if self.day % 7 == 2:
# print("Wednesday")
# if self.day % 7 == 3:
# print("Thursday")
# if self.day % 7 == 4:
# print("Friday")
# if self.day % 7 == 5:
# print("Saturday")
# if self.day % 7 == 6:
# print("Sunday")

net_lumber = 560
net_nuclear = 240
net_agriculture = 800
net_chemical = 640
net_mining = 320

input_output_table_0 = [[5, 0, 5, 0, 1],
                        [2, 1, 1, 3, 2],
                        [15, 10, 20, 10, 25],
                        [0, 5, 3, 15, 1],
                        [2, 2, 1, 5, 2],
                        [25, 15, 100, 40, 20]]

demand_0 = [100000, 100000, 100000, 100000, 100000]


def net_lumber_calc():
    return (25 * lumber_workers * lumber_hours * len(lumber_days) * 4) - (5 * lumber_workers * lumber_hours * len(lumber_days) * 4) - (
                5 * agriculture_workers * agriculture_hours * len(agriculture_days) * 4) - (1 * mining_workers * mining_hours * len(mining_days) * 4)


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
