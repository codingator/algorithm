import java.util.SortedMap;
import java.util.TreeMap;

class HashL2 {
    String chk = "0"; // 이거 어케하노...
    public boolean solution(String[] phone_book) {
        SortedMap<String, Boolean> hm = new TreeMap<>();
        boolean answer = true;
        
        for (String s : phone_book) hm.put(s, true);
        for (String s : hm.keySet()) {
            if (chk.charAt(0) != s.charAt(0)) {
                chk = s;
                continue;
            }

            if (hm.computeIfPresent(s, (k, v) -> s.startsWith(chk) ? true : false)) return false;
        }

        return answer;
    }
}