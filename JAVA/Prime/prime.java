// package Prime;

public class prime{
    
    public static void main(String[] args) {
       for(int i=0;i<110;i++){
        checkPrime(i);
       }
        
    }
    static void checkPrime(int n){
        Boolean Flag=false;
        for(int i=2;i<n/2;i++){
            if(n%i==0){
                // System.out.println(n+" is not prime.");
                Flag=true;
                break;
            }
        }
        if (!Flag){
            System.out.println(n+" is prime.");
        }

    }
}