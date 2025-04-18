'''
n&1 으로 가장 오른쪽 비트를 확인하기
n = n >>1로 비트를 오른쪽으로 이동시키면서 반복

O(K) => K는 n의 비트 길이. 숫자의 비트 수만큼 반복.
시간 복잡도는 비트 길이에 비례함

O(1) => 추가 메모리 사용 없이 상수 공간만 사용

Runtime 0ms
Memory 17.71mb
'''

def hammingWeight(self, n: int) -> int:
    count = 0
    while n :
        count +=n & 1
        n >>= 1
    return count
