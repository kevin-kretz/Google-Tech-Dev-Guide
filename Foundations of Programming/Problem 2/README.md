# <a href="https://goo.gl/1vdL4z">The Challenge</a>

Given a non-empty string like "Code" return a string like "CCoCodCode".

More examples:
- stringSplosion("Code") → "CCoCodCode"
- stringSplosion("abc") → "aababc"
- stringSplosion("ab") → "aab"

This is a simple "warm-up" drill for a Java based exercise.

## <a href="mySolution.java">My Solution</a>
```
public String stringSplosion(String str) {
  String prev_chars = "";
  String final_string = "";
  
  for (int i=0; i < str.length(); i++) {
    prev_chars += str.charAt(i);
    final_string += prev_chars;
  }
  
  return final_string;
}
```
This coding problem was pretty simple.  I simply made two strings: one for the previous letters, and one for my final string.  I simply added my current letter to the previous letters string, and then took that list and added it to my final string.

## Optimal Solution
```
public String stringSplosion(String str) {
  String result = "";
  // On each iteration, add the substring of the chars 0..i
  for (int i=0; i<str.length(); i++) {
    result = result + str.substring(0, i+1);
  }
  return result;
}
```
The optimal solution, takes what I did and uses substrings instead of two seperate string.

## Things I learned:
I was reminded of how to iterate over a string using a for loop in Java.
