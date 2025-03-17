//5.  5.Explain how Interfaces and Abstract Classes enable Polymorphism. When should you use one over the other?


using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CSharpPolymorphism
{
    interface ICalci
    {
        public abstract int Add(int x, int y);
    }

    abstract class IcalciSub
    {
        public abstract int Subtract(int x, int y);
    }

    class CasioCalci : IcalciSub,ICalci
    {
        public int Add(int x, int y)
        {
            return x + y;
        }

        public override int Subtract(int x, int y)
        {
            return x - y;
        }
    }


    class Question5
    {
        static void Main(string[] args)
        {
            CasioCalci c1 = new CasioCalci();
            Console.WriteLine(c1.Add(1, 2));
            Console.WriteLine(c1.Add(2, 3));
            Console.WriteLine(c1.Add(3, 4));

            Console.WriteLine(c1.Subtract(3, 4));
            Console.WriteLine(c1.Subtract(32, 4));
            Console.WriteLine(c1.Subtract(35, 4));

        }

    }
}
