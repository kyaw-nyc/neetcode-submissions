class Solution:

    def encode(self, strs: List[str]) -> str:
        dummystr = ""
        for i in range(len(strs)):
            count = len(strs[i])
            dummystr += str(count) + '#' + strs[i]
        return dummystr

    def decode(self, s: str) -> List[str]:
        lst = []
        pointer = 0
        while pointer < len(s):
            n = 0
            while s[pointer] != '#':
                n = n * 10 + int(s[pointer])
                pointer += 1
            pointer += 1
            word = ""
            for i in range(n):
                word += s[pointer]
                pointer += 1
            lst.append(word)
        return lst