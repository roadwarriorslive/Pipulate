===============
pipulate v0.1.8 - Automate Google Sheets for SEO
===============

:Author: `Mike Levin, SEO <http://mikelev.in>`_

There's a reason spreadsheets remain as popular as they do in the face of more
capable databases. Spreadsheets are designed for humans. You don't rely on a
developer to do every little thing. It's a nice place to put daily dashboards,
and you can use spreadsheets in many places where a database would be overkill.
However as anyone who's tried to build durable long-term automations around
spreadsheets using VBA, AppScript or any of the other obvious choices, it ain't
so easy.  That's what I fix here with Pipulate; from OAuth2 to grabbing the
area of the spreadsheet you're going to update to pushing the changes back
up... and **nothing in-between**. For that, there's Pandas.


.. contents::
    :backlinks: none

.. sectnum::


######################################## 
Pipulate Philosophy
########################################

I've worked on a long history of similar projects, building framework after
exhausting framework, maintaining my own custom django-like libraries — and
then I discovered the combination of Google Sheets, Jupyter Notebook and Pandas
that together virtually obsolete all my past work in the most delightful way I
could imagine — Python with Pandas (very mainstream stuff) *is my framework*,
and then all I needed was a way to easily pump data in and out of GSheets with
minimal muss, fuss, and indeed even thought. It goes like this::

    cl, df = gs.pipulate(tab, rows, cols) #Get range from GSheet
    #Do stuff to df in Jupyter Notebook using Pandas (but not to the cl)
    gs.populate(tab, cl, df) #Push altered df back into GSheet

That's it. That's Pipulate. The rest is your imagination.

######################################## 
Installing Pipulate
########################################

Step #1: Install https://www.anaconda.com/download/ start Jupyter Notebook.
Make a new Python 3 notebook and type::

    !pip install pipulate --upgrade

This command executes as an operating system command (because of the
exclamation mark) and not Python code. It may take awhile, but you will
eventually get the output of the pip program vomit out a bunch of messages
about installing this-and-that dependency. Most Pipulate requirements are
already met by Anaconda, but if you're in some other Python environment, you
can install all the rest of the requirements for Pipulate with pip install
pandas (a VERY BIG install).

######################################## 
For the impatient
########################################

The quickest way to pipulate is as follows, but I suggest you read through this
documentation down to where I cover Python functions and how they get called by
the Pandas df.apply() method in order to properly grok the power here::

    import pipulate as gs
    import pandas as pd
    tab = gs.name('Your Sheet Name').sheet1
    cl, df = gs.pipulate(tab, rows=(1, 20), cols=('a', 'b'))
    df['B'] = 'foo'
    gs.populate(tab, cl, df)

****************************************
Things even the impatient must know
****************************************

- You must be on Python >= 3.x.
- You must be using a Google Spreadsheet in online mode.
- You must exactly match 'Your Sheet Name' with your actual sheet name.
- You must be able to recognize row and column indexes when you see them.
- When you import pipulate as gs, Google will (1-time) throw up a giant blue
  link that you must click and login with the same Google account you used to
  make the Google Sheet with.

****************************************
Things about OAuth2 you should eventually know
****************************************

Upon first-run, Pipulate asks you once for access and then not again until
things goes wrong and you have to login again. You should be aware that a file
named ouath.dat is dropped in your working directory (where you Jupyter
Notebook .ipynb files save) which allows full access to your Google stuff.
There is a refresh token there that grants new rapidly-expiring access tokens,
but which itself doesn't expire. It is used to frequently re-log you in
invisibly in the background. If you're interested in seeing these tokens, you
can open oauth.dat in a text editor. It really helps to start to demystify
OAuth2. Occasionally, Google WILL make even the refresh token have to be
recreated with a new Web login, so just be aware of that especially if you
build real automations (non-Jupyter Notebook) around Pipulate.

######################################## 
A tour through Pipulate
########################################

Even if you're new to Python and computer programming, Pipulate is a good place
to start. Run Jupyter Notebook by either looking for an icon named Jupyter
Notebook in your Start Menu after an Anaconda install, or select
Anaconda-Navigator from your Applications folder and Launch Jupyter Notebook
from there. There's a few ways to get Jupyter Notebook running, but so long as
something pops up in your web browser where you can choose New / Notebook:
Python 3, then you found it. After you have a new Notebook, if you haven't done
step #1 already, then execute:

    !pip install pipulate --upgrade

Once pipulate is installed, you don't have to do that again, so after it's done
(it can take awhile), you can delete the command and it's ugly output and get
onto the real action. There are alternative ways to do pip installs in
"Anaconda Prompts" (with more control outside the browser) but details vary on
Macs vs. Windows vs. Linux, so I prefer to tell people how to do pip installs
from within Anaconda. The --upgrade parameter ensures you always have the
latest because I will be updating it often. Step #2, execute:

    import pipulate as gs

This will cause an enormous Google Web login-link to appear in your Jupyter
Notebook that you must click, which will open another tab in your browser
presenting a Google login prompt. Choose which Google account you want to use
to access Sheets. It must have permission to the sheet you're manipulating. It
also asks for various other Google Service permissions while it has the chance,
in case you plan on using Pipulate to track your YouTube view-counts and such,
which you should totally do.

****************************************
Pipulate naming conventions
****************************************

In case you're wondering why I recommend the convention of importing pipulate
as gs, it's because my other Github module GoodSheet got fully wrapped in here,
and I like reminding everyone Pipualte is in fact GoodSheet. I also got very
fond of how gs.pipulate() looks, and I think it helps that gs also stands for
Google Sheet. It also avoids the verbosity of pipulate.pipulate() or
abbreviation-confusion of pi.pipulate() vs. pip.pipulate(), etc. 

For those familiar with the Flask web microframework, it might help to think of
Pipulate as something lightly sprinkled in to connect GSpread and Pandas, and
not really trying to do all that much itself except a few API innovations to
help. The act of pipulating is just picking up an Excel-style rectangular
spreadsheet range as both a GSpread cell_list and a Pandas DataFrame, altering
the df completely with Pandas, and then using the symmetrical act of populating
to push the changes back into Google Sheet.


****************************************
Of Pandas & dependencies
****************************************

Pipulate is designed to let you do all your challenging data-manipulation work
in Pandas. Pandas is not part of Python "core", but then neither is Google
Sheets or GSpread, so don't complain. You're drinking deep of both the Google
and Python Koolaid with Pipulate. You could do a lot worse. Any disenfranchised
SQL-users out there, Python Pandas is where you should be going. Not to put too
fine a point on it, but SQL has let you down. You need a more universal
lightweight "general case" data manipulation tool, and Pandas is it whether you
realize it yet or not. It's not like Oracle's going to buy Python too. So just
go ahead and import Pandas::

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

It's good to switch from using GSheet file-names to their unique "keys" for the
sake of avoiding future confusion about which document you're actually working
on. It's far too easy to have 2 files with the same name. Be sure to use the
long string of characters copied out of a Google Sheet URL for the key. That's
the long string of alphanumeric gobbledygook not broken up by slashes. The
tab_name is always "Sheet1" on a freshly-made sheet. If you rename it or want
to manipulate a different tab, be sure to make it match this. The rows and cols
tuple defines the rectangular region you will want to manipulate.

Okay, let's generate some text to manipulate with Pipulate. Enter and execute::

    import this

...and you will now have 20 nice new lines about the Zen of Python to
copy/paste from Jupyter Notebook to a newly-made Google Sheet you can use for
the below exercise. In other words, create a new Google Sheet and paste the 20
Zen of Python lines into cells A1:A20. You are now ready to pipulate.

****************************************
Connecting to sheet
****************************************

Open the connection to the Google Sheet (as if it were a database) and copy a
rectangular range in both the GSpread cell_list format and as a Pandas
DataFrame. This is setting the stage to pipulate, by creating two identical
shapes, but of different types (one from GSpread and the other from Pandas)::

    sheet = gs.key(key)
    tab = sheet.worksheet(tab_name)
    cl, df = gs.pipulate(tab, rows, cols)

Even though the cl is a cell_list from GSpread, it is also very similar to
Python's core datatype called list. Jupyter Notebook lets you inspect the
contexts of cl or df simply by running them on their own line. Type this and
hit Enter::

    cl

As you can see, GSpread cell_lists are just what one might call a
one-dimensional array in other languages, which is the same as a normal Python
list datatype. However, a few extra attributes have been layered onto each
cell, such as cl[0]._row to see what row a cell belongs to and cl[0]._col for
its column. In this way, GSpread avoids more complex shapes like a list of
lists or a list of tuples, but it does make manipulating it directly as if a
spreadsheet a challenge, which is pretty frustrating because that's the entire
reason you use a library like GSpread.

Have no fear; Pandas to the rescue! It's not the cl we're going to manipulate.
It's the df, which is a Pandas DataFrame and has a lot of powerful
database-like tricks built-in. All we have to do is NOT TOUCH the cl until such
time as we push our changes back to the spreadsheet. You can also inspect the
df with Jupyter Notebook::

    df

****************************************
And now a word about Jupyter Notebook and REPL enviornments
****************************************

You can inspect objects like cl and df this way because you are in a REPL
(read, eval, print, loop) for Python code execution where the contents of a cl
or df is just sort of "hanging around" frozen in memory MID-EXECUTION for your
casual perusal. This is both a small miracle, and makes Jupyter Notebook the
ideal place for for scientists and marketers to "feel their way around" data
before building resilient automations.

I'm also helping you jump on the same bandwagon that's helping scientists solve
the crisis of reproducibility that hit their field a few years back when they
realized that 70% of published scientific research was unreproducible. While
much credit goes to Jupyter Notebook, it's really Anaconda that gets it all
installed and erases that pesky multi-platform issues that usually become very
major stumbling blocks—even for scientists.

****************************************
Your first pipulation
****************************************

Say you wanted to just plug the value "foo" into column B::

    df['B'] = 'foo'

You can now "push" your changed dataframe object back into the still
compatibly-shaped cell_list object, but peek at it first "in memory" by just
typing df all by itself::

    df

Make the changes that you see in memory push back out to the spreasheet. Watch
the browser as you populate to see the changes occur!::

    gs.populate(tab, cl, df)

Congratulations. You've just pipulated.

Plugging data dynamically into Google Sheets is nothing new. Pipulate just
simplifies it. To do something slightly more interesting, you can simply copy
the contents of column A to B::

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
automation. 

****************************************
Appending strings
****************************************

If you wanted to append foo to column A and put the result in column B (like
above, but appending strings to an already already string-type column).::

    df['B'] = df['A'] + 'foo'


****************************************
Alternatives to Pipulate
****************************************

Embedded application languages like Microsoft's VBA or Google's AppScript can
achieve similar results, but if I need to explain to you why these are not as
good as using Python on the back-end, you're in the wrong place. The same goes
for the ever-increasing selection of paid-for Excel and GDocs plug-ins and
other proprietary vendor products which probably don't quite do what you need.

Pipulate is mostly about Python and Pandas. You could replace gs.pipulate() and
gs.populate() with pd.read_csv() and pd.to_csv() and take Google Sheets out of
the equation entirely, or use Excel instead of GSheets by swapping PyExcel for
GSpread. My thinking is that if you have to learn and master one tool for this
sort of data manipulation, it might as well be Python/Pandas.

****************************************
Cheerleading for Anaconda, Jupyter Notebook and Pandas
****************************************

The above example with .astype() also shows that even if you know Python,
there's some new learning to do here for things like casting datatypes, which
is actually different from pure Python. Pandas sits on NumPy which is a popular
C-optimized Python library that provides N-dimensional arrays for the same kind
of work that IBM dinosaurs still do in Fortran for science and stuff. Pandas is
a FRAMEWORK on top of NumPy for such work, but which turns out to be perfectly
designed for what I used to use Pipulate for when it was a Flash-based Web app.

****************************************
Applying a Python function to every row of a Google Sheet
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
Giving Python function entire row of Google Sheet as input
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

****************************************
CAVEAT! Row-aware Pipulate functions grab values from row by index
****************************************

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
appear in column C. This is where it starts getting more complex, and there are
ALWAYS costs to complexity. Mapping has to go somewhere, and I currently choose
to put it INSIDE Pipulate functions, which is not necessarily the best
long-term decision, but complex as it may be, you're going to be able to follow
everything that's going on right there in front of you without maintaining
some awful set of per-project externalized mapping tables... ugh! You'll suffer
through that sort of thing soon enough. For here, for now; MAGIC NUMBERS!

****************************************
FYI: Python execution-context choices
****************************************

Remember that the Python code is running under your control so you are not
limited as you would be using Google's own built-in Apps Script (Google's
answer to VBA) for the same purposes. Your Python code is running on your local
machine (via Jupyter Notebook) and can easily be moved to the cloud or on cheap
hardware like Raspberry Pi's. Truth be told, Jupyter Notebook is optional.

All your data manipulation or "creative work" is taking place in Pandas
DataGrids which you are "painting" onto in memory. Aside from copying the
initial range out of a spreadsheet and then pasting the identically-shaped but
altered rectangular spreadsheet range back in, this entire system is just
becoming adept at Pandas using GSheets instead of CSVs.

****************************************
Giving your function "extra" argument data per row
****************************************

When stepping row-by-row through a Python Pandas DataFrame, it is often
desirable to insert "meta" attributes that can be used in the function WITHOUT
putting those numbers wastefully on every row of the spreadsheet you're
manipulating. Say the data we wanted to add is a date and it was the same date
for every row. It would be a waste to copy the exact same date down an entire
column. Instead, the Pandas API provides for passing in both fixed-position
arguments and labeled arguments by sort of "side-loading" them in as follows::

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

########################################
Working with very large lists
########################################

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

########################################
Hitting the APIs directly
########################################

Pipulate processes lists, and when things go wrong you sometimes want to leave
both Pipulate and Pandas and focus directly on the Python function. When it
comes time to hit an API directly, you put the Python code directly into
Jupyter Notebook so that you can play around with it.

########################################
Did somebody say SEO?
########################################

Coming soon:

- Connecting to your Google Analytics
- Connecting to your Google Search Console
- Capturing search engine result pages (SERPs)
