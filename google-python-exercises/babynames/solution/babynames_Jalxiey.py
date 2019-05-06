#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Jalsey Xie 2019.05.06
import sys
import re
import os

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  # LAB(begin solution)
  # The list [year, name_and_rank, name_and_rank, ...] we'll eventually return.
  names = []

  #file operation
  file = open(filename, 'rU')
  text = file.read()
  file.close()

  #find the year of the list
  year = re.search(r'Popularity\sin\s(\d\d\d\d)', text)
  # print(year.group(1))
  #extract data from html file
  rawdata = re.findall(r'<tr align="right"><td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', text)
  #
  # for item in rawdata:
  #     print(item)
  # print(rawdata)
  length = len(rawdata)
  boyname = []
  girlname = []
  allname = []

  #function of customized sorting
  def MyFn(s):
    return s[1]

  #get data of all boy
  for i in range(length):
      boyname.append((rawdata[i][0],rawdata[i][1]))
  sortedboyname = sorted(boyname, key=MyFn)
  #get data of all girl
  for i in range(length):
      girlname.append((rawdata[i][0],rawdata[i][2]))
  sortedgirlname = sorted(girlname, key=MyFn)
  for i in range(length):
      allname.append((rawdata[i][0],rawdata[i][1]))
      allname.append((rawdata[i][0],rawdata[i][2]))
  sortedallname = sorted(allname, key=MyFn)

  #boy list
  list_B = []
  #girl list
  list_G = []


  list_B.append((year.group(1),'Boy Name'))
  list_G.append((year.group(1),'Girl Name'))
  names.append(year.group(1))

  for i in range(length):
      list_B.append(sortedboyname[i][1]+' '+sortedboyname[i][0])
      list_G.append(sortedgirlname[i][1]+' '+sortedgirlname[i][0])
      names.append(sortedallname[i][1]+' '+sortedallname[i][0])

  for item in names:
     print(item)

  # return names
  # LAB(replace solution)
  # return
  # LAB(end solution)


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  # args = sys.argv[1:]
  #
  # if not args:
  #   print 'usage: [--summaryfile] file [file ...]'
  #   sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  # summary = False
  # if args[0] == '--summaryfile':
  #   summary = True
  #   del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary files
  year = input(r'Enter the year from 1990 to 2008 or type "all" to get all the data> ')

  if year != 'all':
      filename = '/Users/jalxiey/Desktop/google-python-exercises/babynames/baby'+year+'.html'
      extract_names(filename)
  else:
      #find all the file end with .html
      path = '/Users/jalxiey/Desktop/google-python-exercises/babynames'
      text_files = [f for f in os.listdir(path) if f.endswith('.html')]

      for i in text_files:
          extract_names('/Users/jalxiey/Desktop/google-python-exercises/babynames/'+i)


if __name__ == '__main__':
  while(1):
      main()
