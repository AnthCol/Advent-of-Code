import java.io.*;
import java.util.*;

// PART TWO
public class day02 {
    
    public static void main (String[] args) {
        try (Reader in = new FileReader(args[0]);
             BufferedReader br = new BufferedReader(in)) {

            String line;
            List<String> list = new ArrayList<>();

            while ((line = br.readLine()) != null) {
                list.add(line);
            }
            
            for (int i = 0; i < list.size(); i++) {
                for (int j = 0; j < list.size(); j++) {
                    if (i == j) {
                        continue;
                    } 
                 
                    List<Character> common = new ArrayList<>();
                    
                    for (int k = 0; k < list.get(i).length(); k++) {
                        if (list.get(i).charAt(k) == list.get(j).charAt(k)) {
                            common.add(list.get(i).charAt(k));
                        }
                    }
                    
                    if (common.size() == list.get(i).length() - 1) {
                        for (Character c : common) {
                            System.out.print(c);
                        }
                        System.out.println();
                        return;
                    }
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}


// // PART ONE
// public class day02 {
    
//     public static void main (String[] args) {
//         try (Reader in = new FileReader(args[0]);
//              BufferedReader br = new BufferedReader(in)) {

//             String line;
//             int twoCount = 0;
//             int threeCount = 0;

//             while ((line = br.readLine()) != null) {
//                 Map<Character, Integer> m = new HashMap<>();
                
//                 for (char c : line.toCharArray()) {
//                     m.put(c, m.getOrDefault(c, 0) + 1);
//                 } 
//                 boolean two = false;
//                 boolean three = false;
//                 for (char c : m.keySet()) {
//                     if (m.get(c) == 2) {
//                         two = true;
//                     } else if (m.get(c) == 3) {
//                         three = true;
//                     }
//                 }
                
//                 twoCount += (two) ? 1 : 0;
//                 threeCount += (three) ? 1 : 0;
//             }

//             System.out.println(twoCount * threeCount);

//         } catch (Exception e) {
//             e.printStackTrace();
//         }
//     }
// }
