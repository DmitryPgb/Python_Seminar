
# 39. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# Пример:
# Входные данные:
# 'ываабв лповап абвцукв алоабвабв ываываыв'
# Входные данные:
# 'лповап ываываыв'

text = 'ываабв лповап абвцукв алоабвабв ываываыв'
text_word = text.split()
find = 'абв'
new_text = []

for i in text_word:
    if find not in i:
        new_text.append(i)

print(new_text)
text_2 = ' '.join(new_text)
print(text_2)