using System;

namespace cSharp.Intermediate
{
    // this is an example of a class for a game
    public class Weapon
    {
        public string name;
        public float fireRate;
        public int maxAmmo;
        public int ammoCount;

        //this is a class constructor
        public Weapon(string name, float fireRate, int maxAmmo){
            this.name = name;
            this.fireRate = fireRate;
            this.maxAmmo = maxAmmo;
            this.ammoCount = this.maxAmmo; // initialize the object with full rounds
        }

        public void printWeaponAttr(){
            Console.WriteLine("Weapon Name: " + this.name +
                              "\nFire Rate:" + this.fireRate + 
                              "\nMax Ammo: " + this.maxAmmo +
                              "\nCurrent Ammo Count: " + this.ammoCount
            );
        }

        public void Shoot(){
            if (this.ammoCount > 0)
            {
                Console.WriteLine("BANG!");
                this.ammoCount -= 1;
            } else
            {
                Console.WriteLine("Click")
            }
        }

        public void Reload(){
            Console.WriteLine("Reloading...\nReloaded!");
            this.ammoCount = this.maxAmmo;
        }

    } 
}