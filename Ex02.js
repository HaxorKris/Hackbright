/*
def fibonacci_set(max):
    if max > 1:
        fib_list = [1]
        current_fib = 1
        while current_fib < max:
            fib_list.append(current_fib)
            current_fib = fib_list[-1] + fib_list[-2]
        return fib_list
    else:
        return [1, 1]
## Tell me if a number is even
def even(n):
    return n % 2 == 0

print sum(filter(even,fibonacci_set(4000000)))

*/


function fibonacci_set(max) {
    var firstNumber = 0;
    var secondNumber = 1;
    var sumOfTwo = 0;
    var sumOfEvens = 0;
    var fibonacci_list = [0, 1];

    for (i = 0; (firstNumber + secondNumber) < max; i++) {
        sumOfTwo = firstNumber + secondNumber;
        firstNumber = secondNumber; //
        secondNumber = sumOfTwo;

        fibonacci_list.push(sumOfTwo);
    }
    return fibonacci_list;
}

function new_filter(fibonacci_list) {
    list_of_evens = [];
    for (i = 0; i < fibonacci_list.length; i++) {
        if (fibonacci_list[i] % 2 === 0) {
            list_of_evens.push(fibonacci_list[i]);
        }
    }
    return list_of_evens;
}

function add_evens(list_of_evens) {
    var sumTotal = 0;
    for (i = 0; i < list_of_evens.length; i++) {
        sumTotal += list_of_evens[i];
    }
    return sumTotal;
}

function run_this_stuff(max) {
    fibonacci_list = fibonacci_set(max);
    list_of_evens = new_filter(fibonacci_list);
    sum = add_evens(list_of_evens);
    
    console.log(sum);
}

run_this_stuff(4000000);