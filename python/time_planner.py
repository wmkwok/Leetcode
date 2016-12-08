##Implement  meeting planner that can schedule meetings between two persons at a time.
class Solution():
    def plan(self, dur, t1, t2):
        i = 0
        j = 0
        while(i < len(t1) and j < len(t2)):
            ##if there is an intersection
            if((t1[i][0] <= t2[j][0] and t1[i][1] <= t2[j][1]) or
               (t1[i][0] >= t2[j][0] and t1[i][1] >= t2[j][1])):
                ##if the intersect's duration is enough
                if(abs(max(t1[i][0], t2[j][0]) - min(t1[i][1], t2[j][1])) >= dur):
                    return [max(t1[i][0], t2[j][0]) , max(t1[i][0], t2[j][0])+dur]

            ##increment the one that ends earlier
            if(t1[i][1] < t2[j][1]):
                i += 1
            else:
                j += 1
        return []

sol = Solution()
t1 = [[6, 7], [13,20],[8,10],[1,4]]
t2 = [[2,5],[7,10],[12,16]]
t3 = [[1,4],[6,8]]
t4 = [[2,4],[5,7]]

print sol.plan(3, t1, t2)       
print sol.plan(3, t3, t4)
        
        
