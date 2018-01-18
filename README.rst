########################################
Pipulate - Automate Google Sheets for SEO & Social Media
########################################

Have you ever tried to programatically manipulate data in Google Spreadsheets
like it was a database only to be frustrated by OAuth2 login issues, API
complexity, or simply not really knowing how to program yet? If like me your
life evolves around changing data in spreadsheets and you simply MUST automate,
then go install https://www.anaconda.com/download/ then start Jupyter Notebook.
Make a new Python 3 notebook, and then type::

    !pip install pipulate

Pipulate facilitates online data-investigations that marketers and others like
doing by simplifying the Python part. You don't even need to clone this Github
repo. Pipulate is just a library you just call at the top of your own arbitrary
new Jupyter Notebook in whatever directory and .ipynb file you happen to be
working in. Your next step in that file is::

    import pipulate as gs

This will cause an enormous link to appear in your Jupyter Notebook that you
must click, which will open another tab in your browser presenting a Google
login prompt. Choose which Google account you want to use to access Sheets. It
must have permission to the sheet you're manipulating. It also asks for various
other Google Service permissions while it has the chance, in case you plan on
using this to track YouTube view-counts and such.

In case you're wondering why I recommend (conventionally) importing pipulate as
gs, it's because Pipulate is actually Goodsheet (my parallel project that
became the new Pipulate) and I like the way gs.pipulate() looks. The old
Goodsheet is now fully wrapped into Pipulate.

****************************************
Of Pandas & Dependencies
****************************************

Pipulate is designed to let you do all your challenging data-manipulation work
in Pandas. Pandas is not part of Python "core", but then neither is Google
Sheets or GSpread, so don't complain. You're drinking deep of both the Google
and Python Koolaid with Pipulate. You could do a lot worse. Any disenfranchised
SQL-ites out there, Python Pandas is where you should be going anyway. Not to
put too fine a point on it, but SQL has let you down (admit it). You need a
more universal "general case" data manipulation API, and Pandas is it whether
you realize it today or tomorrow. It's not like Oracle's going to buy Python
too. So just go ahead and import Pandas::

    import pandas as pd

****************************************
Configuring a job
****************************************

In that same Jupyter Notebook that you imported pipulate and pandas into, you
can now set the values that will allow you to connect to our spreadsheet (file)
and worksheet (tab), along with the cell range defined as a set of row and
column indexes, using row-numbers and column-letters that display in
spreadsheet user interfaces::

    key = '[Your GSheet key]'
    tab_name = 'Sheet1'
    rows = (1, 20)
    cols = ('a', 'b')

Be sure to use the long string of characters copied out of a Google Sheet URL
for the key. That's the long string of alphanumeric gobbledygook not broken up
by slashes. The tab_name is always "Sheet1" on a freshly-made sheet. If you
rename it or want to manipulate a different tab, be sure to make it match this.
The rows and cols tuple defines the rectangular region you will want to
manipulate.

It may happen that you don't have a Google Sheet set up and have NOTHING in
mind for this first experience. Okay, go to a new cell in Jupyter Notebook and
type on its very own line::

    import this

...and you will now have 20 nice new lines about the Zen of Python to
copy/paste from Jupyter Notebook to a newly-made Google Sheet you can use for
the below exercise. In other words, create a new Google Sheet and paste the 20
Zen of Python lines into cells A1:A20. You are now ready to pipulate.

****************************************
Connecting to sheet
****************************************

Open the connection to the Google Sheet (as if it were a database) and copy a
rectangular range in both the GSpread "cell_list" format and as a Pandas
DataFrame. This is setting the stage to pipulate, by creating two identical
shapes, but of different types (one from GSpread and the other from Pandas)::

    sheet = gs.key(key)
    tab = sheet.worksheet(tab_name)
    cl, df = gs.pipulate(tab, rows, cols)

Even though the cl is a cell_list from GSpread, it is also very similar to one
of Python's "core" lists. At this point because Jupyter Notebook lets you
inspect the contexts of cl or df simply by running them on their own line. Type
this and hit Enter::

    cl

GSpread cell_lists are normal flat Python lists with just a few has extra
attributes layered-on, such as cl[0]._row to see what row a cell belongs to and
cl[0]._col for its column. But you don't need to know that because you just
leave cl alone at this point and do all your manipulations in the Pandas
DataFrame (df) which have built-in capabilities that make it the equivalent of
a very powerful spreadsheet and database combined. We now manipulate the df and
then push it back into the location of the otherwise untouched cl. Just to
satisfy curiosity, you can inspect the current state of the df::

    df

****************************************
Jupyter Notebook is a REPL enviornment
****************************************

You can inspect objects like cl and df this way because you are in a REPL
(read, eval, print, loop) code execution environment for Python code execution
where the contents of a cl or df just sort of "hang around" in memory
mid-execution for your casual perusal and interactive massaging. This is as
opposed to invoking the normal Python interpreter from a command-line or
webserver where interaction with the user only occurs where the developer
programmed it to occur. With REPLs like Jupyter Notebook, your interaction with
"still executing" code is... well, a small miracle. Take advantage of it.

****************************************
Your first pipulation
****************************************

Now say you wanted to just plug the value "foo" into column B::

    df['B'] = 'foo'

And you can now "push" your changed dataframe object back into the still
compatibly-shaped cell_list object. This is the magic moment. Feel free to peek
at it first "in memory" by just typing df all by itself again in a Jupyter
Notebook cell. Then type the following command and watch the spreadsheet in the
browser as you do this. You will see the values change!::

    gs.populate(tab, cl, df)

Congratulations. You've just pipulated.

Plugging data dynamically into Google Sheets is nothing new. Pipulate just
clarifies and simplifies the process. To do something slightly more
interesting, you can simply copy the contents of column A to B::

    df['B'] = df['A']
    gs.populate(tab, cl, df)

****************************************
Working with numbers
****************************************

Say there were numbers in column A and you wanted column be to be that number
times 2. Notice I have to convert column A to integers even if they look like
numbers in the spreadsheet, because GSpread converts all numbers to strings::

    df['B'] = df['A'].astype(int) * 2

This example will throw an error if you try it on the Zen of Python data, you
would get ValueError: invalid literal for int() with base 10: 'The Zen of
Python, by Tim Peters'. But you can put numbers in column A and execute this to
see a simple *2 operation and acquaint yourself with how automate-able things
start to become when you replace tedious manual Excel processes with
automation. Yes, there are the proprietary vendor embedded-languages like
Microsoft's VBA (Visual Basic for Applications) or Google's App Script
(GSheet's VBA-equivalent) designed to do similar things.

****************************************
Cheerleading for Anaconda, Jupyter Notebook and Pandas
****************************************

The above example also shows that even if you know Python, there's some new
learning to do here for things like casting datatypes, which is actually
different from pure Python. Pandas sits on NumPy which is a popular C-optimized
Python library that provides N-dimensional arrays for the same kind of work
that IBM dinosaurs still do in Fortran for science and stuff. Pandas is a
FRAMEWORK on top of NumPy for such work, but which turns out to be perfectly
designed for what I used to use Pipulate for when it was a Flash-based Web app. 

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

We now want to move the SQL query OUTSIDE the function intended to be called
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

The 2 lines above convert a Pandas DataFrame into a standard Python list and
then into a fragment of a SQL statement. When people talk about being
expressive AND brief in Python, this is what they mean. Being able to read and
write statements like those above is a pure joy. You can look at the urls value
in Jupyter Notebook to confirm it's good (if a bit wordy) valid SQL that will
slip right into a query. Now, we unify the SQL fragment above with the rest of
the SQL statement using the endlessly beautiful possibilities of the Python
API::

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

You can now use the above function that really only returns the not-executed
multi-line text string which is used to populate a Pandas DataFrame and cache
the results locally just in case you come back during a separate Jupyter
Notebook session, you won't have to re-execute the query (unless you want the
freshet data)::

    df_sql = pd.read_sql(sql_stmt(urls, start='2018-01-01', end='2018-01-31'), con=conn)
    df_sql.to_csv('df_sql.csv') #In case you need it later
    df_sql = pd.read_csv('df_sql.csv', index_col=0) #Optional / already in memory

****************************************
Correlating URLs in Google Sheet and Pandas Dataframe
****************************************

We will now use this data source which now contains the "result" list of URLs
with the accompanying the number of hits each got in that time-window to create
your own Pipulate data source (or service). The GROUP BY in the query and
sum(hits) is aggregating all the hit counters into one entry per URL. The
correlation here is similar to an Excel VLookup. We make a pipualte function
for the DataFrame.apply() method to use THIS local data::

    def hits(row, **kwargs):
        url = row[1]
        df_obj = kwargs['df_obj']
        retval = 'Not found'
        try:
            retval = df_obj.loc[df_obj['url'] == url]
            retval = retval['hits'].iloc[0]
        except:
            pass
        return retval

****************************************
Using local Pandas DataFrame as "external" datasource
****************************************

Now instead of hitting the remote, slow, expensive SQL database every time, we
execute the SQL once at the beginning and can use the local data to pipulate::

    key = '[Your GSheet key]'
    tab_name = 'Sheet1'
    rows = (1, 1000)
    cols = ('a', 'b')
    sheet = gs.key(key)
    tab = sheet.worksheet(tab_name)

    cl, df = gs.pipulate(tab, rows, cols)
    df['B'] = df.apply(hits, axis=1, df_obj=df_sql)
    gs.populate(tab, cl, df)

Or if it's over a huge list or is error-prone and will need rows entirely
skipped because of bad data or whatever, we can step by stride by replacing the
above 3 lines with::

    stride = 10
    steps = rows[1] - rows[0] + 1
    for i in range(steps):
        row = i % stride
        if not row:
            r1 = rows[0] + i
            r2 = r1 + stride - 1
            rtup = (r1, r2)
            print('Cells %s to %s:' % rtup)
            cl, df = gs.pipulate(tab, rtup, cols)
            try:
                df['B'] = df.apply(hits, axis=1, df_obj=df_sql)
                gs.populate(tab, cl, df)
            except:
                pass
