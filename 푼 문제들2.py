'''
문제 설명
단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

재한사항
s는 길이가 1 이상, 100이하인 스트링입니다.

입출력 예
s	      return
"abcde"	    "c"
"qwer"	    "we"
'''


def solution(s):
    answer = ''
    while 1 <= len(s) <= 100:
        if len(s) % 2 == 0:
            Even_middle = s[(len(s)//2-1):len(s)//2+1]
            answer += Even_middle
            return answer
        elif len(s) % 2 != 0:
            Odd_middle = s[len(s) // 2]
            answer += Odd_middle
            return answer

print(solution('ttui'))







'''
배열 arr에 입력된 원소들의 평균값을 return 하는 함수를 구하시오. 
'''

def solution(arr):
    answer = 0
    answer+=sum(arr)/len(arr)   # 배열 원소의 총합을 구하고 배열 원소의 길이를 나누면 평균이 된다
    return answer

print(solution([1,2,3,4]))      #쨘


'''
문제 설명

문자열 s를 숫자로 변환한 결과를 반환하는 함수, solution을 완성하세요.

제한 조건

s의 길이는 1 이상 5이하입니다.
s의 맨앞에는 부호(+, -)가 올 수 있습니다.
s는 부호와 숫자로만 이루어져있습니다.
s는 0으로 시작하지 않습니다.

입출력 예

예를들어 str이 '1234'이면 1234를 반환하고, '-1234'이면 -1234를 반환하면 됩니다.
str은 부호(+,-)와 숫자로만 구성되어 있고, 잘못된 값이 입력되는 경우는 없습니다.

'''

def solution(s):
    answer = 0
    while 1<=len(s)<=5:
        answer+=int(s)        # 문자열이 없는 이상
        return answer

print(solution('-1234'))





'''
문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요.
예를 들어 s가 a234이면 False를 리턴하고 1234라면 True를 리턴하면 됩니다.

제한 사항

s는 길이 1 이상, 길이 8 이하인 문자열입니다.

입출력 예

s	   return
'a234'	false
'1234'	true
'''


def solution(s):
    answer = True
    if len(s)==4 or len(s)==6:
        try:
            int(s)
            return answer
        except ValueError:
            return False
    else:
        return False


# isdecimal 함수로는 설명하는 조건에 완전히 부합하지 않는다. 왜냐하면
# isdecimal 함수는 int 변환이 가능한 문자열만을 보여주기 때문에 다른 특수문자가 전혀 개입할 수 없기 때문이다,
# 문제를 씨발 개같이 냈다.




print(solution('#125'))

'''
문제 설명

정수 num이 짝수일 경우 Even을 반환하고 홀수인 경우 Odd를 반환하는 함수, solution을 완성해주세요.

제한 조건

num은 int 범위의 정수입니다.
0은 짝수입니다.

입출력     예
num	    return
3	    Odd
4	    Even

'''

def evenodd(num):
    answer = ''
    while int:         # 음수도 포함되어 있어야 하니, 전체를 다 int(정수)로 표현
        if num%2==0:
            answer+='Even'        # 2로 나눌때 나머지 없으니 짝수로
        else:
            answer+='Odd'         # 2로 나눌때 나머지 있으니 홀수로
        return answer

print(evenodd(-1))



'''
문제 설명

자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.

제한사항

N의 범위 : 100,000,000 이하의 자연수

입출력     예
N	    answer
123	    6
987	    24

입출력 예 설명

입출력 예 #1
문제의 예시와 같습니다.

입출력 예 #2
9 + 8 + 7 = 24이므로 24를 return 하면 됩니다.
'''

def digitnum(x):
    answer=0
    while x<=100000000:
        answer+=sum([int(i) for i in str(x)])    # 정수 i를 문자열로 대입하여 리스트로 만들기 + 리스트 원소를 다 더해버리기
        return answer

print(digitnum(353255))