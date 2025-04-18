# converting all uppercase letters into lowercase letters 
# remove all non-alphanumeric characters

'''
(1) 모든 문자를 lowercase로 변경
(2) 띄어쓰기, 쉼표 등을 모두 제거
'''

def isPalindrome(self, s:str) -> bool:
    s = s.lower()
    # 소문자 알파벳과 숫자가 아닌 문자가 제거됨
    s = re.sub('[^a-z0-9]','',s)
    return s == s[::-1]
