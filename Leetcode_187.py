class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        #A,C,T,G
        #repeats in substring 10 letter long
        #bruteforce put each 10 letter in hash and check hash each time , timeO(n), space O(n)
        #sliding window? wouldnt work except niche cases and still best O(n)
        
        ht = {}
        # set over array eliminate repeated values 
        final = set()
        for i in range(0,len(s)-9):
            #print statment double checking lenth calculation are correct 
            #print(i,s[i])
            sub = s[i:i+10] 
            if sub in ht:
                #print(s[i:i+10])
                final.add(sub)
            else:
                ht[sub] = sub
                #print((s[i:i+10])
        return list(final)
    
# optimized shorter code double set 
#eliminates need for else and makes more sense in flow of code
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen,final = set(),set()
        for i in range(0,len(s)-9):
            sub = s[i:i+10] 
            if sub in seen:
                final.add(sub)
            seen.add(sub)
        return list(final)