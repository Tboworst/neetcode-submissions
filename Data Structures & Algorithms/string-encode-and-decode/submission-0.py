class Solution:

    def encode(self, strs: List[str]) -> str:

        #once the string is encoded you pass it in the decode
        result = ""
        for s in strs:
            result += str(len(s))+ "#"+s
        return result



    def decode(self, s: str) -> List[str]:
        result = []

        i = 0

        while i < len(s):
            hash_idx = s.index('#',i)

            length = int(s[i:hash_idx])

            string = s[hash_idx+1:hash_idx+1+length]
            result.append(string)
            
            i = hash_idx+1+length
        
        return result


'''
Input strs-> first function takes a lits of strings and returning a strings
Input s -> takes in that string and decodes it back to a list of strings



'''