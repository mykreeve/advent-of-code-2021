# 15, 4
# 14, 16
# 11, 14
# -13, 3
# 14, 11
# 15, 13
# -7, 11
# 10, 7
# -12, 12
# 15, 15
# -16, 13
# -9, 1
# -8, 15
# -8, 4

# push input[0] + 4
# push input[1] + 16
# push input[2] + 14
# pop. input[3] == input[2] +14 - 13
# push input[4] + 11
# push input[5] + 13
# pop. input[6] == input[5]+13 -7
# push input[7] + 7
# pop. input[8] == input[7]+ 7 -12
# push input[9] + 15
# pop. input[10] == input[9]+15-16
# pop. input[11] == input[4]+11-9
# pop. input[12] == input[1]+16-8
# pop. input[13] == input[0]+4-8


# input[3] = input[2] + 1
# input[6] = input[5] + 6
# input[8] = input[7] - 5
# input[10] = input[9] - 1
# input[11] = input[4] + 2
# input[12] = input[1] + 8
# input[13] = input[0] - 4


# part 1: 91897399498995
# part 2: 51121176121391

