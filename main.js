// let num = 89
// console.log(num.length)
// // let x = prompt("how is it going?")
// // alert (x.length)
// console.log((num/26))
// console.log("")
// myObject = {name:"kdjfskjfh",job : "teacher",}

// Import the readline module for user input
const readline = require("readline");

// Create an interface for input and output
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

// Game constants
const EASY_LEVEL_TURNS = 10;
const HARD_LEVEL_TURNS = 5;

// Helper function to get input as a Promise
function ask(question) {
  return new Promise((resolve) => rl.question(question, resolve));
}

// Function to check guess
function checkGuess(guess, answer) {
  if (guess > answer) {
    console.log("Too high.");
    return false;
  } else if (guess < answer) {
    console.log("Too low.");
    return false;
  } else {
    console.log(`You got it! The answer was ${answer}.`);
    return true;
  }
}

// Main game logic
async function game() {
  console.log(`
 ,----.                                      ,--.  ,--.                  
'  .-./   ,--.,--. ,---.  ,---.  ,---.     ,-'  '-.|  ,---.  ,---.     
|  | .---.|  ||  || .-. :(  .-' (  .-'     '-.  .-'|  .-.  || .-. :    
'  '--'  |'  ''  '\\   --..-'  \`).-'  \`)      |  |  |  | |  |\\   --.    
 \`------'  \`----'  \`----'\`----' \`----'       \`--'  \`--' \`--' \`----'    
                                                                                                                          
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
`);

  // Generate a random number
  const answer = Math.floor(Math.random() * 100) + 1;

  // Choose difficulty
  const difficulty = (await ask("Choose a difficulty. Type 'easy' or 'hard': ")).toLowerCase();
  let attempts = difficulty === "easy" ? EASY_LEVEL_TURNS : HARD_LEVEL_TURNS;

  let correct = false;

  // Game loop
  while (attempts > 0 && !correct) {
    console.log(`\nYou have ${attempts} attempts remaining to guess the number.`);
    const guess = parseInt(await ask("Make a guess: "), 10);

    if (isNaN(guess)) {
      console.log("Please enter a valid number.");
      continue;
    }

    correct = checkGuess(guess, answer);
    if (correct) break;

    attempts--;
    if (attempts === 0) {
      console.log(`You've run out of guesses. The number was ${answer}. You lose!`);
    } else {
      console.log("Guess again.");
    }
  }

  rl.close();
}

// Start the game
game();
