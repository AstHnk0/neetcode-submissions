# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        arr = []

        for i in range(len(pairs)):
            j = i - 1
            while j >= 0 and pairs[j + 1].key < pairs[j].key:
                tmp = pairs[j + 1].key
                tmp2 = pairs[j + 1].value

                pairs[j + 1].key = pairs[j].key
                pairs[j + 1 ].value = pairs[j].value

                pairs[j].key = tmp
                pairs[j].value = tmp2
                j -= 1
            arr.append([Pair(p.key, p.value) for p in pairs])
        return arr