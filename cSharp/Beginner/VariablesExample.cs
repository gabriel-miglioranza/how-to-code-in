using System;
namespace cSharp.Beginner
{
public class VariablesExample {
    // this variable primitive types exists in C#
    public int aInt = 23;
    public bool aBool = true;
    public float aFloat = 1.22f;
    public double aDouble = 2.2125151561561351561651;
    public string aString = "I'm a String.";
    
    public void DisplayMyVariables(){
        Console.WriteLine("Integer: " + aInt + 
                          "\nFloat " + aFloat +
                          "\nDouble " + aDouble +
                         "\nString: " + aString
                         );
    }
}
}