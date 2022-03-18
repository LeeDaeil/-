# -------
r = 2   # 반지름
h = 5   # 높이
# -------
print('=' * 70)
print(f'[1번 문제]')
print(f'높이가 {h} 이고 반지름이 {r} 일때 원기둥의 겉넓이를 구하시오. 10점')
print('=' * 70)
# -------

# -------
pi = 3.14
B_A = pi * (r ** 2)
S_A = 2 * pi * r * h

A = 2 * B_A + S_A
V = B_A * h
# -------
print(f'[1번 해설]')

ans_1 = f'원기둥의 겉넓이 = 2 * 밑넓이({B_A}) * 옆넓이({S_A})'
ans_11 = f'원기둥의 겉넓이 = {A}'
ans_2 = f'원기둥의 부피 = 밑넓이({B_A}) * 높이({h})'
ans_21 = f'원기둥의 부피 = {V}'

print(f'{ans_1}\n{ans_11}')
print(f'{ans_2}\n{ans_21}')
print('=' * 70)
# -------

# -------
student_name = '이대일'
student_ans1 = '87.92'
correct_ans1 = student_ans1 == f'{A:2.2f}'
student_ans2 = '60.80'
correct_ans2 = student_ans2 == f'{V:2.2f}'
print(f'[답 제출]')
print(f'-이름         \t: {student_name}')
print(f'-원기둥 겉넓이 \t: {student_ans1:10}[{correct_ans1}]')
print(f'-원기둥 부피   \t: {student_ans2:10}[{correct_ans2}]')
print('=' * 70)