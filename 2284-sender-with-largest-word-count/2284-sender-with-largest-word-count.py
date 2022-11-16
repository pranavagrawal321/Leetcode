class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        d = defaultdict(int)
        for i in range(len(senders)):
            d[senders[i]] += len(messages[i].split())
        max = 0
        name = []
        for i in sorted(d):
            if d[i] >= max:
                max = d[i]
                name.append(i)
        name.sort()
        return name[-1]
