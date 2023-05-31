public class Rectangle {
    private double weight;
    private double height;

    public Rectangle() {
    }

    public Rectangle(double weight, double height) {
        this.weight = weight;
        this.height = height;
    }

    public double getWeight() {
        return weight;
    }

    public void setWeight(double weight) {
        this.weight = weight;
    }

    public double getHeight() {
        return height;
    }

    public void setHeight(double height) {
        this.height = height;
    }

    public double getArea() { // Diện tích hình chữ nhật
        return this.weight * this.height;
    }

    public double getPerimeter() { //Chu vi hình chữ nhật
        return (this.height + this.weight) * 2;
    }
}