'''
문제 설명
양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다.
예를 들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다.
자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수, solution을 완성해주세요.

제한 조건
x는 1 이상, 10000 이하인 정수입니다.

입출력     예
arr	    return
10	    true
12	    true
11	    false
13	    false

입출력 예 설명
입출력 예 #1
10의 모든 자릿수의 합은 1입니다. 10은 1로 나누어 떨어지므로 10은 하샤드 수입니다.

입출력 예 #2
12의 모든 자릿수의 합은 3입니다. 12는 3으로 나누어 떨어지므로 12는 하샤드 수입니다.

입출력 예 #3
11의 모든 자릿수의 합은 2입니다. 11은 2로 나누어 떨어지지 않으므로 11는 하샤드 수가 아닙니다.

입출력 예 #4
13의 모든 자릿수의 합은 4입니다. 13은 4로 나누어 떨어지지 않으므로 13은 하샤드 수가 아닙니다.
'''


def harshad(x):
    answer = True
    while 1<=x<=10000:
        if x%sum([int(i) for i in str(x)])==0:      # 푼 문제들2.py 에서 자릿수 합 구하기를 알았다면, 크게 어렵지 않을 것이다.
            return answer                           # 자연수에 자릿수 총합을 나눌수 있다면, 그것이 하샤드 수이기에,
        else:                                       # 자연수 x에서 총합의 나머지가 0이기만 하면 된다.
            return False
print(harshad(18))



'''
문제 설명
프로그래머스 모바일은 개인정보 보호를 위해 고지서를 보낼 때 고객들의 전화번호의 일부를 가립니다.
전화번호가 문자열 phone_number로 주어졌을 때, 
전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 *으로 가린 문자열을 리턴하는 함수, solution을 완성해주세요.

제한 조건
s는 길이 4 이상, 20이하인 문자열입니다.


입출력             예
phone_number	return
'01033334444'	'*******4444'
'027778888'	    '*****8888'
'''


def solution(phone_number):
    answer = ''
    while 4<=len(phone_number)<=20:
        answer+='{}'.format('*'*(len(phone_number)-4),phone_number)+phone_number[-4:]
        # 전화번호 뒷자리 4 개를 제외하고 나머지만 *로 바꿔줘야만 한다. 그렇다면 4개를 제외한 나머지를
        # format 함수를 이용하여 대체한다. 4자리만 제외한 자리만 *로 대체하기 위해,
        # len(phone_number)-4를 삽입한다. 미안하다. 한 눈에 이해하기 힘든 코딩이라 설명하기 어렵다.

        return answer


print(solution('024635677'))




'''
문제 설명
두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요. 배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다. 예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.

제한 사항
두 수는 1이상 1000000이하의 자연수입니다.

입출력 예

n	m	return
3	12	[3, 12]
2	5	[1, 10]

입출력 예 설명

입출력 예 #1
위의 설명과 같습니다.

입출력 예 #2
자연수 2와 5의 최대공약수는 1, 최소공배수는 10이므로 [1, 10]을 리턴해야 합니다.


'''


import math

def solution(n, m):
    answer = []
    answer.append(math.gcd(n,m))             # n 과 m 의 최대공약수 구해서 answer 에 추가.
    answer.append((n*m)//math.gcd(n,m))      # n 과 m 을 곱한 다음, 최대 공약수를 나누면 최소공배수가 나온다.
    return answer

print(solution(2,5))





'''
자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

제한 조건
n은 10,000,000,000이하인 자연수입니다.

입출력 예
n	    return
12345	[5,4,3,2,1]
'''

def reverseArray(n):
    return [int(i) for i in str(n)][::-1]   # n 을 문자열로 캐스팅하고 [::-1]로 거꾸로 출력, int 로 캐스팅한 i를 반복하여 출력해준다.
print(reverseArray(12345))

# 아직 한 줄짜리 함수에는 익숙치가 않다. 