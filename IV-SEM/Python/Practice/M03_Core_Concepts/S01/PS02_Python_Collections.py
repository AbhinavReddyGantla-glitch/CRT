#1480 running sum of a list
nums = [1,2,3,4]
res = []
s = 0
for ele in nums:
    s += ele
    res.append(s)
print(res)

ans = []
for i in range(1,len(nums)+1):
    ans.append(sum(nums[:i]))
print(ans)
#217 contains duplicates
nums = [1,2,3,1]
print(not(nums == list(set(nums))))

#1672 richest customer wealth
accounts = [[1,2,3],[3,2,1]]
max_wealth = sum(accounts[0])
for i in range(len(accounts)):
    if sum(accounts[i])> max_sum:
        max_sum = sum(accounts[i])
print(max_sum)
