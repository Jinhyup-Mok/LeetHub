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