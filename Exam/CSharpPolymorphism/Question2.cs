//2.  2.What is the difference between Compile-Time (Static) and Run-Time (Dynamic) Polymorphism in C#?
//Provide Code Examples.using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CSharpPolymorphism
{
    class Calculator
    {
        public int Add(int a, int b)
        {
            return a + b;
        }
        public int Add(int a, int b, int c)
        {
            return a + b + c;
        }
        public double Add(double a, double b)
        {
            return a + b;
        }
    }


    class Animal
    {
        public virtual void Speak()
        {
            Console.WriteLine("Animal makes a sound.");
        }
    }

    class Dog : Animal
    {
        public override void Speak()
        {
            Console.WriteLine("Dog barks.");
        }
    }

    class Cat : Animal
    {
        public override void Speak()
        {
            Console.WriteLine("Cat meows.");
        }
    }

    class Question2
    {
        static void Main()
        {
            Calculator math = new Calculator();

            Console.WriteLine(math.Add(5, 10));
            Console.WriteLine(math.Add(5, 10, 20));
            Console.WriteLine(math.Add(2.5, 3.7));




            Animal myAnimal;

            myAnimal = new Dog();
            myAnimal.Speak();

            myAnimal = new Cat();
            myAnimal.Speak();
        }
    }
}
