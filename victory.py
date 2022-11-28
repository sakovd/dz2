writers = ["А. Пушкин", "Н. Гоголь", "Л. Толстой", "И. Тургенев", "А. Чехов"]
writers_born = [1799, 1809, 1828, 1818, 1860]
answer_tips = ["1799 или 1825","1800 или 1809","1828 или 1853","1758 или 1818","1860 или 1900"]
repeat_test="Да"
right=0
wrong=0
while repeat_test == "Да":
    for i in range(len(writers)):
        print("В каком году родился: ", writers[i], "\n возможные варианты:", answer_tips[i] )
        if int(input()) == writers_born[i]:
            right +=1
    wrong=len(writers)-right
    print("Количество правильных ответов = ", right)
    print("Rоличество ошибок = ",wrong)
    print("Процент правильных ответов =",right*100/len(writers),"%")
    print("Процент неправильных ответов =", wrong * 100 / len(writers), "%")
    repeat_test = input("Начать с начала? ")