total_sum = 0
for i in range(4):
    print('ผนังเบอร์:', i+1)
    width = int(input('ความกว้างผนัง= '))
    height = int(input('ความสูงผนัง= '))
    area = width * height
    cost = 150
    total = area * cost
    print('รวมค่าใช้จ่าย: ', total ,' บาท')
    print('------------')
    total_sum = total_sum + total

print('SUM: ',total_sum)
