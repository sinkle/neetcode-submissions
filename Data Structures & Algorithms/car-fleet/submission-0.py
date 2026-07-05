class Solution:
    # def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
    #     st = []
    #     d = {position[i]: (speed[i], 0) for i in range(len(position))}
    #     res = 0
    #     while d:
    #         for p, (s, step) in d.items():
    #             d.pop(p)
    #             step += 1
    #             p += s
    #             if p in d and d[p][1] == step:
    #                 pass
    #             else:
    #                 d[p] = (s, step)
                
    #         for p, (s, step) in d.items():
    #             if p >= target:
    #                 d.pop()
    #                 res += 1
    #     return res

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        st = []
        l = list(zip(position, speed))
        l = sorted(l, key=lambda x: x[0], reverse=True)

        for p, s in l:
            t = (target - p) / s
            if not st:
                st.append(t)
                continue
            if t > st[-1]:
                st.append(t)

        return len(st)

