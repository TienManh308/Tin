public class danhSachNew {
    public static void main(String [] args)
{
    Person [] b = new Person[2];
    for (int i = 0; i < b.length; i++)
    {
        b[i] = new Person();
        b[i].name = "tien"+i;
        b[i].age = i+1;
        b[i].height = 1.7f;
    }
    for (int i = 0; i < b.length; i++)
    {
        System.out.println(b[i].name);
        System.out.println(b[i].age);
        System.out.println(b[i].height);
    }
}
}
