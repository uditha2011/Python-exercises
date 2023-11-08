Expects the user to provide two command-line arguments:
  the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and
  the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.
Converts that input to that output, splitting each name into a first name and last name. Assume that each student will have both a first name and last name.

Input: 

name,house
"Abbott, Hannah",Hufflepuff
"Bell, Katie",Gryffindor
"Bones, Susan",Hufflepuff
"Boot, Terry",Ravenclaw
"Brown, Lavender",Gryffindor
"Bulstrode, Millicent",Slytherin
"Chang, Cho",Ravenclaw
"Clearwater, Penelope",Ravenclaw
"Crabbe, Vincent",Slytherin
"Creevey, Colin",Gryffindor

Output:

first,last,house
Hannah,Abbott,Hufflepuff
Katie,Bell,Gryffindor
Susan,Bones,Hufflepuff
Terry,Boot,Ravenclaw
Lavender,Brown,Gryffindor
Millicent,Bulstrode,Slytherin
Cho,Chang,Ravenclaw
Penelope,Clearwater,Ravenclaw
