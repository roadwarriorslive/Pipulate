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
follow along in its evolution. 

What's different? Well, just about everything except for the fact that the core
concept remains doing most of the tedious data gathering, transforming and
reporting work that monopolizes so many hours in an SEO's day.

In other words, Pipulate is all about performing stupid data tricks into Google
Sheets... now with Python pandas! I could write a book on why I don't have to
write my own framework anymore, and how what I'm doing here is just some
super-light touches to release miraculous potential which I'm betting a ton of
us out there suspect and hunger for, but can't yet quite articulate.

Spreadsheets and databases should both be pretty much the same things, because
well, they're both pretty much the same thing. So, where's my SQL in
spreadsheet-land?

With Google Spreadsheets, we've basically got free ad hoc databases that should
serve so many of the purposes we used to use generic Rails CRUD apps for, so
why not? That Google sheet will outlive you (talk about data security).

All the other libraries take care of the important stuff, like handling OAuth
with google-api-python-client (a huge part of the challenge) and GSpread for
adding a nice Excel-ish API to Google Spreadsheets.

All I need to do is provide a convenient bridge between the land of Google
Sheets and the land of pandas. And so, without further ado...




