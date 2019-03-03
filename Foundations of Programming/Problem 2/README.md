You can view Google's official challenge here: https://goo.gl/1vdL4z

# The Challenge

Given a non-empty string like "Code" return a string like "CCoCodCode".

More examples:
- stringSplosion("Code") → "CCoCodCode"
- stringSplosion("abc") → "aababc"
- stringSplosion("ab") → "aab"

## Learning Objectives
This is a simple "warm-up" drill for a Java based exercise.

## My Solution
This coding problem was pretty simple.  I simply made two strings: one for the previous letters, and one for my final string.  I simply added my current letter to the previous letters string, and then took that list and added it to my final string.

You can view my solution here: <a href="mySolution.java">My Solution</a>

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
