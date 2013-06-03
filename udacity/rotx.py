#! /usr/bin/python

def escape_html(s):
   for (i, o) in (("&", "&amp;"),
                  (">", "&gt;"),
                  ("<", "&lt;"),
                  ("\"", "&quot;")):
     s = s.replace(i, o)
   return s


def rotx(phrase, X):
  new_phrase = ""
  for i in range(0,len(phrase)):
    pi = phrase[i] 
 
    if pi.isalpha():
      # Letter: work in lower case for convenience 
      isup = pi.isupper()
      if isup:
        pi = pi.lower() 
      num = (ord(pi) - ord('a')) + X
      if num > 25:
        num = num - 26
      new_pi = chr(num + ord('a'))
      if isup:
        new_phrase += new_pi.upper() 
      else:
        new_phrase += new_pi 
    else:
      # Everything else
      new_phrase += pi

  return escape_html(new_phrase)

