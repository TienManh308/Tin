import mypack.Person;

public class danhsach 
{
    public static void main(String[] args) 
    {
        Person a = new Person("tien",10,1.8f);
//        a.age = 10;
//        a.height = 1.5f;
//        a.name = "Tien";
        System.out.println(a.name);
        System.out.println(a.age);
        System.out.println(a.height);
        
        a.eat("rice");
        int age = a.getAge();
        System.out.println(age);
    }
}
