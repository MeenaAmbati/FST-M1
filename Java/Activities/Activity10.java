import java.util.HashSet;

public class Activity10 {
    public static void main(String[] args) {
        HashSet<String> hs = new HashSet<String>();
       
        hs.add("A");
        hs.add("M");
        hs.add("E");
        hs.add("E");
        hs.add("N");
        hs.add("A");
        
        
        System.out.println("Original HashSet: " + hs);        
       
        System.out.println("Size of HashSet: " + hs.size());
        
       
        System.out.println("Removing A from HashSet: " + hs.remove("E"));
      
        if(hs.remove("Z")) {
        	System.out.println("Z removed from the Set");
        } else {
        	System.out.println("Z is not present in the Set");
        }
        
        //Search for element
        System.out.println("Checking if M is present: " + hs.contains("M"));
        //Print updated HashSet
        System.out.println("Updated HashSet: " + hs);
    }
}
