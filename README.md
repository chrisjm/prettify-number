# MCG Health - Data Engineer - Code Challenge

## General Instructions

This is a project intended to give you the opportunity to show off your design, problem solving and testing skills.
Your solution should be as complete and unit tested as possible, we want to see a first simple pass at how you think and how you work.
The problem is intended to take a couple of hours at most to complete.

Code Exercise - Write a number prettifier:

Write tested code (in any OO language, such as C# or Java) that accepts a numeric type and returns a truncated, "prettified" string version.
The prettified version should include one number after the decimal when the truncated number is not an integer.
It should prettify numbers greater than 6 digits and support millions, billions and trillions.

Examples:
   input: 1000000
   output: 1M

   input: 2500000.34
   output: 2.5M

   input: 532
   output: 532

   input: 1123456789
   output: 1.1B

   input: 9487634567534
   output: 9.5T
