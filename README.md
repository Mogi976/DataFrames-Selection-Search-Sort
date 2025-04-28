Questions

Below, the data array refers to the array of monthly adjusted U.S. grocery store retail sales (in millions of USD) called data that is found in this file: grocery.py Download grocery.py.

Create a DataFrame object from data, where the years are the row labels and the monthly data are the columns of the DataFrame object.  Use descriptive names for the columns.  Call this DataFrame object df.
Extract the column of March data and call it march.  Using the loc mechanism:  From march, extract the value for the year 1996 and call it march1996.  From march, extract the value for the range of years 1998-2003, inclusive at both bounds, and call it march_range.
Using the iloc mechanism, extract the same values from march as you did in #2 and compare those values to the ones you extracted in #2.  Print a message to screen that indicates they are the same (hint: you may want to use the NumPy function allclose).
Do the same as #2 and 3 (that is, compare between what is obtained using loc and iloc), except use df as the starting point in all selections and do the comparison for the years described in #3 and the August-October columns.  You do not have to create march.
Do the same as #4 except with the columns April, June, and December.
Select all rows of df where the January values are greater than 45,000 millions of USD.  Save this subset of the data as bigjan.
Select and save all values of bigjan that are greater than 48,000 millions of USD and less than 50,000 millions of USD.
Create a copy of df and sort that so the rows are ordered in descending years.
In the year range 1998-2003, pretend the only valid values are those less than 34,000 millions of USD or greater than or equal to 35,000 millions of USD.  What are the April and June values corresponding to the value in December that is just higher than the lowest value in December, for this period and under these constraints?
