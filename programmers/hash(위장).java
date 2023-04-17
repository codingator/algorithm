import java.util.List;
import java.util.stream.Stream;

import org.w3c.dom.css.Counter;

class HashL3 {
    public int solution(String[][] clothes) {
        int answer = 0;
        
        return answer;
    }

    public static void main(String[] args) {
        String[][] q = {{"yellow_hat", "headgear"}, {"blue_sunglasses", "eyewear"}, {"green_turban", "headgear"}};
        String[][] w = {{"crow_mask", "face"}, {"blue_sunglasses", "face"}, {"smoky_makeup", "face"}};
        HashL3 a = new HashL3();

        System.out.println(a.solution(q));
        System.out.println(a.solution(w));
        
    }
}