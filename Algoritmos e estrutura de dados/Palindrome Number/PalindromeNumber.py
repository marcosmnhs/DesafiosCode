class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        copy = x
        cont = 0

        while copy >= 10:
            copy = copy // 10
            cont += 1
        cont+= 1

        copy = x
        final = 0

        while cont != 0:
            algarismo = copy % 10
            copy = copy // 10
            cont -= 1
            final += algarismo*10**(cont)
            
        if x == final:
            return True
        return False
