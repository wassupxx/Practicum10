def vowel_consonant(sentance):
    """Функция печатает общее количество гласных
       и общее количество согласных букв в предложении.

       Функция принимает в качестве входных данных
       предложение на русском языке (строку)
    """
    vowel = 'аеёиуюяоыэ'
    alphabet = 'бвгдеёжзийклмнопрстуфхцчшщьыъэюя'
    vowels = []
    consonants = []
    for letter in sentance.lower():
        if letter in vowel:
            vowels.append(letter)
        elif letter in alphabet:
            consonants.append(letter)
    print(f"Количество гласных в строке: {len(vowels)}")
    print(f"Количество согласных в строке: {len(consonants)}")


vowel_consonant()

