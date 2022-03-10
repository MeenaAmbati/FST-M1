import java.util.HashMap;

public class Activity11 {
    public static void main(String[] args) {
        HashMap<Integer, String> hash_map = new HashMap<Integer, String>();
        hash_map.put(1, "Pink");
        hash_map.put(2, "Navy Blue");
        hash_map.put(3, "Red");
        hash_map.put(4, "Orange");
        hash_map.put(5, "Violet");

   
        System.out.println("The Original map: " + hash_map);
        
       
        hash_map.remove(4);
        
        System.out.println("After removing Orange: " + hash_map);
        
        
        if(hash_map.containsValue("Pink")) {
            System.out.println("Pink exists in the Map");
        } else {
            System.out.println("Pink does not exist in the Map");
        }
        
      
        System.out.println("Number of pairs in the Map is: " + hash_map.size());
    }
}
