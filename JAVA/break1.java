public class break1{
     public static void main(String []args){
        int[] array = {1,2,4,8,9};

        for (int i=0; i<array.length; i++) {
        	if (array[i] == 4) {
        		System.out.println("Index:"+i);
        		break;
        	}
        }
     }
}