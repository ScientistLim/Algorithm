class Solution:
    def isPalindrome(self, s: str) -> bool:
        #모든 대문자를 소문자로 변환
        s = s.lower()

        # 문자열에서 알파벳과 숫자만 유지
        chars = [char for char in s if char.isalnum()]
        s = ''.join(chars)
        
        # 회문 확인
        return s == s[::-1]