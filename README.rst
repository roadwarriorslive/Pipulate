Pipulate
=======================

Have you ever had to manipulate data in a Google Spreadsheet and got tripped up
on how difficult it is to use Google's OAuth2 login, and dealing with complex
APIs? If you have a gmail or corporate GSuite email that you can use, simply:

    import pipulate as gs

This will open your web browser and cause a standard Google Password Prompt.
Choose which Google account you want to use and login. It will give you a long
string of characters (token) to copy back to your Python code execution. All
data manipulations are achived using Python pandas 3rd party library, so as
your next command, import pandas:

    import pandas as pd

Next, you set the arguments standing for the spreadsheet (file) and worksheet
(tab) you want to manipulate, along with the cell range defined as a set of row
and column indexes, using row-numbers and column-letters that display in
spreadsheet user interfaces.

    key = '[Your GSheet key]'
    tab_name = 'Sheet1'
    rows = (2, 10)
    cols = ('a', 'b')

Now that we've set the parameters, we need to open the connection to the Google
Sheet (as if it were a database) and populate a couple of "compatibly shaped"
objects, a GSpread "cell_list" and a Pandas DataFrame object.

    sheet = gs.key(key)
    tab = sheet.worksheet(tab_name)
    cl, df = gs.pipulate(tab, rows, cols)

Now say you wanted to just plug the value "foo" into column B.

    df['B'] = 'foo'

And you can now "push" your changed dataframe object back into the still
compatibly-shaped cell_list object:

    gs.populate(tab, cl, df)

To do something slightly more interesting, you can simply copy the contents of
column A to B:

    df['B'] = df['A']

Say there were numbers in column A and you wanted column be to be that number
times 2. Notice I have to convert column A to integers even if they look like
numbers in the spreadsheet, because GSpread converts all numbers to strings.

    df['B'] = df['A'].astype(int) * 2


