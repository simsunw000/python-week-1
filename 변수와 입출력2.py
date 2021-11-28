# 입력 input

# 1) 문장 입력
# 변수 = input('입력 전에 작성할 수 있는 안내문을 작성할 수 있는 공간')

# 2) 숫자 입력
'''
number = input('숫자를 입력해주세요.')

print(number + 10) # 오류 발생 이유 : number 는 str 타입, 문장이므로
'''
# 캐스팅(casting)을 이용하여 해결
# 캐스팅이란? 특정 형태를 다른 형태로 변경하는 행위 (형 변환)

# number = int(input('숫자를 입력해주세요.'))

# 입력과 출력 기능을 이용해서 다음 상황을 연출해보자.

# 1. 안내문을 통해 플레이어의 이름을 입력 받겠습니다.

# 2. 플레이어의 정보는 랜덤으로 설정됩니다. (힌트 참고)
# 능력치의 설정은 HP , ATK, DEF
# 각각의 능력치는 다음과 같습니다.
# HP의 경우 50 + 1 ~ 10 사이의 랜덤값
# ATK의 경우 1 ~ 5 사이의 랜덤값
# DEF의 경우 0 ~ 3 사이의 랜덤값

# 3. 출력문을 이용해 상태창을 표현합니다.

import random
# 해당 문장 작성 시 random.py의 기능을 사용할 수 있다.

a = random.randint(1,10)
b = random.randint(1,5)
c = random.randint(0,3)

HP = a + 50
ATK = b
DEF = c

name = input('플레이어의 이름을 입력해주세요.')

print('''
캐릭터 이름: {}
HP: {}
ATK: {}
DEF: {}
'''.format(name,HP,ATK,DEF))


''' 풀이
Player_name = input('플레이어의 이름을 입력해주세요.')

HP = 50 + random.randint(1,10)
ATK = random.randint(1,5)
DEF = random.randint(0,3)

print (f"[이름:{Player_name} HP {HP} ATK {ATK} DEF {DEF}]")
'''









