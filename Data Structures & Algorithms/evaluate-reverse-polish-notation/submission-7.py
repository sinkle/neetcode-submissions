class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for t in tokens:
            if t == "+":
                s_a = st.pop()
                f_a = st.pop()
                st.append(f_a + s_a)
            elif t == "-":
                s = st.pop()
                m = st.pop()
                st.append(m - s)
            elif t == "*":
                s = st.pop()
                m = st.pop()
                st.append(m * s)
            elif t == "/":
                s = st.pop()
                m = st.pop()
                st.append(int(m / s))
            else:
                st.append(int(t))
        return st.pop()