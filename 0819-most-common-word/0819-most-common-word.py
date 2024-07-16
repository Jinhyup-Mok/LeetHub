class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub("[^\w]", " ", paragraph).lower() # ^\w : 단어가 아닌 모든 문자 필터링
        words = [word for word in paragraph.split() if word not in banned]
        # 리스트 컴프리헨션을 이용한 필터링!!

        word = collections.Counter(words)

        # most_common(1) : 가장 빈도수가 높은 1순위까지
        # most_common(1)[0] : 가장 빈도수가 높은 1순위까지 중에서 첫번째 값 선택
        # most_common(1)[0][0] : ["값", 빈도수]에서의 "값" 출력
        return word.most_common(1)[0][0]



        