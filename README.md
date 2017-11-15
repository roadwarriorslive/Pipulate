# Hello World

This is another Pipulate reboot, but this time it's to get rid of all the
custom Flask webserver hosting stuff, calling for a shouldn't-be-necessary
server somewhere (even if virtual on your desktop) when you've got the power of
your native desktop there. 

## Enter Anaconda

https://www.anaconda.com/download/ Download it. Install it.

Run Jupyter Notebook, then from a location accessible to Jupyter Notebook:

    git clone https://github.com/miklevin/Pipulate.git

## Pipulate 3.0 is a Blank Repo?

And so, Pipulate 3.0 is born, but because of all those Github stars and
followers, the action occurs here. I'll produce YouTube videos so you can
follow along in its evolution. I'll also probably have to rebase this at some
point to get rid of all the orphaned git cruft here in the invisible .git
folder. Believe me, it's much worse over on Levinux. But gitub cred is cred,
and so an in-location... reboot! Apologies to anyone still on the older Flask
webserver system. And so we move forward in an interesting, creative and
totally appropriate new direction:

## What's New? (Mostly Jupyter Notebook)

What's different in Pipulate 3.0? Well, just about everything except for the
fact that the core concept remains doing most of the tedious data gathering,
transforming and reporting work that monopolizes so many hours in an SEO's day.

It's all Jupyter Notebook based (a very good idea). Jupyter Notebook gets
installed with a whole bunch of goodies, is part of Anaconda. Anaconda is a
free and open source endeavor to get everything you need onto your local
machine so you can tap into the power of your local machine. This gives you a
high level of ability to execute Python code on your own local machine easily
through a Web browser, but then also later in more "grown up" (and
automate-able and scaleable) ways. It also makes your code quite portable,
shareable, Github-friendly, etc.

The Jupyter Notebook approach also takes such things as virtual boxes and
containers and cloud servers and a whole bunch of other code execution context
requirements out of the picture (I.e. to run this app, you also have to run
and/or pay-for this server). This problem faced scientists wanting to share
their reproducible findings with each other. Accountability in science; imagine
that! Well, we all benefit. Now, you can take advantage of these same tools in
order to perform a whole bunch of stupid SEO tricks.

In other words, Pipulate is all about performing stupid data tricks using data
from any source, but then pushing the results (and sometimes raw data or temp
tables) into Google Sheets as tabs. When you're happy with your stupid trick,
you "extract" your Jupyter Notebook-based .ipynb code into a traditional
CPython .py text file, and pop it into a standard Linux/Python scheduling
system, and you're golden.

## Webmaster Repurposed... Into Datamaster!

Under this scenario, those still in-love with being a jack-of-all-trades
Webmaster becomes a Datamaster. The Webserver becomes a Dataserver and the
request/response model of webserving becomes the according-to-plan model of
pushing data around programatically; no human to serve until they look at the
finished product on their own good time by pulling up a URL that is the fully
baked report pulled out of the oven... daily, or whatever.

But really, it's about the progress from exploratory work (purely in Jupyter
Notebook) to optimizing your work (as you move it to scheduled CPython scripts)
to eventually more Machine Learning processes.

But I get ahead of myself.

## A Tale of 2 Pandas

After having dealt with one type of Panda for many years (the Google nickname
for some tweaks they did to fight SEO spammers), I've finally discovered and
plunged into (known about it for awhile now) the pandas library, in combination
with such amazing framework-like conventional features of .apply() just turns
pandas into Pipulate... just add easy GSheet connectivity. And so I shall!

I could write a book on why I don't have to write my own framework anymore, and
how what I'm doing here is just some super-light touches to release miraculous
potential which I'm betting a ton of us out there suspect and hunger for, but
can't yet quite articulate. From data-pulls to pandas to GSheet... over and
over... and scheduling and tweaking and refining and color-coding and trending
and visualizing until... profit!

## The Itch I'm Scratching / Questions You May Ask

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

## Just Connecting Dots

Not that I would equate this project to being anywhere as far along or
fundamental as Flask, but like Flask mostly just connected the dots between
Werkzeug and Requests to make a lightweight web framework that calls for you to
provide actually quite a lot on your own, I too I am just trying to lightly
connect the dots between other libraries that are already doing most of the
important stuff, like google-api-python-client to handle OAuth (actually, a
huge part of the challenge) and GSpread for adding a nice Excel-ish API to
Google Spreadsheets.

With just those libraries, you have some ideally granular building blocks of
data automation systems... even for newbs just getting started and unfamiliar
with Python, typical of "technical" SEO's looking at how to reposition
themselves now that Google is finally waking up and some sort of android robot
nearly thinking thingie is taking over for PageRank and the link graph.

## SEO Leadership

The iron is hot. It's time for me to step in and illuminate the way for a bunch
of other technical SEO's looking at how to reposition themselves in this
turbulent industry, where we all live on the fault line, frequently pulling in
and escaping to the safe haven of being social media worker elves or bidding
arbitrators. No thank you, not for me. I'll stay in SEO for awhile now that
pandas has really piqued my interest and morphed into a critical piece of the
next and best coming of Pipulate.

So, please excuse me and bear with me while I retool, and push out some
examples that will be meaningful to you. Also excuse my mustache for not being
waxed. I'm the backroom internal system building guy you may sometimes read
about, but will not ever see on a Whiteboard Friday.

For throwing my hat into the ring of genuine, all I need to do is provide a
convenient, popular and oh-so-intuitively logical bridge between the land of
Google Sheets and the land of pandas. And so, without further ado...




