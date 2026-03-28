def sms(message):
    """
        Ограничивает длину сообщения для СМС до 160 символов.

        Args:
            message (str): исходное сообщение

        Returns:
            str: сообщение длиной не более 160 символов
    """
    symbols = []
    message_outcome = ''
    for symbol in message:
        symbols.append(symbol)
    print(symbols)
    print(len(symbols))
    if len(symbols) <= 160:
        return message
    else:
        for index in range(160):
            message_outcome += symbols[index]
        return message_outcome


message = input("Enter a message: ")
print(sms(message))
