/*
Given a non-empty string like "Code" return a string like "CCoCodCode".


stringSplosion("Code") → "CCoCodCode"
stringSplosion("abc") → "aababc"
stringSplosion("ab") → "aab"
*/


public String stringSplosion(String str) {
  String prev_chars = "";
  String final_string = "";
  
  for (int i=0; i < str.length(); i++) {
    prev_chars += str.charAt(i);
    final_string += prev_chars;
  }
  
  return final_string;
}
