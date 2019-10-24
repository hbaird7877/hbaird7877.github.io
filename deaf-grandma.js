// Import implementation of prompt from library
let prompt = require('prompt');

let gbyes = 0;

function deafGrandma() {
  prompt.start(); // start prompt
  prompt.get('Say_something_to_Grandma', function(err, msg) { // Get input from Grandma's visitor
    if (gbyes < 2) {
      let note = msg.Say_something_to_Grandma; // Save message to a variable
      if (note == "" || note == null || note == undefined) {
        rant = 'WHAT!';
      } else if (/[a-z]/.test(note)) {
        rant = 'SPEAK UP, KID!'; 
      } else if (note == 'GOODBYE!') {
        if (gbyes == 0) {
          rant = 'LEAVING SO SOON?';
          gbyes++;
        } else if (gbyes == 1) {
          rant = 'LATER, SKATER!';
          gbyes++;
        }
      } else if (note === note.toUpperCase()) {
        rant = 'NO, NOT SINCE 1946!';
        }
      }
    console.log(rant);
    if (gbyes < 2) {
      deafGrandma();
    }
  })
}

deafGrandma();
