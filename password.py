p = 0
while p < 3:
    password = input('請輸入密碼(最多輸入三次): ')
    if password != 'a123456':
        print('密碼錯誤')
    elif password == 'a123456':
        print('登入成功')
        break  
    p = p + 1 
