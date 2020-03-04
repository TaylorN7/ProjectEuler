# Problem_029.py - Distinct Powers

distinct_nums = []

for a in range(2, 1001):

    for b in range(2, 1001):

        total = a**b

        if total not in distinct_nums:
            distinct_nums.append(total)
        else:
            continue
