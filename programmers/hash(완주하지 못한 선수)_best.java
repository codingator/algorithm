import java.util.HashMap;

class HashL1S {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        HashMap<String, Integer> hm = new HashMap<>();
        for (String player : participant)
            hm.put(player, hm.getOrDefault(player, 0) + 1);
        for (String player : completion)
            hm.put(player, hm.get(player) - 1);

        for (String key : hm.keySet()) {
            if (hm.get(key) != 0) {
                answer = key;
                break;
            }
        }
        return answer;
    }

    public String solution2(String[] participant, String[] completion) { 
        HashMap map = new HashMap<>(); 
        for (int i = 0; i < participant.length ; i++) { 
            map.compute(participant[i], (k, v) -> v != null ? null : 1); 
            if (i < completion.length) map.compute(completion[i], (k,v) -> v != null ? null : 1); 
        } 
        
        return (String) map.keySet().iterator().next();
    }
}

