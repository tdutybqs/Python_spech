import speech_recognition


def game():
    import speech_recognition as sr
    import random
    words = ["яблоко", "банан", "груша", "апельсин", "манго", "лимон"]
    word = random.choice(words)
    r = sr.Recognizer()
    mic = sr.Microphone()
    audio = ""
    answer = ""
    count = 1
    while answer != word:
        with mic as source:
            r.adjust_for_ambient_noise(source)
            print("Говори")
            audio = r.listen(source, phrase_time_limit=2)
        try:
            answer = r.recognize_google(audio, language="ru-RU")
            if str(answer).lower() == word:
                print(f"Да, это {answer}. Тебе удалось угадать с {count} попытки")
            else:
                print(f"Нет, это не {answer}")
                count += 1
        except speech_recognition.UnknownValueError:
            print("Не удалось разобрать фразу")


def test():
    import speech_recognition as sr
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        r.adjust_for_ambient_noise(source)
        print("Говори")
        audio = r.listen(source, phrase_time_limit=10)
    try:
        answer = r.recognize_google(audio)
        print(answer)
    except speech_recognition.UnknownValueError:
        print("Не удалось разобрать фразу")


if __name__ == "__main__":
    game()