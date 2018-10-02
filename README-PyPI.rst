===============
pipulate v0.2.0 - Free and Open Source SEO Software (Automate Google Sheets)
===============

- Do you make reports using Google Analytics, Search Console and other sources?
- Are you using expensive plug-ins or products to keep these reports updated?
- Do you feel all this stuff should be free if you could just wire it up?

Here's the basic API-invocation::

    cl, df = gs.pipulate(tab, rows, cols)
    # Do stuff to df
    gs.populate(tab, cl, df)

This loads the rectangluar region you defined with the rows and columns into
memory in a way where you can treat it a lot like a tab in Microsoft Excel or
like a SQL table. You can manipulate the pandas "DataFrame" (abbreviated as
df), and then push the changes back out to the Google Sheet. For example::

    import pipulate as gs
    sheet = gs.key('119mnC8Day68KexU_yv7J_wfA3p7iZeXa0YEtmg1Igu4')
    tab = sheet.worksheet('Sheet1')
    cl, df = gs.pipulate(tab, rows=(1, 5), cols=('A', 'C'))
    df['A'] = 'foo'
    df['B'] = 'bar'
    df['C'] = df['A'] + df['B']
    gs.populate(tab, cl, df)  # Watch the sheet update :)

Congratulations! You have been infused with datamastering super-powers that
will help you along to your career after SEO. 

If you use Jupyter Notebook (from the Anaconda install), you can execute these
commands line-by-line in your browser and interactively play around with the
data, doing all the things you'd normally do in Excel or SQL like applying
formulas to columns and joining tables (vlookups) and pivots. If written well,
the code from Jupyter Notebook can be copy/pasted over to a standard Linux
scheduling system to keep your reports updated daily, weekly, monthly or even
every minute (Google has very permissive API quotas). No expesinive 3rd-party
products required!
