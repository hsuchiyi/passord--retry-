pwd = 'a123456'
i = 3 
while True:
    password = input('請輸入密碼(最多輸入三次): ')
    if password != pwd:
        i = i - 1
        print('密碼錯誤!還有', i, '次機會')
        if i == 0:
            break
    elif password == 'a123456':
        print('登入成功')
        break  

