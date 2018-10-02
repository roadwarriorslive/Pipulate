===============
pipulate v0.2.0 - Free and Open Source SEO Software (Automate Google Sheets)
===============

:Author: `Mike Levin, HitTail Inventor & SEO in New York City <http://mikelev.in>`_

.. image:: https://raw.githubusercontent.com/miklevin/Pipulate/master/pipulate-logo.svg?sanitize=true

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

If you use Jupyter Notebook (from the Anaconda install), you can execute these
commands line-by-line in your browser and interactively play around with the
data. You can install Pipulate from a Jupyter Notebook with this code::

    import sys
    !{sys.executable} -m pip install pipulate

And that's it. What you do with the Pandas DataFrame (df) is up to you. All
Pipulate does is pull down the rectangualar cell-range you define and plop it
into df. You then can modify the df however you like (refer ro Pandas
examples). So long as you keep the rows x columns shape the same as what you
selected, you can push the altered data back into the GSheet. Once you're happy
with your script, you can copy/paste it into a .py file and schedule it with a
standard Linux scheduler.
