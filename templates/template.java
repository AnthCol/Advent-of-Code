import java.io.*;
import java.util.*;


public class Template {
    
    public static void main (String[] args) {
        try (Reader in = new FileReader(args[0]);
             BufferedReader br = new BufferedReader(in)) {

            String line;
            while ((line = br.readLine()) != null) {
            
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

