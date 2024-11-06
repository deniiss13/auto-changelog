def words_in_commit(message: str, words: list) -> bool:
    """
    Функция проверяет, есть ли в коммите слова, которые надо игнорировать
    :param message: commit message
    :param words: list of ignored words
    """
    for word in words:
        if word in message:
            return True

    return False
