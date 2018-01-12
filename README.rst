########################################
Pipulate - Automate Google Sheets
########################################

Have you ever been frustrated trying to automate data-jobs directly in Google
Spreadsheet due to tricky OAuth2 login issues or just dealing with the complex
APIs? If you have a gmail or corporate G Suite email that you can use, simply::

    import pipulate as gs

This will open your web browser and cause a standard Google Password prompt.
Choose which Google account you want to use and login. It will give you a long
string of characters to copy back into Jupyter Notebook. All data manipulations
are achieved using Python pandas 3rd party library, so as your next command,
import pandas::

    import pandas as pd

****************************************
Configuring a job
****************************************

Set the arguments standing for the spreadsheet (file) and worksheet (tab) you
want to manipulate, along with the cell range defined as a set of row and
column indexes, using row-numbers and column-letters that display in
spreadsheet user interfaces::

    key = '[Your GSheet key]'
    tab_name = 'Sheet1'
    rows = (2, 10)
    cols = ('a', 'b')

****************************************
Connecting to sheet
****************************************

Open the connection to the Google Sheet (as if it were a database) and copy a
rectangular range in both the GSpread "cell_list" format and as a Pandas
DataFrame. This is pipulating... setting the stage with 2 similar shapes::

    sheet = gs.key(key)
    tab = sheet.worksheet(tab_name)
    cl, df = gs.pipulate(tab, rows, cols)

Even though the cl is a cell_list from GSpread, it is also very similar to a
simple Python list; only difference is that it has some extra attributes thrown
in to represent spreadsheets (like row and col attributes per cell). The df on
the other hand is a Pandas DataFrame and is very much like a spreadsheet with
rows, columns and all the accompanying built-in spreadsheet-like (and database)
capabilities that the pandas framework provides. That is why we MANIPULATE the
df and then push it back into the location of the otherwise untouched cl... and
then pipulate.

****************************************
Your first pipulation
****************************************

Now say you wanted to just plug the value "foo" into column B::

    df['B'] = 'foo'

And you can now "push" your changed dataframe object back into the still
compatibly-shaped cell_list object. This is the magic moment. Watch the
spreadseet in the borwser as you do this. You will see the values change!::

    gs.populate(tab, cl, df)

Congratulations. You've just pipulated.

Plugging data dynamically into Google Sheets is nothing new. Pipulate just
clarifies and simplifies the process. To do something slightly more
interesting, you can simply copy the contents of column A to B::

    df['B'] = df['A']

Say there were numbers in column A and you wanted column be to be that number
times 2. Notice I have to convert column A to integers even if they look like
numbers in the spreadsheet, because GSpread converts all numbers to strings::

    gs.populate(tab, cl, df)
    df['B'] = df['A'].astype(int) * 2

****************************************
Applying a function
****************************************

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

****************************************
Giving function data from entire row as an argument
****************************************

While the above example is powerful, it's not nearly as powerful as feeding TWO
arguments to the function using values from out of each row of the dataframe.
To do that, we simply call the .apply() method of the ENTIRE DATAFRAME and not
just a row::

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
answer to VBA) for the same purposes. Your Python code is running on your local
machine (often via Jupyter Notebook) or the cloud or on cheap hardware like
Raspberry Pi's. All your data manipulation or "creative work" is taking place
in Pandas DataGrids which you are "painting" onto in memory. Aside from copying
the initial range out of a spreadsheet and then pasting the identically-shaped
but altered rectangular spreadsheet range back in, this entire system is just
becoming adept at Pandas using GSheets instead of CSVs.

****************************************
Giving function "extra" argument data
****************************************

When stepping row-by-row through a Python Pandas DataFrame, it is often
desirable to insert "meta" attributes that can be used in the function WITHOUT
HARD-WIRING MAGIC NUMBERS into the function or putting it in the other obvious
place, which is its own dedicated column in the spreadsheet. Now say this was a
date and it was the same date for every row. It would be a waste to copy the
exact same date down an entire column. Instead, the Pandas API provides for
passing in both fixed-position arguments and labeled arguments by sort of
"side-loading" them in as follows::

    df['C'] = df.apply(funcname, axis=1, args=('X', 'Y'), foo='bar', spam='eggs')

Exactly like we had to tell the function WHICH values from the row we are
interested in INSIDE the named function, we ALSO have to show which position
out of the tuple-like fixed-position arguments to use and which labeled data to
use::

    def funcname(row):
        url = row[0]
        keyword = row[1]
        arg_one = args[0]
        arg_two = args[1]
        label_one = kwargs['foo']
        label_two = kwargs['spam']
        rv = 'default'
        #do stuff here
        return rv

In this way our functions can either per-row input parameters found in the
selected range OR it can use values injected directly into the API-calls to
pandas. Say you had a URL, keyword and you wanted to look up some metric like
number of clicks on that URL for that keyword for a given day::

    df['C'] = df.apply(search_console, axis=1, adate='2018-01-01')

All we have to do is make the function that this Pandas command is invoking to
be AWARE of where to grab the date from::

    def search_console(row):
        url = row[0]
        keyword = row[1]
        adate = kwargs['date']
        # Now we do something to get clicks
        clicks = gsc_clicks(url, keyword, adate)
        return clicks

And there you have it. That's pretty much the basic use of Pipulate for
completely open-ended semi-automated Python Kung Fu in Google Sheets. Let the
crazy ad hoc SEO investigations of your dreams begin. Just add functions ;-)

****************************************
Working with very large lists
****************************************

Google Sheet is not always the best place to process very large lists, but the
alternative is often worse, so the trick is to just decide by what size chunks
you should process at a time. This concept is sometimes called step-by-stride.
To use step-by-stride with Pipulate we take a basic example and simply add a
"stride" variable and edit out the last 2 lines that set and push the values::

    import pandas as pd
    import pipulate as gs
    stride = 100
    key = '[Your GSheet key]'
    tab_name = 'Sheet1'
    rows = (1, 10000)
    cols = ('a', 'b')
    sheet = gs.key(key)
    tab = sheet.worksheet(tab_name)
    cl, df = gs.pipulate(tab, rows, cols)
    #df['B'] = 'foo'
    #gs.populate(tab, cl, df)

****************************************
Step by stride
****************************************

In the above example, we only added a "stride" variable and edited out the last
2 lines that updates the sheet. Say the sheet were 10,000 rows long. Updating A
LOT of data with one of these AJAX-y data-calls is never a good idea. The
bigger the attempted update of a GSheet in one-pass, the more mysterious things
are going on while you wait, and the likelihood of an entire update failing
because of a single row failing goes up. The solution is to travel 10,000 rows
by 100-row strides (or smaller) and we wanted it to take 1000 steps. We replace
the last 2 lines with the following step-by-stride code::

    steps = rows[1] - rows[0] + 1
    for i in range(steps):
        row = i % stride
        if not row:
            r1 = rows[0] + i
            r2 = r1 + stride - 1
            rtup = (r1, r2)
            print('Cells %s to %s:' % rtup)
            cl, df = gs.pipulate(tab, rtup, cols)
            df['B'] = 'foo'
            gs.populate(tab, cl, df)

And that's pretty much it. All together, the code to process 10,000 rows by
100-row long strides directly in Google Sheets for accomplishing almost
anything you can write in a function to replace 'foo' with one of the fancier
pandas API calls described above::

    import pandas as pd
    import pipulate as gs
    stride = 100
    key = '[Your GSheet key]'
    tab_name = 'Sheet1'
    rows = (1, 10000)
    cols = ('a', 'b')
    sheet = gs.key(key)
    tab = sheet.worksheet(tab_name)
    cl, df = gs.pipulate(tab, rows, cols)
    steps = rows[1] - rows[0] + 1
    for i in range(steps):
        row = i % stride
        if not row:
            r1 = rows[0] + i
            r2 = r1 + stride - 1
            rtup = (r1, r2)
            print('Cells %s to %s:' % rtup)
            cl, df = gs.pipulate(tab, rtup, cols)
            df['B'] = 'foo'
            gs.populate(tab, cl, df)

########################################
SQL Data Sources
########################################

It's easiest to pipulate when you only have to apply one quick function to
every line of a list because it takes advantage of the Pandas framework
conventions; how the .apply() method works in particular. HOWEVER, if your
per-row query is a slow and expensive SQL query INSIDE a pipulate function like
this (the WRONG way)::

	def hits(row, **kwargs):
		import psycopg2
		import apis
		url = row[1]
		start = kwargs['start']
		end = kwargs['end']
		a = apis.constr
		atup = tuple(a[x] for x in a.keys())
		user, password, host, port, dbname = atup
		constr = "user='%s' password='%s' host='%s' port='%s' dbname='%s'" % atup
		conn = psycopg2.connect(constr)
		sql = """SELECT
			url,
			sum(hits) as hits
		FROM
			table_name
		WHERE
			url = '%s'
			AND date >= '%s'
			AND date <= '%s'
		GROUP BY
			url
		""" % (url, start, end)
		df = pd.read_sql(sql, con=conn)
		return df['hits'].iloc[0]

****************************************
Connecting to SQL from Pandas
****************************************

We now  want to move the SQL query OUTSIDE the function intended to be called
from .apply(). Instead, you get all the records in one go and plop them onto
your drive as a CSV file and hit THAT later in the function from .apply().
Getting psycopg2 installed is usually easiest through Anaconda's conda repo
system (not covered here). First we connect to SQL::

    a = apis.constr
    atup = tuple(a[x] for x in a.keys())
    user, password, host, port, dbname = atup
    constr = "user='%s' password='%s' host='%s' port='%s' dbname='%s'" % atup
    conn = psycopg2.connect(constr)

****************************************
Building very long SQL WHERE's 
****************************************

Next, we're going to need to build a string fragment for use in the SQL query
that calls out every single URL that we want to get data back on. One of the
worst parts about SQL is "in list" manipulations. The only way to be sure is a
pattern like this::

    WHERE
        url = 'example1'
        OR url = 'example2'
        OR url = 'example3'
        OR url = 'example4'

...and so on for as many URLs as you have to check. They're probably in your
Google sheet already, so let's grab them into a list in a way that creates
almost the exact above pattern (yay, Python!)::

    urls = df['A'].tolist()
    urls = "url = '%s'" % "' OR url = '".join(urls)

Now, we unify the SQL fragment above with the rest of the SQL statement::

	def sql_stmt(urls, start, end):
		return """SELECT
			url,
			sum(hits) as hits
		FROM
			table_name
		WHERE
			%s
			AND date >= '%s'
			AND date <= '%s'
		GROUP BY
			url
		""" % (sql_urls, start, end)

****************************************
Using Pandas CSVs as SQL temp table
****************************************

You can now use the above function to populate a Pandas DataFrame:: 

    df_sql = pd.read_sql(sql_stmt(urls, start='2018-01-01', end='2018-01-31'), con=conn)
    df_sql.to_csv('df_sql.csv') #In case you need it later
    df_sql = pd.read_csv('df_sql.csv', index_col=0) #Optional / already in memory

We will now use this data source that now contains a list of URLs and the
number of hits each got in that time-window to create your own Pipulate data
source (or service).
