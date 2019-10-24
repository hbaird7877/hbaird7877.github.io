

function romanNumerals(numeral) {
  let romanNumValues = [
    1000, 
    900, 
    500, 
    400, 
    100, 
    90, 
    50, 
    40, 
    10, 
    9, 
    5, 
    4, 
    1];
  let romanLetters = [
    "M", 
    "CM", 
    "D", 
    "CD", 
    "C", 
    "XC", 
    "L", 
    "XL", 
    "X", 
    "IX", 
    "V", 
    "IV", 
    "I"];
  let convert = "";
  for (let array = 0; array < romanNumValues.length; array++) {
    while (romanNumValues[array] <= numeral) {
      convert += romanLetters[array];
      numeral -= romanNumValues[array];
    }
  }
  return convert;
}
romanNumerals(1021); 