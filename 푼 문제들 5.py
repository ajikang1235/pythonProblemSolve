'''
정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수, solution을 완성해주세요.
단, 리턴하려는 배열이 빈 배열인 경우엔 배열에 -1을 채워 리턴하세요. 예를들어 arr이 [4,3,2,1]인 경우는 [4,3,2]를 리턴 하고, [10]면 [-1]을 리턴 합니다.

제한 조건
arr은 길이 1 이상인 배열입니다.
인덱스 i, j에 대해 i ≠ j이면 arr[i] ≠ arr[j] 입니다.  ← 중복값이라고 생각해주면 좋다.

입출력 예
arr	        return
[4,3,2,1]	[4,3,2]
[10]        [-1]
'''


def solution(arr):
    answer=[]
    if len(arr) > 1:                      # 배열 중 최솟값을 골라야 하니 배열의 길이는 최소 2 이상이어야 한다.
        arr.remove(min(arr))              # 배열의 최솟값을 골라내서 remove 로 제거해 준다.
        answer += arr
        return answer
    elif len(arr)<= 1:                    # 길이가 1 이하인 배열은 모두
        answer.append(-1)                 # answer 에 -1을 추가해준다.
        return answer



print(solution([1,1,1,2]))

# 단 , 이 방식은 한 배열에 최솟값이 중복되는 경우 ex) arr = [2,2,3,4]
# remove 함수로 제거했을 시 하나의 최솟값 만을 제거해주기 때문에 중복되는 값 모두를 제거해줄 수 가 없다.
# 그래서 반만 완성된 풀이방식이다.


'''
문제 설명
함수 solution은 정수 n을 매개변수로 입력받습니다. n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요.
예를들어 n이 118372면 873211을 리턴하면 됩니다.

제한 조건
n은 1이상 8000000000 이하인 자연수입니다.

입출력 예
n	    return
118372	873211
'''

def solution(n):
    answer = 0
    reverse_num=sorted(str(n),reverse=True)   # 숫자열 n 을 문자열로 캐스팅 후, 내림차순 정렬
    strIntoint=''.join(reverse_num)           # 정렬된 리스트를 다시 join 함수로 문자열로 바꿔준다.
    answer+=int(strIntoint)                   # 문자열을 숫자형으로 캐스팅, 결과값에 반환
    return answer


print(solution(118372))




'''
문제 설명
대문자와 소문자가 섞여있는 문자열 s가 주어집니다. s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True,
다르면 False를 return 하는 solution를 완성하세요. 'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다.
단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.

예를 들어 s가 pPoooyY면 true를 return하고 Pyy라면 false를 return합니다.

제한사항
문자열 s의 길이 : 50 이하의 자연수
문자열 s는 알파벳으로만 이루어져 있습니다.

입출력     예
s	      answer
pPoooyY	  true
Pyy	      false

입출력 예 설명
입출력 예 #1
'p'의 개수 2개, 'y'의 개수 2개로 같으므로 true를 return 합니다.

입출력 예 #2
'p'의 개수 1개, 'y'의 개수 2개로 다르므로 false를 return 합니다.
'''


def solution(s):
    s=s.lower()                               # 모든 문자를 소문자화 해준다. 이러면 P 가 오든 p 가오든, 같이 처리가 가능하다.
    if s.count('p')==s.count('y'):            # s안에 p와 y의 개수가 같으면 True로 반환
        return True
    elif s.count('p')!=s.count('y'):          # 다르면 False 를 출력
        return False


print(solution('oo'))                         #  p 와 y 둘 다 없으면, 갯수는 둘 다 0이니 첫 번째 조건에 부합한다.



'''
String형 배열 seoul의 element중 Kim의 위치 x를 찾아, 김서방은 x에 있다는 String을 반환하는 함수, solution을 완성하세요.
seoul에 Kim은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.

제한 사항
seoul은 길이 1 이상, 1000 이하인 배열입니다.
seoul의 원소는 길이 1 이상, 20 이하인 문자열입니다.
Kim은 반드시 seoul 안에 포함되어 있습니다.

입출력 예
seoul	        return
["Jane", "Kim"]	"김서방은 1에 있다"
'''

def solution(seoul):
    kim_seoul=seoul.index('Kim')       # index 함수는 find 함수와 같이 특정 문자를 찾는데에 도움을 준다.
    return "김서방은 {}에 있다".format(kim_seoul)
    #  그러나 index 함수는 find 와 달리 배열, 튜플에도 적용이 가능하다.
    # format 함수에 집어 넣어준다.


print(solution(['Jane','Kim']))


'''
1937년 Collatz란 사람에 의해 제기된 이 추측은, 주어진 수가 1이 될때까지 다음 작업을 반복하면, 모든 수를 1로 만들 수 있다는 추측입니다. 작업은 다음과 같습니다.

1-1. 입력된 수가 짝수라면 2로 나눕니다.
1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더합니다.
2. 결과로 나온 수에 같은 작업을 1이 될 때까지 반복합니다.
예를 들어, 입력된 수가 6이라면 6→3→10→5→16→8→4→2→1 이 되어 총 8번 만에 1이 됩니다.
위 작업을 몇 번이나 반복해야하는지 반환하는 함수, solution을 완성해 주세요.
단, 작업을 500번을 반복해도 1이 되지 않는다면 –1을 반환해 주세요.

제한 사항
입력된 수, num은 1 이상 8000000 미만인 정수입니다.

입출력 예
n	    result
6	    8
16	    4
626331	-1

입출력 예 설명

입출력 예 #1
문제의 설명과 같습니다.

입출력 예 #2
16 -> 8 -> 4 -> 2 -> 1 이되어 총 4번만에 1이 됩니다.

입출력 예 #3
626331은 500번을 시도해도 1이 되지 못하므로 -1을 리턴해야합니다.
'''



def solution(num):
    count = 0
    while num>1:
        if num%2==1:        # num 이 홀수라면
            num=(num*3)+1   # num 에 3을 곱하고 1을 더해주고 카운트를 하나씩 추가. num 과 동일 값을 입력해준다.
            count+=1
        elif num%2==0:      # num 이 짝수라면
            num=num/2       # num 을 2로 나눠주고 카운트에 하나씩 추가, 역시 num 과 동일 값을 입력해준다.
            count+=1
        elif num==1:        # num 이 1이 되면, 빠져나온다.
            break

    if count>=500:          # 카운트가 500 이상일 겅우, -1 을 반환해준다.
        return -1


    return count


print(solution(626331))

# 입력 인수의 값을 변하게 만들려면, 인수를 변수로서 추가하는 방법이 있다. 잘 활용해두길 바란다.