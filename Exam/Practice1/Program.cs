namespace Practice1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //Console.WriteLine("Hello, World!");
            int a = 10;
            try
            {
                int b = a / 0;
                string name = "fniifn";
                name.Substring(0, 10);   
            }
            catch (ArgumentOutOfRangeException e)
            {
                Console.WriteLine("Caught ArgumentOutOfRangeException:");
                Console.WriteLine(e.Message);
            }
            catch (DivideByZeroException e)
            {
                Console.WriteLine("Caught DivideByZeroException:");
                Console.WriteLine(e.Message);
            }
            catch (Exception e)
            {
                Console.WriteLine("Caught Exception:");
                Console.WriteLine(e.Message);
            }
        }
    }
}
