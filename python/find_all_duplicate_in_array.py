# for (i = 0; i < size; i++)      
# {
#     if (arr[abs(arr[i])] >= 0)
#     arr[abs(arr[i])] = -arr[abs(arr[i])];
#     else
#     printf(" %d ", abs(arr[i]));
# }
# }

class Solution(object):
    def dup(self, l):
        answer = []
        for i in range(len(l)):
            if l[abs(l[i])-1] >= 0:
                l[abs(l[i])-1] = -l[abs(l[i])-1]
            else:
                answer.append(abs(l[i]))
        return answer

sol = Solution()
print sol.dup([4, 3, 2, 7, 8, 2, 3, 1])
                
