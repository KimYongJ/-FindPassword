import os
import itertools
import zipfile
import winsound
import time
import datetime
str1="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
str2="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()_+|`-=/.<>[]}{?,"
password_binding=''
max_password=0
ZipPath=''

def clear():
    os.system('cls')


def decryption(password_binding, min,max,ZipPath):
    clear()
    start = time.time()
    print('\n[ 암호 해독 중 시간이 오래 걸립니다. 암호가 길 경우 며칠이 걸릴 수 있습니다. ]\n')
    for i in range(min,max+1):
        print(f'{i}자리 수 암호 찾는 중 ...')
        string = itertools.product(password_binding, repeat=i)
        for j in string:
            password = ''.join(j) # j를 string으로 바꾸기위해 ''.join(j) 코드를 쓴다.
            try:
                ZipPath.extractall(path='C:/MadeByKYJ', pwd=password.encode()) # extractall(압축해제할 경로, 비밀번호) 압축해제할 경로를 적을 때 폴더가 없으면 생성한다.
                ZipPath.close()
                end = time.time()
                time_result = str(datetime.timedelta(seconds=end-start)).split(".")[0].split(":")
                text1 = '\n걸린 시간 : '+time_result[0]+'시간 '+time_result[1]+'분 '+time_result[2]+'초'
                text2 = '\n알집 비밀번호 : '+password
                f = open('c:\MadeByKYJ\Password.txt','w')
                f.write(text1+text2)
                f.close()
                return text1+text2
            except:
                pass


while True:
    while True:
        print('\n[ 알집의 경로를 입력하세요. 단, 알집의 이름까지 같이 입력해야 합니다.]\n')
        print('ex) C:\exam\example.zip\n')
        path=input('입력 : ')
        try:
            ZipPath = zipfile.ZipFile(path) # zip파일의 경로와 zip파일 이름을 같이 넣어야한다.
            break
        except:
            clear()
            winsound.Beep(2000,30)
            print('!! 경로가 올바르지 않습니다. !!')
    while True:
        clear()
        print("\n[ 비밀번호 조합 종류 선택]\n")
        print("1. 숫자 + 영어대소문자 조합")
        print("2. 숫자 + 영어대소문자 + 특수문자를 포함한 모든 경우의 수\n")
        num=input('입력 : ')
        if num.isdigit() and (num=='1' or num=='2'):
            password_binding = str1 if num=='1' else str2
            break
            
    while True:
        clear()
        print('\n[ 찾을 비밀번호의 최대 자릿수 입력 ]\n')
        print('ex) 비번이 최대 7자리일 경우 7 입력\n')
        max_password=input('입력 : ')
        if max_password.isdigit() and int(max_password)>0:
            max_password=int(max_password)
            break
    
    
    
    print(decryption(password_binding,1,max_password,ZipPath))
    print('\n암호해독 성공, 비밀번호는 C드라이브에 MadeByKYJ 폴더 안에 Password.txt파일로 저장됩니다.')
    while True:
        input('')


    