using System;
using cSharp.Beginner;
using cSharp.Intermediate;
namespace cSharp
{
    class Program
    {
        static void Main(string[] args)
        {   
            VariablesExample ex = new VariablesExample();
            Weapon revolver = new Weapon("Revolver", 2.3f, 6);
            Console.Title ="myCSharpProgram";
            revolver.printWeaponAttr();
            revolver.Shoot();
            revolver.printWeaponAttr();
            revolver.Shoot();
            revolver.Shoot();
            revolver.Shoot();
            revolver.Reload();         
            revolver.printWeaponAttr();

            Console.ReadKey();
        }
    }
}
