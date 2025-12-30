import secrets #Для генерации символов (подробнее о ней можно почитать в PEP 506). 
import string

class PasswordGenerator:
    
    def __init__(self):

        self.ascii_letters = string.ascii_letters #Добавляем атрибут для верхнего и нижнего регистра символов.
        self.digits = string.digits #Добавляем атрибут для цифр.
        self.punctuation = string.punctuation #Добавлен атрибут для знаков пунктуации.

    def generate(self, complexity):

        if complexity == 'Легкий': #Пароль будет сгенерирован без знаков пунктуации для облегчения запоминания.
            length = secrets.choice([4,5,6,7]) #Для генератора. Количество символов в пароле.
            atributes_of_password = self.ascii_letters + self.digits #Генератор будет использовать только буквы и цифры.

        elif complexity == 'Средний':
            length = secrets.choice([8,9,10])
            atributes_of_password = self.ascii_letters + self.digits + self.punctuation #Генератор будет использовать буквы, цифры и знаки препинания, максимум - 10 символов.

        elif complexity == 'Сложный':
            length = secrets.choice([11,12,13,14,15])
            atributes_of_password = self.ascii_letters + self.digits + self.punctuation #Генератор будет использовать буквы, цифры и знаки препинания, максимум - 15 символов.

        else:
            raise ValueError('Неизвстный уровень сложности, попробуйте снова')
        
        password = ''.join(secrets.choice(atributes_of_password) for _ in range(length))
        
        return password, length
            
def main():
    
    generator = PasswordGenerator() #Создан генератор.
    complexity = input('Выберите сложность пароля:\nЛегкий (4-7 символов без знаков препинания)\nСредний (8-10 символов со знаками препинания)\nСложный (11-15 символов со знаками препинания)\n')

    try:
        
        password, length = generator.generate(complexity) #Команда, запускающая процесс генерации в зависимости от выбранной сложности.
        print(f'Длина пароля: {length} символов')
        print(f'Ваш пароль: {password}')
        
    except ValueError as e:
        print('Неизвстный уровень сложности, попробуйте снова')
        
if __name__ == "__main__":
    main()
