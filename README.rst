Pipulate
=======================

This project aims to combine the convenience of interacting with data through
Spreadsheet software with the power of manipulating data through the Python
Pandas package. It does this by alleviating the number one barrier: OAUth2

If you have a gmail or corporate GSuite email that you can use, simply:

    import pipulate as gs

This will give you a long convoluted string to paste into your web browser
address bar that will cause a standard Google Password Prompt. Choose which
Google account you want to use and login. It will give you a long string of
characters (token) to copy back to your Python code execution environment
(often, Jupyter Notebook, I suppose), and you will now have access to Google
Sheets. Create a new Sheet for this purpose, give it a name, and copy the
document identification key from the URL, and use like this:

    key = 'insert your key here'
    sheet = gs.key(key)
    tab = sheet.sheet1

You now actually have a live connection to Sheet1 of that web spreadsheet and
can start manipulating it in any way you would with the GSpread API. If you
fill column A with a bunch of URLs and want the length of their homepages
in column B, you would do the following:

    cl, df = gs.pipulate(tab, 2, 'a', 'b')

This says grab all the data starting from row 2 from column A to column B. This
default guesses the bottom row based on the first empty row. You have now
populated identicaly shaped:

- GSpread cell_list
- Pandas DataFrame

You can do any manipulations you like to put data into column B of the
dataframe, for example just filling it with foo:

    df['B'] = 'foo'

And then you could update it back to the spreadsheet like this:

    gs.populate(tab, cl, df)

What about those homepage length counts? First let's grab requests:

    import requests

Pipulate is designed to move the heavy-lifting of spreadsheet data manipulation
onto your local machine where you can tap the power of Pandas under Python
(often under Jupyter Notebook) to crunch numbers, crawl websites, chat with
APIs, or whatever it needs to do Python-side, and then push the (identically
shaped) results back out to the spreadsheet it grabbed from.

This is different from Google JavaScript-based AppScript that runs on the
Google cloud. Instead, this leverages the old (never depricated?) GData API
that was around before the Google API Console that deals purely with row &
column data (no formatting) similarly to the Excel-centric way (A1:B2) of the
OpenPyXL package. I hope to soon make this work with either GSpread or
OpenPyXL.

----

