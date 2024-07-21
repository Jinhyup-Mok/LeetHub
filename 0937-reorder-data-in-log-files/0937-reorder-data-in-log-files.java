class Solution {
    public String[] reorderLogFiles(String[] logs) {
        
        List<String> digits = new ArrayList<>();
        List<String> letters = new ArrayList<>();

        for(String str : logs) {
            String[] strs = str.split(" ");
            int len = strs.length;
            if(strs[len-1].matches("[0-9]+")) {
                digits.add(str);
            } else {
                letters.add(str);
            }
        }

        Collections.sort(letters, (s1,s2) -> {
            String[] part1 = s1.split(" ", 2); // [identifier, contents] 로 split
            String[] part2 = s2.split(" ", 2);
            // split(split 기준, 배열 limit)
            // split(" ", 2) : 공백을 기준으로 split 하되 split한 결과의 배열의 크기는 2로 제한 -> 즉, 첫번째로 등장한 공백만을 기준으로 split 된다 ex) ["hello", "my name is jinhyup"]
            
            // compareTo == 0 : 비교한 두 값이 같다! -> identifier 기준으로 정렬!
            if (part1[1].compareTo(part2[1]) == 0) return part1[0].compareTo(part2[0]);

            // compareTo == 1, -1 -> 비교한 두 값이 다르므로, contents 기준으로 정렬!
            return part1[1].compareTo(part2[1]);
        });

        for(String dig : digits) {
            letters.add(dig);
        }

        String[] result = new String[letters.size()];
        result = letters.toArray(result);
        // ArrayList인 letters를 String[] result의 문자배열 자료형으로 변환

        return result;
    }
}
