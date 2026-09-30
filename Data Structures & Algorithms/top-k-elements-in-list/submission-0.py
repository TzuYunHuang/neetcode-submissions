class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1
        dic_sort = sorted(dic.items(), key=lambda x: x[1],reverse=True)
        return [d[0] for d in dic_sort[:k]]
        