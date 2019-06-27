:Author: `Mike Levin SEO in NYC, Commodore & 360i alum, HitTail creator, J2 Global employee. <http://mikelev.in>`_

Pipulate Free & Open Source SEO Software (Automate GSheets for Dashboards)
##########################################################################

.. image:: https://raw.githubusercontent.com/miklevin/Pipulate/master/pipulate-logo.svg?sanitize=true

- Do you make Spreadsheet Reports using Google Analytics, GSC and other Data?
- Are you using expensive plug-ins or products to keep these Reports Updated?
- Do you feel all this stuff should be FREE if only you could wire it all up?

Then It's Time To Learn a Little Python!
========================================

Pipulate is designed to make playing with data in Jupyter Notebook easy. The
easiest way to install Pipulate from Jupyter is to execute these commands from
within a Notebook::

    import sys
    !{sys.executable} -m pip install --upgrade --no-cache-dir pipulate

If you're not using Anaconda, then you will have to install Pandas first.

The first time you import Pipulate, you will receive a Google OAuth prompt to
allow access to the Google Spreadsheet you want to edit.  Click the big link
and paste the resulting token back into the field shown in Jupyter Notebook or
your command-line. Once this is done, the basic use is::

    import pipulate as gs
    cl, df = gs.pipulate(tab, rows, cols)
    # Do stuff to df
    gs.populate(tab, cl, df)

This loads the rectangular region you defined with the rows and columns into
memory in a way where you can treat it a lot like a tab in Microsoft Excel or
table in SQL. You can manipulate the pandas "DataFrame" (abbreviated as df),
and then push the changes back out to the Google Sheet. For example::

    import pipulate as gs
    sheet = gs.key('119mnC8Day68KexU_yv7J_wfA3p7iZeXa0YEtmg1Igu4')  # your key
    tab = sheet.worksheet('Sheet1')
    cl, df = gs.pipulate(tab, rows=(1, 5), cols=('A', 'C'))
    df['A'] = 'foo'
    df['B'] = 'bar'
    df['C'] = df['A'] + df['B']
    gs.populate(tab, cl, df)  # Watch the sheet update :)

And that's it. All Pipulate does is pull down the rectangular cell-range you
define and plop it into df. What you do with the Pandas DataFrame (df) is up to
you. I'll load the examples directory with ideas, but this is very open-ended,
designed to make automation of traditional tedious tasks in SEO much simpler.
Once you're happy with your script, you can copy/paste it into a .py file and
schedule it with a standard Linux scheduler, which is another part of this
project I'll be expanding considerably (generic task-scheduling under Linux).

Parametrizing Your Arguments
============================

The time has come the Walrus said to talk about automation. While this is not
about Pipulate, after you get something working in Jupyter Notebook what are
you going to do? Well, you're going to put the code in a scheduler somewhere in
a parameterized fashion so you can feed it different sites, Google Analytics
IDs, keywords, filters and whatnot. It's way too much to cover here, but I may
as well show you how to develop with parameterized arguments in Jupyter
Notebook then have those same arguments able to be used on the command-line
when invoked form a Linux Scheduler. You're welcome::

    (py36) MikeL@LunderVand:$ filename.py --kung "foo"
    kung: foo

You can alternatively use::

    (py36) MikeL@LunderVand:$ filename.py -k "foo"
    kung: foo

To support more arguments, just make more of the parser.add_argument() function
calls and access them through the args dictionary. Here's the code in
filename.py in the above commands. When this is run from Jupyter Notebook, the
"foo" value is set in the "if jn:" if-block. It's fairly likely you'll have
code like this at the top of any Pipulate script that starts out in Jupyter
Notebook and is destined for scheduling. Clear? Enjoy!::

    name = 'kung'
    jn = True
    try:
        get_ipython()
    except NameError:
        jn = False
    if jn:
        val = 'foo'
    else:
        import argparse
        parser = argparse.ArgumentParser(description='Parses args when run from console.')
        parser.add_argument('-k','--kung', default='foo', help='', required=False)
        args = vars(parser.parse_args())
        val = args[name]
    print('%s: %s' % (name, val))`

The Shameless Hype
==================

Why is this billed as "SEO software" when all it does is make updating Google
Sheets easy? It's because this is the main missing ingredient in building all
those custom reports necessary to surface actionable data every day. It's also
your easy route into data manipulation with Python/Pandas and the repurposing
of your aging SEO career into something simultaneously more timely and
timeless.

Learning just the right Linux, Python, vim and git (LPvg) will set you on a
good course for the next 10-years and beyond. If you're still scared of the old
text-based command-line interface to computers which is both the past and
future of tech, then stick your hand into the Gom Jabbar of Linux, my other
popular Repo here on Github: Levinux: /github.com/miklevin/levinux and repeat
after me: I must not fear. Fear is the mind-killer. Fear is the little-death
that brings total obliteration. I will face my fear. I will permit it to pass
over me and through me.

.. image:: https://raw.githubusercontent.com/miklevin/Pipulate/master/mike-levin-seo-nyc.png
