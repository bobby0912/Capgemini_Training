//4.  4.How does Method Overriding work in C#? Demonstrate with Code and Explain the `override`, `virtual`, and `new` Keywords.

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CSharpPolymorphism
{

    class Animal1
    {
        // Virtual method to allow overriding
        public virtual void Speak()
        {
            Console.WriteLine("Animal makes a sound.");
        }

        // Method hidden using 'new' (not overridden)
        public void Show()
        {
            Console.WriteLine("This is an animal.");
        }
    }

    class Dog1 : Animal1
    {
        // Overriding 
        public override void Speak()
        {
            Console.WriteLine("Dog barks.");
        }
    }

    class Cat1 : Animal1
    {
        // Overriding 
        public override void Speak()
        {
            Console.WriteLine("Cat meows.");
        }

        // Hiding the base class Show() method using 'new'
        public new void Show()
        {
            base.Show();
            Console.WriteLine("This is a cat.");
        }
    }

    class Question4
    {
        static void Main()
        {
            Animal1 myAnimal;

            myAnimal = new Dog1();
            myAnimal.Speak();

            myAnimal = new Cat1();
            myAnimal.Speak();

            Cat1 myCat = new Cat1();
            myCat.Show();

            Animal1 animalRef = new Cat1();
            animalRef.Show();
        }
    }
}
