/* sum = 0
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        sum += i
print sum */

var sum = 0;

for (var i=0; i < 1000; i++) {
    if (i % 3 === 0 || i % 5 === 0){
        sum += i;
    }
}

console.log(sum);