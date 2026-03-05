numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
# находим индекс пропущенного элемента
index_None = numbers.index(None)
# удаляем пропушенный элемент
del numbers[index_None]
# вычисляем среднее арифметическое
average = sum(numbers) / (len(numbers) + 1)
# вставляем среднее значение обратно на место пропущенного элемента
numbers.insert(index_None, average)
print("Измененный список:", numbers)
