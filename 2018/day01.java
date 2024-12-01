import java.io.*;
import java.util.*;


// PART TWO
public class Day01 {
    public static void main(String[] args) {

        try (Reader in = new FileReader(args[0]);
             BufferedReader br = new BufferedReader(in)) {

            String line;
            int freq = 0;
            ArrayList<String> lines = new ArrayList<>();

            while ((line = br.readLine()) != null) {
                lines.add(line);
            }
            
            int index = 0; 
            Set<Integer> s = new HashSet<>();            

            while (true) {
                line = lines.get(index);
                char sign = line.charAt(0);
                int value = Integer.parseInt(line.substring(1));
                freq += (sign == '+') ? value : -value;
                
                if (s.contains(freq)) {
                    System.out.println(freq);
                    break;
                } else {
                    s.add(freq);
                }

                index = (index == lines.size() - 1) ? 0 : index + 1;
            }

            
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}




// PART ONE
// public class Day01 {
//     public static void main(String[] args) {

//         try (Reader in = new FileReader(args[0]);
//              BufferedReader br = new BufferedReader(in)) {

//             String line;
//             int freq = 0;

//             while ((line = br.readLine()) != null) {
//                 char sign = line.charAt(0);
//                 int value = Integer.parseInt(line.substring(1)); 
//                 freq += (sign == '+') ? value : -value;
//             }

//             System.out.println(freq);

//         } catch (Exception e) {
//             e.printStackTrace();
//         }
//     }
// }