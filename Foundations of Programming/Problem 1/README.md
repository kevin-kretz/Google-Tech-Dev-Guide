You can view Google's official challenge here: https://goo.gl/wzrCS8

# The Challenge

Given a string S and a set of words D, find the longest word in D that is a subsequence of S.
Word W is a subsequence of S if some number of characters, possibly zero, can be deleted from S to form W, without reordering the remaining characters.
Note: D can appear in any format (list, hash table, prefix tree, etc.
For example, given the input of S = "abppplee" and D = {"able", "ale", "apple", "bale", "kangaroo"} the correct output would be "apple"
- The words "able" and "ale" are both subsequences of S, but they are shorter than "apple".
- The word "bale" is not a subsequence of S because even though S has all the right letters, they are not in the right order.
- The word "kangaroo" is the longest word in D, but it isn't a subsequence of S.

## Learning Objectives
This question gives you the chance to practice with algorithms and data structures. It’s also a good example of why careful analysis for Big-O performance is often worthwhile, as is careful exploration of common and worst-case input conditions.

## My Solution
I copmleted this program by solving this problem with on word in the set and a string on a piece of paper.  I knew I could make a brute force solution for this problem, but I wanted to make something slightly better by replicating how I would solve it in real life, even though this might not be the best solution.  I realized that part of my solution would involve being able to search only a subset of the string, because I have already searched it and I am not allowed to go backwords from the last letter I have found. I replicated this by saving the position of the last found letter, and then searching from the letter after that through the end of the string.

You can view this solution here: <a href="./first_solution.py">My first solution</a>
