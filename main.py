def find_all_sums(numbers, target_sum, fixed_numbers, index=0, current_sum=0, used=set(), combination=[]):
    if current_sum == target_sum:
        print(f'Se encontró una combinación que suma {target_sum}: {combination}')
        return [combination]
    if index >= len(numbers):
        return []

    num = numbers[index]
    results = []
    if index not in used:
        used.add(index)
        results += find_all_sums(numbers, target_sum, fixed_numbers, index + 1, current_sum + num, used, combination + [num])
        results += find_all_sums(numbers, target_sum, fixed_numbers, index + 1, current_sum - num, used, combination + [-num])
        used.remove(index)

    results += find_all_sums(numbers, target_sum, fixed_numbers, index + 1, current_sum, used, combination)
    return results

if __name__ == '__main__':
    numbers = [519.24, 283.78, 230.82, 596.25, 394.56, 50.88, 151.72, 506.35, 1.15, 540.51, 1.11, 618.36, 678.27, 275.55, 342.35, 738.02, 1183.28, 1226.84, 854.77, 914.22, 1017.27, 643.93, 306.59, 842.54, 922.64]
    target_sum = 265.56
    fixed_numbers = [832.84, 815.65, 762.75]  # Example fixed numbers

    # Adjust the target sum and initial combination with fixed numbers
    initial_sum = sum(fixed_numbers)
    initial_combination = fixed_numbers[:]

    results = find_all_sums(numbers, target_sum, fixed_numbers, current_sum=initial_sum, combination=initial_combination)

    if not results:
        print(f'No se encontró ninguna combinación que sume {target_sum}')