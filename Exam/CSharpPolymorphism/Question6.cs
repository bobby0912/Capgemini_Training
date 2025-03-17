using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CSharpPolymorphism
{
    

    abstract class Shape
    {
        public abstract double CalculateArea();
        public void Display()
        {
            Console.WriteLine("Calculating area of the shape...");
        }
    }

    class Circle : Shape
    {
        private double radius;

        public Circle(double radius)
        {
            this.radius = radius;
        }
        public override double CalculateArea()
        {
            return Math.PI * radius * radius;
        }
    }

    class Rectangle : Shape
    {
        private double length, width;

        public Rectangle(double length, double width)
        {
            this.length = length;
            this.width = width;
        }

        public override double CalculateArea()
        {
            return length * width;
        }
    }

    class Triangle : Shape
    {
        private double baseLength, height;

        public Triangle(double baseLength, double height)
        {
            this.baseLength = baseLength;
            this.height = height;
        }

        public override double CalculateArea()
        {
            return 0.5 * baseLength * height;
        }
    }

    class Question6
    {
        static void Main()
        {
            Shape shape;

            shape = new Circle(5);
            shape.Display();
            Console.WriteLine($"Circle Area: {shape.CalculateArea():F2}");

            shape = new Rectangle(4, 6);
            shape.Display();
            Console.WriteLine($"Rectangle Area: {shape.CalculateArea():F2}");

            shape = new Triangle(3, 7);
            shape.Display();
            Console.WriteLine($"Triangle Area: {shape.CalculateArea():F2}");
        }
    }

}
