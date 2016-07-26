All the functions used are pretty easy to understand except for the %9 part 
See that is used for separating the array into 9 different arrays which then makes our job faster and efficent 
###### Why %9 instead of anything else you ask ?
That's because when do number%9 we get sum of all digits and then sum of all digits for that and so on until we get a single digit number 
```python
18123%9 = 6
1+8+1+2+3=15 => 1+5 =6
```
See what I am saying, except for 9 multiples and 0-9 we get 0 which is okay because that's unique
We seperate the array elements into 9 groups because modulo only returns 0-8 that makes them 9 groups 
-------------------------------------------------------------------------------------------------------------------------------
Rest of the code is self explainatory and feel free to email me at python.hithesh@gmail.com
