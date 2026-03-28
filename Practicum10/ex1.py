import string


def vowel_consonant(sentance):
    """Функция печатает общее количество гласных
       и общее количество согласных букв в предложении.

       Функция принимает в качестве входных данных
       предложение на русском языке (строку)
    """
    vowel = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
    vowels = []
    consonants = []
    translator = str.maketrans('', '', string.punctuation)
    cleaned = (sentance.translate(translator)).lower()
    for letter in cleaned:
        if letter in vowel:
            vowels.append(letter)
        elif letter != ' ':
            consonants.append(letter)
    print(f"Количество гласных в строке: {len(vowels)}")
    print(f"Количество согласных в строке: {len(consonants)}")


vowel_consonant("Привет всем, друзья!")
