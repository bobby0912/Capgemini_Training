//Multiple Interface Implementation: Suppose your application requires two interfaces
//(ILogger and IDatabaseSaver) that both have a method named Save(). How would you practically
//handle implementing these conflicting methods in a single class?



using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CSharpAdvancedQuestions
{
    interface ILogger
    {
        void Save();
    }

    public interface IDatabaseSaver
    {
        void Save();
    }
    class Question1: ILogger, IDatabaseSaver
    {
        void ILogger.Save()
        {
            Console.WriteLine("Save method from ILogger");
        }
        void IDatabaseSaver.Save()
        {
            Console.WriteLine("Save method from IDatabaseSaver");
        }
    }

}
