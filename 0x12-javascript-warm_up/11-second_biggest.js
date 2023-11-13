#!/usr/bin/node
// Write a script that searches the second biggest integer in the list of arguments.
if (!process.argv[2]) {
    console.log(0);
  } else if (!process.argv[3]) {
    console.log(0);
  } else {
    const MyList = process.argv.slice(2);
    const SortedList = MyList.sort(function (a, b) { return a - b; });
    const RevList = SortedList.reverse();
    console.log(RevList[1]);
  }