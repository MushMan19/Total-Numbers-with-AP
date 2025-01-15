from itertools import permutations

def generate_combinations(num:str, patterns):
    base_list = map(int, num)
    # base_list = [1, 2, 2, 3] for num = '1223'
    
    unique_combinations = set(permutations(base_list))
    print(f'Total Numbers: {len(unique_combinations)}')
    correct_num_list = {pattern: [0, []] for pattern in patterns}
    
    for comb in unique_combinations:
        n = ''.join(map(str, comb))
        for pattern in patterns:
            if pattern in n:
                correct_num_list[pattern][0] += 1
                correct_num_list[pattern][1].append(n)
                break
    
    with open('nums.txt', 'w') as file:
        for i, j in correct_num_list.items():
            file.write(f'{i}: ({j[0]}) {j[1]}' + '\n\n')
    print(f'Numbers with AP: {sum(i[0] for i in correct_num_list.values())}')


def generate_aps(numbers:str, czero):
    aps = set()
    
    for length in range(3, len(numbers) + 1):
        for perm in permutations(numbers, length):
            if not czero and perm[0] == '0':
                continue
            perm_str = ''.join(perm)
            if is_arithmetic_progression(perm_str):
                aps.add(perm_str)
    
    return aps

def is_arithmetic_progression(s):
    nums = [int(x) for x in s]
    if len(nums) < 2:
        return False
    
    diff = nums[1] - nums[0]
    for i in range(1, len(nums) - 1):
        if nums[i+1] - nums[i] != diff:
            return False
    return True


numbers = '0122' #Enter numbers here 
count_zero_in_unit_place = False # if numbers like 012 that start with 0 are allowed 
patterns = generate_aps(numbers, count_zero_in_unit_place)
print(f'APs: {patterns}')
aps = generate_combinations(numbers, patterns)
