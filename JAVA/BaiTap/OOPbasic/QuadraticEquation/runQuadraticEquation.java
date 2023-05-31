public class runQuadraticEquation{
    public static void main(String[] args){    
        QuadraticEquation pt = new QuadraticEquation(1, 4, 3);
        double a = pt.getA();
        double b = pt.getB();
        double c = pt.getC();
        double delTa = pt.delta();
        double x1 = pt.x1();
        double x2 = pt.x2();

        System.out.println(x1);
        System.out.println(x2);
    }
}