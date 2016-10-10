<p align="center"><img src="http://mikelevinseo.com/LogoSVGs/pipulate-logo.svg" width="640px"></p>
<div style="width:100%;text-align:center">
<ul style="width:80%;text-align:left; margin:0 auto;">
<li>Pipulate is a system for scheduled and ad hoc SEO jobs and tasks that runs under Jupyter Notebook.</li>
<li>Jupyter Notebook is an environment for easily distributing, sharing and
running programming <a href="https://github.com/miklevin/Pipulate/blob/master/pipulate.ipynb">code</a>.</li>
<li>This combines the power of your desktop with the best of the generally server-based tools around.</li>
<li>Once you get this working (not too hard), your SEO and Social Media career will never be the same.</li>
<li>Get started by downloading and installing the Python 3.5 version of <a href="https://www.continuum.io/downloads">Anaconda</a> for your desktop OS.</li>
</ul>
</div>

# Free &amp; Open Source SEO Software to teach you Python 3.5

## Who is Mike Levin?

Hello World! I'm Mike Levin, an SEO in New York City. That is, I help people
like you connect website content with your intended audience. Probably what I'm
best known for is creating the enduring <a href="https://www.hittail.com/"
target="_blank">HitTail</a> keyword tool from 2006. My most recent Pipulate
project (this) is me attempting teach you how to do the same, while learning
Python 3.5 and developing <a
href="https://www.continuum.io/anaconda-overview">superpowers.</a> as you go.
My intended audience for this project is SEO and Social Media professionals
(and hopefuls) who want the skills they're developing to survive the in the
long-run of a 5 or 10 year career, while every other tool goes obsolete. Please
read on, but feel free to learn more about me:

- [Subscribe to my YouTube Channel](https://www.youtube.com/mikelevin)
- [Follow me on Twitter](https://twitter.com/miklevin)
- [Connect on LinkedIn](https://www.linkedin.com/in/miklevin)
- [My SEO Daily Work Journal](http://mikelevinseo.com)
- [My WordPress Site](http://mikelev.in/)

## What Is Pipulate?  

This latest rendition of Pipulate runs from within an amazing programming
environment called Jupyter Notebook, which replaces the prior version of
Pipulate (still in this repo's history) that ran on Python 2.7 on a webserver.
The old webserver approach made this tool a bit hard to set up, and didn't
exactly encourage you to go in and start customizing the Python code. But this
version takes advantage of the game-changing tool in data science being taken
up by scientists all over the world to make their research more shareable.
Pipulate is a lightweight framework that runs on Jupyter Notebook, letting you
easily carry out the most common (and often expensive) tasks in the industry,
while preparing you to customize and take it much farther, per your unique
requirements and ideas.

## Jupyter Notebook

The moment I truly groked what Jupyter Notebook was, I re-wrote Pipulate from
scratch, targeting it and Python 3.5, making the code one-tenth of its original
size, making it easier to run, and much more enticing to get you to go in and
customize it to your own purposes -- whether you're already a Python programmer
or not. The funny thing here is that now that Jupyter Notebook exists, Python,
and the whole coding thing is lots more accessible to non-technical folks --
like scientists! Anyone who needs to manipulate a lot of data as part of their
job would do well for themselves to consider jumping onto the Anaconda, Jupyter
Notebook and Python bandwagon. Pipulate will help you jump.

## Next Steps

I encourage you to take a look at the new code, and I'll start posting
links to the YouTube videos here that will introduce you to the new system and
help get you up and running. Until those videos appear, simply go to the
continuum.io website, and download Anaconda for your host operating system:

https://www.continuum.io/downloads

I'm working on the instructions, so check back soon. In the meanwhile, take a
look at the code, and how well Github renders Jupyter Notebook .ipynb files
(and think about what that means):

https://github.com/miklevin/Pipulate/blob/master/pipulate.ipynb

# Important Notes

## To Do

- A strong visual way to turn on/off Pipulate colums (special token like
  @functionname?
- Make sure the Append() behavior adds rows when needed.
- Make sure functions with order sensitivity work.
- Convert data-types more elegantly when json/pyobjstrings are in cells.
- Settle on explicit representation for Empties and Nones.
- Add Timestamps to debug and console output, especially while scheduling.
- Defer generating the proxy list until actual need for proxy occurs.
- Report on which proxies were actually used for what (maybe)
- Add Geolocation to proxy discovery and selection process.

## Important to Get Across

- How virtualenv's work under Anaconda
  - How Jupyter Notebook "kernels" are actually those virtualenv's
  - How bona fide Python virtual machines (VMs) are actually "spun up" from
    those kernels, whenever you make a new Jupyter Notebook file/tab.
  - How each open Python notebook gets its own VM process (server)
  - How closing a tab (without halting) doesn't actually stop it
  - How this gets used to achieve reliable scheduling
  - How this means your "server" will be "Desktop" machine (not headless)
  - How this means you can have multiple, independently running instances of
    Pipulate, each having it's own "tab" (VM)
  - How VMs, even though running separately, can derive from the same
    kernel/virtual environment (not bound to app-folder like virtualenv)
- How the 2 repo systems, pip and conda, co-exist and interplay
  - How even though you have pip, you DON'T use virtualenv, because Anaconda
    has conda built-in.
  - Why conda is a necessary thing for difficult-to-resolve platform dependency
    issues, particularly under Windows (conda does what pip can't)
  - How you have to initiate a "conda" command to set up the venv/vm
  - How even after that, you have to do a pip-install -r requirements.txt
  - How even after that, you may still have to conda install --name MyEnv
    --file condarequirements.txt

## Installation Instructions

I am currently working on the pip freeze requirements.txt file to make
installation much easier, but until then, I'm getting the explicit
(top-of-the-dependency-chain) pip requirements documented here, especially
since I will support the minimal version of Anaconda, called MiniConda, for my
lightweight Linux virtual machine, Levinux. The hardest dependencies are the
OS-provided XML-parsing services (for things like BeautifulSoup4 to do
screen-scraping), which if you're on a Debian-based Linux derivative (Ubuntu,
mostly), you can take care of these dependencies with:

    apt-get install libpq-dev python-dev

### Anaconda

- Install Miniconda3 for your OS: 
    - http://conda.pydata.org/docs/install/quick.html
    - http://conda.pydata.org/miniconda.html

During the install, you will at some point be promoted whether you want to
update the environment variables to make typing the following commands easier
(not having to specify paths). Answer Yes to this question.

    conda create -n py35 python=3.5 jupyter
    source activate py35
    pip install gspread
    pip install httplib2
    pip install google-api-python-client
    pip install bs4
    pip install lxml
    jupyter notebook

### MiniConda3

- Install Miniconda3 for your OS: 
    - http://conda.pydata.org/docs/install/quick.html
    - http://conda.pydata.org/miniconda.html

When you install MiniConda, it gives you a choice of whether to add the path to
the environment variables to the .bashrc, but I'll give the instructions for if
you answer "no" to this question so that you can see where everything goes.

    ~/miniconda3/bin/conda create -n py35 python=3.5 jupyter
    source ~/miniconda3/bin/activate py35
    pip install gspread
    pip install httplib2
    pip install google-api-python-client
    pip install bs4
    pip install lxml
    ~/miniconda3/bin/jupyter notebook

And finally, you'll need a private.py file that you create yourself, because...
well, because everything private that you never want to risk committing to a
git repo goes in there. Currently, the system only expects a few values needed
for performing Google Analytics and Search Console reports from your website.
So, you have to make a file in the repo folder named private.py and contains:

    site = '[http://www.yoursite.com]/'
    gaid = '[your google analytics id]'

## Longer-Term

- Update Levinux to support MiniConda3, Jupyter Notebook & the new Pipulate

