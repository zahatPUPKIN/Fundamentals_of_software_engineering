import random
import time
n = int(input("Введите количество примеров: "))
correct_answers = 0
total_time = 0.0
for i in range(1, n + 1):
    print(f"Вопрос {i}/{n}")
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    correct_result = a * b
    start_time = time.time()
    while True:
        try:
            user_input = input(f"{a} x {b} = ")
            answer = int(user_input)
            break  
        except ValueError:
            print("Пожалуйста, введите целое число!")
            
    time_spent = time.time() - start_time
    total_time += time_spent 
 
    if answer == correct_result:
        print(f"Верно! (Время: {round(time_spent, 1)} сек)")
        correct_answers += 1
    else:
        print(f"Неверно! Правильно: {correct_result} (Время: {round(time_spent, 1)} сек)")

avg_time = total_time / n if n > 0 else 0
percentage = (correct_answers / n) * 100 if n > 0 else 0
print("========================================")
print("СТАТИСТИКА:")
print("========================================")
print(f"Общее время: {round(total_time, 1)} секунд")
print(f"Среднее время на вопрос: {round(avg_time, 1)} сек")
print(f"Правильных ответов: {correct_answers}/{n}")
print(f"Процент правильных ответов: {round(percentage, 1)}%")
