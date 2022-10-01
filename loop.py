numbers = [12, 75, 150, 180, 145, 525, 50]

for divisible_by_five in numbers:


    if divisible_by_five%5 != 0:
        num_index = numbers.index(divisible_by_five)

        numbers[num_index] += 1

        print(num_index)

        #numbers[num_index] += 1











