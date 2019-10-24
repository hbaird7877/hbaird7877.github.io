
function factorial(integer) {
  let fact = 1;
  if (integer < 0 || integer === null || integer === "" || integer === undefined || Number.isInteger(integer) === false) {
    console.log("Please enter a non-negative integer and try again!");
  } else if (integer === 0 || integer === 1) {
    console.log(fact);
    return fact;
  } else {
    for (let i = 1; i <= integer; i++) {
      fact = fact * i;
    }
  } 
  console.log(fact);
  return fact;
}

factorial(0);
factorial(1);
factorial(4);
factorial(5);
factorial(6);
factorial(7);
factorial(8);