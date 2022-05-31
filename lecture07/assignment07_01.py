# Є словник з ключами-строками та елементами-списками строк, наприклад:
#
# data = {
#  	'colors': ['red', 'green', 'blue', 'purple],
#  	'fruits': ['pineapple', 'orange', 'banana'],
#  	'clothes': ['coat', 'tshirt']
# }
#
# Завдання: перебудувати словник (не створюючи новий) таким чином що
#           його значення стануть ключами значенням котрих буде їхній
#           ключ з початкового словника.
#
data = {
'colors': ['red', 'green', 'blue', 'purple'],
'fruits': ['pineapple', 'orange', 'banana'],
'clothes': ['coat', 'tshirt']
}

d = {i:j for j in data.keys() for i in data[j]}

print(d)