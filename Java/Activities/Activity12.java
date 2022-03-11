package examples;

interface Addable {
    int add(int c, int d);
}

public class Activity12 {
    public static void main(String[] args) {

     
        Addable ad1 = (c, d) -> (c + d);
        System.out.println(ad1.add(10, 20));

       
        Addable ad2 = (int c, int d) -> {
            return (c + d);
        };
        System.out.println(ad2.add(100, 200));
    }
}
