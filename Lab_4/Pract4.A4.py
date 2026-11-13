
def is_valid_number(card_str):
    return card_str.isdigit() and len(card_str) in [13, 15, 16]

def get_checksum(card_str):
    checksum = 0
    reversed_digits = card_str[::-1]
    
    for i in range(1, len(reversed_digits), 2):
        offset = 9 if int(reversed_digits[i])*2 >9 else 0
        checksum += int(reversed_digits[i])*2 - offset
    for i in range(0, len(reversed_digits[i]), 2):
        checksum+= int(reversed_digits[i])
    return checksum

def is_valid_sum(sum):
    return sum%10 == 0

def get_card_type(card_str):
    
    if (len(card_str)==13 or len(card_str)==16) and card_str.startswith('4'):
        return 'Visa'
    if len(card_str)==15 and (card_str.startswith('34') or card_str.startswith('37')):
        return 'American express'
    if len(card_str) == 16 and any(card_str.startswith(str(num)) for num in range(51, 56)):
        return 'MasterCard'
    return 'Неизвестная карта'

while True:
    card_number = input('Введите номер карты')
    if not is_valid_number(card_number):
        print('Некорректный  ввод')
    else:
        break

if is_valid_sum(get_checksum(card_number)):
    if get_card_type(card_number) != 'Неизвестная карта':
        print(f'Карта с номером {card_number} является картой {get_card_type(card_number)}')
    else:
        print(get_card_type(card_number))
else:
    print(f'Карты с номером {card_number} не существует')