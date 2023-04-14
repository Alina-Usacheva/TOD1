import numpy as np
# 1 task
arr1 = np.loadtxt('minutes_n_ingredients.csv', delimiter=',', skiprows=1, dtype=np.int32)
strings = arr1[:5, :]
print(f'TASK 1: \n {strings} \n')
# 2 task
arr2 = arr1[:, 1:]
print('TASK 2: \n', f'Среднее значение: {np.mean(arr2, axis=0)} \n'
      f'Минимум: {arr2.min(axis=0)} \n',
      f'Максимум: {arr2.max(axis=0)} \n'
      f'Медиана: {np.median(arr2, axis=0)} \n')
# task 3
print(f'TASK 3: \n {np.clip(arr1[:, 1], 0, np.quantile(arr1[:, 1], 0.75))} \n')
# task 4
print('TASK 4: \n', f'Продолжительность равна 0 у {np.count_nonzero(arr1[:, 1] == 0)} рецептов \n')
# task 5
print(f'TASK 5: \n {len(np.unique(arr1[:, 0]))} \n')
# task 6
print('TASK 6: \n', f'{len(np.unique(arr1[:, 2]))}, \n {np.unique(arr1[:, 2])} \n')
# task 7
arr3 = np.copy(arr1)
smt = (arr3[:, 2] <= 5)
print(f'TASK 7: \n {arr3[smt, :]} \n')
# task 8
number = arr1[:, 2] // arr1[:, 1]
print(f'TASK 8: \n {number.max(axis=0)} \n')
# task 9
arr4 = arr1[arr1[:, 1].argsort()][-100:]
print(f'TASK 9: \n {np.mean(arr4[:, 2])} \n')
# task 10
number = 10
rand = np.random.randint(1, 100000, size=(1, 10))
print(f'TASK 10: \n {arr1[rand]} \n')
# task 11
less = (arr1[:, 2] <= np.mean(arr1[:, 2]))
print(f'TASK 11: \n {len(arr1[less, :]) / len(arr1) * 100} \n')
# task 12
arr5 = arr1.copy()
rec = [1 if (row[1] <= 20) & (row[2] <= 5) else 0 for row in arr5]
arr6 = np.insert(arr5, 3, rec, axis=1)
print(f'TASK 12: \n {arr6} \n')
# task 13
proc = (arr6[:, 3] == 1)
print('TASK 13: \n'
      f'{len(arr1[proc, :]) / len(arr6) * 100} \n')
