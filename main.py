# def find_prime_factors_count(input_number):
#     counter = 0
#     result = []
#     res_num = input_number
#     prime_list = create_prime_list(input_number)
#     for i in range(len(prime_list)):
#         res_i = prime_list[i]
#         while res_num % prime_list[i] == 0:
#             counter += 1
#             res_num /= prime_list[i]
#         else:
#             temp_res = (prime_list[i], counter)
#             if counter != 0:
#                 result.append(temp_res)
#                 counter = 0
#     if input_number == 1:
#         result = [(1,1)]
#     return result
#
#
# def create_prime_list(input_number):
#     num = input_number
#     num_list = []
#     if num > 1:
#         for i in range(2, num + 1):
#             num_list.append(i)
#     for i in range(len(num_list)):
#         for j in range(len(num_list) - 1, i, -1):
#             if num_list[j] % num_list[i] == 0:
#                 num_list.pop(j)
#     return num_list
#
#
# def print_result(input_number):
#     for i in input_number:
#         if i[1] == 1:
#             print(f'({i[0]})', end='')
#             continue
#         print(f'({i[0]}**{i[1]})', end='')
#
#
# print_result(find_prime_factors_count(320))
def is_balance_number(number):
    num = list(str(number))
    sum_number = 0
    if len(num) % 2 == 0:
        i = 0
        while i < len(num) / 2 - 1:
            sum_number += int(num[i]) - int(num[-1 - i])
            i += 1
    if len(num) % 2 == 1:
        i = 0
        while i < int(len(num)/2):
            sum_number += int(num[i]) - int(num[-1 - i])
            i += 1
    if sum_number == 0:
        return True
    else:
        return False

def test_Is_balance_number():
    assert is_balance_number(1) == True
    assert is_balance_number(11) == True
    assert is_balance_number(111) == True
    assert is_balance_number(12) == True
    assert is_balance_number(122) == False
    assert is_balance_number(345678) == False
    assert is_balance_number(343434) == True
    assert is_balance_number(70016) == True
    assert is_balance_number(15007) == False

is_balance_number(1)
is_balance_number(11)
test_Is_balance_number()
print(is_balance_number(112311))