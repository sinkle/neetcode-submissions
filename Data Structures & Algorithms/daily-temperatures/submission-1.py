class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            # if not st:
            #     st.append((t, i))
            #     continue

            while st:
                if t > st[-1][0]:
                    prev = st.pop()
                    res[prev[1]] = i - prev[1]
                else:
                    break

            st.append((t, i))


        return res
            

