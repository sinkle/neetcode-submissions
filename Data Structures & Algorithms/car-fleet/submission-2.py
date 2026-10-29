class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        data = list(zip(position, speed))

        data = sorted(data, key=lambda d: d[0], reverse=True)

        it = []
        for d in data:
            it.append((target - d[0]) / d[1])
        
        c_m = -1
        res = 0
        for i in it:
            if i > c_m:
                res += 1
                c_m = i
        return res
             

            