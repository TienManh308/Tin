public class QuadraticEquation{
    private double a;
    private double b;
    private double c;

    public QuadraticEquation(double a, double b, double c){
        this.a = a;
        this.b = b;
        this.c = c;
    }
    public double getA(){
        return a;
    }
    public double getB(){
        return b;
    }
    public double getC(){
        return c;
    }
    public double delta(){
        return b * b - 4 * a * c;
    }
    public double x1() { //tính nghiệm x1
        return (-b + Math.sqrt(this.delta())) / 2 * a;
    }

    public double x2() { //tính nghiệm x2
        return (-b - Math.sqrt(this.delta())) / 2 * a;
    }
}