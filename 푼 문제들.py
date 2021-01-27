'''
문제 설명

두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.

제한 조건

a와 b가 같은 경우는 둘 중 아무 수나 리턴하세요.
a와 b는 -10,000,000 이상 10,000,000 이하인 정수입니다.
a와 b의 대소관계는 정해져있지 않습니다.
'''



def solution(a, b):
    answer = 0
    if a == b:           # a,b 의 수가 같다면 둘 중 하나를 리턴해줘도 상관없다. (아니그런가?)
        return a or b
    elif a > b:                       #a가 b보다 높을 경우, answer에 반환할 자리를 바꿔보면 된다.
        return sum(range(b,a+1))
    answer += sum(range(a,b+1))       # a=0.b=6이라면 0에서 7까지의 정수. 즉,0~6까지의 모든 정수를 더하는 것이다.
    return answer

print(solution(0,6))


# 정말 조심해야 할 점. return 반환값은 가능하면 while 문과 동일한 열에 배치하자. 자칫하면 while 문 안의 일부 조건만 반환된다.




'''
문제 설명

길이가 n이고, 수박수박수박수....와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요.
예를들어 n이 4이면 수박수박을 리턴하고 3이라면 수박수를 리턴하면 됩니다.

제한 조건

n은 길이 10,000이하인 자연수입니다.

'''


def solution(n):
    answer = ''
    while n < 10000:
        s = '수박' * n          # 변수 s 에 '수박' 과 입력한 정수의 값을 곱해준다.
        answer += s[:n]        # 곱한
        return answer





'''
문제 설명
정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.

제한 사항
n은 0 이상 3000이하인 정수입니다.


입출력 예
n	return
12	28
5	6
입출력 예 설명
입출력 예 #1
12의 약수는 1, 2, 3, 4, 6, 12입니다. 이를 모두 더하면 28입니다.

입출력 예 #2
5의 약수는 1, 5입니다. 이를 모두 더하면 6입니다.
'''


def solution(n):
    answer = 0
    count = []
    for i in range(1,n+1):
        if n % i == 0:
            count.append(i)          #약수 구하기
    answer += sum(count)            # 약수 모조리 더해버리기
    return answer


print(solution(14))




# 원 문제는 소문자가 대문자보다 앞서 나오게 되는 문장도 추가하라고 했지만, 이 부분은 해결 방법을 찾지 못해 삭제했습니다.
# 나중에 추가적으로 편집할 수 있으니 우선 여기에 배치해 놓겠습니다.

'''

문제 설명
문자열 s에 나타나는 문자를 큰것부터 작은 순으로 정렬해 새로운 문자열을 리턴하는 함수, solution을 완성해주세요.
s는 영문 대소문자로만 구성되어 있다.

제한 사항
str은 길이 1 이상인 문자열입니다.

 입출력          예
   s	     return

"Zbcdefg"	"gfedcbZ"

'''

def solution(s):
    answer = ''
    while 1<=len(s):
        s=sorted(list(s))
        s=''.join(s)
        answer+=s
        return answer



print(solution('ghdjsbfkjwF'))
