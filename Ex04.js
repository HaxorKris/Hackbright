
/*
* Write methods that increase and decrease the properties of 'cat'
*     e.g.: "feed", "sleep", "pet"
* Write a method that prints out the cat's status in each area
*/

var cat = {
        tiredness: 20,
        hunger: 20,
        loneliness: 3,
        happiness: 15,
        obedience: -5000,
        feed: function() {
            console.log("Om nom nom");
            this.hunger = this.hunger - 5;
        },
        sleep: function() {
            console.log("ZzzZzZzzZzzZz");
            this.tiredness -= 10;
        },
        pet: function() {
            console.log("*purr*");
            this.happiness += 10;
            this.loneliness -= 1;
        }
};

console.log(cat.tiredness);
// ^^ etc.

