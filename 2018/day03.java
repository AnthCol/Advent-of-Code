// PART TWO
import java.io.*;
import java.util.*;
import java.util.stream.*;

public class day03 {

    static class Index {
        public int x;
        public int y;

        public Index(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public boolean equals(Object obj) {
            Index i = (Index)obj;
            return this.x == i.x && this.y== i.y;
        }

        @Override
        public int hashCode() {
            return Objects.hash(x, y);
        }
    }    

    public static void main (String[] args) {
        try (Reader in = new FileReader(args[0]);
             BufferedReader br = new BufferedReader(in)) {
            
            Map<Index, Boolean> map = new HashMap<>();

            String line;
            int validClaim = -1;
            while ((line = br.readLine()) != null) {
                List<Integer> values = Arrays.stream(line.split("\\D+"))
                                             .filter(string -> !string.isEmpty())
                                             .map(Integer::parseInt)
                                             .collect(Collectors.toList());
                
                int startingColumn = values.get(1);
                int startingRow = values.get(2);
                int width = values.get(3);
                int height = values.get(4);
                
                boolean allUntouched = true;                

                for (int i = 0; i < width; i++) {
                    for (int j = 0; j < height; j++) {
                        int xVal = startingColumn + i;
                        int yVal = startingRow + j;
                        Index index = new Index(xVal, yVal);

                        if (map.get(index) != null) {
                            allUntouched = false;
                        } else {
                            map.put(index, true);
                        }
                    }
                }
                
                if (allUntouched) {
                    validClaim = values.get(0);
                }
            }
            
            // NOTICE: 
            // I have no idea what's up with this. 
            // The correct answer was the 
            System.out.println(validClaim);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}


// // PART ONE
// import java.io.*;
// import java.util.*;
// import java.util.stream.*;

// public class day03 {

//     static class Index {
//         public int x;
//         public int y;

//         public Index(int x, int y) {
//             this.x = x;
//             this.y = y;
//         }

//         @Override
//         public boolean equals(Object obj) {
//             Index i = (Index)obj;
//             return this.x == i.x && this.y== i.y;
//         }


//         @Override
//         public int hashCode() {
//             return Objects.hash(x, y);
//         }
//     }    

//     public static void main (String[] args) {
//         try (Reader in = new FileReader(args[0]);
//              BufferedReader br = new BufferedReader(in)) {
            
//             Map<Index, Integer> map = new HashMap<>();

//             String line;
//             while ((line = br.readLine()) != null) {
//                 List<Integer> values = Arrays.stream(line.split("\\D+"))
//                                              .filter(string -> !string.isEmpty())
//                                              .map(Integer::parseInt)
//                                              .collect(Collectors.toList());
                
//                 int startingColumn = values.get(1);
//                 int startingRow = values.get(2);
//                 int width = values.get(3);
//                 int height = values.get(4);
                
//                 for (int i = 0; i < width; i++) {
//                     for (int j = 0; j < height; j++) {
//                         int xVal = startingColumn + i;
//                         int yVal = startingRow + j;
//                         Index index = new Index(xVal, yVal);
//                         map.put(index, map.getOrDefault(index, 0) + 1);
//                     }
//                 }
//             }
            
//             long count = map.values().stream().filter(val -> val > 1).count(); 
//             System.out.println(count);

//         } catch (Exception e) {
//             e.printStackTrace();
//         }
//     }
// }

