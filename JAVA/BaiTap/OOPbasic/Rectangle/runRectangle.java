public class runRectangle{
    public static void main(String[] args)
    {
       Rectangle HCN = new Rectangle(10, 5);
       double weight = HCN.getWeight();
       double height = HCN.getHeight();
       System.out.println(weight);
       System.out.println(height);
       double chuVi = HCN.getPerimeter();
       System.out.println(chuVi); 
    }
}