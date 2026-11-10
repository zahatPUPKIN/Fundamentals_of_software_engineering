def proverka():
    packets = input("Ввод:\n")
    if len(packets) < 5:
        print("Ошибка: Длина строки должна быть не меньше 5.")
        return
    if not all(char in '01' for char in packets):
        print("Неверный ввод. Используйте только символы '0' и '1'!")
        return

    total_packets = len(packets)
    lost_packets = packets.count('0')    
    max_zeros = 0
    current_zeros = 0
    for packet in packets:
        if packet == '0':
            current_zeros += 1
            if current_zeros > max_zeros:
                max_zeros = current_zeros
        else:
            current_zeros = 0

    loss_percentage = (lost_packets / total_packets) * 100
    if 0 <= loss_percentage <= 1:
        quality = "отличное"
    elif 1 < loss_percentage <= 5:
        quality = "хорошее качество"
    elif 5 < loss_percentage <= 10:
        quality = "удовлетворительное качество"
    elif 10 < loss_percentage <= 20:
        quality = "плохое качество"
    else:
        quality = "критическое состояние сети"
    print("Вывод:")
    print(f"Общее количество пакетов: {total_packets}")
    print(f"Количество потерянных пакетов: {lost_packets}")
    print(f"Длина самой длинной последовательности потерянных пакетов: {max_zeros}")
    print(f"Процент потерь: {round(loss_percentage,1)}%")
    print(f"Качество связи: {quality}")

proverka()
