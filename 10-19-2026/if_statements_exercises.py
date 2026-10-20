# 5-3 Alien Colors #1
# passes
alien_color = 'green'
if alien_color == 'green':
    print('+5 points!')

#fails
alien_color = 'red'
if alien_color == 'green':
    print('+5 points!')

# 5-4 Alien Colors #2
# if statement output
alien_color = 'green'
if alien_color == 'green':
    print('+5 points!')
else:
    print('+10 points!')

# else statement output
alien_color = 'yellow'
if alien_color == 'green':
    print('+5 points!')
else:
    print('+10 points!')

# 5-5 Alien Colors #3 if-else chain into if-elif-else chain
#if statement output
alien_color = 'green'
if alien_color == 'green':
    print('+5 points!')
elif alien_color == 'yellow':
    print('+10 points!')
else:
    print('+15 points!')
#elif statement output
alien_color = 'yellow'
if alien_color == 'green':
    print('+5 points!')
elif alien_color == 'yellow':
    print('+10 points!')
else:
    print('+15 points!')
#else statement output
alien_color = 'red'
if alien_color == 'green':
    print('+5 points!')
elif alien_color == 'yellow':
    print('+10 points!')
else:
    print('+15 points!')
#5-6 Stages of Life (Logic helped by Popcorn/I need to study math more)
age = int(input('How old are you:'))

if age < 2: # 2
    print('You are a baby!')
elif age <= 3: # 4
    print('You are a toddler')
elif age <= 12: # 13
    print('You are a kid')
elif age <= 19:  # 20
    print('You are a teenager')
elif age <= 64: # 65
    print('You are an adult')
else:
    print('You are an elderly')

# 5-7 Favorite Fruit
favorite_fruits = ['Apple', 'Banana', 'Orange', 'Blueberry', 'Pear']

if 'Apple' in favorite_fruits:
    print('You really like apples!')
if 'Pineapple' in favorite_fruits:
    print('You really like pineapples!')
if 'Pear' in favorite_fruits:
    print('You really like pears!')
if 'Mango' in favorite_fruits:
    print('You really like mangos!')
if 'Orange' in favorite_fruits:
    print('You really like oranges!')



