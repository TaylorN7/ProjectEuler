# Problem_029.py - Distinct Powers

distinct_nums = []

for a in range(2, 101):
    print(a)

    for b in range(2, 101):
        #print(b)
        total = a**b

        if total not in distinct_nums:
            distinct_nums.append(total)
        else:
            continue

how_many = len(distinct_nums)
print(how_many)