Line 2 - The Alphabet variable declaration is not necessary outside the caesar_cipher function because we can infact declare it inside the function just after 
the function declaration like the following: ``` const alphabet: string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' ``` notice that I'm using a small letter on the variable 
name so as to encourange camelCase or snake_case identifier naming conversions so that the code will be more redable. You can visit the following link to read 
more on JavaScript/TypeScript conversions: https://www.w3schools.com/js/js_conventions.asp

Line 5 - ``` const caesar_cipher<T> = (string: T, shift: string) => { ``` This line of code will raise a SyntaxError because the 'T' inside the angle brackets and on the
string: argument is not defined, and the shift: argument must be of type number because it takes a number as a parameter. We can fix this by the following code: 
``` const caesar_cipher = (string: string, shift: number) => { ```

Line 13 - The conditional statement ``` if (shift > 26) { ``` will raise an error because before this statement you defined it on the caesar_cipher() function that 
the shift: argument will take a string as a parameter instead of a number and this will cause a SyntaxError.

Line 15 - ``` shift = shift % 26; } ``` Due to the error I have mentioned above we cannot perform arithmetic operations on strings, since you have defined that the shift: argument is going to take a string as its parameter, arithmetic operations will not be possible.

Line 33 - ``` encodedText += alphabet[alphabetIndex + shift - 26]; ``` On this line of code we have another syntaxError because since you defined the shift: argument to be of type
string, another arithmetic operation is being done here by subtracting 26 from shift and this is not possible since already you have difined that the shift: argument on the caesar_cipher()
function is of type string.

Line 51 - ``` print(caesar_cipher('GUR DHVPX OEBJA QBT WHZCRQ BIRE GUR YNML SBK.', 39)); ``` This line of code raises another syntax error because you have used the print() function 
instead of the console.log() function. The print() function is used in Python programming, console.log() is used in JavaScript and TypeScript. Your line of code was supposed to be
like the following: ``` console.log(caesar_cipher('GUR DHVPX OEBJA QBT WHZCRQ BIRE GUR YNML SBK.', 39)); ```


Your implementation of the Caser Cipher using TypeScript is outstanding, Kudos for that!


The final code was supposed to look like the following: 

``` 
// Function: Caesar Cipher
const caesarCipher = (string: string, shift: number) => {
  // Alphabet
  const alphabet: string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';

  // Encoded Text
  let encodedText: string = '';


  if (shift > 26) {
    shift = shift % 26;
  }

  // Iterate Over Data
  let i: number = 0;
  while (i < string.length) {
    // Valid Alphabet Characters
    if (alphabet.indexOf(string[i]) !== -1) {
      // Find Alphabet Index
      const alphabetIndex: number = alphabet.indexOf((string[i]).toUpperCase());

      // Alphabet Index Is In Alphabet Range
      if (alphabet[alphabetIndex + shift]) {
        // Append To String
        encodedText += alphabet[alphabetIndex + shift];
      }
      // Alphabet Index Out Of Range (Adjust Alphabet By 26 Characters)
      else {
        // Append To String
        encodedText += alphabet[alphabetIndex + shift - 26];
      }
    }
    // Special Characters
    else {
      // Append To String
      encodedText += string[i];

    }

    // Increase I
    i++;
  }

  return encodedText;
}; 
//printing the output to terminal to test for correct output
//should print THE QUICK BROWN DOG JUMPED OVER THE LAZY FOX.
console.log(caesar_cipher('GUR DHVPX OEBJA QBT WHZCRQ BIRE GUR YNML SBK.', 39)); ```




