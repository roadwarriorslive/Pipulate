# Hello World

This is another Pipulate reboot, but this time it's to get rid of all the
custom Flask webserver hosting stuff, calling for a shouldn't-be-necessary
server somewhere (even if virtual on your desktop) when you've got the power of
your native desktop there. 

Enter Anaconda.

Install it.

Run Jupyter Notebook, then from a location accessible to Jupyter Notebook:

    git clone https://github.com/miklevin/Pipulate.git

And so, Pipulate 3.0 is born, but because of all those Github stars and
followers, the action occurs here. I'll produce YouTube videos so you can
follow along in its evolution. I'll also probably have to rebase this at some
point to get rid of all the orphaned git cruft here in the invisible .git
folder. Believe me, it's much worse over on Levinux. But gitub cred is cred,
and so... reboot!

What's different in Pipulate 3.0? Well, just about everything except for the
fact that the core concept remains doing most of the tedious data gathering,
transforming and reporting work that monopolizes so many hours in an SEO's day.

It's all Jupyter Notebook based, now with Data Science. Jupyter Notebook, which
gets installed with a whole bunch of goodies, is part of Anaconda. Anaconda is
a free and open source endeavor to get everything you need onto your local
machine so you can tap into the power of your local machine. This takes such
things as virtual boxes and containers and cloud servers and a whole bunch of
other code execution context requirements out of the picture. If you can do
what data scientists all over the world are doing in downloading and installing
Anaconda, then you too can do a whole bunch of stupid SEO tricks.

In other words, Pipulate is all about performing stupid data tricks from data
from any source, but then into Google Sheets. When you're happy with your
stupid trick, you "extract" your Jupyter Notebook-based .ipynb code into a
traditional CPython .py text file, and pop it into a standard Linux/Python
scheduling system, and you're golden.

Webmaster repurposed... into Datamaster. [ebserver becomes Scheduleserver and
the request/response model of webserving becomes the according-to-plan model of
pushing data. But really, it's about the progress from exploratory work (purely
in Jupyter Notebook) to optimizing your work (as you move it to scheduled
CPython scripts) to eventually more Machine Learning processes.

But I get ahead of myself.

I've found the pandas library, in combination with such amazing framework-like
conventional features of .apply() just turns pandas into Pipulate... just add
easy GSheet connectivity. And so I shall!

I could write a book on why I don't have to write my own framework anymore, and
how what I'm doing here is just some super-light touches to release miraculous
potential which I'm betting a ton of us out there suspect and hunger for, but
can't yet quite articulate. From data-pulls to pandas to GSheet... over and
over... and scheduling and tweaking and refining and color-coding and trending
and visualizing until... profit!

## The Itch I'm Scratching

Spreadsheets and databases should both be pretty much the same things, because
well, they're both pretty much the same thing. So, where's my SQL in
spreadsheet-land?

Okay, yeah, tons of proprietary stuff, but I want to do this all sort of
generically in a way that won't tie me into kooky annual license fees or
fragile dependencies. I want to do what's good for my abilities and my nomadic
wandering datamaster career. Pandas? Hmm.

But then, where do I house the data? I don't want to have to pay for, much less
deal with a MySQL database, or even specialized services that are fad-laden
and moving targets over the long-run, fragile either because of the
vulnerability of either my particular instance, or the platform itself. Google
Sheets? Hmm.

With Google Spreadsheets, we've basically got free ad hoc databases that should
serve so many of the purposes we used to use generic Rails CRUD apps for, so
why not? That Google sheet will outlive you (talk about data security). If only
we could generically access and control a Google Sheet with an API. GSheet?
Hmm.

All the other libraries take care of the important stuff, like handling OAuth
with google-api-python-client (a huge part of the challenge) and GSpread for
adding a nice Excel-ish API to Google Spreadsheets.

Sprinkle in a few more libraries like the google-api-python-client to do the
heavy lifting of OAuth authentication and login to Google services, and you
have some ideally granular building blocks of data automation systems... even
for the as-yet-not-coding Python newb, typical of "technical" SEO's looking at
how to reposition themselves in this post-ML world that turns old school SEO
upside down... actually, really, finally as predicted.

Time to step in and illuminate the way for a bunch of other technical SEO's
looking at how to reposition themselves. Please excuse my mustache for not
being waxed. I'm the backroom internal system building guy you may sometimes
read about, but will not ever see on a Whiteboard Friday.

For throwing my hat into the ring of genuine, all I need to do is provide a
convenient, popular and oh-so-intuitively logical bridge between the land of
Google Sheets and the land of pandas. And so, without further ado...




