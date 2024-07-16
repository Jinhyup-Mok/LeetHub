class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        letters = []
        digits = []
        
        for log in logs:
            # 조건문에서 split을 활용하여 조건문에서만 split한 log를 활용하고, 나머지에서 log의 형태를 그대로 쓸 수 있게!!
            if log[-1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        # 두가지 기준으로 정렬
        # list.sort(key= ...) 으로 정렬의 기준을 정할 수 있다!!
        # First key : content, if First is same then Seconds key : identifier
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))

        return letters + digits


        