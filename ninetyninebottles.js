

function ninetyNineBottles(num) {
  let bottles = num - 1;
  while (num > 0) {
    if (bottles === 1) {
      console.log(`${num} bottles of beer on the wall, ${num} bottles of beer. \nTake one down and pass it around, ${bottles} bottle of beer on the wall.`);  
    } else if (num === 1) {
      console.log(`${num} bottle of beer on the wall, ${num} bottle of beer. \nTake one down and pass it around, no more bottles of beer on the wall. \nNo more bottles of beer on the wall, no more bottles of beer. \nGo to the store and buy some more, 99 bottles of beer on the wall.`);
    } else {
      console.log(`${num} bottles of beer on the wall, ${num} bottles of beer. \nTake one down and pass it around, ${bottles} bottles of beer on the wall.`);
    }
  num = num - 1;
  bottles = bottles - 1;
  }
}
  
ninetyNineBottles(99);
  