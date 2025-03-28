//Abstract Class vs Interface (Versioning Scenario): You're developing a library that's
//frequently updated. Would you choose an abstract class or an interface for extending
//functionality without breaking existing implementations ? Justify your choice with practical reasoning and an example.


using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CSharpAdvancedQuestions
{
    class Question2
    {
        // Answer: 
        // I would choose an interface for extending functionality without breaking existing implementations.
        // An interface is a contract that defines the properties and methods that a class must implement.
        // An abstract class is a class that cannot be instantiated and is used to define common behavior for derived classes.
        // If we use an abstract class and add a new method to it, all the classes that derive from it will have to implement the new method.
        // This can break existing implementations if the new method is not implemented in all the derived classes.
        // On the other hand, if we use an interface and add a new method to it, the classes that implement the interface will have to implement the new method.
        // This allows us to extend the functionality without breaking existing implementations.
        // Example:
        // Let's say we have an interface called ILogger that defines a Log method:
        public interface ILogger
        {
            void Log(string message);
        }
        // We have a class that implements the ILogger interface:
        public class ConsoleLogger : ILogger
        {
            public void Log(string message)
            {
                Console.WriteLine(message);
            }
        }
        // Now, we want to add a new method to the ILogger interface:
        //public interface ILogger
        //{
        //    void Log(string message);
        //    void LogError(string message);
        //}
        // If we were using an abstract class instead of an interface, all the classes that derive from the abstract class would have to implement the new LogError method.
        // This could break existing implementations if the new method is not implemented in all the derived classes.
        // By using an interface, we can extend the functionality without breaking existing implementations.
    }
}
