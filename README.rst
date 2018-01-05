Pipulate
=======================

Have you ever had to manipulate data in a Google Spreadsheet and got tripped up
on how difficult it is to use Google's OAuth2 login, and dealing with complex
APIs? If you have a gmail or corporate GSuite email that you can use, simply::

    import pipulate as gs

This will open your web browser and cause a standard Google Password prompt.
Choose which Google account you want to use and login. It will give you a long
string of characters to copy back into Jupyter Notebook. All data manipulations
are achieved using Python pandas 3rd party library, so as your next command,
import pandas::

    import pandas as pd

Next, you set the arguments standing for the spreadsheet (file) and worksheet
(tab) you want to manipulate, along with the cell range defined as a set of row
and column indexes, using row-numbers and column-letters that display in
spreadsheet user interfaces::

    key = '[Your GSheet key]'
    tab_name = 'Sheet1'
    rows = (2, 10)
    cols = ('a', 'b')

Now that we've set the parameters, we need to open the connection to the Google
Sheet (as if it were a database) and populate a couple of "compatibly shaped"
objects, a GSpread "cell_list" and a Pandas DataFrame object::

    sheet = gs.key(key)
    tab = sheet.worksheet(tab_name)
    cl, df = gs.pipulate(tab, rows, cols)

Now say you wanted to just plug the value "foo" into column B::

    df['B'] = 'foo'

And you can now "push" your changed dataframe object back into the still
compatibly-shaped cell_list object::

    gs.populate(tab, cl, df)

Plugging data dynamically into Google Sheets is nothing new. Pipulate just
clarifies and simplifies the process. To do something slightly more
interesting, you can simply copy the contents of column A to B::

    df['B'] = df['A']

Say there were numbers in column A and you wanted column be to be that number
times 2. Notice I have to convert column A to integers even if they look like
numbers in the spreadsheet, because GSpread converts all numbers to strings::

    gs.populate(tab, cl, df)
    df['B'] = df['A'].astype(int) * 2

Now say you wanted to apply a function to every line of the DataFrame to do
something like retrieve a title tag from a web address, and you had a function
that looked like::

    def status_code(url):
        import requests
        rv = 'failed'
        try:
            rv = requests.get(url).status_code
        except:
            pass
        return rv

Now you can get the status code of every URL in column A with::

    df['B'] = df['A'].apply(status_code)

This is where the "framework" known as Pandas steps in with its own
conventions. Pandas knows to take the function named in the apply method and
for every row of the dataframe, plug the value found in column A into the
function called status_code and plug the resulting value into column B. Look
carefully at what's going on here, because it's about to get a lot more
complicated.

While the above example is powerful, it's not nearly as powerful as feeding TWO
arguments to the function using values from out of each row of the dataframe.
To do that, we simply call the .apply() method of the ENTIRE DATAFRAME and not
just a row:

    df['B'] = df.apply(funcname, axis=1)

There's a few things to note here. First, we HAVE TO include the axis=1
argument or else each COLUMN will be fed to the function by default as it
iterates through the dataframe. When you use the df.apply() method, you can
step through the entire dataframe row-by-row or column-by-column, and we simply
have to include axis=1 to PRESERVE the row-by-row behavior of calling the apply
method directly from a row (when it's implicit). Now, we can select a 3-column
range::

    key = '[Your GSheet key]'
    tab_name = 'Sheet1'
    rows = (1, 4)
    cols = ('a', 'c') # <--Switched "b" to "c"
    sheet = gs.key(key)
    tab = sheet.worksheet(tab_name)
    cl, df = gs.pipulate(tab, rows, cols)

Now we plan on putting a URL in column A and some text that we're going to look
for on the page in column B. Instead of just returning a response code, we will
return how many times the text was found in the retrieved HTML of the page. So,
we will desire to apply this command::

    df['C'] = df.apply(count_times, axis=1)

However now the count_times function has more responsibility than the
status_code function. Specifically, it needs to know to get the URL from column
A and the keyword from column B, so we rewrite status_code as follows::

	def count_times(row):
		import requests
		url = row[0]
		keyword = row[1]
		rv = None
		try:
			ro = requests.get(url)
		except:
			pass
		rv = '--'
		if ro and ro.status_code == 200:
			rv = ro.text.count(keyword)
		return rv

With the above example, you put the URL you want to examine in column A and the
text whose occurrences you want to count on the page in column B. The results
appear in column C. 

Remember that the Python code is running under your control so you are not
limited as you would be using Google's own built-in Apps Script (Google's
answer to Visual Basic for Applications or VBA) for the same purposes. Your
Python code is running on your local machine (often via Jupyter Notebook) or
the cloud or on cheap hardware like Raspberry Pi's. All your data manipulation
or "creative work" is taking place in Pandas DataGrids which you are "painting"
onto in memory. Aside from "copying" the initial range out of a spreadsheet and
then "pasting" the altered range back in, this entire system is just becoming
adept at Pandas using GSheets instead of CSVs.

