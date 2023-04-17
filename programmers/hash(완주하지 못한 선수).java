import java.util.Hashtable;

class HashL1 {
    public String solution(String[] participant, String[] completion) {
        Hashtable<String, Integer> ht = new Hashtable<String, Integer>();
        String answer = "";
        
        for (String s : participant) {
            if (ht.containsKey(s)) {
                ht.replace(s, ht.get(s) + 1);
            } else {
                ht.put(s, 1);
            }
        }
        
        for (String k : completion) {
            if (ht.containsKey(k)) {
                ht.replace(k, ht.get(k) - 1);
            }
            
            if (ht.get(k) == 0) {
                ht.remove(k);
            }
        }
        
        answer = ht.keys().nextElement();
        return answer;
    }
}