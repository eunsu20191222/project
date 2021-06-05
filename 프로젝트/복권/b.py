import random
from time import sleep 

lottery = ["1", "2", "3", "4", "5", "6", "7", "8" , "9", "10"]

result = random.choice(lottery)
result2 = result

print('세번의 기회가 있습니다, 시작 합니다')

print(3)
sleep(1)
print(2)
sleep(1)
print(1)
sleep(1)

ask = input("1 부터 10까지에 복권 숫자를 너어 주세요: ")
str(ask)

if ask == result2:
    print('정답 1000만원 당첨')
else:
    print("아깝")
    print(result)
    lottery.remove(result2)

ask = input("2번째: 1 부터 10까지에 복권 숫자를 너어 주세요: ")
str(ask)

if ask == result2:
    print('정답 1000만원 당첨')
else:
    print("아깝")
    print(result)
    lottery.remove(result2)

ask = input("3번째: 1 부터 10까지에 복권 숫자를 너어 주세요: ")
if ask == result2:
    print('정답 1000만원 당첨')
else:
    print("아깝")
    print(result)
    lottery.remove(result2)


#끝