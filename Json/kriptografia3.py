print("Введите зашифрованный текст: ")
shifr = input()
s =''
alphabet=['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', '_', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', '_' ]
rash = [10, 11, 0, 4]
for i in range(1, (len(shifr))+1):
    ind_in_al = alphabet.index(shifr[i-1])
    if i%4==1:
        s+=alphabet[ind_in_al-rash[0]]
    elif i%4==2:
        s += alphabet[ind_in_al - rash[1]]
    elif i%4==3:
        s += alphabet[ind_in_al - rash[2]]
    elif i%4==0:
        s += alphabet[ind_in_al - rash[3]]
with open('test.txt', 'w', encoding='utf-8') as f:
    f.write(s)
print(s)
