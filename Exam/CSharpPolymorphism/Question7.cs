using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CSharpPolymorphism
{

    class BaseClass
    {
        public void Show()  // Not marked as 'virtual'
        {
            Console.WriteLine("BaseClass Show() method.");
        }
    }

    class DerivedClass : BaseClass
    {
        public new void Show()  // Hides BaseClass Show() method
        {
            Console.WriteLine("DerivedClass Show() method.");
        }
    }
    class Question
    {
        static void Main()
        {
            BaseClass baseObj = new BaseClass();
            baseObj.Show(); // Calls BaseClass method -> Output: "BaseClass Show() method."

            DerivedClass derivedObj = new DerivedClass();
            derivedObj.Show(); // Calls DerivedClass method -> Output: "DerivedClass Show() method."

            BaseClass baseRef = new DerivedClass();
            baseRef.Show(); // Calls BaseClass method -> Output: "BaseClass Show() method."
        }
    }
}
