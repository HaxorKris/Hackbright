/* Given an array in Javascript, write a function that returns any items 
in the array that are duplicated. The data contained in the array may be 
an integer or a string, or a boolean, but it will not be an array or a 
javascript object. */




function checkMyList(providedList) {
    singles_list = [];  // to store the first instance of anything
    duplicates_list = [];  // to store the second instance of anything
    for (var i=0; i < providedList.length; i++) {
        var objectToSearchFor = providedList[i];

        if (singles_list.indexOf(objectToSearchFor) >= 0) {
            if (duplicates_list.indexOf(objectToSearchFor) === -1) {
                duplicates_list.push(providedList[i]);
            }
        }
        else {
            singles_list.push(providedList[i]);
        }
    }
    return duplicates_list;
}

var votesToGoEatCake = [true, true, true, true];  // should return "true"
var hackbrightStudents = ["katie", "amy", "jenny", "katie", "kelley", "katie", "amy"];
  // should return "katie" and "amy"
var classroomIds = [47, 12, 19, 22, 26, 99, 30, 50, 324, 003, 44, 33, 346, 354, 44, 235, 45, 34, 44, 590, 09, 099, 0, 1, 3, 33, 999, 9];
  // should return "44" and "33"
var randomJunkIFound = ["katie", "true", true, 19, "gargoyles", "!", 2 + 3, "2 + 3", 19, "19", 19 === "19", 6, false, false];
  // should return "19" and "false"

console.log(checkMyList(votesToGoEatCake));

console.log(checkMyList(hackbrightStudents));

console.log(checkMyList(classroomIds));

console.log(checkMyList(randomJunkIFound));


