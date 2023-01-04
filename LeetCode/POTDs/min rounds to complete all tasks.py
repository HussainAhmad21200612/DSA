import collections
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        ll=collections.Counter(tasks)
        # for i in tasks:
        #     if i not in ll:
        #         ll[i]=tasks.count(i)
        tot_ans=0
        print(ll)
        for a in ll.keys():
            i=ll[a]
            if i==1:
                return -1
            if i%3==0:
                tot_ans+=i//3
            elif i%3==2:
                tot_ans+=i//3+1
            elif i%3==1:
                tot_ans+=i//3+1
        return tot_ans
