--------------------------------------------------------------------------------
## Wed Jun 12, 2019
### Two Paths to Career Advance: With & Without Headless Chrome

I have the same aversion to starting my own business as my dad always did.
Ultimate responsibility coming down on your head will kill you. Who needs it?
It's better to be a Samurai-style master carpenter who works for a lord patron,
supporting your endeavors so you can focus on your craft, serve best, and
nurture a reputation that makes you obsolescence-proof in your lifetime. That's
what I'm doing, and that's what I endeavor to do every day.

To do this every day, we must first begin by structuring our day. This does not
come by easy or ever flow automatically by habit. Sure, sitting down at the
right place and taking out the right tools may come by habit, but every day is
different and we are navigating a way through life which always takes special
thought and consideration above and beyond that which you can do automatically
by muscle-memory, dropping into some sort of fugue state.

So, psyche yourself up! What are the goals out there large and small that you
are pursuing? Why is your actual very life going to be better after today? What
have you done that you had not been able to do (or even identify the need to
do) yesterday? 

There's a notion of perfection in the pursuit of things in life that is the
ideal but unachievable. Truth is that life is statistical in nature and you
zero in on goodness by laying it down in small layers that fit into the day. We
lose our state each night from sleep, so regaining this state is of the utmost
importance, if even just to lay down one more small layer.

Okay, I fixed the problem in hyper.is with the clear command not working. That
was subconsciously keeping me from starting screen-casting again, but now with
Camtasia. I just upgraded Camtasia to version 2019.0.2. Ugh! Keystrokes and my
conversation with their tech group. Let me quickly research software to show
all my keystrokes onscreen.

I'm facing a sort of existential crisis of career that I've got to come to
grips with, and overcome. I'm about to reboot my experience. This is a good
thing. This is always a good thing situation allowing because you don't lose
what you've got, and you get to accumulate-up and incorporate-in a bit more of
new important stuff. Things change in tech and you've got to change with it.

I'm facing a rabbit hole. Some rabbit holes, you do run down and you're better
off for it. Other rabbit holes you run down and don't ever come up from. Still
others trap you for quite awhile or get you complexly entangled with your
personal psyche and don't let go easily. Something inside's telling you that
you're onto something, evidence and guts supports it, and if you just push a
little bit harder you'll get the uncommon reward; uncommon by virtue of the
exact fact that most people give-up right before this point. It's where the
satisfyingly still-undiscovered or not-yet-appreciated vibrating-edge of
important new stuff exists.

The question in such time comes down to continue-to-invest or cut-your-losses?
And if continue, why not back up and pivot a little then re-tackle the problem
fresh and new? Why not psychologically reboot your thought-process by
documenting out the step-by-step baby-steps fresh and anew? This is your career
you're talking about and it's just so critical to get these butterfly-effect
moments correct. Things that are easy to do now are going to be much more
difficult later if you're too far down the wrong path.

So, choose a path wisely. Know you're picking it for solid and perhaps
future-proofing reasons. It makes me nervous investing too much into Chrome
automation and all the potential JavaScript new-learnings and overhead that
comes with that, when I could just say go with the Selenium API and stick with
Firefox or the Webdriver. But that'd be ridiculous now that Google's announced
that even Googlebot will be using the latest headless version of the Chromium
browser for all site-rendering. Does that mean for all crawling entirely?
Maybe.

You can't tell the future and it's always good thinking to believe that the
simpler subsystems continue to run as a sort of a safety-net against the
astoundingly more complex new operations. To fully render a web-page as if a
human web-surfer with a browser takes, I would guess, thousands of times more
computing resources than just reading and parsing the text found in the
view-source of the HTML code emitted at that URL. 

So in other words, the work involved in crawling the web went from being an
almost text-only game into being a complex and sometimes animated document
object model (DOM) with the execution of JavaScript code and probably lots of
subsequent little html-calls to other resources to build the page. That's a lot
of processing power dedicated to documenting every page of the Web by Google.

In order to standardize and make well-understood the entire process, Google has
made Chromium (the FOSS version of Chrome) able to run headlessly and be
automated so we can do many of the same sorts of things Google does with
Googlebot. We'll know we're on the same friggin' code as them and no longer be
limited to only crawling things in view-source. We also get thumbnail images
and a bunch of other goodies.

My career really is that of an SEO. But instead of chasing tweets and
conferences and articles, I'll chase the data. All that cool old stuff that
used to be the single-handed love of the Webmaster, I'm banking on becoming the
single-handed love of the Datamaster. I'm pretty darn sure and pumped about it
because Python Pandas. Wow, is this a thing. As is all the investigation and
automation surrounding it. 

Things don't automate easily, and to be the sort who knows all the things that
go into it, do all the exploration to make sure what you're attempting is even
feasible, to do the initial build, to run that code on-demand, to run that code
on a scheduled basis, and then to make sure it all continues has great value.
You can replace an entire department in a single person, with fairly reasonable
results. It's an excellent application of the 80/20-rule: getting 80% of the
benefit from the first 20% of the effort.

But it is in this exact 80/20-rule thinking that I want to back away from
Chrome automation through Puppeteer because... well, because tech-yuck! I have
to get a whole bunch of stuff installed in a whole bunch of places and get all
the scripts I run portable between these places... only then to have to futz
around with JavaScript, even if only the smallest and most appropriately
domain-specific location, that I could make it. 

I'm writing small JavaScript programs that only do single tasks well. In this
way, I don't have to deal with very much JavaScript, except insofar as
necessary to grab a piece of data out of the DOM according to some rule
expressed as an xpath, json, regex or some other method. JavaScript is a tool.
I am allowed to use tools other than my nearly religiously adored favorites
like Python. 

In fact, I make this concession to the use of a very un-favorite tool
(JavaScript) so that I may practice the API of another favorite (but slightly
less-favorite than Python) tool, Linux. My entire stack-or-whatever is Linux,
Python, vim and git. I do not exclude the use of other wacky and useful tools
like nodejs/JavaScript because there's some parts I don't want to have to learn
much about cranking around in there. I'll learn a little about it; just enough
for small screenshot or scraping functions. 

The key to that is the Unix/Linux type-in text interface. When I say that the
four key things to learn are Linux, Python, vim and git, what I'm really saying
in regard to Linux is that you need a Unix-like operating environment in which
you can run (or optionally schedule) commands that essentially are read out of
a text file like a series of commands being typed in a command-line terminal.
Such syntax usually goes:

    path/filename arguments

This is so small but brilliant in *nix. The first item is taken to be some sort
of command by which control of the system is handed over, really taking over
from the operating system. It is expected to be a binary executable piece of
code targeting that particular host-machine's hardware/processor. In
DOS/Windows terms, that would be a .exe file (for executable). In Unix/Linix
land, these files lack file-extentions but have an executable bit set in its
file's description bits. The part that follows the name of the command are the
arguments. 

We say arguments instead of parameters because parameters indicates the values
that go into the arguments. You want to think of taking something that would
normally run one particular way and make arguments to make it run some other
way. There are a lot of options on how to handle command arguments. They could
be positional or keyword arguments using switches or not. Unix/Linux has a few
conventions, key thing being that everything that comes AFTER the executable in
the command are fed to the command itself. And by this simple trick, all your
language are belong to us.

This is where Linux/Unix has really become the "plumbing" of tech. Because when
a system boots-up the operating system has control first. No matter how your
program application is run, there's a hand-off that occurs from the operating
system that was installed on the hardware. Of course with cloud hardware, a lot
of this is obfuscated and abstrated away, but you would be doing yourself a
major disservice ignoring how you can take command of a machine right away on
boot. 

That's the Linux part. You'll not always have a place to run your code but also
a way to make sure it starts on start-up and on any subsequent time-interval or
conditions, and how your program can be "invoked" differently based on the
arguments on the command-line. This was true in the 1970s when Unix was
invented, and it'll likely be true in the 2070s. It doesn't care WHAT the
command is, so long as it runs and gets access to the arguments it's being fed.
Sprinkle in an explanation of scripts, pipes and return values, you've got a
mostly technology agnostic system for gluing systems together and passing data
around between systems whose basic trick and value is assured to last not only
for a career, but for several lifetimes. How rare is that in tech?

So that forward-slash in paths is a little pesky. You'd think it'd be
universal, right? Wrong! This is one of the many things that Microsoft in ages
long ago screwed up and made so much fatiguing overhead for so many of us
forever forward by using backslashes. This is why the Linux/Unix knowledge
isn't universal. Windows is still very proprietary in how it does many of its
things, but it is goign to ship a full Linux kernel in Windows 10 soon. This
means that the Windows Subsystem for Linux (WSL 2) will come standard with
Winodws and perhaps even the Linux-version of Anaconda could be installed,
avoiding the path inconsistency problems that Windows introduces. Until that
ideallic day, we must deal with path-conversion. It always helps to keep
everythning relative to the current working directory on program-launch, which
is usually the directory the program is in when it starts unless otherwise
somehow specified. By keeping paths relative, they convert between
forward-slashes and back-slashes most easily. You don't want the part of the
path going up to the hard drive on Windows like C:\Program Files. Ugh!

Ugh, okay so all this is to say that when you venture into another language
like JavaScript, one of the most useful things you can do is to figure out how
to run your programs from the command-line using arguments, and it's suddenly a
magical new candidate tool for you to incorporate into your Datamastering.
Because so long as you can get everything installed correctly to run that
command correctly, who cares what language is being executed. In fact it
expands your capabilties a thousand-fold by just being able to wrap any old
thing into your Datamaster ecosystem.

Okay, so what next? 1, 2, 3... 1? Go Right! Hmmm. I've had a number of reports
I'm in the process of retiring. First comment them out of pipulate-left.
They're left there because we want to leave those older reports and technqiues
behind us. We want to move things into pipulate-right. That was my first
thought, moving the one thing I still want to keep running over there, but I
think it's best to comment all the other stuff out first. Go one step at a
time. Deactive portions of the old report but don't do the additional risk of
changing the good (right) script. Okay, check! Next?

Okay, Iv'e gone crazy of late dealing with the multiplatform headless Chrome
(Chromium) issues. There was the fact that Chromium couldn't be called directly
to reliably create screenshots across platforms. This is common for argument
support to vary across platforms especially in a constantly moving codebase.
I've seen it before in QEMU. It's always best to stay close to the well-beaten
path, and there's no chance that any of the releases of Chromium won't work
with the newly created JavaScript API which is greatly simplified by using the
Puppeteer client library provided by Google that runs on nodejs. And so to keep
things simple we need to invoke headless chrome through JavaScript files
written for execution by nodejs that communicates to the local install of
Chromium through its JavaScript API. Pshwew! It gets even more complex with the
above-mentioned path problems if you're on that most alluring of platforms,
Jupyter Notebook, for development work. I have to just leave one project active
using this tech and let it gradually sink-in over time.

So I'm going to start on a pair of parallel tracks, implementing the same app 2
different ways; one with a headless Chrome browser and the other with
traditional html/json scraping/api-work that requires little more than the
standared Python library, but for which I use the Requests pagage just to
simplify http calls. 1, 2, 3... 1?

First record these 2 URLs:
- https://www.seroundtable.com/google-pagespeed-insights-aggregated-speed-data-origin-25935.html
- https://twitter.com/VeryDanNutter/status/1009365962997542913

Okay, my attention is no longer on paths. I can reduce my focus on the
portapath repo. Don't forget it. You will soon be revisiting what you learned
there. But for now, a new nickname? A brand new speeddash folder. Make it
speeddash. I can evetually retire the speedtest folder. But build up this app
"from scratch" such as it were, knowing it's never really from scratch anymore
with pipulate.

Okay, this is where I have to wrap up for today. I'm at a fairly good point to
hit hard tomorrow.

## Mon May  6, 2019
### 1, 2, 3... 1? Go Right! Bootstrapping Daily Productivity

There is a consistent, even, familiar rhythm to getting started with work. If
you're not feeling that rhythm, you're not getting started with work. Work is a
funny thing. Work leads to reward, like living life for one more day. Or at
least, that's what getting to work once meant to human beings when we were in a
more nomadic tribal state, following the seasonal migration herds of vegetable
grazing animals. No longer. Our basic needs are met by society, at least if you
can keep your act together enough to explain your situation to somebody who'll
care. And if you have enough fuel and brilliance in that internal engine of
yours to keep you going, you'll claw your way up and out and prevail.

I have to be mentally all-in today on the work at-hand. Shit, okay, take your
own advice and focus! 1, 2, 3... 1? Go Right! The repeating rhythm of life.
That means go one screen to the right which will contain Chrome, go to Tab-1 by
hitting Ctrl+1, go to the top of the page and hit Esc, 0, 0, Enter, drop your
cursor in block-one and hit Shift+Enter. Pshwew! A story is starting to be
told. It is the story of regaining-state of the last time you were here doing
the work in the forefront (in center stage, in the spotlight, in focus, etc.)
and as the subject of you being in The Zone. You're going to release the last
version of yourself you had just been using to get here, this far.

Maybe start some music now. Maybe try achieving that blissful elusive silence,
or maybe crickets, running water, background noise or whatever. You have to go
through a transition that's easy for some folks and hard as heck for others.
It's like telling someone to think about something else other than some
ridiculous thing that's impossible to get out of your mind. Absurd combinations
of animals and colors come to mind like blue monkeys or pink elephants. Better
yet, blue monkeys riding pink elephants. Don't think about them! Okay, some
say. It's a snap and they've somehow got that mode-switch-trick down or they're
lying. 

You've got to win over your body with hardware-tricks that your conscious mind
will write off as ridiculous or not having a chance against it, like deep
breathing, and then activating some deep animal trigger, like the alpha brain
state your mind wanders into shortly before falling asleep, where you're very
relaxed and thinking about nothing. Call this state meditating, hypnosis,
zoning-out or eggbert, for all I care. It's a documented thing. The front part
of your brain that hosts all that human thinking stuff you're doing right now
gives it a rest, kicks off it's shoes, hops into a happy place and gently
discorporates. Taking 10 deep, slow, deliberate breaths is always a good place
to start with these hardware tricks.

Okay, there's lots of distractions including your own mind. 1, 2, 3... 1? Go
Right! Keep getting yourself back on-track. Upgraded Hyper.is to version 3...
ugh! One more distraction because I HAD to fix the config file (to point to
bash.exe) to continue to be productive. Okay, done. I can not emphasize enough
how much the combo of Window's Linux bash.exe under Hyper.is makes a Windows
system usable for a Unix/Linux-minded person.

--------------------------------------------------------------------------------
## Thu Apr 18, 2019
### Chrome Screenshots with NodeJS

Okay, think through next steps. Publish yesterday's entry. Okay, done. Check in
Github... Yep, that entry from yesterday about incorporating nodejs into my
daily workflow got pushed out into the Pipulate repo. This is the least way I
could do personal publishing now for the sake of forcing myself to move forward
faster using the principles of commitment and consistency.

Anyway, I've learned that I can invoke node commands from within Python so I
can put files like screenshot.js into the same folder with some script.py and
call it from within Python like this:

    NODE_LOCATION = "/usr/bin/node"
    file_name = "screenshot.png"
    url = "https://www.amazon.com/"
    cmd = r'%s screenshot.js %s %s' % (NODE_LOCATION, file_name, url)
    subprocess.getoutput(cmd)

The home folder need only have the screenshot.js file sitting there. I guess
you could break it out into a separate repo, but then things get more fragile.
Stuff breaks less when everything works out of the same folder. The
screenshot.js file that I developed yesterday is this:

	console.log('Starting');
	const puppeteer = require('puppeteer');
	const filename = process.argv[2];
	const url = process.argv[3];
	(async () => {
	  const browser = await puppeteer.launch({headless: true,
		executablePath: '/usr/bin/chromium-browser',
		args: ['--no-sandbox', '--disable-setuid-sandbox']});
	  const page = await browser.newPage();
	  page.setViewport({ width: 1080, height: 2500 });
	  await page.goto(url);
	  await page.screenshot({path: filename});
	  await browser.close();
	})();
	console.log('Done');

You can actually use screenshot.js from the Linux terminal to take screenshots
with commands like:

    node screenshot.js amazon.png https://www.amazon.com/

...and a file named "amazon.png" would be deposited into the current folder
after Chrome is headlessly invoked. Technically, it's Chromium and not Chrome
but it doesn't seem to make any difference. We talk about headless Chrome and
not Chromium, but Chromium is the truly free and open source version of Chrome.
Also, the above code has headless: true, but it works just as well set to false
and actually watching Chromium pop up for a moment. I have this working
correctly under Python in Jupyter Notebook, under the Ubuntu Bash Shell in the
Windows Subsystem for Linux (WSL) and of course on a generic Linux cloud
server, where it really is only ever running headlessly. 

The important thing here is that I CAN run it non-headlessly for development
and debugging purposes, now in BOTH Jupyter Notebook and the WSL Bash Shell.
That later part was not an easy thing. I still have to document the magic
cocktail mix and incantations that got it working. I believe it was:

1. sudo apt-get install ubuntu-desktop
2. sudo apt install nodejs npm
3. npm i puppeteer
4. apt-get installing a bunch of other dependency stuff I'll document later
5. Exporting some environment variables and putting them in .bash_profile
6. Installing a Windows XServer and making sure it's running correctly

So I basically have this done twice; once for WSL and once for the Anaconda
environment under which Jupyter Notebook runs. So I have nodejs installed twice
on the same system, once for each execution environment. The one on the cloud
server makes 3 separate Python/Node/Chrome execution environments.

--------------------------------------------------------------------------------
## Wed Apr 17, 2019
### Invoking NodeJS from Command-line With Arguments

Okay, my "static-locations" workflow is evolving again right now. It's time
that I start pushing out these daily journal entries into the Pipulte repo.
It's the least I can do with getting back on-track with being a semi-public
persona, sharing the details of what I'm doing with my day-to-day work. I'll
write this journal entry with this in mind. Just as a quick recap for those
just following along now, I keep a single "forever" text-file as a personal
journal in a private Github repo. So why are you reading this here in the
Pipulate repo? Because whenever I load my journal, I'm actually loading TWO
files, one from each repo. In fact this is the macro I use to do it:

	if [ -f /mnt/c/Users/mikle/github/journal/.journal.md.swp ]; then
		rm /mnt/c/Users/mikle/github/journal/.journal.md.swp
	fi
	vim /mnt/c/Users/mikle/github/journal/journal.md /mnt/c/Users/mikle/github/pipdev/theleakyjournal.md

That vim command means I'm loading two documents at once into vim, one in each
buffer. For almost the entire time, I'm in the first buffer which is my main
daily journal. Weeks or months usually go by with me working just that way.
Sometimes I don't even make the private journal entries at all. But when I need
to think things through out loud, it's there. And I usually do better when I
use the journal. The journal is most useful at times like now when I'm going
through tricky career repositioning. When it's time to push out that day's
journal entry, I just use my vim-macro @p (for "publish") which is in my
~/.vimrc file:

	let @p = '?--------------------------------------------------------------------------------^Mjji### Published^M^[:w^MkkkVj/--------------------------------------------------------------------------------^Mky:bn^Mggpjjddo^M^[ki### ^[kdd$a'

Okay, that's going to scroll-right pretty far. But I'll see how the Github
markdown rendering handles it. These little shortcuts like the "j" command to
launch vim with the 2 journal buffers goes into /usr/local/sbin while the
shortcuts from within vim go into /home/[username]/.vimrc. That "home" location
which has your username in it has the shortcut ~/ making this location also
known as ~/.vimrc. All these special paths and locations are from the Unix and
Linux worlds and are very, very, very standard. As strange as some of the stuff
I'm talking about may seem, I'm actually trying to stay as mainstream standard
as possible for the sake of code stability, longevity, and portability.

I work out of a number of different directories (a.k.a. folders) and on
different files. One of my sbin commands is "g" which uses the git command to
back-up and push all the latest changes up to Github. From inside vim what I
can do (after a save) is temporarily dropping out of vim into a vim-provided
command-line with the :sh command and then just typing "g" and waiting for the
script to finish, and then just typing "exit" to go back into vim. Gonna do it
now... okay, done. 

When I add new workflow control shortcut files and such to these directories, I
see git show red-text indicating they're not yet git-tracked files. This
workflow allows me to always make sure I have a "core" set of main files that
are always backed up in Github. When I make changes like adding new files to my
workflow, such deviation is regularly brought to my attention when I use my "g"
shortcut. 

All I really do for all this customization is edit a few script-files that are
written in the most standard of all ways in computer-dom, Unix shell scripts.
More precisely, I'm using the "bash" flavor of this scripting language which
has slightly more logic-flow control (if/than statements and such) than
standard Unix shell scripts which is okay because the Bash dialect of Unix
shell scripts is the most universally popular. It is for example what Microsoft
has built into their Windows subsystem for Linux (WSL).

Okay, I could talk this way in my journal all day and waste the day on
exposition and reminding myself how and why I do the things I do, but it's time
to get to today's business: Chrome automation under the Windows Subsystem for
Linux (WSL) WITH a graphics sub-system active so that I can run Chrome NOT
headlessly. In other words, I launch scripts from a WSL Bash terminal (courtesy
of Microsoft) and the Chromium browser actually pops up and shows you what's
going on. This provides a great opportunity for debugging and adjusting timing
in the Chrome automations; something that is very difficult to do headlessly.

The background here is that Google has recently added the ability to control
Chrome with external scripts and released a client library called Puppeteer to
make it easier, but this is in conflict with my recently blossomed love for
Python under Jupyter Notebook (in a web browser). Puppeteer JavaScript code is
I actually figured out how to use the Python Pyppeteer wrapper-library to use
Puppeteer through Python through Jupyter Notebook and did my first few
scheduled automations by moving the script from Jupyter Notebook into a
standard python text-file and over to a Linux cloud server running Chrome
headlessly (as indented). 

This Jupyter Notebook/Python-wrapper approach to executing node code has worked
for me so far for the first few Chrome automations. The Puppeteer-installed
Chromium does indeed momentarily pop up and I can do some debugging. However,
the JavaScript code that's still really being executed by nodejs doesn't really
go away or become much more "Pythonic" when you're using Pyppeteer. As such,
the "win" I'm looking for is unsatisfying and I feel needlessly isolated from
node. You just LOOK AT the JavaScript code embedded inside a Python file and
it's a lot of extra thought overhead when if you just took Python and Jupyter
Notebook out of the picture, I would be doing my work in native JavaScript
(using vim as my text editor) and executing the code in node.

Ugh! There ARE issues with this graphics subsystem. Or maybe the Chromium
version. Or maybe the lack of a sandboxed environment. Anyway, I keep getting a
failure on apt-get update due to the inability to remove certain files. Googled
it and StackExchange had the answer as usual.

	sudo mv /var/cache/app-info/xapian/default /var/cache/app-info/xapian/default_old
	sudo mv /var/cache/app-info/xapian/default_old /var/cache/app-info/xapian/default

Ugh! It's 11:00 PM. Not everything has worked out as well as I would have
liked, but I'm going to try to give working during the night in bed next to Nat
a try. I get to put on the headphones and go into the zone for as long as I
like and Billy is next to me and I can pet him as much as I like. These are two
things I am generally not able to do during the day. Okay, let's take advantage
of this potentially long stretch of focus and push "the system" forward as much
as we can. Of course the system in this case and for the most part is just
generic Linux and a few other tools like Chrome thrown in. Okay, where am I and
what next?

I need to assert better control over Chrome automation (still)! 1, 2, 3... 1?
Go Right! Then, Go Right, Go Right! Hmm. Okay the problem I'm encountering
right now is that the screenshot parameter to chrome isn't working with this
graphics subsystem. However, it is working in my barebones.js example where I'm
going through node. So why not just go through node all the time. Okay, node
accepts arguments from the command-line: https://flaviocopes.com/node-cli-args/

Okay, it's easy enough to step through non-labeled fixed-position arguments:

    for (let j = 0; j < process.argv.length; j++) {  
        console.log(j + ' -> ' + (process.argv[j]));
    }

The above code given three arguments would return this, and so we can see that
position 0 gives you the command, position 1 gives you the fully qualified path
to the input-file and then the rest are positional arguments.

    0 -> /usr/bin/node
    1 -> /mnt/c/Users/mikle/github/puppetshow/barebones.js
    2 -> first
    3 -> second
    4 -> third

Okay, so my barebones.js file is going to become a screenshot.js file that
takes positional input arguments.


--------------------------------------------------------------------------------
## Thu Jan 31, 2019
### Getting Pipulate into readthedocs.org

I keep loosing grip on the next and most important project... firming-up the
broad strokes of the necessary components of Data Mastering. I should really
start drawing diagrams using this incredible laptop I have. But I'm not exactly
sure where the stylus is for this thing. I don't remember the last place I put
it. Shit, I should be better at keeping track where this sort of stuff is.
Think! We need a pulse and a rhythm. We need a place where I will always
impulsively be checking, and that it is okay to. I just need to know that
everything is working well, with a sort of Zen calm and assuredness. 

It's also time to conduct a bit of this in public. I plan on rebooting my
YouTube series soon, but before that it should really be about doing a kick-ass
job for my employer. But journaling into the Pipulate development repo doesn't
detract from that. In fact, it ADDs to it, in getting on the record in a public
way that doesn't (I believe) conflict with my employer. It brings personal
investment and clarity of thought to topics that I'm not being given technical
guidance on by my employer. It's all just got to spring from my mind.

The first trick is to get VPN out of the picture. What do I always do to check
on the cloud server? Move THAT into a GSheet. 1, 2, 3... 1? Go Right!

Well, the start of all this stuff is in my Pipulate pipdev repo. It's time for
me to start using readthedocs.org. So I make a docs directory inside pipdev per
these instructions:
https://docs.readthedocs.io/en/latest/intro/getting-started-with-sphinx.html

    pip install sphinx

Then I cd into the docs directory and type:

    sphinx-quickstart

Answer a bunch of questions, Then you can cd into docs/build/html and type:

    make html

That makes the html files locally. Okay, I did the Github integration and
changed the theme. I had to actually install the theme:

    pip install sphinx_rtd_theme

And then I had to edit the docs/source/conf.py file and alter the theme line to
this:

    html_theme = "sphinx_rtd_theme"

And now I have this location which appears to update on the git push without a
manual make html. https://pipulate.readthedocs.io/en/latest/

Okay, what I'm really doing here is using the Sphinx Python Documentation
Generator. 

--------------------------------------------------------------------------------
## Wed Oct 10, 2018
### Getting Headless Chrome Running Under Windows 10 Ubuntu BASH Terminal

Okay so yesterday was very interesting. I needed a more rapid development cycle
than transmitting .py files to the EC2 cloud could provide. I wanted to run
everything I can do in Jupyter Notebook and on the cloud Linux server also on
my local Windows Ubuntu Terminal. Windows 10 allows you to have an optional
genuine Ubuntu Linux kernel running and an accompanying Linux BASH terminal. So
in general workflow, I "flesh it out" in Jupyter Notebook and then copy-paste
the Python code into a .py file and test-run it immediately from an always-open
(and cd'd to the same folder) terminal window.

This is my normal day-to-day Linux terminal, but it has nuanced differences
from one that comes with a genuinely installed instance of Ubuntu because it's
being managed by Windows. It's lack-of an acceptable sandbox apparently makes
it different to run Chrome in headless server mode. It felt like a rabbit hole
a little bit, but also if I can't do stuff like that it's pretty invalidating
of being able to use a Windows Ubuntu terminal as a genuine one. The error
message said that if I turned off sandbox mode (and live dangerously) it would
work. It's an acceptable risk because of how it fits into the workflow. I'm not
running malicious JavaScript code, but rather only the code on pages I'm
scraping. And so I figured out how to pass arguments to the invocation of a new
Browser instance under pyppeteer (different from Chrome's puppeteer library).
Sheesh! Complex. 

I already have things running identically to Jupyter Notebook in Anaconda
consoles, but Anaconda consoles are terrible. They are very reminiscent of the
Windows command window or Powershell-- both of which are completely
unacceptable in approach I'm taking. Learning (becoming proficient at) another
command-line environment than the Linux (BASH) one is a terrible proposition.
It's better to just keep it in the BASH Terminal shell provided by Ubuntu under
Linux, but it's a whole separate code execution environment. This is especially
so after creating a virtualenv instance to keep the right version of Python
running and all the dependencies isolated. I had a few problems to overcome and
realizations that I had. For example, never sudo this command or local (within
the virtualenv) pip installs will never work.

    Correct:
    virtualenv --python=python3.6 ~/py36

    Incorrect:
    sudo virtualenv --python=python3.6 ~/py36

If you DO sudo the virtualenv command, it's going to make root the owner of
stuff in home ( ~/ ) and it will have to be undone with a chown command:

    chown -R MikeL:MikeL ~/py36

Once ownership was correct, I was able to get all the pip requirements from the
prior environment (non-virtualenv) with the following (before in the
virtualenv but after cd'ing into the pipdev repo directory):

    pip freeze > requirements.txt

I then launched the virtualenv which is now down automatically and by default
by this entry in my .bash_profile:

    source ~/py36/bin/activate ~/py36

And then I could "unfreeze" the requirements by doing the install out of the
requirements file:

    pip install -r requirements.txt

These are the ADDITIONAL pip installs I had to do from the virtualenv. I have
to work this out for better process/documentation.

    python3.6 -m pip install pipulate
    python3.6 -m pip install pandas
    python3.6 -m pip install pyppeteer
    python3.6 -m pip install --upgrade oauth2client
    python3.6 -m pip install pyfiglet
    python3.6 -m pip install colorama
    python3.6 -m pip install logzero

Then to get Chrome running headlessly, it was very similar to the apt-get
installs I had to do on the Amazon EC2 Ubuntu instance I'm using, but it had
one extra command because libgtk never got installed for anything else along
the way.

    sudo apt-get install libx11-xcb1
    sudo apt-get install libxcomposite1
    sudo apt-get install libxcursor1
    sudo apt-get install libxdamage-dev
    sudo apt-get install libxi6
    sudo apt-get install libxtst6
    sudo apt-get install libnss3-dev
    sudo apt-get install libcups2
    sudo apt-get install libxss1
    sudo apt-get install libxrandr2
    sudo apt-get install libasound2
    sudo apt-get install libpangocairo-1.0-0
    sudo apt-get install libatk1.0-0
    sudo apt-get install libatk-bridge2.0-0

And one that was necessary on Windows Ubuntu. This is the graphics stuff that
headless Chrome requires so triggering off this particular apt-get takes a
really long time. It's like turning your graphics-only BASH terminal virtualenv
environment capable of running desktop-apps requiring graphics, mouse, and
desktop interface.

	sudo apt-get install libgtk-3-0

And then FINALLY the extracted .py files (from Jupyter Notebook .ipynb files)
actually ran correctly from Windows 10 Ubuntu Bash terminal. This is almost
exactly the same process as I had to do to get it working on my Amazon cloud
server. The version of Ubuntu is exactly the same on both sides:

    >> lsb_release -a
    No LSB modules are available.
    Distributor ID: Ubuntu
    Description:    Ubuntu 16.04.5 LTS
    Release:        16.04
    Codename:       xenial

I actually ALSO had to upgrade the default Python 3.5 release that comes with
16.04 to 3.6. I did this a few weeks ago on the EC2 and I just did it now on
Windows Ubuntu. This is what I had to do to get myself onto Python 3.6 on
Ubuntu 16.04 (both in the Amazon cloud and on my local Windows 10 machine) as
documented at: https://stackoverflow.com/questions/41712326/how-to-install-python3-6-in-window-ubuntu-bash

    sudo add-apt-repository ppa:jonathonf/python-3.6
    sudo apt update
    sudo apt install python3.6

And then after Python 3.6 is installed, I sort of lock myself into that
virtualenv (I find stepping in and out of virtualenv's a pain) by putting this
line at the top of my ~/.bash_profile:

    source ~/py36/bin/activate ~/py36

--------------------------------------------------------------------------------
## Mon Jun  4, 2018
### Fortress of Natitude? Honey Badger Don't Care

Wowsers, and shazam! My small Urby studio apartment now has a Garden of
Natitude. FYI, magic is real and I got a feel from a recent experimental spell
I'm working on. Thanks to the folks running the show. Our smartphone magic
wands are far more powerful than most people can use 'em for.  Honey Badger
don't care.  The Crazy Nastyass Honey Badger by Randall, hahaha, the first
genuine LMAO and ROTFL video of significant importance to my life in a long
while. This is my new Dinosaurs by Squelch on YouTube. Wow, yet another case of
life dishing out just the right thing at the right time simply my holding your
hand out and saying you're ready. If it's a reasonable request, it seems to be
granted in my case.

Nat. I can't make "gnat" my word of affection for a special someone I just
recently met, who I conjured with my spell. I want to finish my book now. Go
all "data master" on my Twitter feed. Follow through on a bunch of things that
you KNOW if you follow through on, you'll make a big splash. Go out with a
bang... but in style like Gandalf did with the Balrog. Don't be a douche bag
MBA-tycoon whose never really happy because they get trapped into the
money-reward feedback-loop. Money is an excellent proxy for things, but not all
things. Money can't buy you love, but that's no biggie if you never really knew
what it felt like, being the natural child after a guilt-ridden adoption.

You know, I used to get tuned into the vibe by all my relatives that I got the
short end of the stick because they were able to turn themselves into the sort
of fathers who could provide for their family, 2nd marriages, lots of children
and half-children, family cruises every year for the extended family of very
educated and scholarshipped cousins. I rarely had anything going for me in my
life except maybe for a brief stint at Commodore Computers in my back yard as a
teenager and a brief stint running my dad's last-ditch check cashing company
for about a year after he died 2 weeks after I graduated college and assured
him I had a job with Scala Multimedia. 

Dad was soooo relieved at me having that job in tech lined-up. He never made
the transition, a Jew stuck in textiles. I think my Dad had his own plans
nobody knew about. I was launched into life in classic Batman-style, eerily
similar to how I once expressed to him how my "blessed" life spared my any
chance of a real hardening. I wasn't being critical. It's just something I
knew: real character is built from challenge. And as challenged as it might
have been emotionally and in the private-school area, it was NOT in the
day-to-day sense. Seen Stranger Things? ET? Basically that down to the cheezy
orangish and lime-green decors. 

I was 6 when Star Wars came out, and couldn't appreciate it properly creating a
Star Wars blind-spot for the rest of my life because things were not so easy to
watch over and over then after it was out of the theaters. Most people didn't
even have VCRs then and if they did, they didn't own Star Wars. My old house
growing up was a beautiful one in a beautiful neighborhood surrounded by the
80's dream-people-- a lot of them of the private-school type. But even the
public-school ones at my public high school went on to become dotcom tycoons
and reality TV stars. My endearing next door neighbor friend growing up still
joke about and compare ourselves to that kid. I laugh. 

The journey is the reward. I couldn't think of a fate worse than that much
success that early.  Probable interesting futures for you suddenly disappear
when there's so much money in your life that it will become the main proxy for
absolutely everything else... including the love you so desperately need and
aren't even aware of.  Once rich, the motivations of the people around you can
never be guaranteed pure. You will never know if someone loves you for just
being you again in life-- a reward even the poorest on this planet can still
cherish, for there are few rewards in life quite so great as finding just the
right person to cohabitate (at least occasionally) your local-space with.

Yeah sure, sour grapes a little bit. That could have been me. But in the halls
of Commodore Computers, I fell in love with the hardware as a means of creative
expression-- a tool and a weapon much in the way a Samurai Sword is an
extension of the Warrior's body. In one smooth practice perfect motion, the
skilled servant of the local lord could decapitate any ill-prepared civilian in
sword's reach. In this way, many large battles did not need to be fought to be
won. It was an agreeable arrangement between the Walrus and the Carpenter. By
the way, the poem of the Walrus and the Carpenter as read by tweedledum and
tweedledee were not actually in Alice's Adventures in Wonderland, but actually
the 2nd book, Through the Looking Glass (FYI).

Obviously (I hope by now, or you wouldn't be here), I relate to and aspire to
be the Carpenter. However in reality, I am much more like the chimney sweep
lizard, Bill. Poor Bill-- a fact I joke about readily with my 7 year-old
daughter who by this time, deeply "gets it" and will tell you while her Daddy
thinks both Alice and Dorothy are 2 of the finest characters in two of the most
important books ever written, but that he prefers Dorothy's "American"
take-charge Yosemite Sam-style guns-blazing style who gets Aunt Em and Uncle
Henry... oh, but I don't want to be a spoiler. Everyone who ever told you the
12 more books after the original Oz are not as good and not worth reading are
giving you a line of bullshit and trying to keep you from being a better
person.

So says Shaggy Man... a character who doesn't appear until book 5, The Road to
Oz-- just as important as any other, 'cause that's where I realized even
children's books like these can throw in a character for the old divorced dad
to relate to. Anyone who follows my Twitter feed knows that I think L. Frank
Baum is a channeller of emotional physics on an order not often seen or felt in
actual successful-in-their-lifetime folks. They usually either kill themselves
or die failures and unrecognized in their own age. The main response to
creative genius is secret jealousy, fear and monkey-brained plotting against
you. It's like the subject of half the tragedies out there. 

Just look at Alan Turing-- basically won WWII for the Allies by inventing
computers and cracking codes more surely as the Atomic Bomb (war was already
over by then but we "Dorothy's" couldn't resist. Similarly, all the stodgy old
German judges never gave Einstein the Nobel prize for Relativity, haha!
Dumbasses. If the world around you seems remarkably stupid for reasons you can
write a world-changing paper on, you too might be an Einstein. Don't let the
nattering nabobs intimidate you. They're scared of you and trying to clip your
wings in case you're actually onto something and they think will (in their own
twisted minds) make them look bad. I know this an under-the-radar flying
observer, and not any sort of scientist, philosopher or theorist.

I'm just here to tell you about how you can frame the entire world, especially
in the eyes of young girls, in the context of Alice's and Dorothy's adventures.
They are 2 of the most important book series ever written. Diamond age gives a
nice Oz-esque modern interpretation as do countless other modern pop-culture
series from Foster's Home for Imaginary Friends to Kim Possible. These stories
are the gifts that never stop giving and teach the world's most important
lesson: only Creativity Violates Physics. Everything else has to play by a
bunch of statistical normal distribution rules that most decidedly DO NOT work
in your favor. These two iconic book-series don't get put into "Young Lady's
Primer" terms often enough in pop-culture, but I do in everyday life with my
daughter...  perhaps annoyingly so. 

And it's impossible to put all this life's proper-journey / life's
proper-reward stuff together for yourself until all the King's horses and men
can hardly put you together again-- although even that's changing to be
less-true every day as technology starts accelerating faster than we age.

I'm 47 years-old, and it's time for me to spring into some writing-action. I've
moved to the gates of Oz.  I've left my love magnet at the door, and I'm
tapping into all that excess energy of not having to always do everything for
everyone (like a "real man").  My spirit animal could still be either the
Griffon, Raven or Honey Badger-- the hat couldn't decide (though I do/did own a
snake). I'm stuck in that vibrating middle of lots of possibility yet deeply
misunderstood. Honey Badger don't care (Thanks Nat for the instantly-treasured
reference). 

This is obviously (to me now that it's many paragraphs underway) that THIS is
my first life's work that I've been dying to write for awhile now that just
started pouring out as I sat down to write journal-style, as I have more or
less done every day for the past 30-years. I put in a bit more than my 10K
hours and 10 years into just expressing myself through righting, and most
recently through vim, the best environment yet written for writers in only a
way a tech willing to master an old-school Samurai Sword could appreciate. 

My path is not the one more often traveled, nor do I even recommend it for
everyone. No, this is a path you should only go on if you are in it for the
love of the work... and the work happens to be expressing yourself through the
automating of things in the world around you as naturally as you read, write or
speak once you put that 10K hours in... because you want-to, not because you
have to or your parents tell you or you got hypnotized by money. 

So now it should be easy for me. It's something I do every day and have been
practicing for 30 years (yep, writing almost daily since the day I was 18) and
haven't really published a single wit of anything of importance in all those
years. I feel now that between a background on the Amiga computer that makes
everything of today's miraculous world right down to augmented reality feel
like a second coming, and all my other irons in the fires of NYC that are
finally panning out (an SEO never met a metaphor they wouldn't mix), this
should be a breeze if I just do it the way I write. Just add a little planning,
structure and use any special motivations or channeling when you are lucky
enough to receive it.

Hello World. I'm Mike Levin, and I've recently started to take offense when
called a Muggle by my daughter. I'm a wizard; a freshly minted minor one to be
sure, but have taken the long, weak slow-grow path of the 80's wizards of the
Advanced D&D sets. I'm finally beyond the bag of holding and can cast a few
doozies. I'm finely balanced between the houses, and my daughter refuses to
align herself with a single particular Powerpuff Girl. She's on my adventure
with me as I desperately work to upgrade myself from the Humbug Wizard of Book
One to the more sympathetic old man with new tricks that followed. 

Though as tempted as I am to cast myself as the man behind the curtains, I am
no more that than I am the Carpenter, Caterpillar, Cheshire Cat, or even (and
of most obvious immediate comparison) the Mad Hatter. Due to the chances of
life or whatever, I'm still poor Bill chasing the Dodo's opportunity of a
lifetime. After enough years and making sure the opportunities of a lifetime
were still all valuable for the experience-- often learning quite a bit more
than the Dodo ever expected possible-- you transform gradually into something
new, like the slowly cooking frog, until one day you realize you're at least a
White Wizard. Is that PC to say? F-it. Walk your own path and let 'em talk.

Let's cast some powerful life-changing spells together.

--------------------------------------------------------------------------------
## Fri May 25, 2018
### Advice to Self: Be The Shaggy Man

We live in a very statistical universe. Astoundingly large collections of
things are clumping together to erase non-statistical single-particle
non-entangled effects. All things that are are entangled with other things.
Individual particles existing apart in such isolation that it can stay in
counter-intuitive superimposed states (particles being in more than one place)
are so fleeting at the macro-scale as to be non-existent. Everything that
"exists" as we experience has undergone decoherence and integrated into the
universe. Any Heisenberg uncertainty is erased through collapse but also
because all things interact with each other, the observer paradox ALSO
interferes. I think the net result is an underlying low-resolution
predetermined universe like Einstein liked to believe. The more "alive" you
are, the more you can push and twist the actual reality (head of the Github
repo wall call our timeline) in different and unpredictable directions. So try
to be unexpected like that. Be original information in the system. Don't allow
whatever compression algorithms that come in to make human history more
digestible for super-beings erase you.

The very first thing an API has to create is some sense of labels and walls so
that observations and interactions can even occur. Otherwise, we'd all just be
blended together stuff. Apartness and separateness of one thing from another
is, per genesis and just about every reasonable way of thinking about these
things, is that some blend of mystery-soup needs to be parcelled out into
separate bowls or lumps so things can happen to each other. As the lump of
stuff known as you, one of the most effective ways to interact with other
things is to make accurate observations about how those walls and labels have
been made around you and of you. You're probably going to find something with
lots of hierarchies and circular orbits. Things fly apart if there's not a
forcer pulling it together. But it would be self-defeating if the things got
pulled together so tightly their ability to interact with things around them
disappeared powerful techniques in interacting with other things Programming or
coding is a process of making illusions out of labels and walls that represent
(encode) what's there. And THIS line of thinking is where all those
anthropomorphic models of the world come into play. The fact that we're here to
make these observations means that the universe (we live in) must favor all
those rules about establishing labels and walls that make us possible.

Of course, there's tons more than JUST walls and labels, but those take in a
lot of abstract concepts. The stage on which things occur (time/space) is sort
of implied in the separation of things through labels (names, symbols or
whatnot-- a common language so that 2 lumps of stuff can focus their attention
on a third or each other) and walls (some way to separate lump-A from lump-B,
which could very well be a clumping-force like gravity and not a membrane-style
wall at all). Enough parenthesis. I'm listening to Our Mathematical Universe in
case you couldn't tell I was reading a freaky philosophical book. Mathematics
somehow exists outside space and time. Mathematical constructs are evolving and
permutating producing everything. That stuff that produces our type of
planet-bound wet carbon life had to, almost logically, have to evolve through
permuting universes where about 32 of the universal constants of existence are
trying out different values. Those constants are like the speed of light,
Planck's constant and such. The dials have to be set just-so (the fact that
fuels anthropomorphism-- the belief the universe was uniquely made for us) to
support life like us has ended up that way not through miracles, but rather
through almost statistical inevitability given enough... uh... time? to work
with? Time and heat-energy. Those are the two tricky ones that point to the
idea that it's uniquely sequenced information information that's cascading
through these mathematical structures as sort of standing waveform templates.
"Dumb" matter gets swept-up by and carried around by such standing waveforms,
becoming new physical instances of this continuously evolving template.

Yep, I think about these things in Pipulate.

Overshare without oversharing. Show your whole damn deep-self with gusto. Let
others get swept up by your enthusiasm for things. Do so in at least 3 popular
mainstream media-channels where the spark could ignite, but don't go lighting
the fire. Just keep packing a better and better big T-pee tent of layered
combustible material. Just keep building a good bonfire. Someone else will
light the flame when the time is right. Or I may do so myself. However, the
thing I have inside of me that needs saying has not yet actually taken its full
form yet. Yeah sure, Linux, Python, vim and git-- emphasis on Python. But
that's not all. It's WET vs. DRY. It's getting up to your own version-3 of a
thing, and then forge onto version 1001, by which time "your thing" has
probably morphed, evolved, and totally changed like 2 or 3 times. 

That's about where I am today, having gone from multimedia software like
AmigaVision and Scala to tracking-gif software like Google Analytic (yeah, I
used to WRITE the tracking-gif data-collectors) at various of my past
workplaces. One is still alive today in the form of HitTail. But the systems
I've built that have iterated to and beyond version-3's include Ruby on Rails
"CRUD"-style relational database front-end scaffolding-building frameworks.
Yup, I did a version of ROR before ROR, but on VBScript. A version from 2002 is
still running. That's an enterprise system of mine from 2002 in the Philly
'burbs still running, and a system of mine from 2006 still being a popular SEO
tool site. After web-bugs and crud-apps (quite inauspicious beginning to a
career of someone who idolizes our great scientists), I took up what I can best
describe as monkey-in-the-middle API-work. 

It's becoming good... indeed, mastering... this in-between stuff where I've
been spending most of my time of-late. Very specifically, it's doing it in such
a way as to exercise as many nasty vendor dependencies and gotcha's and
basically everything that self-sabotages all your endeavors before they even
get off the ground for reasons you cannot even know about yet... until you're
20 or 30 years into it like I am. With me approaching 50, my arguably 40-years
that I've had has been plenty to take-up and master plenty of things-- without
even putting too much of a burden on myself. If it takes about 10-years or
10,000 hours of practice and dedication and immersion in a thing to truly
master it, then starting at about age-10 by which time you really might have
found a thing you LOVE, that thing could have morphed into or been swapped for
another 1 or 2 times, and gone through the whole mastery-achieving cycle again
and again, taking up say violin and running. Imagine! But alas, we don't learn
all these lessons about how you could have been better using your time until
its used up. And THAT shifts an awful lot of the burden for laying out a vast
array of possibilities upon parents or whatever older generation is shepherding
the younger one into the world.

For Adi, that's Adi's mother who is homeschooling her, and it is me who has her
every single weekend for as long as she'll have me. That makes HER MY PROJECT,
but hopefully not in a way that limits her options in life. In my
Audible-listening (I still want to say "books I'm reading" but still can't), I
got up to the part in Our Mathematical Universe where the author talking about
the suicide of the daughter of Hugh Everett, author of the Multi-Worlds theory
of quantum mechanics who was never acknowledged by the field of physics in his
lifetime and died bitter. His daughter's suicide note said that she was going
to be with her father in a parallel universe. I can hardly even write these
words. Then there's Ada Lovelace. Sure, adversity and daddy-issues probably
made Ada stronger, but not so with the attention-starved children of other
double-alpha obsessives. I've got those leanings inside of me, but I keep them
in check through a rigorous routine of self-sabotage that keeps me humble and
enjoying the journey. Be the Shaggy Man. That's a good model.

Today is Friday and I traditionally pick up Adi from classes in the city, so
today's a good day to go into the office. I'll have been in the office Monday,
Wednesday and Friday this week, and that's pretty good. I have a project I want
to deliver for a friend which requires me re-gaining access to a resource I
lost... well, I didn't really lose so much as the site switched to secure, and
I only have access to the data for the pre-secure version of the site. Once I
have that, I can deliver on a very cool deliverable for a friend that has sort
of a tricking-out from the center-well effect. Yep, everything I needed to know
about being a tech asshole, I learned from a tech asshole except that I am very
determined to share the wealth in a version-3 now that I know how to way.

Now I'm actually on the train still typing. It's actually quite amazing how the
not being scared to actually CLOSE a Windows laptop PC makes such a huge
difference. In addition to not being scared to close it, least it lose network
connection and require you to log in again with a potentially very long, secure
and difficult to type password every time. Microsoft seems to have solved that.
Even though it's still sleeps-hot Intel processors, the industry has still
somehow learned to put equipment into some sort of low-power mode when you
close the laptop. Thank goodness the concept of explicitly setting sleep versus
hibernate has gone away. 

Sheesh! EVERYTHING is user interface design one way or the other, isn't it?
Even if it's the API's for controlling whatever, you still have to DESIGN the
API, and it's not always a matter of just sending a few numeric or string
values as arguments in on a couple of parameters. Our eyes and skin and every
sensor and really everything in the world that interacts with anything else in
the world has an API. Things lump arbitrarily so that they can be effectively
passed in and out of functions in discrete lumps of manageable stuff. And
THAT'S how all this ties together, which is ironic because I for a long time
have considered everything having to do with UI (user interface) design toxic.
This is the main thing keeping me away from the general full web stack-- too
much emphasis on user interaction from a graphical user interface standpoint.

Just talked with the vendor of the API I'm currently using. The situation is
pretty much what I thought. Got an excellent update on the status of that
project to my coworkers. Now I have just over an hour to get ready for the 1:00
meeting. These meetings are 2-hours earlier than most of the rest of the week,
and those 2 hours make a huge difference. The good news is that I'm in a really
good place. Focus to make the good place a fabulous place by 1:00 PM. An hour
is a huge amount of time to work with when you have your center. So, Go Right!

Windows had restarted just in the short time since the train ride. I guess
updates were waiting to install and just got it done. It's a good test of this
stuff. Absolutely, first thing is Chrome on Windows virtual screen #2. Too bad
there's not direct-number index access like there is in Chrome with
Ctrl+[Number] to jump between tabs and vim with :b[Number] to jump between
buffers. Having it in Windows too would just be too sweet but DO NOT use silly
little mods if it's not the native OS to get such features, or you're acquiring
wasted muscle memory-- UNLESS it maps to the modern tools. Mercurial hg for git
for example is fine. Using VirtuaWin to get virtual windows on Windows 7 is
fine. 

Just think about whether the 10,000 hours you're going to have to put into
mastering the thing is worth it, based on the likelihood of it still being
applicable then. Nothing like having just fully mastered the tool of a dying
industry. It's not pleasant going down with the ship and if you have even the
slightest inkling towards the technical or data-driven, then you'd be crazy to
not install Anaconda and take up Python... right now. Today. Next thing you do.
Just get Anaconda installed. Figure out how to start Jupyter Notebook and
create a new Python 3 notebook in your browser. That alone is just such a huge
first step. Have somewhere to easily run your code that puts you on a good and
true path.

Okay, I had to change my password. Be on the lookout for breaking automations.
Maybe go in and manually start a report in each repo. Thank goodness it's just
3 directories (ever) now for automation: Left, Center and Right. Nice! VERY
good for muscle memory. Go Right!

--------------------------------------------------------------------------------
## Thu May 24, 2018
### Follow your path. Let them talk.

Had an interesting worksession with a co-worker yesterday who is positioning
herself as a Data Scientist, per the bloginvention of a major. If you're
WRITING the data models that other people who are applying that actually
innovates something new as a result of a hypothesis, experiments and new
findings, then fine; you're a scientist. But if you're just applying other
people's data-models, linking up sequences and making processes and algorithms,
then sorry, you're an artistic technician, much like me as an SEO. That's why
you feel a certain kindred with and knowledge that you could do well in the
field of SEO. It's all about highly linked nodes in a network... duh. Don't pat
yourselves on the back too much for realizing that. Your flashcards was my
HitaTail, twelve years-old and still continuously running (in a single Jupyter
Notebook script sense) and still winning new subscribers with its basic tenant
that amounts to nothing more than an Excel formula to a real-time influx of
data. No matter how much things have changed over that time, algorithms only
needed to be tweaked and processes re-implemented on more modern and
cloud-friendly tooling. 

Really, HitTail has been based on VBScript (old fashioned Microsoft ASP), Ruby
on Rails and most recently, Microsoft C#. Really hardly matters-- it's just a
few thousand lines of code that takes care of business. Anyone could do it, and
it's not much more than the academic web logfile parsing of yore, such as
Webtrends (remember that?). Even during the rise of the machines, expressing
yourself well (clearly, effectively, yadda yadda) as a plain old human,
speaking plain old pre-A.I. computer languages will always have value, because
presumably humans will always still be participating in decision-making, and it
will always be useful to have languages more precise than the spoken sort as an
interoperable language. In short, I predict that Python or something almost
exactly like it will have to stay in the picture as an interoperable layer to
most machine learning systems, just as it is today through such libraries as
SciKitLearn, TensorFlow or Keras which sits on top of all of those lower-level
learning libraries providing a common ML language for Python the way Pandas
provides a common SQL-like language. This is where you ought to be if you have
even the smallest respect for processes being data-driven and some intent to
"become technical". That's all I did, back around after I got out of college
and started my first "real" job at Scala, Multimedia.

Before I get into that, I need to use the wisdom of yesterday's post. That's
another advantage of keeping your "blog" in one long text-file in a Github
repo with vim or something. You can see the headline of yesterday's post right
below where you're typing, even in a long post. It just keeps pushing it down,
yet immediately beneath your cursor as you go. It's hard to forget your
"topping of the day" and deriving an H3 headline for the day's post bit of info
staring you in the face until you acknowledge it. Start the day with physical
muscle memory. Start your In The Zone music play-list. Go Right!

Wow, what a brilliant approach. Go right. Ensure Chrome is selected on Windows
10's 2nd virtual screen in the ribbon. Close unnecessary tabs. Click tab 1 or
press Ctrl+1 (same thing, yay!). If you're not scrolled to the top of your
pipulate-center.ipynb file (I'm speaking to myself, not instructing you) then
hit Esc and then Home. At this point, Optionally hit 00[Enter] to make Jupyter
Notebook restart even though it won't waste time changing anything showing in
the browser. It's a fast-track Kernel / Restart menu option. Drop your pointer
(click center of screen on my Surface Book). 

I'm getting a very strange jumping around in large code-blocks in Jupyter
Notebook. I figured if I'm feeling that pain, it must be felt x 10,000
throughout the world (am I wrong-- long blocks in Jupyter Notebook?) so I
searched and found:

    https://github.com/ipython/ipython/issues/4809/

And so from a Conda terminal, I'm:

    conda update conda

Okay, I'm upgrading from 4.4.10 to 4.5.4. I neglected to quit out of Jupyter
Notebook first and got (maybe related) related to 'block' not being an internal
or external command. I quit JN and re-ran conda update conda and it seems to
have gotten through with no errors. Restart Jupyter Notebook, refresh my
notebooks that are still "in-browswer" (hooray Web stack!) Oops, misspelled
hooray in some posts yesterday. But that's MUCH easier. Even when web-funkiness
sets-in, it's good to google and update. It's good to be on mainstream stuff.
It's strange that the mainstream stuff is so non-Ivory-tower awesome!

Ugh, there's been a fatal stabbing on the 3rd floor, I believe over at the
other building, here at Urby. Shit, not what I need this weekend. It's not like
that's going to stop the festivities going on here with Fleet Week. I took down
my just-published (only 4 views) video walk & talk from this morning. The
increased police presence around here lately wasn't only from Fleet Week. Okay,
so I'm aware of this but I'm not going to focus on it. Back to my music. Best
strategy is to get on about my day. Someone getting killed last night in the
building next to me... okay... testing continues. Adapt.

I used my muscle memory to regain a starting point. That worked well. That led
to getting rid of the agonizingly annoying scrolling problem in Jupyter
Notebook. It's getting close to the time when a meeting should be held. Get
that sort order thing down. Just google DataFrame sort.

...well THAT was a long time ago. No timestamps still interesting to me. A
journal with hours at a time passing between paragraphs... strange. Hard to get
that very precise time-accounting of progress, but that's the point.
Accountability is on a per-day basis... API-design, haha! It's almost 4, and I
pick up Adi at 4:45. So do your final Hail-Mary of today.

--------------------------------------------------------------------------------
## Wed May 23, 2018
### The "Go Right" Physical Memory To Boot The Day

It's totally freaky that I don't have to worry about online vs. offline anymore
when I "sit down to work". Of course, the work is the thought-work that I would
normally over the past ~10 years have had to have done directly into my phone
into some app or other, maybe cloud-sync'ed but just as often not. Personal
"on-you" space that travels with you wherever you go is actually a remarkable
thing. 

I was never much of a laptop carrier, ever since I think my first
office-provided laptops over the years starting with Scala. Then, it felt too
heavy to carry around to be worth the benefit, and it has remained feeling so
over the past quarter-century or so that I've been looking for my samurai sword
secret weapon of tech-- something that I actually COULD put the 10,000-hours of
practice and mastery into and have it actually still be there in 10 years.  My
prospects have been bleak, full of false-starts including the Mac switching to
Unix (but without any worthwhile built-in FOSS repo / yeah yeah brew, macports,
blah bah not Apple) and probably the current one of Microsoft supporting
managed sub-kernels including Ubuntu Linux. 

What a trick, Microsoft!  My hat's off to you. Just like when Bill said about
the iPhone that Microsoft didn't reach high enough, they sure as heck did with
Windows 10 plus the Surface Book hardware. And I'm not talking about just the
Surface Pro tablet, or Windows 10 naked without a Linux kernel. No, I'm talking
specifically about the laptop-ish version of the Surface line, which is more a
"portfolio" design than a classic clamshell laptop-- and I LOVE it. It hasn't
withstood the test of time yet, but so far so good. 

Okay, at about this time if I'm not already dived deep in some topic, I review
my recent writing. The priority goes, if you've got motivation on some
such-and-such topic-y thing, run with it. That's a precious energy colored
unique, and you may never be playing that precise tune again, so tease out the
melody and see if anything's there. But beware of the hypnotic effect of
rabbits running with waistcoats; they can destroy your productivity for the
day, your mood for the week, or even the rest of your life if you're not
careful. We are little else but the decision-makers of the incredibly abstract
higher-order decisions that don't fall to whatever keeps your heart pumping and
legs moving; and so each of those strange and often paradoxical A or B type
moments that percolate up to that part of you that's reading this is a critical
life-path decision... maybe. 

Critical because the butterfly effect is absolutely real and the smallest of
your decisions could have profound path-in-life altering consequences; but
maybe because most of your decisions don't really even matter at all against
the background of statically predetermined events going on around you. There
will always be a tomorrow, and if you don't screw up, it will at least be
another day much like yesterday-- per the program. And I'm not saying there's
any conspiracy or collaboration here; no, just human nature. We are our own
best self-saboteurs, deep down in our lizard brain core really just wanting to
be warm and cozy as we digest our food... and to be able to receive our next
bite through lazy (efficient) reptilian ambush rather than through the much
more mammalian scurrying about... thanks to carrying around our own heating
system. Get it?

Go watch the first few episodes of that documentary program "Inner Fish".
Return. This is my omage to the computer that becomes self-aware in Hitchiker's
Guide who in order to get what it meant to be human was referred to the
complete works of William Shakespeare and then after a moment's pause gives a
sympathetic "Ohhh..." Yeah, I think making sense of Shakespeare should be built
into robot kernels akin to Asimov's rules of robotics that our real-life
death-kill strike-drones seem to lack today. No big. Anything without the
inherent hardware ability to heal and grow isn't that big of a threat because
all matter decays. 

Every single day, the ramifications of e=mc^2 sinks in deeper. First, m=c^2/e
due to maths. Shit, think about that. Matter (you and me) are EQUAL TO in terms
of equivalent energies the Speed of Light x the Speed of Light divided by the
total amount of energy your body could release in total matter/anti-matter
annihilation. So the "m" that is you probably took considerably less pure-force
energy than a small lump of gold, because that lump is stuffed with a whole lot
more quarks (3 per proton or neutron which are much fewer in carbon than gold).
And we humans do seek gold intuitively... but us. How could WE, such complex
thinking and sometimes even self-aware beings, be LESS VALUABLE in our total e
than a lump of gold? Because there's a disconnect between matter/energy (same
thing) and information (not the same thing).

Okay, in the office. Log into office-provided "static, light-show" laptop. Go
Left (if not already). Type "go". Type "z". Take note of place in process and
take note of timestamp values. Subtract a minimum of 4 (5 when on daylight
savings)... okay, looking good.

Pushing out my video, Blitter Data Master w/GSheet & Pandas. Doing that from
iPhone, so no keyword fields on the upload. Don't forget to add the keywords
immediately after upload. Keep the ideas flowing. You've got the motivation and
a few hours going into this meeting. Use it! 1, 2, 3... 1? Go Right!

    Ctrl+Windows, Right-arrow
    Ctrl+1 (as long as Chrome is showing)
    Esc, Home (gets out of Jupyter Notebook edit mode and jumps to top.
    THIS LOCATION is my "Go Right & Center Yourself" location.

Drop your pointer into the should-be active cell (in Jupyter Notebook) and
click the run button on the browser. Ctrl+Enter would also do, but I'm not
going to be a stickler for using the keyboard while in a web browser. A browser
is like the definition of a point-and-click environment, so yield to the
browser. Just don't take up JavaScript as your main programming language. Okay,
so... switched Tab name to Health. Get everything lined-up and get it working.
Okay, now figure out how to input values BACK INTO the config tab without
file-bloat. How can you express this most simply? Okay, done. Next?

Meeting coming up and I will need to run multiple versions... do a test run.
Work through it. Do it all in the next 15 minutes before my 2:00 PM
pre-check-in. Deep breath...

Okay, that went well. It is much later in the evening. 8:15 in fact and I'm
waiting for the Adi call while I'm here on the train. I may not accept the call
and spare us both the frustration, then text her some train emoji's. Maybe I'll
do that right now... Done. Good move. I sent her a rocket ship, then a
helicopter then a canoe. Adi sent me a series of green and blue hearts. That
may shape up to be our logo, hers and mine.

--------------------------------------------------------------------------------
## Mon May 21, 2018
### Go Right

Interesting. Okay. Monday morning. At office. Have to be at the office in
person a few times a week. Good always to start out with Monday to get off on
the right foot. Make the best of your commute. That video you did this
morning... 10 minutes no talking, spectacular view... was a good start. But now
throw yourself completely and whole-heartedly into the report(s) this morning.
Get that grabbing of the category benchmark correctly (enough) to feed a good
category estimate (percentage) for the difference calculation. You've to to
start allowing "math" (justified as the inputs and outputs of functions...
haha! (publish this)) if you want to do your job the best you possibly can
here. You have to stop brushing off the derivative formulas as final-mile
details. The more you start with the purpose and spirit of the derivative
formulas in mind, the better will be your selection of the data to sample out
of the deep and vast flowing ocean of data that's available already through
various "web-scale" APIs provided by Google, Amazon and others. But mostly,
Google and Amazon. Know these 3 things:

    - Google Services
    - Amazon Services
    - Local & Cloud-based Hardware
    - API Nuance Wrangling
    - Having/Realizing Vision

Yup. That's about it. Don't let too much time slip by this Monday morning.
Update your boss with this / better clarified in terms of what it means to him.

- Final stages of API nuance wrangling.
- Final Master Template instance inches away.
- Big payoffs here. Allow me to enumerate.

Enumerate! Don't forget the heroic date_ranger() function... implemented on
some iterating object to give you arbitrary number of date-ranges corresponding
to an arbitrary number of fed-in "days-ago" integers along with an optional
unit representing the number of days in the range (defaults to 30). So this
accommodates all the current common cases except for the increasingly unpopular
calendar-date ranges. 1, 2, 3... 1?

Check the reports! 10:30 AM is an opportune time to look, right in the middle
of a hard-scheduled periodic run (organic.py). Hmmm. Yep. Still appropriate for
publishing. It's no mystery an SEO interested in Google Sheet automation is
also interested in the subject-matter of organic search traffic. I have after
all embedded a few sample GA and GSC (Google Analytics and Google Search
Console) and now I see it going into the big, laborious GSC CSV
generation-phase because until recently, you could only get a 3-month window
out of GSC, which was not long enough for the necessary-for-business
annual-cycle predictions and so necessarily needed to be archived. Rethinking
necessary. I upped my business-account quota on my Google Data storage so I
could go up to 100GB of company-related storage. Very interesting move to dodge
having to refactor everything around Amazon S3. 

I was completely disinterested in doing this on the "old" pipulate files which
are currently "on the left"...  left behind, preferably each time you re-think
and redo (aka scrap-and-rebuild) based on newer realities and newer tools and
techniques and even business principles. We cannot lose sight of the impact of
generally technology-driven disruption. We also must not lose sight that it's
remarkably difficult to tell the real long-term winners from losers until after
the dust settles. I think it'll be our children or grandchildren who really
will be able to accurately judge the long-term efficacy of the plans and moves
of Amazon vs. Google vs. Apple vs. every other musky company you can insert
here. 

I'm increasingly believing that what we're immersed in the middle of right now
and have difficulty expressing as a not-scifi tinfoil hat sort of thing is the
race to construct the evolutionarily obvious next-step digital nervous system
ushering in light digital versions of group-conciousness-- group by virtue of
the fact that some in-common digital assistant akin to the computer on the
bridge of the Starship Enterprise, precisely as envisioned by the granddaddy
engineers at Google before they started distracting us from that key-goal with
an alphabet soup of distraction.  Just follow the AdWords money. Protecting
THAT revenue-stream is top priority around Google... NOT self-driving cars.

Okay, so distraction is my greatest weakness, but occasionally following the
threads of those distractions to their logical conclusions, and coming out the
better and more capable (if not battle-scarred for it) is the source of my
greatest secret weapons and strength. Currently, that's being expressed best by
FINALLY investing myself whole-heartedly and "all-in" on a thing... which
happens to be Python, mainly. But then also vim secondarily, and generally a
nice generic but diverse smattering of Linux from non-desktop versions like the
minimum core version of Tiny Core Linux that leaves out the graphical desktop
to a nice bloated Debain version like Ubuntu and at least one Redhat-lineage
Linux like CentOS just so you're exposed to rpm/yum and stuff. By the end of
that experience, you'll know tce-load, apt-get and yum. 

That's not a bad place to be on the Linux-front. It may drift somewhere
adjacent over the next 10 to 20 years, like to more embedded-systems or
high-level systems that layer in the amazing augmented reality capabilities of
modern hardware without forcing you to do low-level platform-dependent hardware
programming. I know they say that the abstraction layers of modern languages
are supposed to spare you from that, but try telling that to an iOS developer
versus an Android or XBox or PlayStation developer. Hardware surprisingly still
matters... a lot. I'd certainly be an iPhone app developer today were it not
for Objective C. Their opinion swung back towards pragmatic, but not before it
was too late, and they lost me to Python. And Python's big weakness is mobile.
How's that for irony? The thing I advocate most is mobile least. Ugh! So take
whatever I say with a grain of salt. My credibility always hangs in the brink.
I'm a risk taker. I'm placing my bet on Python. Welcome to SEO. You're reading
the writing of the real-deal, doing their thing in the noosphere, knowing
you'll be poking around in here sooner or later if this pipulate thing takes
off... haha! vipgq

There's a whole lot of specialties out there to trap you like an Alice in
Wonderland Rabbit Hole from which there is no return... because all your highly
receptive underutilized and yet-to-be-programmed synapses get the first layer
of learning laid-down with whatever you chance into... and too often, that's
Java because of college compsci courses or JavaScript because of the sexy, sexy
front-end user interface job market and potential Rockstar status.

If you want to be the baddest ass of badasses, also learn pacman under Arch
Linux, and throw in some Raspberry Pi sd-card imaging, and you'll be a
hardware-controlling kernel-shuffling virtual-god on the order of any of the
old school (not old'skool) Unix sysadmins of yore who got off on choking their
enemies off from their budget-given... 1, 2, 3... 1? 80/20-rule escape! It's
already 11:00 AM. Check your email and find your Jupyter Notebook
browser-center. You have 2 actual center's here... Left and Right. The center
of the center is the OS. It's the gluon. 

The OS is whatever provides the Amiga+N, the Ctrl+Windows+Left/Right, the
3-finger left/right swoosh on a trackpad or whatever it is you're going to have
to do to navigate between static-memory-biasing "fullscreen" configurations
sweeping desktop since mobile showed "us" the way. And by us, I mean you people
who never knew the joy of Amiga+N in the EIGHTIES!!! At any rate, by whatever
technique you navigate quickly between Left and Right at Center is a function
of which host OS (platform/whatever) you're choosing. Some have certain
difficult-to-decline advantages like always-just-working that keep this part of
the tool equation deeply rooted in the proprietary-tool solutions. This is
where I am still on Microsoft-hardware running Windows 10. 

If you're talking about Bill, you're talking about my g, g, generation. I'll
stop trying to put him down, just because he played dirty in his day. What's
coming out of their labs have clearly learned the lessons of the Amiga, better
in fact than the Mac, and in ways that embrace new technologies like
touchscreens sooner, faster and better than Apple. Wow... didn't think I'd see
the day in the one direction (Apple's miraculous recovery/ascent) and then the
other (Microsoft's miraculous recovery/ascent). And for these to be my everyday
thoughts, and for me to take such joy in the return of technology muscle-memory
recovery (achieving for the first time "for-real") is a kick and a breath of
fresh air every day. I have to pay-back my employers (for the time, not
equipment which is my own) with remarkable productivity now. The butterfly must
come out of its cocoon. 

Begin rolling out this no-system system. Immerse yourself in the work in
lighthearted little loveworthy ways every day, and let it organically grow and
spiral out from there. Let it blossom like a flower. Don't try stomping on it
like a tube of toothplaste. I've been in the role of that tube of toothpaste
goodness to be squashed flat and rolled-up and discarded too many times to not
recognize the latest rendition. Fear not! This is never (rarely) the
intentional behavior of the task-masters. People who hire wizards expect magic
without an appreciation for what it requires to actually BE the type of person
who can marshal those resources and visualize those subtle cascading
connections of cause-and-effect, and then to perform that magical sequence of
symbols and gestures so as to trigger of that cascading magical moment.

And trust me, that moment is pure magic to those who need it and witness it and
covet it. And the best wizards don't hoard magic or keep secrets. Because the
practicing of such magic should almost in every case lead to better lives for
everyone in the all-around everybody-wins fairytale future that we're perfectly
capable of making if only everyone were open about everything that matters
because it impacts other people and that's just called being a decent human
being. But believing we are on the verge of infinite inexhaustible resources,
including time, space and matter, is a pretty tough sell to the luddites who
generally run the place, because the keys to power are closely guarded and
handed down generationally, first in the family, second in the tribe, and third
over their dead bodies.

Shit. 1, 2, 3... 1? Center. You're Left. Go Right, my son. Oh! The Web Browser!
I'll be vibrating back and forth here while I calibrate for a hyper-effective
few hours of work. Be proud by 3! 1, 2, 3... be proud by 3. You could have 1 if
only you knew what 2 do...

Tab 1 is this, even though it's not your work-in-progress file, but rather a
Jupyter Notebook provided directory-listing of your Center repo. This makes
sense because even though it is Tab 1 because... oops! Things have changed.

    http://localhost:8888/tree/github/pipulate-center

The above may end up being Tab 2 or opened only as-needed, because the way
Chrome behaves recently changed. It used to be that Tab 1 was Ctrl+0 as far as
keyboard shortcuts were concerned to jump-around tabs. This is an excellent
example of where you actually do have to keep your muscle-memory a wee-bit
flexible, even on multi-platform, seemingly fabric-of-the-Internet tools (but
really, not) like Chrome. Even here you must be aware-of and concerned with a
certain vendor dependency to your habits that sneaks in at the edges where you
wouldn't expect. Google might switch the Ctrl+[number] keyboard shortcuts that
let you jump around your browser tabs without taking your hands off of the
keyboard from being a 0-based to being a 1-based index... hahaha!

Trust me, nobody appreciates this as much as me. I am THE audience for that
person there who made the final decision, and they don't even know it because
there's not enough time in the day to participate in every tool's RFC
discussions. I used to that sort of thing, but got it and everything like it
out of my system in the late 80s and early 90s before the Web set in. Commodore
and the Amiga in particular had a pre-Web twisted-pair (old phone system) and
user group (pre socialmedia) version of pretty much everything-- including
vim... Fred Fish #591 in 1991... which I received in the middle of enemy
territory at Drexel University where I went to college-- the first one to
require every incoming freshmen compsci or not to buy a computer. First in the
country to do that, and they required Macs! My alma matter was one of the
biggest feathers in the history of Apple's cap, and there I was an avid Amiga
user and president of the local user group squatting on a monthly meeting place
and storage closet for like 4 years. Those were the glory days. I'm such a
geek. It's such a pleasure to see the world finally catching up. Go Right!

Got it! Your work-in-progress can NOW ALWAYS BE BOTH TAB-1 VISUALLY AND CTRL+1
KEYBOARD SHORTCUT-WISE and this is huge for muscle memory. This is the first
time in years. Okay, push observations like that out into the twittersphere
when they occur to you. Be the Seinfeld of tech. These sort of things occur to
you and are genuinely important and sometimes funny and certainly must be
commented upon. And so I have:

    https://twitter.com/miklevin/status/998589254472265733

...although my delivery and laughtrack is decidedly and lot quieter and drier
than Seinfeld's. Oh well. It's for my entertainment (and assurance of forward
progress) not yours. Go Right (has the potential to ascend to be as useful as
1, 2, 3... 1?). Ah, you ran pipulate-center.ipynb for the first time today a
few moments ago. Take down some cache stats. They're uniquely well displayed
there right now. Immerse yourself in your system-making non-system system
conventions. See? It's just a few working-together conventions that make the
system-- NOT some django-like mega-framework. I'm really getting the difference
now between Django and Ruby on Rails though I can't really express it well yet.
You will continue to be well-served though by avoiding Django, I do still
believe that, even though I never really tried it and there is one lightweight
derivative version for Web CMS (as an alternative to static files) that does
appeal to me. But those Web publishing days (as a thing) is mostly behind me
now. It's all about these Github-repo-project-embedded journals now and for the
foreseeable future. What did I see when I went Right?

    app_sdks: 2
    category: 1
    app_data: 28
    estimate: 168

Wow, this is really, really powerful! Okay, hit this friggin thing home for the
3:00 PM. It's staged to spike. Run report again and get the new numbers. Okay,
only app_sdks got re-run. Cache it... well, it ran TWICE after the cache was
added... same behavior as during the Friday call. Smoking gun. For whatever the
conditions are that I'm creating (Jupyter Notebook REPL execution context) or
by design of the cache's default behavior (a possibility I must investigate),
it takes 2-runs before a function-call is cached and it's printing side-effects
are no longer invoked (by a "real" non-cached function-call).

Okay nice, I'm now getting no uncached function-run outputs. Solid. Fast
iteration-land. Nice feeling inside. Watch your caches. Control your caches.
Pushed a tweet out to that effect. Okay, you're closing in on the important
thing for the meeting. I want to eat, but maybe just another caffeine boost.
Nothing more. Do it here with the crap powered coffee machine... no... Dr.
Pepper. Don't drink bad coffee when old magic potion is available. Okay, doen.
Body tricked into thinking it has what it needs. Take advantage of it now!
Forget about your clever date_ranger desire (to make it more flexible with any
number of ranges based on number of start-dates input) as a major code elegance
improvement to pipulate, but that's not what you need most now.

Okay, so what I have now is a vibrating between Left and Right with a gluon
(hardly existing) Center. What is your Left, Right and Center can vary based on
what you're doing. For example, switching screens has no center per se. It's
the process of transition that makes center. However, oh the Left, Journal is
center. However, Journal even has a Left (Private Thoughts) and Right
(Pipulate's Leaky Journal)... so the metaphor of Left/Center/Right is just
mapped over whatever other concept however it needs to be to make sense and to
best service muscle memory. Sometimes Center is virtual-glue (never "seen" as a
screen) and sometimes it is an actual screen and file and "on-deck"
work-in-progress like pipulate-center.ipynb and pipulate-center.py.

Good workflow. Go Right.

The meeting went fairly well. The rabbit I must not chase right now is how I
put the data retrieved through the API BACK INTO the config tab, tempting as
this final bit of meta-magic may be. Instead, just copy/paste the data from the
gui for each of those "time-frames"... okay. So you're just mapping to the
closest month. 30 is last full month (April). 90 is probably February. That
would make 180 last December. That will work for now. Get those numbers in
pronto!

Okay and the last thing now is the trajectory column. You get to lift that
formula directly from the mock-up.

It's 6:45 PM and I'm at the SI Ferry terminal Manhattan-side, sitting on a
window ledge vimming into my Surface Book 2 actually on my lap. I remember when
the joke was that laptops were for anything but your lap, for every reason from
design to how hot they ran. Well, it's another thing that's gone full-circle.

You know what else has gone full-circle? Magic. It's easy to imagine lands like
Asgard per the Marvel movies existing due to the fact that any civilization
sufficiently advanced will have allowed it to have accidentally slipped into
the realm of magic... due to the AI "spirits" having been self-repairing and
taking human requests in verbal format for a few generations-- just long enough
to forget, and otherwise lose interest in, the "old-school" way of doing
things. Why learn Python today if some collaborative design-bot out to bring
out your best enables you to just forget about it and focus on verbal
expressiveness-- which is what humans are wired to do well anyway.

Okay, it's clear that I'm ever-so-gradually falling back in love with
technology after a long winter of betrayal and perpetually "floating position"
setbacks and undo's thanks to greedy and incompetent vendors-- no matter how
meritorious the platform. I'm of the school of Atari 2600... those of us who
knew the otherwise Atari VCS, when 8-bit machines were highly proprietary and
Jack Tramiel was pitching computers for the masses, not the classes. This was
before even the Apple Macintosh 1984 commercials and before IBM PCs commonly
even had color graphics-- something not considered "necessary" in a serious
business machine.

--------------------------------------------------------------------------------
## Fri May 18, 2018
### Daterange Function Drawn and Quartered (grisly metaphor)

Let there always be gratitude. You always have someone to thank.

Let the day begin. It is another Hail Mary (by 1:00 PM) Friday.

You can do this. JUST GET THE FORMULAS DONE!

This involves a benchmark for every time-range.

This involves the time-ranges being really 30, 90 and 190.

This involves datetime work I don't want to cram in, so support faking a date.

This involves maintaining focus in a way I rarely can pull off in 2-hours.

But do it. Show your gratitude for this chance. You're aspiring to be a data
samurai ninja. Be one. 1, 2, 3... 1? Oh god, Windows 10 mysteriously freezes
all input for seconds at a time. What is that a sign of this day-and-age with
hardware this powerful... a lag that can last for 5 or 10 seconds? Shit,
remember to Google for what's going on there. Mac's don't do that. When they
freeze, they're toast. When Windows 10 freezes, just hang tight and keep that
special rage reserved for idiots on the road in-check. Don't let that kind of
ire get directed at a platform that only just became usable in every other
regard. The Amiga crashed, after all. Momentary freezes are wayyyy better than
crashing, even if it is to report all your activities to mama.

1, 2, 3... 1? Center. Center means pipulate-center.ipynb now. Go check it out
in the browser... okay, runs well.

Interesting thing with the cache though. I expected AS MUCH hitting the cache
today as after clearing the cache yesterday, but it wasn't. I think I didn't
think through the behavior of the maxage parameter of percache fully.

I have to also fully internalize the new slate of pipulate left, right and
center sbin commands. If in doubt, always type:

- p[Enter] (to list pipulate services running)
- pc[Enter] (to toggle the pipulate serice on or off)

Between those two commands, I can always ensure that the 24x7 pipulate services
(currently only pipulate-left but soon pipulate-left and pipulate-right) are
running. Pipulate-center gets toggled on and off according to whether my
"centered work" is actually in the scheduler or not. More often than not, it's
going to be in Jupyter Notebook still, which is interesting. I've got a quick
test to do there regarding invoking entire modules from inside other modules
without relying on invoking classes or functions from inside the module. I'm
looking for the global effect of just important the module to be able to be
re-executed by the Python schedule PyPI module. I used to import them using the
normal Python import statement, keep global side-effects to a minimum, and then
invoke module_name.Main(), relying on the presence of a conventionally named
Main() function to be there for scheduling. But because cramming everything at
the script's global root into a function like completely throws away the
REPL-advantages of Jupyter Notebook and throws intuition out the window for
anyone dealing with such a script in Jupyter Notebook, the right solution is to
figure out how to intentionally import (or load/reload or whatever) a Python
module primarily for it's global "on-first-run" behavior. This very much leads
me to think I'll be using the same trick in the pipulate-right main scheduler
script (clearly destined for a reworking) in a very similar way to how I'm
dynamically loading and refreshing Pipulate every time from ../pipdev. See? The
solution is looking me in the face, already in my pipulate-center.ipynb.

It's worth pointing out now that I have some VERY STRONG NICKNAMES (and
therefore conventions) in play now. Specifically, my main work files are
ALWAYS:

    [wherever]/github/pipulate-center/pipulate-center.ipynb

This is the current (often highly customized) version of:

    [wherever]/github/pipdev/main_template.py

Every morning, I try to "find my center" to be fully effective. I don't fully
know what it means, but it works. It has something to do with Elon Musk's First
Principles, or the axioms, givens, truths, assumptions of philosophy, math,
whatever. But the point is that you always build-up AND build-down. You're
vibrating back and forth on a generally similar stack of stuff. The more
similar the stack of stuff each day you're scanning and sampling back-and-forth
between, and the more linear our back-and-forth scanning is (as opposed to the
formidable task of a SETI-sky-search), the more effective you can be each day
at banking a few of the important difficult (and no-takeback) things required
to keep moving your life forward, and forever closer to your own personal
whatever's if you've got 'em. I do; although they're not always clear.

EVEN THIS WRITING IS A DISTRACTION.Back on track for meeting... in just over an
hour. Get it to a good demonstration-point. It doesn't have to be done... just
obviously just about there. Put all the benchmark placeholders in the config
tab. You've GOT to think those through. Okay, THIS is the way to do it. Just
start filling data in and flex the system you JUST MADE THAT FLEXIBLE into
shape. Yeah, I'm doing some remarkable stuff here. Don't apologize for your
speed or sell yourself short. Correct component-selection combined with elegant
Language/API-use to keep it all... well... LOVE-WORTHY thus scalable by a
single individual... yeah, that's it. That's important. That's a tenant of
modern effective Python-centric datamastering. Even though other people will
have APPEARED to have been here before you, you are really actually
homesteading in the noosphere. I feel it in my bones. 1, 2, 3... 1?

Get those date-ranges correct, dumbass! That's a big dependency for other
things, and it's come up in a few meetings already. It's YET ANOTHER spin on
the date_range function, but it's highly abstracted now in its latest rendition
in pipulate (go look at the repo for yourself), and so I should be able to:

1. Limit the function to ONLY ever return 30-day ranges.
2. Take a tuple of days-ago as an input (180, 90, 30).
3. Make the whole date-range thing EVEN SIMPLER as a result. So worth it.

Okay, so I need this in Jupyter Notebook and NOT in experiments.ipynb... good,
I'm making muscle-memory mappings and connections and wired-pathways or
what-have-you to some very concrete locations in the nothingness of the
informationscape. Next to pipulate-center.ipynb is ALWAYS experiments.ipynb and
pipulate-center.py... see? Very tightly confined scope of "center" and contents
in "center". When I bring my center in focus, let there be no misunderstanding
of what I am working on right-now and why.

Let pipulate-center.ipynb always reside on the 2nd Chrome tab, because that
maps to Ctrl+1. This loosely corresponds to the :b1 vim command I frequently
use to get back to this, my private thoughts journal-- `before I copy/paste
select entries to the vim-buffer residing on :b2. Simply moving entries from b1
to b2 IS THE ACT OF PUBLISHING THEM, because it will get swept-up in a general
update by the "g" command that I'm always updating to keep all my key repos
up-to-date on Github. Muscle-memory, see? The sbin location, and a cascading
effect of distributed revision control that familiarity with one-letter sbin
commands of your creation kickstarts your self-navigating momentum... because
complex concepts start becoming as easy to express as:

    g

Gee, that's easy. And this is progress too. I'm in a friggin' pupa stage still
of datamasting. I'm a friggin chrysalis. I accept and admit that. It makes me
slower than I'd like to be at work, but I'm about to emerge as a butterfly
here. Maybe I can lay claim to the mantle of the Caterpiliar as my soul-match
in Wonderland, after all. I tell Adi that while I may sound like the
Caterpiliar, in reality I'm more like Bill... poor Bill. But Burt does have
some mad sidewalk-VR skills. But that's the nonlinear thinking that must get
swept under the rug of daily effectiveness. It's coming up on Noon, and you are
SO CLOSE. Drive this puppy home! 1, 2, 3... 1?

Run pipulate-center.ipynb again now that the cache is populated for today and
the 9 benchmark placeholders are in the config tab. Okay, to get this formula
down... axioms...

1. You ALWAYS HAVE BENCHMARK DATA in config dict (by whatever means).
2. Every formula-invokation must know for what time-range (1, 2 or 3).
3. Every formula-invokation must know for what metric ('dl', 'dau', 'rev')

The formula is always:

    ((newer - older) / newer) - ((bm_newer - bm_older) / bm_newer)

The newer and older values have the following parameters:

    - the metric's name: ('dl', 'dau', 'rev')
    - the time_range: (1, 2 or 3)

Okay, so slam out the global dictionary with the new time-ranges. Lift
date_ranger function from pipdev... on your local machine. Can be done right in
Jupyter Notebook (the web browser)!

Phone-call had. Went well. Want to pick up Adi by 7:00 PM. It's about 5:00 PM.
Once I pick her up, I'll probably get nothing else done for the weekend,
realistically. Haven't eaten anything or taken a shower yet today either. Tick
Tock! Keep aware of the clock. Keep aware of the vision. Don't let up. It's
okay to eat while you work. Do a shower last thing before leaving to pick up
Adi.

This next step is the argument-passing mental gymnastics of how Panda's
DataFrame.apply() works. It's not loading the function in the tradtional way,
so one would not expect a cache decorator to work with it. It might. But
really, that's besides the point. It's about parameter passing and not caching. 

Wow... so much mental gymnastics today! Look over your work today and make sure
it's on-track. Okay, there's a bit of follow-up work on the new date_ranger
function. It's so friggin awesome. It's api is:

    dates = date_ranger(starts=(30, 90, 180), days=30)

And you get back 3 date-ranges of 30-day intervals starting 30, 90 and 180 days
ago. This is where the grisly concept of drawn and quartered in the headline
came from. It's spreading the 30-day date-ranges over a broader total distance.
There are nuances here. I find the API I'm working with to be good with 30-day
ranges but not 60-day ones for example, so the 180 days can't be more
comprehensively split up with:

    dates = date_ranger(starts=(60  120, 180), days=60)

That would have better day-coverage over the 3-ranges in 60-day sets, but the
API choked on it. So, drawn and quartered it is.

--------------------------------------------------------------------------------
## Thu May 17, 2018
### pip install percache / Firefly Tiffany Lamp Destroyed

Today... a weekly report day. Make it one for the history books. Solve lots of
long-standing problems. I actually thought I did that with lru_cache from the
standard library, but turns out, that's just "in-session"... or during one
execution-run, such as it were. This is probably fine for webservers where the
parent task stays in memory (and thus the cache) until a server restart, but
with scheduled tasks, memory gets cleared between every run. And especially
with Jupyter Notebook, it gets cleared every time you simply re-run your
script... and that's no good for my use. So I'm trying to get something
basically API-compatible with lru_cache. It's an old case of how easy it was to
switch to git because I knew hg (Mercurial, a git-equivalent distributred
revision control system written in Python).

Ugh, Billy has given me the greatest gift of a totally clear desk, free of my
new Tiffany firefly desktop lamp which he broke in a mad-dash to get food that
he thought that wasn't coming out, but wasn't. So it was over nothing. I think
it was like $250 or something. Oh well, live and learn. There's always matter
that you think is going to matter edging its way into your life, then turns out
not mattering at all because other jealous matter saw to it. Yup, although
living, the cats are the most jealous bits of matter in my immediate orbit--
until the weekend begins, which is tomorrow night. Wow... okay, I feel
ever-more ready for Adi in my tiny Urby studio.  Big lessons in life in this.
Don't put ANYTHING out that you're not okay with getting broken or destroyed...
sometimes meaninglessly. Just wrong place at wrong time.

I have a whole theory about the wants and desires of matter to become entangled
in your life, for the sole purpose of becoming entangled with a local "god" of
matter, who can bend and shape and form it-- reducing disorder and wrapping
out-of-the-game (or lesser-participating) matter into in-the-game or
more-participating matter. There's (probably) dark matter/energy and there's
light matter/energy (all we can see) and then there's things we call alive and
things we don't call alive. In some form or another, I think we're going to
find out that going from information to light to matter is actually the first
step in life. Not that all matter is life, but all matter is maybe like
proto-life. Its the stuff that has to exist first, before life (like ours) can
exist. And that's a very workable theory. Gets solidly into Star Wars force
territory, but I think there's a good slice of truth in there, like so many
artists get when intuiting (channeling?) their way through stuff.

To have a good showing by this 3:00 PM, I definitely want the formula correct
AND a better cache in use. Install perchace... do it from the Anaconda
prompt...

    pip install percache

Okay, now test it from a brand new notebook. Do it in pipulate-center but call
it experiments.ipynb so you know nothing in there never really needs to be
kept. But DO add it to the git repo. Also upgraded from pip 9.0.1 to pip 10.0.1
under Anaconda prompt.

Wow, what an interesting day. Yes, one for the history books, but it turned out
to be because of the chain of discoveries culminating in using the
game-changing percache library, which is basically API-compatible (a few small
edits) with Python's lru_cache built into the standard library. My education
that culminated in this discovery went something like this:

- Python can pickle any Python object for long-term storage
- Pickled objects can be stored in "shelves" using key/pickles
- The old web browser cookie-nesting for sub-keys trick also applies here
- Ohhh, so home-grown caching systems are a cinch to implement. Implemented.
- Oh, that's a whole lot to maintain with all those "with open's"... yuck!
- Elsewhere in my Python education, I discover decorators (during Flask work)
- Raymond Hettinger, you say lru_cache from Standard Library uses decorators?
- Well, caches and decorators are a match made in heaven, aren't they?
- Oh wait, that's not caching between script-runs... waaaait a minute.
- It's solving the 2nd half of my pandas.apply() problem, but not the first.
- Can't I just swap lru_cach for something API-compatible and persistent?
- Search, read, search, read... yep. Per chance, it is percache.
- Swapped in perchance code (removed the parenthesis after @cache).
- Assured myself of behavior of print() statement from cached function call.
- Wrote support-function for bottom of cached function for assurance's sake.
- I realize THIS IS WHAT DECORATORS AVOID for and will later modify percache.  
- Test my control over clearing the cache by setting maxage argument.
- Totally satisfied with percache behavior... pshew!
- Weekly report. Attempting to not look like an idiot for the more visible
  "top-line" items not getting done.

Publish? Publish.

--------------------------------------------------------------------------------
## Mon May 14, 2018
### Finding my Pipulate-Center

Very strange times and mind-space. Don't blow it. First, the rules of the API
are all-important. Know those details and corner their rules. Confine, make
examples, focus on edge-cases to establish API-boundaries. What are the errors
on bad input? Fuzzed input? Don't get hung up on this sort of thinking today,
but DO use it in making your quick decisions. You have to work quick today!
MERCILESSLY suppress/put-away, take out of your focus ANYTHING THAT DISTRACTS--
and that can't be this journal, because this journal is your focus. It is a
shadow cast by your train-of-thought through having good muscle-memory in vim.

This paragraph is a distraction, but I feel I must get it out of my system
quick. FIRST, check the reports! Okay, done. Things don't look bad, but I think
something may be crashing in the schedule. Ugh, that's the pipulate-left
service for you. All that stuff ought to be left behind. Let's get this right.
Once things are right, they last 'cause they're house-of-brick design; and I
assure you that stable, meaningful, vendor-independent, easily read,
maintained, duplicated and transformable digital dashboard systems for
marketing that can be envisioned, implemented, refined and maintained by a
single person as a sort of secret weapon today and major feather-in-our-cap
bragging point in the future as an example of innovative thinking is not a
common thing. Neither is a sentence that long or concept so convoluted.

I guess developing the ability to construct a sentence like that and somehow
still make it work is the reason I had to take this slightly icky stroll
through the field of SEO. I mean, we're not all totally slime-balls, but I do
realize that we're on the edge of mysticism peering into crystal balls that are
just low-resolution 4-dimensional strange attractors holographic ally projected
like a floating head at Disney World. If you get yourself into the right
head-space RIGHT NOW, you can do this. Control all the factors. No matter how
interesting the Chaos audio book is right now, you've got to switch to either
silence or your zonelist. I like that concept: my zonelist. Even Adi noticed
the hysterically laughing Professor Hubert J. Farnsworth adorning the cover of
my favorite playlist-- whether I'm at work or home doing things I want to or
have to. I feel my full-integration philosophy at work there.

Speaking of full-integration, get to work! Navigate. Do an expert bit of
navigating here. You need a ritual that's more-than and better-than "check the
reports" and your 3 daily metaphors (most broken, biggest bang, and plates
needing spinning). It's got to involve the actual application of THIS
muscle-memory and type of time you're spending right here and getting you over
doing particular things in "screens and tabs" relative to where you are here--
actual finger-movement-wise. Make forward-progress an inescapable result of
naturally occurring finger-movements before you even start to consciously think
about what you need to do each morning. I'm reducing the re-initialization and
re-capturing of the in-the-zone creative state and creative act (producing the
actual PRODUCT of creative behavior) into a martial arts kata. Yeah, that's
basically it. So it's pretty easy to see that this journal entry is going to
go-public, and I had better walk the walk now that I'm two paragraphs past NO
DISTRACTIONS! Pshwe, okay... 

Begin the light-show. The light-show has to be brilliant. It has to exude truth
and competence and that samurai datamaster feeling; ALL THE TIME AND IN ALL
THINGS. You are embarking on a world of sides and middles. You are always
working on something in the middle. You live in the middle. And you are the
crazy acrobatic meaning-instilling API-monkey in the middle. You don't need no
stinkin' vendors, and the whole damn world is as big as all 5 boroughs plus the
Catskills-- and occasionally Philadelphia, because that's what even the
greatest of native New Yorkers in their independent movies fantasize about
being from, so we genuine tiger-eyed Italian Stallions who are quite difficult
to knock down for the count. Sure technicalities, but everyone really knows
that's just the judges making a subjective call.

It's funny, I keep skipping Limbo as my first song, going right to Ain't Got
Rhythm-- much better for getting into the zone. It's amazing how much
"alignment" of the matter around you (me) is necessary to get it all just to
fade away into a flow of thought that CAN include things that are under the
category of HAVE TO DO rather than want to do-- there's something about finding
the love for the work in this process-- tying ANY task to the love of
exercising the muscle-memory necessary to making it real. And in this case, I
just blasted out the pipes by running the upper-portion of my current
pipulate-center project. It's currently called apptopia.ipynb and is in a
private github repo for pipulate-center. Probably a bad idea to say stuff like
that, but f-it. Nothing here is top secret, and I'm actually trying to make
this stuff blow-up... eventually... ever-so gradually. No rush, in fact. Just
plant flags and document. And that's what entries like this are. Nice
discovery, huh? Hahaha! Thought you invented this little corner of the
noosphere. Nope, mine! GSheets as Dashboards as heart of the modern
Pandas-centric Datamaster movement... epicenter: SEO. Good headline possibility
there. Don't forget.

Okay, better center. Better focus. Better epicenter of all your work... it
converges on Jupyter Notebook and it converges on:

    ~/github/pipulate-center/pipulate-center.ipynb

Guess it doesn't get any more centered than that. I will never NOT be able to
find my current work. It's in experimental (not-scheduled (non-automated?))
mode in Jupyter Notebook-- so all the goodness of vim goes... goes...
short-circuit! Not @j... no, that's a new journal entry. It's just plain old j
at a Linux prompt that is the dot begging to be connected here. My true center
is not a single file. It's... 

    ~/github/pipulate-center/pipulate-center.ipynb
    ~/github/pipulate-center/pipulate-center.py

YES! Now eat some food while you work to reward yourself, and put
pipulate-center.py in place and git mv oldappname.ipynb to
pipulate-center.ipynb! Wow, my muscle-memory is going to be thanking me forever
for this one. That location on the file-system NOW IS MY CENTER! It is my
Window[1] in Windows 10 virtual screens. It is my Ctrl+1 in Google Chrome. Of
course, those are both zero-based index-systems, so I'm skipping zero for my
"home"-- and THAT'S BECAUSE true home is actually where you keep records of
this, your internal "navigation" voice. Don't let anyone fool you or be able to
(even in a technical capacity-wise) take it away from you. Carry your
universally applicable data-samurai capabilities around with you like an
attached body organ. Evolve it in-- and even that begins with practice.

The concept of Best Practice just rolled through my head like an alarm warning.
I think I'm having a subconscious sleeping on it moment, and had to get on the
record about something that's been bugging me. And I did. I got it out. I'm on
the record, and that should HELP ME FOCUS! One baby-step forward! Make that
query against SDK-ID's. That's urgent. Okay, I'm getting side-tracked by
automatically saving the accompanying .py files. Just capture HOW to do it from
the command line with the note that this can be come by:

    import nbconvert

...as a module IN NOTEBOOK, but I'll get to that later. Manually on-demand
right now, it's:

    jupyter nbconvert --to script pipulate-center.ipynb

Pshwew, okay, this is good 80/20-rule back-off. BACK THE F-OFF! SDK ID's!

First I always have to make sure my token's not expired. Always check! But not
now... haha! That's what gets me (and I'm sure tons of people) into trouble.
But that's not where to put my focus right now. Precious moments. Just solve
this SDK ID thing. Ugh! It's a worse situation than I thought. I have next
question into vendor.

3:00 PM meeting cancelled. Big weight off. Look carefully at how to do a
category performance look-up. Isn't there some way that doesn't require sdk
IDs?

I'm taking these lines out for now:

    %load_ext pycodestyle_magic
    %%pycodestyle   # Edit out leading hash for a pep8 scolding 



--------------------------------------------------------------------------------
## Wed May  9, 2018
### As with my old systems, I can't get away from a config tab

I've never had my instruments so finely tuned to be so well subject to
muscle-memory learning before. I think back to my Amiga-days and I was always
hobbled to a desk somewhere based on a non-laptop Amiga, which is really much
more static than I remember. I think my memory tricks me because I always used
to carry around my highly customized AmigaDOS boot disk that could take over
any Amiga and make it pretty much my own familiar environment. Amiga was much
more auto-configuring to varying peripherals in those days than most other
computers, so it was the rough equivalent of chroot'ing on Unix/Linux. To this
day its hard to imagine how well-familiar I got with all the general Unix API
abstractions by becoming familiar with the Amiga.

Now, the original message is the important thing. I got THAT message. Matter is
here to serve you; not work against you. If it feels like its working against
you, something's wrong. Now I've got matter working for me well for maybe the
first time in 20 or 30 years. It's been a long vast wasteland. If there was
stuff there that was love-worthy that I could have made a career and life on
before Python started to take off and become universal, I don't know what it
was. I always feel like I'm missing or missed the boat. I'm glad I'm staying
tuned-into what's going on on all the different mainstream platforms, or my old
dogma's would have made me miss what was going on with Microsoft.

Okay, so plan today out. I need a more methodical system to plan the day out. A
routine or algorithm. If my system needs a fresh restart, screen 1 in the
ribbon of Windows virtual screens is now always a Hyper.is terminal window
using the local "j" command from sbin to load my journals. It's journals plural
with an s because one is a private repo and one is theleakyjournal.md file in
the Pipulate repo. I "publish" excerpts merely by copying entries from the
private journal where I'm always writing and processing my thoughts over to the
public journal, which will get published when next I use the "g" command from
sbin to git commit and push all my must-be-regularly-updated systems. I can use
the g command as often as I like. The git messages aren't very informative, but
the reliable commits and pushing out of queued leakyjournal entries awaiting
publishing is comforting... g!

There's productive in the material sense, and there's productive in the
information sense. The information sense isn't real until it is expressed
(implemented) in the material sense. Until then, it is theoretical, foggy, and
only potential. Putting ideas to the test creates a rapid and vibrating
feedback loop, which is much like molding modeling clay into position. There's
not a lot of time between now and the 3:00 PM check-in meeting and I want to be
A LOT past where I am now. It's bliss NOT HAVING TO BLAST MUSIC IN MY EARS
ANYMORE TO CONCENTRATE! But put your concentration where your gratitude is.

Surprisingly simplified work-flow. Okay, lots of great progress but the values
in the spreadsheet aren't changed yet. Get the benchmarks for the category now. 

...

I should do some convention like those 3 dots to show some good amount of time
has passed. Very good meeting today. My feeling of non-progress was actually
great progress. Good topics discussed. The things that set me back a bit were
actually the perfect discussion points, and that config tab is fished and turns
the whole thing quite meta.

--------------------------------------------------------------------------------
## Mon May  7, 2018
### First Instance of Customized main_template.ipynb

Wow, okay I walked here FROM the Ferry station this morning. I don't even want
to say what time I got here, suffice to say I am clearly in a big-time
transition and I shouldn't feel bad about any of it. I'm incubating a new
generation type of skill whose value is beyond beyond. It will pay back time
and again... so long as this initial trick contains enough clues and compressed
easily consumed information, control, API-ness to keep each report as deeply
and extensively customized (lots of server-side pre-calculations AND lots of
columns) without overwhelming the user, and I think I have it right now here:

https://github.com/miklevin/Pipulate/blob/master/main_template.ipynb

This is really shaping up. There is a master template for Pipulate now. I
wonder if there's a way to attach the Google Sheet that's connected to the
spreadsheet into the git repository so that people could clone a Sheet template
without hitting a shared actual template at my actual account. The need to have
a sort of actual proprietary template in the picture is still a bit of a
weakness of the system, but if I went discounting the system based on Google
dependences, I wouldn't be here talking about it. Google dependencies are okay,
but in for a penny, in for a pound thinking is not.

The first command to be sure I'm accustomed to is sbin itself. Typing that
brings me into /usr/local/sbin and an ls can show me my whole inventory of
special commands (minus alias's from .bash_profile).

"a" is the temporary alias for the application.py I'm currently working on.
Whenever I have a revision in Jupyter Notebook that's stable enough to be put
into "column-tweaking" mode, I copy/paste from pipulate-center.ipynb (which I'm
running locally) to pipulate-center.py (which I'm running on a remote cloud
server). But until you're column-tweaking, it stays in Jupyter Notebook. Get
SOME VALUE coming back on the secondary function, then put on caching and
expand it to full number of rows on the response. Each time you do this both
"probes" to make sure I've got the correct numbers with right-looking data, but
also uses up 30 or whatever number of rows-per-second because I HAVE been shut
out. I have to touch the API CORRECTLY, which means cached. Which means a few
sample rows to "get a flavor" of the result-set data.

I got the latest squeeze, and so... and so... I adjust my work-flow a little
bit. Get that data back on the secondary query! Why should it be hard AT ALL?

Okay, everything you're doing now in your SLIGHTLY CUSTOMIZED version of
main_template.ipynb is good and correct. Even down to the incorrect secondary
query is good and correct. However, I don't have an environment where I can
EXPLORE the API more effectively. I'm still sort of terrified about using up
the row-calls. Oh, so make a row-number limit! Is that even viable with the
current approach? Oh! Is this where I put stride-by-step back in and just limit
at one step with a small stride? No rabbit holes, but yes, that does sound the
most appealing. Get some food and come back. Maybe take your whole everything
with you and work in the park. That sounds very appealing. It's also a very
solid test of "things". Then get back and show at the... no. The 3:00 PM is too
soon. Every moment counts and is precious. Liquid strike. Coffee, maybe the
Green or the Red plus a light sushi, then back here.

But get your brain working on a problem before you go.

--------------------------------------------------------------------------------
## Sat May  5, 2018
### Adi, Saturday and The Information by The Information by James Gleick

When I first started looking back at my technological past, in my 30s looking
at my 20s... or maybe in my 20s looking at my teens / whatever... pangs of
regrets for paths not taken and dead-end's taken usually was my first and gut
and I guess "truest" reaction. However, the longer I live and the deeper I feel
I know things, the more I appreciate those earlier experiences as a means to
help me triangulate in on better and better... uh... paths? Implementations?
Hardware/software nuanced platform combinations that will serve me well for 10,
20, lifetime's at a time. Life isn't really all that long in the grand scheme
of things, and its a shame the amount of your precious full-on attention
resources y'all gotta go burning on keeping up with the Joneses.js. That's like
the language you speak, English, changing so much mid-novel-writing that by the
time you finish, your opening chapters feel antiquated. Did Mozart and Picasso
have such problems with their tools and instruments? No! Effortless mastery
arises from a one-ness with your tools that only comes from the ness becoming
part of the one.

Yesterday's work was so, so, SOOOO critical to a viable future at the very
company I'm working at, despite the pressure to deliver yesterday. I do what
others don't (can't?) and to be undergoing the next phase of evolution
(speaking of my personal technological capabilities), there's no poorer choice
than to let myself get interrupted (again) on the verge of breakthroughs-- no
matter how much it looks like decipherable (un-trusted) nonsense to muggles. I
think part of my mission has got to be to just share all the wizarding with the
muggles in a way that they can start casting instant magic tricks. THAT's the
true function of main_template.ipynb. It's the path of potentially thousands of
folks to become technically proficient in a way that helps them during that
very same sit-down-and-learn (for the first time) session with Python... via
Pipulate. Generally, the stack goes:

Some Hardware / Some OS / ( Python & Browser) / Your Apps / I/O Devices / User

And that's circular, you see because the user has (or has access to) "Some
Hardware". This is going somewhere! Or maybe it's just circular. Relative
universe, remember? Who's to say that things moving in circles relative to each
other are not actually going somewhere on a grander scale? In fact, that's
exactly what appears to be going on. It's not just the expanding raisin bread,
but the raisins are usually actually clusters of raisins locked into mutual
spiraling corkscrewing orbits with each-other on their greater outwardly
expanding raisin-path. So don't feel bad if you feel locked into a pattern or a
rhythm, so long as you have compounding or accumulating effects of your efforts
day-to-day. Wheel-spinning or losing ground is the conceptual enemy here...
though of course like my Coleco Adam and Commodore Amiga days, who's to say
what experiences yield net positives versus net negatives? There's a lot of
unexpectedness and surprisingly high long-term value in things you long-ago
wrote off as wastes of time. No regreeeeeeets... Thunk/bounce. Give yourself
safety-nets.

Reality itself it's starting to appear (has appeared for a long time?) is just
another hardware/software platform combination, which like any hardware
platform, is in constant drift, flux, evolution, devolution, transition, change
or whatever. I guess it depends a bit on your perspective. I guess the "bit"
depends on your perspective.

Adi's awake. I'm hoping she gets a little more sleep. It's coming on 9:00 AM.
She didn't get to sleep until about 2:30 AM last night because I fell asleep
first and didn't get her to sleep. I'm sure this is a common enough problem and
most parents get their children to sleep before they go to sleep, but my place
is just so awesome when Adi gets here it's always happy party time. However,
now that she's easing awake, every 5 minutes it's Daaaaad... this latest time
was while I was giving Sammy his insulin injection and I told her I'd pay
attention to her when I could. Now I'm letting 5 or 10 minutes go by so she
learns I always respond to her, but not right away. I'm using exponential
backoff-- which I have to incorporate into Pipulate too! Haha! Adi's inability
to entertain herself even for an hour while she lazily wakes up is a developing
API-problem. I have to help her fix it on her side, and protect my sanity (or
at least calm non-stressed state (barely)) from my side. 

There are many echoes here I detect of patterns throughout my life which I am
determined to help Adi deal with better. Don't either BE an emotional bully OR
give in to them. A more practical alternative is, while never backing down from
a bully's antagonizing, neither do you walk or play into their traps. Instead,
dangle bait in their trap and when they take it, parry. Repeat. Dangle bait and
parry. Dangle, parry. So long as YOU'RE the one dangling the bait (whether the
bully actually knows it or not), then you're in control of the interaction.
This is basically the same scene as the man in the red sweater with Buck in
Call of The Wild.  Like Buck, bully's don't know that's what they're doing--
they're just responding to life, coping the only way they know to make staying
in the game a little more tolerable (for them).

So today's May 5th. That's something, right? Cinco de Mayo. Anyway from just
the weather itself, I can feel it. Confirmed that iFly is at 6:00 PM today.
Woot! NO RUSH! Totally open-ended day. Rachel sent me something about something
opening today. Maybe, but maybe just working on the place with Adi. It's
amazing how much disaster-area she can produce just from last evening when I
got her here to about 2:00 AM when I woke up and got her to sleep. She falls
asleep rather fast and easily at that point, and that is a definite up-side.
Getting her to bed by 11:00 PM on a night light that is nigh impossible.

Okay, it's around 2:00 PM. Adi's playing Monopoly with some of the other Urby
weekend kids. Weather fantastic. She was out kit flying with them and out on
her bike. This is the season I have to get her bike riding. I think she's about
ready for the type of freedom (and super powers) that could entail. I love her
being the "inside kid" who actually lives here when other neighborhood SI kids
come to visit. It's like Eloise, but with both parents completely engaged with
her at all times. Very nice. Even this is new. I think nicknaming my laptop
Carroll helped. Recently she asked Carol's a girl's name, right? And I'm
like... well, that would be a whole article in itself suffice to say I
explained both Lewis Carroll and Carroll O'Connor, which is especially
meaningful to me because my dad loved Carroll O'Connor. Again, heady stuff.
Sent her gifs of Archie and Edith singing Those Were The Days... oh, how I get
it. Those where the days.

This sort of weekend time typing... to myself while Adi's occupied and engaged
is novelty enough, but doing so when I'm completely in the zone on my work--
wow, I hardly know what to do with the next few moments. 2 Phones... 2 EC2
servers; 2nd one mine! Yeah, that'll lock me into that righteous feedback loop
for sure. And maybe use the Amazon Service for what you really want to.

I am gradually finding a new center. This is a useful thing. It's your center
that trickles out from your brain to your fingers and eyes and servers that
keeps things reliably happening, as if by you with effortless mastery, but
without you precisely having to be paying it your full-time attention. That's
AUTOMATION! A center is what issues commands out to sub-systems. A center is
the place where a critical enough mass of sub-systems are controlled as to call
it the main thing in charge. Even with that thinking, you'd get at least two
answers: the autonomous and subconscious sub-systems that keep your heart
beating and sugar-levels in the blood steady. We're a fairly complex chemical
reaction which could just have easily have run out of control and off the
tracks as to get to the end of the average turn-length successfully-- whatever
successfully means in this context; probably just alive.

I'm listing to: The Information again now. Actually, for the first time. This
is a book I bought as a Kindle edition, started reading, and never got far past
the African Singing Drums chapter. As interesting as the topic is to me even
Stigand, the patriotic archbishop of Canterbury found it advisable... Well, you
get the idea. It's MUCH easier when you buy the audio accompaniment. And I DO
mean accompaniment because on the android version, it highlights the sentence
you're on until the whole sentence is highlighted, then it starts highlighting
the next sentence as it stops on the last. It's a WONDERFUL read-along
effect... really better than the more 6 year old targeted Speak-a-Boo's. Adi's
growing up. 

I'm really going to try to put her to sleep to one of these audible's reading
along. Unfortunately, the Scarlett Johansson narrated Audible version doesn't
go along with any of the Kindle books (that I can see), because that would be
perfect, and we can't have perfect. Even the iPhone Kindle version, which
DOESN'T DO THE HIGHLIGHTING on the tiny-screen version I'm using doesn't do
that cool read-along highlighting, though it DOES flip the page along with the
narration as you flip the page. Correspondingly, as you flip pages the
narration goes right to where the page begins which is its whole own kind of
cool.

Okay wow it's 4:00 PM. Adi has had a full day of running around with the Urby
kids since around 10:00 AM when we came down for the smoothies. She's currently
playing with Josh's kids, catching upi with them finally. She's really too
much. It's amazing seeing her interact with his boys. She is so... well, Adi. I
think heartbreaker is a bit of an understatement for just the general effect
this kid is going to be able to produce in this world. I think I can give her
no greater gift than... than this. Urby is great. Staten Island is good. It's
5-boroughs plus, like I know I should. I have to be sure to instill into her a
bit of the suburban advantage, and that was completely impossible, especially
in Manhattan... even in Inwood. Thank God things are going the way they are.
I'm deep in operation recover, reorder and instill. Yup.

--------------------------------------------------------------------------------
## Fri May  4, 2018
### Pipulate Main Template: Getting the Bits to be Copy & Pasted Right

Today's journal entry is getting started at 5:00 AM. I am in total immersion in
a project. I am in the zone, actually producing fast in extreme coding style,
delivering as I go, even if it's the fleshing-it-out templates, which is
exactly what I'm doing. This is a crafty craft of template design, 'cause
you're going to have to copy and paste that code A LOT and live with it a long
time. And it's precisely those amazingly difficult to think-through little
details you never get around to thinking through which, if you stop to think
about it, makes all the difference-- precisely because no one else does. And so
let's do some of THAT thinking now, while there are no interruptions or
pressures of forward-progress meetings... shit. Okay, deep breath.

The "config-files" could be yet simpler. But the simpler I make them, the more
I'm pushing code "elsewhere" and making precisely the sort of cruddy framework
system that I abhor. No wonder everyone fell in love with ROR and I didn't,
because I'd been there and done that like 2 or 3 times before. I know what I
like and I don't. The field mapping is powerful, but there should be an
alternative column-naming system used in the dataframe than A through whatever
letters, because now we occasionally have a reliable row1 with field-mapping.
Those could become the column-names directly, and that should be an option of
using Pipulate (an argument?) so that report config-files become simpler. df
fieldnames will look like regular Pandas copy-paste examples, and that'd be
good for the system and long-term maintenance. And THAT'S in pipulate code...
ugh! Gotta do it. Now's the time.

Looking at the pipulate code. Wow, I'm a pretty smart guy, I have to hand it to
myself. I do want to take out the "guess-work" that's built into Pipulate now.
It's not up to this highly zoomed-in granularity of process to sort-of zoom-out
again of its own accord and make guesses about its own parameters (in our case,
a range). No, rather it's up to the outer-process that contains and controls it
like its own jackhammer to back up and move it to some new concrete, and such.
You get the picture. Our "spoken" English language is so strange adapted to
describe processes taking place in another language (Python). It goes something
like this:

The "pipulate" function that's used so much in cl, df = gs.pipulate(tab, rows,
cols) statements actually calls the pipulate cl_df_from_sheet() function, which
for the most part does all the heavy lifting throughout the pipulation process.
It could be used directly to do the pipulate input-statements instead of
gs.pipulate(), but what fun would that be making y'all have to remember
cl_df_from_sheet? It's very literal and pythonic and self-descriptive blah blah
blah, but terrible internal detail to expose. It's bad enough I've got to
populate TWO objects with it's output, but at least it gets y'all having to
understand

    something, about = 'tuple', 'assignment'

...and that's what I'm doing with:

    cl, df = function_returns_tuple()

...because I've gotta keep the cl object around to re-populate with any new
values existing in the mutated df. I say mutated df, because df is always a
pandas dataframe returned from cl_df_from_sheet on which you CAN do all sorts
of wonderful transformations, the leading candidate of which is always
df.apply() because it offloads all the work from pandas onto generic Python,
where my expertise increasingly resides. Generic python comes first.
Pandas-specific (and numpy-by-association) flavor of python comes second. We
(I) will be doing that sort of data munging, but for now I'm gonna be doing a
while lotta df.apply(function_name, axis=1)'s for you see THAT is the key trick
supported by Pandas that makes me able to abandon much of my old work.

That's the trick. THIS is where the sleight-of-hand is occurring that makes
Pandas something more than just another FORTRAN slight simplification to make
matrices algebra accessible to the lower-than-average scientific-mind, which is
me. It's one of the great ironies of science and technology that as your
science capacity goes up, down goes your tech capacity. There's just not enough
Gladwellian hours left over to become effortlessly proficient in two such
radically different fields. If you're gonna do some tech automation-- and
EVERYONE'S gonna need to do some tech automation someday-- then it may as well
be in a language you carry around in your head like a samurai sword ready to be
deployed just as swiftly and effectively as that particular nano-sharp tool.

Okay, think! Push this thing forward. The pay-off here is potentially huge. You
won't have to use all those field-mapping extra layers in your df statements.
Currently, every column maps to it's Excel-style letter: column 1 to A, 2 to B
and so on. The dl that gets returned by gs.pipulate is ALWAYS column-labeled as
such. But it need not be. By the time the pipulate function is called, we are
already sitting on top of a list of field-names as extracted by the
template-side of the pipulation process. The pipulation process is being split
between config-files and package-files. This bit of surgery is to push some
complexity from config-files onto the package.

    df[fm['name']] = df.apply(foo, axis=1)

...becomes:

    df['name'] = df.apply(foo, axis=1)

...if only I make gs.pipulate() support an optional columns list. Duh,
no-brainer. Go right in and do that now. The trick here is that because I
maintain Pipulate now in the PyPI index (the thing controlling what happens
when you pip install pipulate), I don't go through whole official
release-cycles as I iterate fast. I have no idea if I'm going to want the world
to be hit (and potentially interrupted by) my API-changes unless I'm really
happy with them after the work stabilizes and I'm happy with the results and
the particulars of the new interface-language I'm creating. We are always
creating or evolving or twisting our own languages into sorta new ones.

Shit, the sun's coming up. Nail this bad boy now! Go to def pipulate in
__init__.py... yep. Okay, a plan is taking shape. First of all, I need the
power of ALL my code execution contexts-- except interestingly enough the
scheduled one, which gets run really on the remote server primarily unless you
want to go through the trouble of reproducing the systemd service trick on your
local machine be it Windows, Mac or even Linux... good luck! No, the workflow
is solidifying in my mind, and 2 very important pillars are local while the 3rd
pillar is remote of this rapid development of scripts that optionally go 24x7
reliably scheduled and become templates for replication.

But here's how it all ties so beautifully together. We are eliminating flaky
copy/paste out of our life. Copy/paste between different code execution
contexts is a huge enemy to productivity. Avoid it at all cost. And so what
takes its place is... 

I have found my center. A directory named pipulate (by itself with no modifier)
is always a mistake. There is only pipulate-left, pipulate-right and
pipulate-center... in terms of all the official names I will make throughout
the system with:

- pipulate-left: Currently-running 24x7 scripts that should be "left" behind.
- pipulate-right: New and improved 24x7 scripts implemented the "right" way.
- pipulate-center: Rapidly iterating scripts you're getting right right now.

So there will be 3 services instead of 2. Left and right are always running.
It's center that you toggle on and off all the time. I will have yet another
round of file renaming and link-reference editing to do today, but don't have
to worry about that just yet. The urgent thing now is... what? Finishing the
removal of the extra field mapper.

Okay, I just achieved something I've been meaning and trying to for awhile. It
can be stated as:

- I'm working off of one primary main "local" machine first time in awhile.
- The "fixed locations" of things on this laptop are helping me work faster.
- Even though I have the hardware advantage again, I'm keeping old techniques.
- Everything to reproduce my work is also on Github which I push to often.
- In a pinch, I can still sit down almost anywhere and continue working.
- A copy of at least one piece of my work is always on a 24x7 (cloud) server.
- With VPN, I can "log into" that 24x7 always-running job from anywhere.
- I use gnu screen to step in and out of server-maintained terminal sessions.
- Gnu screen eliminates the need to grep log files to see what's going on.
- Log files are still being written for more precise debugging & diagnostics.
- The result is akin to virtual screens, but terminal-consoles on a server.
- The amount of special Unix/Linux you need to know is nominal and even fun.
- Logging into any of these virtual screens shows where the tasks are up to.
- Logging into any of these screens also provides an entertaining light show.
- I have a series of shortcuts in /usr/local/sbin to help navigate screens.
- Perhaps more than anything else, these sbin commands help muscle memory.
- Each 24x7 type job I run is started by a /etc/systemd/system/file.service
- Currently, only one systemd pipulate service is running (pipulate-left)
- Current work on pipulate-center updates every 15-seconds when toggled on.
- Very soon, pipulate-right will be running as a second 24x7 service.
- Reports that have undergone a "clean-up" move from left service to right.
- Reports that are currently undergoing rapid revision go in pipulate-center.
- The pipulate-center.service gets toggled-on only during worksessions.
- My pipulate repository itself from github is in pipdev for development work.
- Any directory just named pipulate aside from what's in pipdev is a mistake.
- Directories named pipulate-left, pipulate-right or pipulate-center are fine.
- These folders house only your arbitrarily named python pipulate config files.
- Most people other than me will have pip installed pipulate (not clone repo).
- This "frees up" any new folders you create to be your own job or task repos.
- Job repos can be .py files but can just as easily be iPython .ipynb's.
- Jobs in pipulate-center frequently start out as Jupyter Notebooks.
- Jobs being rapidly revised are precisely the kind you want in git right away.
- These jobs are nothing more than arbitrary file.py, usually using pipulate.
- These arbitrarily named job files are each called that repo's scheduler file.
- Keep python scheduler filenames similar to their service like python-left.py.
- You can test a scheduler simply with python python-left.py.
- You can test individual jobs it calls simply with python job_file.py.
- If you don't want to pay for private github repos, you can use Bitbucket.

Pshwew! Pushed out a commit. The biggest thing now is... oh! Gotta remove field
mapping reference and see if it still works, haha!

Hot damn! I did it. I eliminated the need for the arbitrary field mapping in
scheduled pipulate jobs! This is huge. It means the pipulate config files are
going to read VERY MUCH like standard Python pandas code examples, and that's
going to go a LONG way. That's going to be the gift that keeps on giving back.

Wow, SO MUCH PROGRESS today. The config file is rapidly becoming beautiful, and
I'm also re-engaged in rapid iteration of the pipulate main package itself,
which is now in pipdev/pipulate/__init__.py.

Alright, things have settled down enough that I should grab for the real
secondary lookup data now. Pshwew! Git commit everything AGAIN and work a
generic template into the main pipulate repo.

Okay, I've banked that awesome main template in the main pipulate repo. That is
huge right there. What it means is that I know EXACTLY where to start from in
future projects, and I get to iterate off of that one template example
improving it over time, committing that one (and only one) template back into
the repo. Wow! I think I may set up my own Amazon EC2 instance this weekend.
This will accelerate at work if I have my own parallel personal projects going
on using all the same concepts that I've used over the years.

Tackle every little issue online. Continue using your Macs and Screenflow when
appropriate. Get more familiar with Techsmith Camtasia Studio as well. That'll
be something like try #5 for Camtasia over the years. Not a big winner when it
comes to being productive fast, the way ScreenFlow was. Oh well, I really have
to re-center myself on Windows 10 now with this awesome laptop, and maybe
things have improved. ScreenFlow captures my keyboard shortcuts which is a
pretty big deal with vim. Camtasia only captured a few choice keys (due to how
Windows works) when last I checked.

Okay, I've got my first version of a "main template" done for Pipulate. WOW! I
think I want to add my services to the repo. Nahhh, that's just a distraction--
especially until I have my own EC2 instance running (again).

--------------------------------------------------------------------------------
## Thu May  3, 2018
### Made "Left-to-Right" improving scripts into my service-naming convention

Okay a big part of really getting back into my work lately is that Windows is
not reprehensible, Mac is increasingly disappointing, and the Surface Book 2 is
the gift that keeps on giving. With the Linux subsystem and well thought out
sbin shortcuts to compensate for the fact you can't just use the ~/ directory
as you would on a pure Linux system, and you'll pretty soon be feeling you're
on the best Linux system money can buy-- at least, hardware-build-wise and how
well Windows snap around into fullscreen and nifty actually usable window
"panes". 

Yup, Microsoft got that right. Whatever Aerosnap evolved into...  reallll nice.
Yeah, almost Amiga-like in its window-navigating elegance. I can live with
Windows Key+left/right to move between virtual screens. A hardwired numerical
index like the Control key plus 0 through 9 like in Google Chrome but in
Windows virtual screens would be nice. Anyhoo, it's getting late on yesterday
and I already started today's journal. So much to think about and do.  So close
to so many things. Let's just nail this little thing that's been plaguing you
for awhile. 

Make main_template.ipynb NOT DEPENDENT on the common.py file, and progressively
move everything into the main template then figure out what to do with the
common components from there. Who knows, maybe common.py will come back, but I
think not. I think most of that belongs in pipulate.

Okay, it's the next morning and this is the best starting point I remember
myself being at in a long time. My overnight sleeping on it realization is that
the file naming conventions for the services is weak:

    - pipulate.py: the 24x7 mission critical scripts
    - pipulate2.py: the occasionally pumped-up to every 15-seconds scheduling

The concept of moving scripts "from left to right" isn't expressed here well
enough, neither is the stuff in "the now" (or the center between left & right),
so here goes another round of file-renaming... okay, finally done all that. Got
distracted by getting to know the new API better. One more Hail Mary before a
2:15 meeting. 1, 2, 3... 1? I have the category ID that I need!

Wow, what a day! Pshwew! Definitely living on the fault line, here. I'm
creating some very special Kung Fu that's going to have grand application and a
long shelf-life. It's replacing the place SQL occupied in my heart and soul,
along with almost every other of my generalized systems I've made in the past,
just generally getting subsumed to Python, totally aware that I'm still subject
to the Blub Paradox, but Pythonance is Bliss.

There was a lot of template work today. It was an excellent worksession showing
that no matter how simple and elegantly meaningful you can make a chart, all it
takes is one worksession to turn it into a difficult-to-maintain monstrosity.
All the little details around it have to be all the tighter, briefer, more
robust and less brittle so that when they want the 1001st variation,
potentially auto-scheduled, you're not ruined at this job. No matter what
pressure is being put on you, one wrong move now will end it more quickly than
not doing it right. So do it right. And quickly. It's 5:00 AM. Time to start
tomorrow's journal entry.

--------------------------------------------------------------------------------
## Wed May  2, 2018
### main_template.ipynb in the pipulate repo is born.

May 1, 2018 was a good day. I finally chased down that Standard Library cache
that I heard Raymond Hettinger (@raymondh) talk about once upon a time which
expires every 24 hours. I did this long-overdue and basic test:

	from functools import lru_cache as cache
	import time

	def func(*row, **kwargs):        
		raw_response = api(*row, **kwargs)        
		# Parse date from raw        
		return raw_response  

	#@cache()
	def api(*row, **kwargs):
		number = row[0]
		tld = row[1]
		start = kwargs['start']        
		end = kwargs['end']
		return number, tld, start, end, time.time()

	raw_response = func('foo', 'bar', 'spam', 'eggs', start='01-01-1970', end='02-01-1980')
	print(raw_response)

	time.sleep(1)

	raw_response = func('foo', 'bar', 'spam', 'eggs', start='01-01-1970', end='02-01-1980')
	print(raw_response)

...wow doing experiments like this (usually carried out in Jupyter Notebook
because you "feel free" to do so) can permanently change your view and
decisions moving forward. It's a game-changing piece of information that must
be recognized as such and incorporated into my everyday patterns far more-so
than it is today, which is pretty easy because I currently don't use lcu_cache
at all (#HEADSMACK!). Yeah, these head-smack moments that change your behavior
forever-forward are rare, but they make such a big difference that they must be
grasped onto and incorporated into your new workflow deliberately and through a
powerful compelling "spoken" narrative too-- such as the one I'm creating here.
Take this in: the response from any function you write can be CACHED
automatically so the function itself doesn't have to run again until the next
24-hour window occurs. Until then, all calls to that function get replied-to by
a sub-program that's living inside your program as a result of:

	from functools import lru_cache as cache

...by which ANY function you write and "decorate" with @cache() above the
function definition (the def keyword on the first line of the function), then
this other program steps in and takes control of all of your functions I/O...
because it is being called "through" the decorator function which can step in
and do whatever it likes to it.

The nuance that I ran into yesterday that set me back is the ambiguous syntax
that kicks-in, because we're also operating through (or calling our functions
FROM) the Pandas DataFrame.apply() method, which takes the names of functions
and invokes them, optionally passing in THE ENTIRE ROW'S (from the DataFrame in
the current row-processing iteration) data as if it were a list... or more
specifically, a traditional python *arg splat argument. The problem arises in
when you're nesting functions called this way because you can't do 2 *arg splat
arguments in a row in Python, and this is what appeared to be called for when
nesting functions called from pd.apply(). This is a classic case of not trying
to fight your findings, or even understand them deeply enough to have a nuanced
work-around that you'll always have to do mental gymnastics to remember. 

No, instead you want an Occom's Razor solution. You want the solution you will
intuitively and immediately and effortlessly come up with again every time you
think about the problem-- all else being equal, the simplest answer or solution
to a problem is probably the correct one. OCCOM'S RAZOR IS NOT SCIENCE! The
scientific method does not mandate that among many solutions that solve your
problem that the simplest one is somehow the most true or right one. All the
other once are actually just as true and right if it solves your stated problem
just as well. If it does but you're still for some reason angry, manybe you
should have stated the problem and its parameters and boundaries more clearly.
That's why we call the I/O here between functions ARGUMENTS. It's arguably one
of the most important issues in all of life, designing how API's work.

I now have all the power of SQL now but without SQL, thanks to Python Pandas.
That is to say, I can pull data in from many data-sources and treat them as if
they were now tables in a local SQL database installation and do all sorts of
table joins, concatenations, merges, correlations, vlookups, or choose whatever
word you want for joining data between tables. If the data doesn't closely
correlate, data science, models, normalization, blah blah blah. I try to stay
away from that world. Just pull data from sources where the rows will closely
correlate to each other and join on say URLs and keywords and such-- right? Am
I right or am I right? Is SEO the not the new canary in the coalmine, Data
Master by-fire survival test going into the era of Machine Learning? 

Are we SEOs not the ones that need to adapt first for this increasingly opaque
black-box world from which "they" can't keep us from looking at their blackbox
I/O, because we live in an analog world and must experience it through our
sensory eyes and ears. If humans are supposed to be able to see and interact
with the data, then it's also scan-able and scrape-able. And the data gathered
from such exercises will always fairly easily yield actionable (and quite
profitable) directional-predictions. While correlation does not mean causation,
it is the modern SEO Data Master's role to see the correlations and suggest
that they might to the various stakeholders who just may layer on the
domain-specific insights that nails some awesome shit down that nobody else
sees.

Okay, this sort of writing ferociously fuels me. I see what I'm doing and I
have deeper insight into my own "felt-through" intuitive actions. Figuring out
that lcu_cache is the thing I want and that it MUST be combined with df.apply()
in such a wall that all API-sub-calls are wrapped-and-cached... THESE are the
things that will make you work faster, more efficiently and effectively forever
forward. You always have to be making forward progress and be able to show it.
The problem here is showing it. Now I've got to use it to show it. You can't
let the whip-snapping, even based on your own progress/delivery time-estimates.
Hold yourself accountable to yourself. Do the right things for the right
reasons and you can't go wrong.

I'm actually in the office now, but from an actual work standpoint now, there's
no difference in the equipment I'm working on. This Surface Book 2 with the
office VPN going for that sort of work is becoming the new day-to-day norm for
me, thank goodness. The dynamic work-anywhere advantage (nomadic powers) with
the static planted-roots advantage (well-tapping powers). To have well-tapping
powers layered on top of a caravan platform built for nomads, then you have
something that is superpower amplifying, indeed. THAT'S what we're doing here,
and I haven't even seen that Infinity Stone movie yet, even though I was
writing about the infinity stones on the Internet on May 3, 2012:
http://mikelev.in/2012/05/yet-another-omnipotence-monologue-prelude-to-a-meeting/

Yet again, I predict what's going to be popular. Heed my words! Let's see...
that was 6 years ago. Not bad. What's coming up? Well, we're all going to be
pursuing the hardware (even if accessed through the cloud) to do some big-sized
machine learning projects. So, we're going to want neural hardware and lots and
lots of storage that can be used as super-fast key/value, hash/blob, name/value
or whatever name your own fast indexed-lookup vocabulary; same thing always
applies. Working with rigidly enforced relational database tabular
row-and-column heavily vendor-flavored infrastructure is on the decline. The
APIs are standardizing, and Python is a good place to be because it wraps or
soon-will wrap everything-- no question. Python won. Sorry Ruby, JavaScript,
Java, Blub and all you other programming folks. I make no ther arguments here,
but for telling you that you will see it play out over the next 8 years, haha!

But for the right-now's, for people who want to live on the bleeding edge with
today's fairly easily cobbled together tools MINUS the Machine Learning,
there's Mike Levin... hahaha! There's ML and there's !ML. Not-ML is important
for me, because my daughter has such a supremely awesome logo for herself
that's going to serve her so well in social media and life that I'm going to
have to sharpen up my own personal and online identity to stay shining as
bright as her. Otherwise, I'll lose her respect. It's a Call of The Wild thing.
I'm the man in the red sweater. Can't get Adi through the violence of the story
yet, but she's got to hear it sometime soon. Big-time lessons of life embedded
in that thing. Oh yeah, the story-telling and the narrative. Powerpoint sucks
and Jeff Bezos is right. We're telling stories, and this is mine in raw form.

Okay, now to do that extreme bit of coding that changes your professional
career forever forward. I've been stalling and delaying because it's... well,
it's the exact moment when the rubber hits the road. It's the collapse of the
wave-function. It's a probability-cloud of potential that has previously only
existed as close to pure information in my head. Despite that itself being a
physical process, we must consider it so complex as to be a tuning-instrument
from beyond. Even if it's not, the butterfly effect as applied to the virtual
particles of the quantum foam may as well make it so. We all exist trapped in a
pulsing orbiting rotation that looks like things like day and night... time for
that later. Pay attention to what you just somehow unaccountably know.

And what I somehow unaccountably know is that the solution to all my problems
comes from convention. And my developing convention principally consists of:

    import pipulate as gs
    import common as co
    import pandas as pd
    import numpy as np
	from functools import lru_cache as cache
    from logzero import logger, setup_logger
    from pyfiglet import figlet_format
    from colorama import Fore

I should work on eliminating the common import.

Okay, getting my screens in order:

- Screen 1: My 2 journals in a full-screen local vim session (shortcut: j)
- Screen 2: Full-screen Chrome browser, fully updated with my synced bookmarks
- Screen 3: Generic terminal window, local.
  - MikeL@LunderVand:/mnt/c/Users/mikle/github$
  - shortcut: github
- Screen 4: Generic terminal window, local.
  - MikeL@LunderVand:/mnt/c/Users/mikle/github$
  - shortcut: github
- Screen 5: Windows 10 desktop, left blank

### Screen 3: 

    Ctrl+Windows (while holding) Right, Right (to get there)
    Full-screen bash shell
    Type go into shell
    z (same as avove)
    Expected heartbeat seen in log file
    Ctrl+A, D (detaches from gnu screen session you just peeked at)

This satisfies me that the 24x7 pipulate service is running as it should. This
reminds me that I have to add logzero to my standard imports. While I'm at it,
I should add pyfiglet and colorama. I think I want to eliminate the need for
common.py. Everything in there either belongs in the "template.py" file or in
pipulate (no longer pipulate.py, interestingly, but now generally
pipdev/pipulate/__init__.py, which is a parallel install on my dev-system, but
which still is not the one REALLY being hit, if I have pip installed pipulate
on that system. It is therefore important to keep in mind that when I do a
development-cycle upgrade on pipulate and want it updated in PyPI, I actually
have to do a series of things that I should really put in an sbin script file,
but they are for posterity:

First, your ~/.pypirc must be in place with your login credentials for PyPI.

I'm using the Twine package from PyPI to do all this. It's really twine that
knows to look at .pypirc for the login credentials. You don't really need to do
this part for using Pipulate, but I'm documenting it for my own edification. If
you're doing development work on something that you maintain in PyPI (things
that pip install easily), then you have to pip install twine to make things
really easy. After twine and your .pypirc file are installed and in place, you
edit 2 files, but really only 1 of them has the significant stuff in it:
setup.py, which you edit to match your needs insert SEO here.

Okay, all the work to get to this point has been to come to THIS point. 

I must stop evading here by writing and exploring in the mental idea-world what
I'm doing and put it to practice "in real life" insofar as the way this stuff
runs on my laptop and on cloud servers is really "in real life". Punt that one
to the philosophers. 1, 2, 3... 1?

Finish the API function that generically hits the 3rd party API you're using.
Create the function that gets wrapped-and-cached. First we wrap. And in this
wrapping, we should be able to bring the "global" field-mapping object derived
from row1 into effect:

	import common as co        # wrap common.py into pipulate & tempalte
	import pipulate as gs
	import pandas as pd
	import numpy as np

	from functools import lru_cache as cache
	from logzero import logger, setup_logger
	from pyfiglet import figlet_format
	from colorama import Fore
	import time

	fm = {'name': 'A', 'number': 'B'}       #field mapping implied by row1

	@cache()
	def api(*args, **kwargs):
	   name = args[gs.aa(fm['name'])]
	   number = args[gs.aa(fm['number'])]
	   start = kwargs['start']
	   end = kwargs['end']
	   return name, number, start, end, time.time()


	def func(*row, **kwargs):
		raw_response = api(*row, **kwargs)
		# Parse date from raw
		return raw_response
		
	raw_response = func('foo', 'bar', 'spam', 'eggs', start='01-01-1970', end='02-01-1980')
	print(raw_response)

	time.sleep(1)

	raw_response = func('foo', 'bar', 'spam', 'eggs', start='01-01-1970', end='02-01-1980')
	print(raw_response)

Wow, that's friggn' it! There's some simplification and subtlety here. I'm
abandoning my old notion of passing an additional fixed-position argument(s)
here. I'm using the standard Python conventions of splatted arguments, and ONLY
splatted arguments. That means that I'm simulating what Pandas
DataFrame.apply() is doing to pass in a row of data as pandas would, simulating
the splat effect. So I have to actually USE the splat symbol (asterisk) on the
argument keyword "row" here, but won't actually have to when it's a pipulate
function proper. In other words, the asterisk will get removed in the
definition of the function named func, which is the "outer" function that gets
called by Panda's DataFrame.apply() method where panda's own API-inventing is
taking place and we really don't want to be guessing what it's doing.
Therefore, if we want to pass a bunch of stuff to the "inner" API-calling and
highly cache-able bit, we want to arrange our call to abide by:

    api(*some_list_object, **some_keywpord_object)

In this way WHENEVER we're doing something that may need to be a cached
function from within pipulate so that multi-column work can be accomplished
without fancy SQL-like pandas table manipulation, we want to allow a
cell-by-cell freely api-hitting processing to be occurring as if APIs had no
cost or speed limitations. Pull back a mountain of data and just use a little
bit pulled out of the large data object to fill in that one little cell you're
filling in on the GSheet-- noooo problem! Why? Because the request is cached
with lru_cache from the Python standard library, and all subsequent calls to
that API using the exact same parameters will get the exact same results, as
delivered by lru_cache as imported above.

And in the end, this makes ALL THE DIFFERENCE!

It's all going to be pulled-in according to the standard Python(ic) *args or
**kwargs convention, and THAT'S HUGE AND I NEED TO INTERNALIZE WHAT I'M SAYING
in order to take the next step and live with it for maybe years or even the
rest of my life if this thing caches on. This is the banned Magic The Gathering
card move I'm designing. This is the information Samurai Ninja Kung Fu right
here. The beautiful part is in keeping it simple and leaning into the strenghts
of the tools so... so lots of things better expressed in code. Most
importantly, eveything you're planning to cache must be exressed argument-wise
very much like this:

    def pipulate_function(row, *args, **kwargs):
        # The Pandas DataFrame.apply() method is going to run this function.
        # row will contain the data of each row of dataframe.
        # args is a list of whatever you pass as list after row on function call.
        # kwargs is dict of remining name/val pairs passed on function call.
        # It's as if args were *row, *args, **kwargs, but that's bad syntax.
        # So when THIS function calls NEXT NESTED FUNCTION:

...Okay, I brought it all into Jupyter Notebook to work out the space collision
of the "row" and the "*args" concepts. They are the same thing on the back, but
not through the incompatible APIs of Python and raw splatting syntax. So you
have to ADD row and *args in the function! Here's what I have, and which I'm
very pleased with. I'm going to ad a gs.ab() method to pipulate so I don't have
to keep subtracting 1 for the zero-based index.

	import common as co        # wrap common.py into pipulate & tempalte
	import pipulate as gs
	import pandas as pd
	import numpy as np

	from functools import lru_cache as cache
	from logzero import logger, setup_logger
	from pyfiglet import figlet_format
	from colorama import Fore
	import time

	fm = {'name': 'A', 'number': 'B', 'id': 'C', 'group': 'D'}          #field mapping implied by row1
	row = ['My Name', 'My Number', 'My ID', 'My Group']
	args = ['one', 'two']

	@cache()
	def api(*args, **kwargs):
	   name = args[gs.aa(fm['name'])-1]
	   number = args[gs.aa(fm['number'])-1]
	   id = args[gs.aa(fm['id'])-1]
	   group = args[gs.aa(fm['group'])-1]
	   start = kwargs['start']
	   end = kwargs['end']
	   return name, number, id, group, start, end, time.time()


	def func(row, *args, **kwargs):
		args = [row] + list(args)
		raw_response = api(*args, **kwargs)
		# Parse date from raw
		return raw_response
		
	raw_response = func(*row, start='01-01-1970', end='02-01-1980')
	print(raw_response)

	time.sleep(1)

	raw_response = func(*row, start='01-01-1970', end='02-01-1980')
	print(raw_response)

Okay, and actually DO that revision to pipulate. And when you do, do something
in the sbin/g program to make sure that the pipsync.py that exists inside this
repo which uses pipdev/pipulate/__index__.py, but as pipsync.py in its own
local directory. Ugh, I know there should be better ways here, but this is how
I'm going to do it for now. It will keep me from having to push lots of
versions in PyPI on the bright side-- just git commit/pushes will do. Done.
Okay... okay... one more bathroom break. One Dr. Pepper. Then the moment we've
all been waiting for, just in time for a 2:00 PM meeting! I have less than one
hour to pull this revision to my workflow miracle out of my butt... and I'm
going to do it! 1, 2, 3... 1?

Okay, I got so close but rate quota denied... shit! Sent them an email to find
out how long I have to wait. I'm impatient and keep hitting the API, but that
may push back the counter. Must stop! Take breather. You earned it. This is a
HUGE step forward, not only on these reports but on your career.

Consider the 365 sheet pulse sheet.

Pipulate 2018 is a good name for a sheet with 365 ticked off cells. Maybe 730
cells: one to show successful script-entry and one to show successful
script-exit at least once for that day. Maybe a counter for how many times the
script was restarted. There should only be one restart/day and AFTER that there
should be a one successful scheduled event for that day recorded at the
beginning of the script (day) and one successful event recorded for the end of
the day (just before reboot). This is a separate confidence-building Pipulate
script you can make that everything else runs RELATIVE TO which you could work
on while you're waiting for the quota to expire.

Okay, doesn't look like that quota is going to clear before I leave today.
Bummer. Approach the API with caution tomorrow, but wow, what progress! 

Not often, but every once in awhile work doesn't feel like work. All too often,
work feels oh too much like work, because you got yourself into a bargain and
now you have to fulfill your end of the bargain to get your paycheck, and that
somehow leaches the pure animal fun out of it, like when you're out hunting on
your own and living or dying by your own wits. That's when you really feel
alive. But the modern clock-punching regimentarium. The feeling of despair is
when someone else, some sort of middle-man, is profiting too much by siphoning
off your margin. Some call that the Pareto Principle of Wealth Distribution. I
call it human nature. To punch a clock and find the joy in work is a precious
thing. If you find it, appreciate it. You have a special sort of employer who
sees the benefit of letting you love what you do.

Okay, time to pay them back for letting me feel the love. It's honestly still
only 10:30 PM, and I'm done with a very short Adi call and I walked all the way
home from 28 West 28th Street, minus the bit on the SI Ferry of course. But it
was glorious. The walk was glorious. This time I passed close to the Brooklyn
Bridge. I work walking distance from where I live, minus the ferry of course.
Wow! I think I'm really starting to feel being a New Yorker. It takes 10 years.

Okay... back to seminal writing. It was all expressed in code, currently in the
pipulate repo. Time to publish THIS and get to sleep.

--------------------------------------------------------------------------------
## Tue May  1, 2018
### Combining lcu_cache with pd.apply()... brilliant!

Wow, what a day yesterday and so far today. Real birth of a non-system system
here. Let me tell you what I'm doing and why this is one of those rare
undiscovered yet meaningful narratives going on right now on the Internet. I've
developed and adopted and used too many systems that have let me down, my own
included, to let myself get caught into the overly-specialized system-building
trap. No, no, no! The point is just to be effortlessly expressive in language
of your choice, which in my case happens to be Python. And in what contexts can
you run Python? In the context of a generic Internet-connected Linux server is
where our story begins. And by all that, I mean a typical Raspberry Pi or
Amazon EC2 or other hardware or cloud instance of something someone'll sell you
as a reliably Linux-running Net-connected (or connectable) machine. Kapish?

Fast-forward to you having it, being able to log into it through an
old-fashioned command line window running terminal software, so you're typing
into some remote machine instead of seeing it as a graphical point-and-click
desktop. You're comfortable enough now to copy and paste text-files around
using commands like sudo, cd and cp. You create files from scratch in
/usr/local/sbin to make your life much simpler and know you have to sudo vim
the filename to get started and sudo chmod +x the file afterwards. But once you
have, you've non-customized customized the operating system. We all have the
write to write our own aliases, shortcuts and macros. But if we keep all those
to simple, easy-to-read commands that you would otherwise know anyway, how
fragile could this really be? Rapidly re-create-able customization on any
platform is the best kind. Copying your files around in a private github repo,
if even just for copy-paste example template code in the future, is best.

This type of customization will endure all types of disruption, so like editing
your ~/.vimrc, ~/.bash_profile and /etc/systemd/system/pipulate.service and
other key files that turn a generic Linux box provided to you into a slick
responding to your age-old muscle memory as if it were you own personal
fine-tuned instrument. Without your config-files and preferences, you are
merely just a highly competent speed demon minus your tricked-out tricks. Oh,
did I mention .bash_login? Yeah, even though p2ss is a file in sbin, the way I
edit pp to it is through the alias command in my .bash_profile. Okay, okay
enough verbalizing things. Do some deep intuiting and doing. Make today by 3
another special time. THIS is how to do it. THIS is sane pacing. Big steps
forward!

I think something's wrong in the existing scheduling routine. I'm getting
aggressive now about cleaning up pipulate.py (now that I've renamed the old
name to pipulate, I take it personal, haha!). I'm also cleaning in the greater
repo folder that it currently lives in that's full of older scripts that I've
scheduled under the new system. There's nothing new about this system except
for me pointing out how easy it is to use it for just about the most common use
case all of use tech jockey jack-of-all-trade type folks repurposing ourselves
yet again need to be mastering: scheduled tasks like it's no big.

So, I've scheduled tasks like its no big. I've got 2 pipulate services, named
pipulate.service and pipulate2.service, respectively. That's because the first
instance actually is special. It doesn't need to be thought about with proper
array numbering, so it's not going to be. The pipulate.service contains
everything that's been "promoted" to the 24x7 intended uptime routine. Other
stuff where rapid iteration development is going to occur gets put in
pipulate2.service, and so on. You can easily extend this system as far as you'd
like. Each services calls via a bash command like this:

    ExecStart=/usr/bin/screen -dmS pipulate /home/ubuntu/py35/bin/python /home/ubuntu/scheduler/pipulate.py

This looks so long just because of all the absolute path names, but
understanding these paths lets you understand A LOT about the Unix/Linux (*nix
in general) operating systems. It's about the same as:

    ExecStart=screen -dmS pipulate python pipulate.py

If it weren't going through the gnu screen command to get the desired
log-in-able terminal session I desire for oversight and viewing of the log file
without looking at log files (you can see the echoed command-line output from
the log program), then the command would look about like:

    python pipulate.py

So you see, with all this work all we're really doing is getting the
pipulate.py program to run 24x7 by virtue of being started by the Linux systemd
service manager, but with the added bonus that you can "log into" these running
scripts and watch it run mid-run. And everything is always mid-run, because
it's always running. I schedule one reboot per day to occur... merely by
scheduling the exiting of the pipulate.py program at a certain time of day,
because the systemd respawner will immediately run it again, by which time that
scheduled moment has passed and won't happen again until another 24 hours.

Why reboot nightly like this at all? You go to sleep at night, don't you? Well,
it's only courteous to allow your machine friend that is working so tirelessly
hard for you to have a break, clear its mind, and start fresh and renewed each
morning just like you do. Fortunately, an Amazon EC2 instance doesn't need as
much REM sleep as you do, so a simple restarting of the Python script should be
enough. Chances are greater that your code needs the nightly reboot than the
hosting Linux machine itself (we can reboot that once a month or so).

Ugh, okay with this muscle memory capability, you have to use it. It's use to
to have it and have it by using it. So get using it...

But not so fast. Big future problems fixed in a BIG WAY now... right now,
because it fixes the problem you immediately face. It's the old row problem
again. But that shouldn't be a problem. I should be able to have a certain
symmetry to how columns are populated. Multiple columns in a a "row" value
assignemnt should be able to be splatted in a typically Pythonic correlated
fashion with a data object (return-value of a function or pd.apply() method).
This is a MUCH MORE ELEGANT approach than simply using a cache for subsequent
calls. The standard library cache that Raymond Hettinger talks about by the way
is (and I should STILL use it soon):

https://stackoverflow.com/questions/1427255/is-there-a-python-caching-library

And it really appears to be this simple:

    from functools import lru_cache as cache

    @cache()
    def f(x):
        return x*x

    for x in range(20):
        print(f(x))

    for x in range(20):
        print(f(x))

Hmmm. Okay, let me look into what splatting return values from a single
function across a row looks like. Read my own Pipulate documentation, haha!

I'm going to have to do a good cleanup of my scheduler directory soon. It got
messy from working fast and furious, but it's evolving into my master
scheduling directory-- for the Python files associated with BOTH systemd
services. Keeping it all in one folder (repo) but split across 2 schedulers (a
running instance each of pipulate.py and pipulate2.py) allows you to reuse
common resources across schedulers without dealing with fancy path issues of
going "up and over" into the other repo's folder. No, keeping everything in one
private Github repo (or Bitbucket or your own git repo server / whatever so
long as it's distributed revision control) is the way to keep scheduling
scripts short and understandable.

Mastering an API is sometimes about perfect alignments and mastering that
alignment. The above-described standard library lru_caching system is
incredibly powerful. I do believe I'm living in the incredibly sweet spot that
people describe still as "a script". We are not really going to be making
programs, as such. I mean, I guess they would qualify as programs, but hmmm.
No, they're more like configuration files for... for the system. The
non-system. So, what system then? I guess the system is Python, and you have to
think of it as just sort of an interpreter to your configuration file. You're
configuring the Python interpreter to act a certain way... to knit fabric or to
play a tune. All the same stuff. I'm just being a bit clearer in my head about
the context in which my automation-code is running. I'm steadily squeezing a
tube of tooth paste. You really must squeeze, but you mustn't hammer. A script.

I am at the edge of known space in the noosphere. Today is significant because
I'm about to test how well the lru_cache decorator from the Python Standard
Library works with the Pandas DataFrame.apply() method. This is a pretty big
friggin' deal for me, because it answers a problem that's been plaguing me on
and off in one way or another for years. And that is, what is the proper way to
populate multi-column output in Google Sheets from an single API-call, when the
system is tooled around df.apply() which is going to try to invoke the function
once per cell; VERY EXPENSIVE from a hitting-the-api standpoint if that's what
the function does every time its invoked, and its invoked on every cell. This
becomes particularly wasteful if what you're doing is just fetching a different
column out of a dataset that each time that contains ALL your answers, and you
really could just grab it all there and... well, and then what is always the
question.

Traditional lines of reasoning at this point and in my experience lead to
unreasonable convolutions that I will not pursue anymore. However, an every
24-hours auto-expiring decorator cache provided by the Python Standard Library
so that subsequent calls after the first column encountered are actually
pulling data from the cache and not the API... well, that I can get into.
Goodbye unnecessarily complex column-manipulations and table-joins. I'm just
gonna pipulate you row-by-row knowing I can economically reuse just-fetched
data so long as the cache decorated function is invoked with identical
arguments again... and that means function wrappers AGAIN. Ugh! Okay, that
part's gotta be part of my convention. Unclear as to whether I'll use
decorators myself or just stupid nesting.

Okay, so this is where the rubber hits the road. Shit, I gotta do it. Okay,
okay. Here's the template for a Pipulate function that covers all the argument
possibilities.

	df['c'] = df.apply(func, axis=1, args=('two', 'peas'),
					   start='2018-01-01', end='2018-01-31')

	def func(row, *args):
		number = row[0]
		tld = row[1]
		start = kwargs['start']
		end = kwargs['end']
		arg1 = args[0]
		arg2 = args[1]
		# do stuff here
		return stuff

The question at-hand is that if you decorate such a function thus:

    from functools import lru_cache as cache

    @cache()
	df['c'] = df.apply(func, axis=1, args=('two', 'peas'),
					   start='2018-01-01', end='2018-01-31')

	def func(row, *args):
		number = row[0]
		tld = row[1]
		start = kwargs['start']
		end = kwargs['end']
		arg1 = args[0]
		arg2 = args[1]
		# do stuff here
		return stuff

...and you invoked the func function with identical parameters again, will it
indeed use the cached version and cut-off any attempt to access an external
resource again? Well, the catch-22 here is that if you invoke it identically,
then you're doing the same thing and it would result in a duplicate column.
That's where teh wrappers come-in. I need to write a generic api-hitting
function that gets called in different ways from wrapper functions that are not
themselves cached. This also does away with any concern as to whether or not
this is supported by the Pandas DataFrame.apply() method. It will be one level
deeper. So the new pattern looks:

	from functools import lru_cache as cache

	def func(row, *args, **kwargs):
		raw_response = api(row, args, kwargs)
		# Parse date from raw
		#return just_your_column

	@cache()
	def api(row, *args, **kwargs):
		number = row[0]
		tld = row[1]
		start = kwargs['start']
		end = kwargs['end']
		arg1 = args[0]
		arg2 = args[1]
		# Do stuff here
		#return raw_data

That's almost copy-paste testable right there in Jupyter Notebook. Let me do
so! Okay, but not quite. I don't want to go mixing the specialized Pandas
parameter passing where row is actually the same splat trick as *args, but you
can't do 2 splats like that in a row according to the Python API, so I've got
to normalize my splats before nesting them. The code that works looks like
this:

	from functools import lru_cache as cache
	import time

	def func(*row, **kwargs):        
		raw_response = api(*row, **kwargs)        
		# Parse date from raw        
		return raw_response  

	@cache()
	def api(*row, **kwargs):
		number = row[0]
		tld = row[1]
		start = kwargs['start']        
		end = kwargs['end']
		return number, tld, start, end, time.time()

	raw_response = func('foo', 'bar', 'spam', 'eggs', start='01-01-1970', end='02-01-1980')
	print(raw_response)

	time.sleep(1)

	raw_response = func('foo', 'bar', 'spam', 'eggs', start='01-01-1970', end='02-01-1980')
	print(raw_response)

With the cache enabled, the same time comes back twice. With the cache
disabled, the time comes back different every time. We can additionally view
the cache-use or clear it with these commands, respectively:

    api.cache_info()
    api.cache_clear()

This is glorious. 

--------------------------------------------------------------------------------
## Mon Apr 30, 2018
### Creation of Pipulation

Welcome ladies and gentlemen to the birth of the wizarding world. All around
you today you will find clues that everything imaginable to humans in on the
verge of coming into being, either virtual or real. Fairylands and wild flights
of fancy are all on the menu, so long as they are economically viable. Virtual
worlds such as World of Warcraft, Second Life and everything that's replaced
them in the modern age showed us that. Books like Verner Vinge's Rainbows End
and Neal Stephenson's Snowcrash and everything that's replaced them in the
modern age have shown us vivid visions of vivid visions. 

The new breed of computer interaction that is upon is is like the next step of
what happened with Star Trek communicators, which we have long-since
leapfrogged. Next-up is all the voice recognition and augmented realities.
When you're casting a spell with a vocal incantation, it will be your own
personal A.I.  agent listening to and responding to you. When you draw gestures
and symbols in the air, it will be that same intelligent agent watching your
augmented reality scribblings. 3D printed robots will provide your flying
drone-fairies and gated-utopia oasis built in whatever otherwise barren harsh
bleak landscapes, such as Kansas farmland, will be your Oz.

There is a certain amount of time between now and then when it won't be nearly
so easy from a natural human spoken-language perspective, or Minority Report
style air-swoosh gestures to bring sophisticated machine automation control to
the average person, education-wise as we know ourselves today to be. It's going
to take several Herculean baby-steps forward to get ourselves as a general
population to where most of us are as comfortable controlling and instructing
machines as we are bossing each other around. Most of the world in other words
is going to have an AI-dependency. They are going to be AI-dependent.

This will apply to everything from driving to typing to tying your own
shoelaces. Handwriting? Who needs it! And in many ways, this thinking is
correct. Progress and the gradual shifting and drifting of social norms
generation to generation could turn common-sense backwards in only about 4 or 5
generations, which is just long enough for everyone alive to no longer have any
living memory of the consequences of the mistakes of the past. Horror which was
once an up-close and personal thing becomes a distant, abstract, and no-longer
an automatic human-decency dissuasion against committing atrocity. The world
forgets to become outraged against genocides and such. That is our present
state, which as Jared Diamond points out (I believe because I have never really
read it) in his book Collapse. We're perched for a plunge.

The rest of this writing today deals with how to keep you from being sheep
according to a new methodology I am developing right here and now today. Things
like it may have existed before, but this particular implementation is mine.
It's called Pipulate and many of you have seen iterations of it in the past.
The coolest one was a Flash microwebserver that streamed a single page back at
you that carried it's entire ongoing I/O throughout the "pipulation" process.
It was awesome, but alas a dead-end because of GUI-issues. 

Mikey no likey front-end work. It's like hand-coding PostScript. No wonder it's
called JavaScript-- it's exactly in the tradition of a language nobody was
every intended to hand-code. It's no wonder all these CSS parsing tools exist
and all these sub-language framework .js libraries pop up like fleas. The
LISP-club is back in the form of The Full Webstack (du jour) movement, and it's
all a bit to arcane and scrap-and-rebuild competitive millennials there for me.
I've seen it and been there and done that a few too many times to let my
precious mapping-space in my brain for muscle-memories that must last for a
lifetime (or at least a career) to get muddled up with beauty contests and
horse races and the latest hardware platform nuanced details.

For those who don't understand what I mean by hardware details, it's all about
the user interface. Take touch-screens for example. Precisely how do they work
code-wise. What about multi-touch? Can you assume pinch-and-zoom? What is the
operating system supposed to do here versus what you're supposed to do
"manually" with your programming code? JavaScript has a lot of this, because
it's event-driven by design. While this may make it ideal for user-interface
design, this is precisely the part of coding that I really despise. I like the
"back end" or invisibly running part of coding. Insert random joke here.

Despite what labels you slap onto these two different types of coding, the
differences are as profound as introvert vs. extrovert... or whether WWF still
means World Wrestling Federation to you. The hardware/software combo that
constitutes the "complete" platform often have rabid fans... rabid fans who
remember their particular hardware that was popular as they were becoming aware
human beings from about age 6 to 16 as the good old days. This is the beginning
of your rosy reminiscence. Monday, Tuesday, Happy Days... groovin' bout tech
with you!

From around 18 to 25 you discover life is awesome but short. If you make it to
28 then in your 30s, hopefully you figure out who you are, what you're about,
and precisely what motivates you and where you "draw energy from" in life--
usually after having given it a few failed attempts. I'm in my late 40s now,
and I'm kinda sorta seeing that if you've made it this far, gone through a
life-altering adjustment or two to keep yourself sane, stabilized things enough
to STILL be thinking about the future, then you're in a position to do a bit of
that Steve Jobs-style Universe-pinging if you've still got it in you. 

The only thing that's different now is that suddenly, with that wee tiny bit of
extra capacity you have due to the nature of having done almost everything
"like that" 2 or 3 times before, when you're faced with new challenges, you can
create 2nd or 3rd generation solutions even just while the rest of the folks
are cluing in on the fact that there clearly should be such a thing in the
modern age as a Data Master. When they realize it and turn to see what a
datamaster should be, here they shall find this journal in the Pipulate
repository, and the seminal articles of the rise of datamastering will be
"discovered" by googling googlers... for you see, I am an SEO.

Today I've decided to life-hack myself into a compulsively addicted to data
datamaster. This is a bootstrapping trick. Once you do this to yourself, you
are deeply accountable to yourself and not off the hook... ever... until you
turn off your automations, disaster strikes, you stop paying your cloud bill,
or your dying days. Really, a properly put-in-place filename.service started
with systemctl enable should run for as long as the system its running on is
still there running. And whatever that thing is that's running will be under
your explicit control, right down to how often the operating system checks to
make sure it's still running. The OS has the responsibility to re-spawn it if
it's not running. Everything is else is up to you in whatever that thing is
that it's running.

And that thing it's running is a Python script that's actually intended to be
able to be running 24x7, but would actually be folly to do so because the world
is not a perfect place, and all machines need a little rest in the form of a
reboot. Nuke the place from orbit, it's the only way to be sure. Wow, I used to
think that quote was Nuke the place for morbid... ugh. Anyhoo, our first step
in our scheduled script is to set a nightly reboot. But I am actually against
the clock once again. I'm not publishing and pushing out these articles nearly
as much as I should. I'm doing my Universe-dinging here and nobody will know it
unless you announce it and push out and forward the narrative.

Okay, I am inspired by Intel's tick-tock model. They had some time-unit in mind
in which they SHOULD be able to produce such-and-such sort of advancements not
beyond their reach according to all their experience, and then hold themselves
accountable to that schedule. Additionally, the cycles of tick and tock
actually mean different things. Tick is a more aggressive and foundational
advancement while a tock cycle is a refinement and optimization cycle. Between
an aggressively culture-itized tick+tock rhythm a company like Intel, which
arguably didn't start out with the best IC-design templates in the world
none-the-less self-improved and self-re-invented such that even if it has to
turn a massive ship to compete with billions little ARM gnats, it can. And
that's an amazing thing.

So, my version of tick-tock, designed to hold MYSELF accountable to a likewise
aggressive, yet sanely sized baby-step advancement routine starts with creating
the routine. The routine is my new Pipulate generalized reporting system for
SEO and a plethora of other uses you will I expect find to put it to.

Everything begins with a login session to some remote machine running
somewhere. In my case, it's a company-provided Amazon EC2 instance. I'm pretty
sure I'm a "home" directory on some larger shared by the occasional
server-needing co-worker. I know this because when I log into that machine and
cd ~/ and then cd .. (one dir up) and ls (list files & folders), I see a bunch
of my co-workers names. I'm named ubuntu. I was the first default user when my
DevOps guy set up this environment (I think). Woot! 

As it turns out, I have my little helper commands that also serve as a sort of
documentation of my own work (reading the contents of your alias shortcuts)
spread between 2 directories: ~/ (aka home) and /usr/local/sbin. This is
interesting because I thought I was on my own dedicated virtual machine, but it
makes sense for them to put multiple users on the same machine. Just keep it in
mind, because naturally now we're timeshare-nested at least 2 degrees deep.
That EC2 server is partitioned out of the Amazon datacenter, and then within
that particular hardware of the EC2 instance (yes, there's real hardware there)
is further shared between whatever users you load on that system, because the
thing the EC2 instance is emulating is a Linux server, which itself is
multi-user. And the number of machines DevOps has to maintain goes down as
user-per-machine goes up. Don't let it bother you. Just keep it in mind. DevOps
folks who let you play with VMs on their budget because they trust you are at
the top of the cool-people column.

Okay, my special keyboard commands right now are:

sd: show all MY running services. It grep's on the word that is common to both
my scheduler.service files. I sd a lot to see if it's just the one (always)
running service or both. If both, I'm in the rapid-creation mode that I need to
create for myself right now, this instance. It's the fire under my ass that I
need. The other command is:

z2s: This STARTS the service that runs on a very rapid basis. Lock yourself
into that cycle and go. Pipulate the hell out of the rest of the time that you
have. You still may not be able to do it, but it really is just still 11:30 AM
and you started at 9:30 AM and you already whipped yourself up into this
frenzied let's make progress mode! Feel GOOD ABOUT YOUR YOURSELF and your
capabilities! Who else can do this? Who else can take this next step and lock
themselves into this new in the noosphere extreme coding technique and very
particular recipe I'm describing. Crackling energies. Lightning about to be
drawn down from the sky.

The things to remember are these:

1. You will have TWO scripts running under systemd from the outset.
2. The OS makes sure each of these scripts is running every 5 seconds.
3. These scripts are scheduler.py and scheduler2.py, respectively.
   - While these names are arbitrary, the repetition helps sbin commands.
4. If the Python scripts are continuously running, the OS does not interfere.
5. By convention, our python scripts use the PyPI schedule library.
6. By convention, we schedule a nightly exit of our Python script.
   - This ensures that we're working with a clean slate every 24-hours.
7. The scheduler2.py is set to be "aggressive" in its schedule-cycle
   - A report is set to update every 30-seconds to 2-minutes.
   - I'm choosing every 1-minute for today's exercise
   - I'm also making the log-file heartbeat be every 15-seconds
   - That's 4 beats to a bar. Good for muscle memory but not quite Johnny Cash.

This is about to be a magical 3 hours-- the complete germination of a new
system. First order of business: making sure you can optionally turn-off the
hitting of the "expensive" (i.e. non-Google) APIs... Okay, edited out the
actual hitting of the API. You must thing of the rest of my writing from this
point on over the next 3 hours just commentary. It is fast-and-furious, because
it is the birth of a new system, and I am working as much on intuition here as
reason, and it ain't no damn tutorial. If this works out, light will show the
way. Anyhoo, 1, 2, 3... 1! No question here. Edit the file scheduler2.py is
invoking every minute. No lack of clarity here. Deep breath. This is the last
moment of the pre-pipulate era. I'm about to do the first real session of what
I hereby coin pipulating. Now, make a light show!

First, we ALWAYS pipulate generally the same way from an initial template. All
we know is that this thing will be run, run and run again every minute, so make
every line of code you put down do its role, and do it immediately. And you
better sure as hell be sure you're taking baby-steps or you're about to have a
systemd respawning loop-the sign of pipulating being out of whack and an
adjustment to the process required. It's just a little Python code sitting in
any old filename.py file that you know Linux is going to keep running if you
don't. Don't let Linux have the chance!

Create the first-row system. If A1 contains the world map, then it's a field
mapping row that should be hidden. Right? This should be row 1 because then you
are always sure to have it above the first frozen row, which must by necessity
be 2. Do it.

Totally in the zone, and this is actually pretty amazing. I can actually "feel"
the fast iteration high feedback ad hoc and scheduled reports being the same
thing system coming into creation. I'll have to expose the git history at some
point. The key insight here is that because you're in a scheduler and you can
therefore pump up the schedule to every minute and get a real-time feedback
loop going on designing the report. This is just so critical on being what you
need to be at this company. After the report's designed, you cut down the
cycle.

Okay, this is the Oh Shit critical moment. I have a dataframe loading from the
sheet. I need to make it look just like a mock-up now. I'm making fabulous
progress. Code is being kept minimal, readable and the function self-evident at
a glance. Very nice. Now I've got to populate a data grid as a test.

And everything went well and the phone-call even went well. And then there was
the follow-up with the stakeholder.

Pshwew! Much of the rest of today went into creating the quick jumping-around
muscle memory /usr/local/sbin shortcuts. I basically applied much of what I was
doing on my local laptop (Carroll) to the remote EC2 cloud server. I also took
a lot of the shortcuts that resided IN THE REPO and thus created ambiguity
about when they worked and when they didn't based on what directory I was cd'd
into, and moved them all to sbin.

I additionally renamed what I've been referring to as scheduler.service and
scheduler2.service into pipulate.service and pipulate2.service, respectively.
That way, the following keyboard shortcuts in sbin do the following:

- p: Lists all running gnu screen sessions with pipulate in the name
- p2: Toggles on or off the pipulate2.service (pipulate.service always runs)
- z: Enters the gnu screen session named pipulate (always running)
- z2: Enters the gnu screen session named p2 if pipulate2.service is running.
- g: Git commits the latest schedule stuff and pushes to repository.
- l: Does screen -ls command to list all gnu screens.
- r: Reloads all daemons and specifically restarts pipulate.service
- r2: Only specifically restarts pipulate2.service (no daemon reload)
- ps: Start (or restart) pipulate.service
- pss: Stop pipulate.service (you don't often want to do this).
- p2s: Start (or restart) pipulate2.service
- p2ss: Stop pipulate2.service (you actually do this quite often).
- pp: Alias for p2ss because you do it quite often and is good vim humor.

And this leads to interesting patterns to wrap your head around. The 2 most
common things you'll want to do is p2 for a toggle or pp to explicitly turn it
off. I can see myself doing this a lot. I'm taking advantage of the short
1-letter command namespace that the patrons of Unix (and by extension, Linux)
so courteously left available to us; especially impressive considering how
short most of the commands like ls, cd, mv, rm and such really are. It wasn't
until PCs and DOS that ls became dir. Durrr. Anyhoo, that's all for today.
Muscle memory upon the morrow assured.

This is where things start to get all Samurai Ninja... or at least suburban
white belt Tae Kwon Do, if it's easier to believe. See you tomorrow.

--------------------------------------------------------------------------------
## Wed Apr 25, 2018
### Creating Your First /usr/local/sbin to show your non-existent service running.

Time to do this part as a public thing. I'm soft-launching Pipulate in PyPI.
That is, you can now pip install pipulate, and now it's time for me to get
started REALLY USING IT. I'm like using it for the really big projects now that
my career is based on, and there's a lot of trying and refactoring until I get
it right. It's a matter of shifting around the responsibility for things until
exactly the right things have exactly the right responsibilities such that all
jobs get carried out reliably and predictably and the oversight and constant
evolving, tweaking and swapping in and out of parts is allowed to occur with
ease and low-risk. The system should be designed to almost invite you in to
make it your own... just by creating a few text files and executing a few
commands. This is Genesis.

In the beginning, you got some generic Linux machine you can run like a
server-- that is to say, constantly. It doesn't need its own Internet
accessible IP like web publishing. It can live inside your firewall, so it
could be a NAS that you keep turned on all the time. A lot of people will end
up on a cloud server such as an Amazon EC2 instance of the sort that started
the whole Cloud movement. Regardless of the nature or location of the hardware
you're running, the main thing is that it supports the new systemd Linux system
service manager and scheduler. It's sort of like cron, but much easier to work
with. You just edit a few text files in a location where you'll have to sudo to
have write permissions. If what I just said intimidates you, stick to the
Jupyter Notebook stuff for now.

Okay, if you're still reading then the next step is to create TWO different
schedulers. Because there's always something running in your automated sequence
that's absolutely essential that it finishes running each morning, you have to
have two separate schedulers... one considered somewhat inviolate so that you
only add things to it that have proven themselves in the less-stable and
non-mission-critical scheduler. I think I've got to call these thing1 and
thing2. There has to be VERY STRONG nicknames surrounding this. You wouldn't
think so, but decisions like create the original base assumptions that are
going to color your entire experience with your own system for perhaps years to
come. You don't want to over-simplify or over-complicate. You've got to strike
that most-natural middle so that you can develop effective muscle memory around
it. This is important.

    /etc/system/systemd/thing1.service
    /etc/system/systemd/thing2.service

Thing 1 runs first. Thing 2 runs too. Okay, this will work. I've got internal
names I'm working with here, and it really doesn't matter what you choose. To
change it later you would just stop the service, disable the service, rename
the file, enable the "new" service and start the "new" service. See? Anyone
who's used the Windows Services manager stuff back in the Windows NT/2000 days
through a graphical user interface stopping and starting services, it's pretty
much the same thing as systemd under most modern Linuxes except that we're
interacting with systemd by making text-files that define the service and then
using the systemctl command to enable, disable, start and stop them. Start by
logging into your server and typing this command to see all the running
services:

    systemctl list-unit-files | grep enabled

Or if it scrolls past too fast:

    systemctl list-unit-files | grep enabled | less

This is classing Linux chaining together of commands to get your desired
effect. The output of systemctl is being fed to grep to filter for just the
lines containing "enabled" which is being fed into the program "less" which
lets you scroll forward and back through something that was otherwise scrolling
past too fast to read. Don't worry about not getting it all at first. Just type
that command to see all the stuff running like system services (or daemons) in
Linux. Any program you write in any language can be turned into a system
service merely by virtue of plopping a text-file in /etc/system/systemd/ with a
.service extension containing the details about when to start it and how often
to check that its still running, and it's a service. And THAT means that an
ALWAYS RUNNING PYTHON SCRIPT can be a service.

Now follow this: if that always-running Python script just so happens to be a
scheduler itself... well, now you have an OS-ensured running Python script
running. It only can't have bad syntax. But if your script flakes-out because
of some untrapped condition, it will respawn itself as fast as you like. I
generally do every 5 seconds. Of course this doesn't ensure your script is
running CORRECTLY-- only that it's still running.  If it craps out in under
5-seconds, then it will get caught in a run, crash, run-loop. Consequently a
way to tell that your script is running regularly and correctly all the way
through is foundational. A scheduling heartbeat is that you know you can get
into the habit of rallying around, perhaps in one and only one Google
Spreadsheet per Pipulate Server that you can always check in on...  easily and
from anywhere... because GSheets.

Technically, we will want TWO heartbeats running into perhaps the same Google
Doc-- but different tabs within the spreadsheet. We can have one sheet for all
Pipulate servers (independent schedulers / can be on same machine). I can't
believe it's already 12:30. I got in the paperwork for taking Adi to work
tomorrow. I hope it's not too late. I have to write my weekly report tonight.
Okay, let's get this down. It's not really about the automation so much
anymore. I wouldn't call it automation, so much as sanity. Okay, I want to make
sure that both scripts are running with an easy to execute command. I'm going
to start using /usr/local/sbin on the webserver when these commands are bash.
Otherwise, I'd have to do ./filename.sh every time I execute it out of the repo
location. First we make the sbin file:

    sudo vim /usr/local/sbin/sd

In vim, hitting "i" gets you into "insert mode". So, hit i and type this in. If
you get anything wrong, hit the Esc key, hit dd to delete the line, then hit i
and try again. Welcome to vim. In about 5 years, it'll all come natural and
actually be worth it.

    systemctl list-units --type=service --state=running | grep 'thing'

To save it, you now can hit [Esc]:wq[Enter]

That is to say, after you're done typing the command into vim, hitting the
Escape key gets you out of insert mode. Hitting the colon key gets you into ex
command-mode from which you issue the "write" command and hit Enter to make it
save and quit. If that was your first experience with vim, congratulations. If
you got through that successfully and the next few commands and make your first
sbin command to see if your service is running, then nothing can stop you. This
is like trial-by-fire for a Datamaster. If you can't set up a basic
Linux/Python scheduler under generic default Linux with just a few pip
installs, then this is not the field for you. After /usr/local/sbin/sd exists,
you want to give it the correct permissions. 

    sudo vim /usr/local/sbin/sd
    sudo chmod +x /usr/local/sbin/sd

Now anytime you connect to this server, you can just type sd and make sure that
your service is still running. Notice I left the .sh extension off, which is
just for rapid-typing convenience. Linux will recognize it as a bash file.

--------------------------------------------------------------------------------
## Tue Apr 17, 2018
### In The Beginning I Re-positioned myself as a Datamaster
#### Challenge a Samurai to Speed Chess

Just say no to Data Science! It's Data Master you want to be concerned with,
because who wants to be a scientist? Well... everyone, I should hope. So in a
final Hail Mary play of wanting to do something significant, I'm going to take
up Python Pandas as my new data samurai sword-- that is to say, a tool which I
can commit to muscle-memory that won't go and get its ass obsoleted in under
one measly decade. 

This is the part where I bore you with background and genesis of this stuff and
my reductionist of using it. But I'm not reductionist on words. I'm about to
ramble about state-of-mind and what it is to be human, and the perpetual battle
we're all locked-in between rule-enforcing static-thinkers (because that's all
they know because they were taught to confidently believe that's all there is
to know) like religious zealots and the CompSci elite priesthood that flocked
from punch-cards to Java (compressed story). I'm likely to piss a lot of people
off, but hey, if you're not acquiring a few enemies, you don't stand for
anything. 

I stand for Truth, Justice and the Golden Rule. You can have your way, like
nearly almost entirely so long as you're not too much of a freak, find others
like you that support you in and reinforce your odd reality, and get along just
fine, having adopted the Golden Rule-- in reverse, I might add. Do NOT do unto
others as you WOULD NOT have them do unto you. Otherwise, you're gonna have
some bad mojo doing the complete reverse of compounding advantage; eroding
advantage? Compounding disadvantage?

Anyhow, I've had the giant reset button of vendor-pivoting (responding to some
alleged competitive pressure ala .NET to Java) pressed on me more than my
fool-me-X-times threshold... which was an embarrassingly high value. I can be
fooled A LOT, apparently. TRS-80 to Coleco Adam to Commodore Amiga to Microsoft
IIS/SQL Server plus variously pfe/Edit Plus kept throwing away invaluable
keyboard shortcut and macro-writing skills text editors... ugh! It's painful
even just to think about. The only truly satisfying experience was the Amiga +
AREXX & Cygnus Editor (CED). Since then, I've been trying to piece together an
equally lovable small... uh... "stack"?

The answer is the nearly disruption-proof and nearly universally applicable to
any domain's problems Linux, Python, vim and git. It is for the most part both
your developer stack and your runtime production environment stack. And it
could all fit on a rather small USB keychain drive. And all that "sync'ing"
your critical information/data/configurations/whatever is done through git
using Github or Bitbucket as your repos-- unless you care to set up your own
repo on perhaps an EC2 or other generic cloud Linux instance. That's the point.
Pluming doesn't matter, so long as it's Linux... or maybe Unix (FreeBSD).

The giant reset button of platform obsolescence is your enemy. I'm talking you
deliberately and right here at this moment upon the reading of this very
article commit to taking up tech with 20-year lifespans AT LEAST and just for
starters. And for me, that's Linux, Python, vim and git. I told you why plenty
now (if you're one of my channel-dispersed 10-thousand-or-so followers), so now
I'm going to tell you HOW. NOW IS THE TIME TO TUNE IN. And it's not to the
exclusion of other tech. Quite the contrary, you won't win any
new-platform-killer-app jackpot race with this platform. Rather, it's going to
qualify you to be a universal plumber and electrician of the information-age.
Very Blue Collar, after awhile. It will be. It's not today.

THAT'S the opening I'm walking into. I want to show other people the way I've
found-- the way I'm typing this into vim right now on the Staten Island Ferry
with no net connection, totally comfortably knowing every word I type will be
published because of the "leaky journal" I'm currently now typing it into in
the main Pipulate branch... hahaha! Well, this is performance art as much as
anything, and it's about time. I'm good at this stuff, and I can make an
informal publishing system by "leaning into" the strengths of the tools I'm
using. This is the computing at 40,000 feet that Linus Torvalds would talk
about as one of the criteria for the git distributed revision control system he
created to take the place of the license-inhibited proprietary product the
Linux kernel had previously been based on. You walk into openings, such as I'm
doing now with helping to define the new breed of Data Master.

I'm often intuiting the next big thing. The list is actually pretty humiliating
that I didn't turn any of these insights into vast material wealth by this
time. I've always tied my material reward the expert practicing of skills...
which happen to take place unavoidably upon PLATFORMS. Hardware has always
mattered quite a bit more than people give it credit for, especially how the
particular hardware in your life during your 5 to 8 year old formative
circumstances predisposes your static-thinking habits. I'm aggressively
un-wiring dangerously anger-producing static-wired states that dance around
settling into my daughter's mind. I thankfully know how to dispel this sort or
anger-- through like almost a lifetime of dealing with it.

Perhaps teaching Adi what controlling your mind and your tools in a
Samurai-like fashion is really best. Poker face. Deep and deadly skills that
make others have to take what you say and do very seriously. Others WILL ALWAYS
take advantage of you and put you down and make you subservient on their
internal image of the social scale that they're mentally mapping you into--
naturally beneath them. They're static thinkers and are staged for disruption
ways that delightfully remind ourselves of who we really are, despite who we
like to think we are. There's a bit of anti-pattern mutation-trying Rocky
Balboa aspect to what I'm promoting. Make up for sheer cleverness by not dying
from your mistakes. Under-promise and over-deliver.

Mapping out "next steps"... self-navigating... requires contemplation,
engagement in the action, and sometimes "feeling out" your path and your way in
a way you can't intellectually do standing at a white-board. APIs have a "feel"
to them, and you've got to grab the reins and give them a few yanks. Even just
the authentication issues (if there are any) are quite telling about the
system. Many of the policies of the contract is exposed at this point. Do they
include or suggest the client library to use for authentication, if it's one of
the more complicated ones like OAuth2.

These days, decisions are even more muddled than they were back in the day.
When the term Web Master was emerging, most do-it-on-the-cheap folks went with
some form of the LAMP stack. That is to say, Linux, Apache, MySQL and PERL (and
later PHP or Python). Ruby was honorarily added to the P-languages of the LAMP
stack just in time for its importance to diminish dramatically by nginx
replacing Apache as the technorati's darling webserver, and Oracle's acquiring
of MySQL... and the rise of JavaScript on the server with node.js... yeah, that
about covers it. CSS. Full Web Stack new rockstar hotshots who also trade in
cryptocurrency. Uh yeah, not me. Methinks mefeels similar preparation for
sudden liquification of limestone bedrock sinkholes.

I was among the early wave of Webmasters, but missed LAMP in favor of the
Microsoft IIS/SQL Server route. I learned the advantages and nuances of
Transact-SQL and the SQLServer hardware on RAID-10 tweaked-out with magic
numbers that give better/cheaper/more-controlled performance than the (then)
cloud equivalent. Well, it's no longer that way, and new systems must rise to
prevalence and prevail while others fade onto their nuanced niche-y places and
my ways ascend as they ultimately must, given how their interfaces are
carefully delineated so as to permit the seeping-in of the accumulating
wins-over-time properties of exercise and practice.

It is in this muscle-memory promoting sprint that I'm bootstrapping a new
"non-system" system nearly from scratch. That is to say, the system is pure
Linux, Python, vim and git knit together into my muscle-memory samurai sword of
tech. And samurai swords are a bit different than other weapons. They're
designed to allow a decapitatingly efficient death-blow in a single
from-relaxed-state movement. THAT'S efficiency. THAT'S OPTIMIZATION. And that's
the 80/20-rule Pareto Curve, leaning into your tools' strengths, or
what-have-you. Don't ruin my happiness nor my child's childhood.

The concepts of both Kung Fu and Samurai keep coming up. Perhaps Ninja, but not
so much for me. Ninjas work in the shadows and are ambush-oriented. That's very
reptilian-- too much for me. I'm optimizing bipedal primate movements. You can
optimize your tools and movements to as well-known static state, such as your
opponent standing within a sword's reach of you, without any sort of
extraordinary armor or lifetime of training/skills. If you're within arm's
reach of a skillful Samurai, your life is at his discretion. But challenge a
Samurai to speed-chess, he'll fall apart.

In the beginning, you didn't know nuddin'. Then you warmed up your brain.
Perhaps the way I'm going to do things isn't exactly the way I think I'm going
to be doing things. The goal here is to do something very advanced without
hardly doing anything at all. Webmastering wouldn't really have become so
popular back in the day if it was really all that hard. The trick is it
requires keeping 10 or 20 things straight in your head at the same time whereas
most people have a hard time with even just 3.

But don't fear! To keep it doable, we're going to start out VERY non-ambitious.
Basically, we'll be making a Linux-launched but Python managed scheduler...
usually of other Python tasks, in turn. And by Python tasks, I mean the
scheduled running of .py files running just as if you ran a script like:

    python file.py

...but from a scheduler! It's EASIER than old LAMP web publishing and such.
You're running scripts you control when you want to run them, and get to space
out all of your tasks like a game of tetris to keep your hardware running at or
near capacity, churning out reports that it has no responsibility for any of
the back-end database stuff. It's just an API-monkey in the middle, carrying
out your commands, leveraging the generic Linux/Python.

So you do something in Jupyter Notebook. It's good. What next? Well you sit
there and "press the button" every day... hahaha! Very Lost.  Guess that's a
recurring topic in history, as it should be. True automation is an illusion. Or
at least, lasting automation is an illusion. Everything takes tender love and
care to keep working. A process neglected is a process likely decaying. And
hence, we embrace scrap and rebuild. Only X-number of reports are in-play, so
why not let Y-decay? That's the scrap-end of the scrap-and-rebuild inchworm of
progress.

The datamaster approaches his work with a scrap-and-rebuild mentality. This can
only work when building is something you do as easily as speaking or writing.

My problem of late is that I've let a number of reports that have an increasing
number of eyeballs on them and importance in the company creep out of control
complexity-wise. There's a lot to have to remember and keep control of
moving-parts-wise. And by that, I mean caches, archived data-pulls, changing
APIs and the like. And this is all on just one EC2 instance and no "back-end"
database to speak of, except for the occasional archiving of .csv files on
Google Drive, local caches to lower unnecessary API-requerying, and Google
Sheets itself. And so I have a bunch of python files that are being run from a
master-script, which is itself being invoked from the default Linux scheduler
and service manager called systemd.

Each report has its own unique problems now. They're nothing I'm going to solve
in a day, and I may end up scrap-and-rebuilding them soon anyway. So, don't put
any craft into the construction of the report itself, except insofar as mastery
of the Python Pandas library and basic spreadsheet formatting skills that
should eventually come as naturally to you as anything else. Don't bother
delving into the in-sheet Excel or AppScript formulas or scripts. There's
nothing you can accomplish there that isn't accomplished better on the
back-end. Just use GSheet as a presentation-layer-- and on rare occasions, for
configuration and setting values.

So, our story starts a bit like life itself. There is barely even any
self-awareness. You can't yet put 2 & 2 together as such. However, you can
start discovering and making use of a series of assertions, which once
discovered, are the first static hook out there you can hang your hat on, so to
speak. Uh oh, American idioms. Sheesh! Well, I am what I am, and so here we go.

These very first proto-steps are documented already either here in this journal
or in the associated README.rst. My intention is that over time I will ramble
on unbearably here, while I continuously refine and improve that file over
there. And so, get yourself an EC2 or something like it. I go with Amazon,
because that's what my DevOps Peeps gave me, so that's what I use. You could do
worse, and it is good to know the Amazon way. Though in the way a Datamaster
starts out, really almost all decent Linux's that have systemd and a good
software repository is good enough and equal for our purposes. The trick is to
think generic here, and you need a generic Linux that runs 24x7 on your behalf,
and you need to be able to log into it with what's commonly known as a terminal
program, like that built into Macs and that added with the Linux Bash subsystem
for Windows. So that means ALL mainstream platforms now offer a native
text-based terminal with an ssh program. Your devops folks will likely give you
your key-file that you use on the ssh command to connect to your EC2 instead of
a password. This is very common and is the company-controlled EC2 context in
which I run. I AM NOT web publishing. This does not run any webserver or even
web services software. It just runs scheduled scripts.

Okay, so HOW does it run those scheduled scripts? Oh yes! Okay, copy the
essentials from elsewhere in this very journal. 

    /etc/system/systemd/keeprunning.service

...which contains:

    [Unit]
    Description=This keeps the Python program the_schedule.py running.

    [Service]
    Type=forking
    Restart=always
    RestartSec=5
    User=ubuntu
    Group=ubuntu
    WorkingDirectory=/home/ubuntu/repo/
    ExecStart=/usr/bin/screen -dmS screenname /home/ubuntu/py35/bin/python /home/ubuntu/repo/the_schedule.py
    StandardOutput=syslog
    StandardError=syslog

    [Install]
    WantedBy=multi-user.target

And here's the variety of commands that enable and start the service:

    sudo systemctl enable keeprunning.service
    sudo systemctl start keeprunning.service

And after edits are made, you can lest the enabled services and reload them.

    systemctl list-unit-files | grep enabled
    sudo systemctl daemon-reload

--------------------------------------------------------------------------------
## Fri Apr 13, 2018
### And Now For Something Completely Different

I desperately need "a system". I need a secret weapon... always. Once upon a
time, it was The Amiga Computer from Commodore, but really from the same
hardware wizard as who brought you the Atari 2600, 400/800-- proprietary shit.
That hardware wizard left Atari and funded by Dentists designed the most
important piece of visionary future-predicting/shaping piece of hardware
unrivaled until Apple showed the world how cool mobile could be. Nothing
interesting came in between, and the desktop "GUI" interface did nothing but
teach a generation of people how to rely on the must static of devices-- a
piece of soap on a string-- as a pointing-device. Sheesh!

There's nothing wrong with the text-based type-in computer interface as
encountered time and again as "the terminal" or the command-line interface (as
we old Amiga-hat's would say). It's just that Steve Jobs needed a conceptual
enemy to peddle soap-on-a-string, and he chose the old DOS interface-- lumping
into it the much more powerful, respectable, and deeply emotionally intuited I
would like to add. Jokes abound about Unix standing for eunuch, which it is.
However you have to understand that in the context of the thing it's chopping
the gonads off of is Multics, an AT&T/GE overlord time-sharing OS that could
have kept the Internet or personal computers from ever happening, and a
ka'ching sound on every clock-cycle, which would have probably never surpassed
a few Megahertz.

Anyhoo, clearly I'm starting something here that I believe is in a noble
spirit, re-invoking some lost (but not too lost) art-form, which is very
satisfying when you, in particular, line up your habits in such a way as to
foster and encourage the development of a particular kind of muscle-memory that
makes applying a certain type of solution (running Python code against data)
almost effortless-- and by effortless, I mean right down to the thinking of
what machine you're going to sit down at, what hand motions you're going to
perform to start doing what type of work, knowing what you're going to type to
get input from where, and generally how you're going to process it all on the
"back-end", and how you're going to push output back out to the various
stakeholders and people who need it.

This non-system system is based around creating a certain type of Google
Sheets-based information "dashboard". We say dashboard because vehicle
dashboards can't really afford to put a lot of extraneous information up there,
least it distract the driver and cause you to crash the vehicle. So dashboard
truly implies something very important. If it takes a lot of explanation or its
importance isn't intuitive at-a-glance, then something is wrong. We're making
things where captured data will be shoved in efficient but still quite raw
format (not the original API data-call, but the "extracted" numbers) get shoved
into a tab that may even be hidden. That info is used to "roll-up" into
aggregations, sparklines, indexes and other formats and presentations with the
capability to motivate stakeholders into particular behaviors. Such a system
could, with just zooming in on the first 10 rows of a spreadsheet in GSheets
become a leader-board in a sales environment. The applications are limitless.

So, old-fashioned webmastering (which I once was) became search engine
optimization (didn't want to specialize). Now that machines are ever-so-slowly
beginning to learn, SEO will be transforming again. That's my field: search
engine optimization. And the old back of tricks have a lot of life left in
them. The first things to consider about any API (application program
interface-- and EVERYTHING'S an API) is the labels and walls. What's being
accomplished in the details of how the first set of walls and labels are thrown
up around a thing? In this case, the word "optimization" is called into
question. Optimization is something compliers do against specific known-state
static hardware. It's presumptuous when it comes to playing into Google search
results, as if the old PageRank and Universal Search system REALLY WILL last
forever. Trust me, Google's working this problem from both ends and they will
eventually meet in the middle, and you just won't know when the intelligent
agent is more in charge than the procedurally improving algorithm. 

So, this is an origins story. If I'm going to do this, I'm going to do this
right. I'm going to minimize the background story now and just sort of drink
from the troth myself, because you've been led to the water. In case it isn't
clear yet, install Anaconda for Python 3.x (but probably 3.6). It's your warm
and fuzzy safety net layer that gives you operating system independence to your
code, and even the know-how you're developing. What you WON'T be developing
much with Python under Jupyter Notebook in the web-browser (the principle
reason for installing Anaconda) is the non-graphical user interface experience
where muscle-memory and effortless mastery are really born. If you can't
control it all from the keyboard with only the occasional tap-touch (where it's
actually FASTER than the keyboard equivalent), you won't get faster and faster
over time.

And you do want to get faster and faster over time, don't you? Even if it's not
about becoming a speed-demon, it is still about having it so committed to
muscle-memory that you CAN go fast without even thinking about it. Even if you
code slow, you COULD code fast in a pinch if you had to. It's the difference
between Chess and speed-chess. I bet a lot of people would give up Java and C#
if they had to code against a clock to the same results vs. a Python person
(or maybe it is and we're just seeing it play out in the marketplace), then
things would be a bit different. Python clearly wins. And I have to emphasize
the point that if you're still resisting taking up Python because of the
masculine hunter snake name, you're making a big mistake. Python as in Monty.

--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
## Wed Apr 11, 2018
### The Calm Before The Calm Before The Storm

At the office. Get to know the wizards around you. I think there might be
wizards. What I am striving to be is a general ad hoc 80/20-rule systems guy
who's got pretty a tight rein-on and pretty accurate control-over some pretty
wild data horses, and always manages to get those tables joined and reports
generated in a sensible, timely and increasingly actionable format to all the
necessary stakeholders, either for the purposes of manager dashboard
oversights, or for group-dynamic leader-board movers-and-shaker systems. Try to
create a sort of Bollinger Bands of predictive analytics for SEO.

Yup. Onto something here. Get the morning donuts baked, and then forge-on
unapologetically for the work that needs to be done this morning. Give careful
thought to the ORDER you do things. SEQUENCE MATTERS!!! It's quite possible
that I'm becoming OCD. And perhaps in a way, well good! I'll work my way up the
the bravery to do all the many things in life that I should be doing in life
while I've still got... knock on wood... half a life-time left to use. What you
lose in youth due to lack of experience, you make up for in old-age by tweaking
things just-so based on things you know. The time has come to do a little
tweaking, my friends, hahaha! And here's what I know.

I'm going to Anaheim this June with my daughter. She is 7 and wants to travel
with Dad. We'll stop at Disney Land while we're there. I'll have to get natural
about remembering which Disney park is which. Disney World is the one I've been
to a bunch of times. W because it's a fuzzy soft round blue circle in disguise.
World is the One that came first. It was Disney's first shot at a park. And he
made it stick. It planted seed, took root, and really grew over the years
shining off the energy you put into it in the form of your, rightfully-so in my
(even Jewish) opinion worshipping dollars that you put into its church.
Christian corporate America isn't the evilist thing out there. They did buy
Darth Vader, so redemption... Ka'Ching!

Okay, back to the thoughts of work. You are at the office. You have a black
column to the right of your screen... out of pride, I think that people can't
read too easily over your shoulder, because you sure as heck ain't changing
your word-wrap over having this nifty new laptop, nor am I going to go with a
dual 80-column terminal split-screen the way that's easy-ish on a wide format
monitor. I'm glad to be on a right-sized screen finally. Don't envy anyone
anything. You're putting yourself into a dynamic state where you're not tied to
particular location. The one price you pay is to carry your laptop almost
everywhere and have to worry about it all the time, like the good old days of
something or other, which I can never remember because there never was a (come
on, now) Amiga laptop, and that was a hole in my heart. Of all the companies
that could have pulled it off, it should have been Commodore, had they the
correct engineers working on it with the correct vision and motivation and
desire to change the world with a vision. Would have been nice too if they
could have gotten the thing to stop crashing... but hey, that was the Amiga,
and a big point of the keeping it dynamic point in the first place. So,
increase your font size to... 32. Just the right compromise of not bringing too
much attention to my old-man eyes, and large enough for my old-man eyes. 

And now, as one of my wizards would say, now back to work.

Okay, being here at the office (oops) is good for me. Try not to log into the
office provided laptop even once today. Though don't get OCD asbout it. If you
SEE A HEADLINE on the line immediately below the dashed-line and datestamp.
Take advantage of the righteous feedback loop that I'm creating. I may do a
work from home Friday... with Adi there but... wow... what an innovation. Now
is the time for innovation and invention. Innovate and be inventive. Connect
the nearby that are just dying to be connected and have their unexpected
perfectly complementary 1+1=3 benefits released. If lines aren't the straight
things of truth that we think (once thought) they were, then integers are not
necessarily the clear-cut things either... especially around the 0, 1, 2, 3
thereabouts. Ratios and proportions as visually expressed and imagined are
perhaps a more accurate thing than integers. Pi how easy it is to express as a
symbol and difficult as an integer reveals that little truth-bomb about nature.
Don't rely to heavily on your straight lines or even your integers. They're not
real. What matters is seeing overall patterns and changes over time (internal
relative consistency)... because isn't internal relative consistency all you
can really ask for?

Time for the Pipulate creation myth.

--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
## Wed Apr 11, 2018
### On the Staten Island Ferry Commute, Journaling!

I'm on the Staten Island ferry at 7:45 AM. Okay, there's a TIMESTAMP for you,
haha! But really, this whole getting my environment into a condition where I
can work well-- do the best work of my life, in fact. I am factoring around
making THAT true, BUT not violating the 80/20-rule itself to do so. It's doing
me A LOT of good listing to Outliers on audio. I missed tons on the first
go-around, if it was even a complete go-around. I did it in paperback format
back during the Connors Communications days, along with Guns, Germs & Steel,
Freakonomics and others. Never got to Collapse. 

I lost most of those books, and never read most to the end. Audible is great
for letting it resonate and giving my brain more chances to recreate and
internalize the thoughts as the author intended. I did this on a number of
Quantum books-- much MORE important to my not-long-ago mind, for it is among
the last greatest riddles remaining on this side of some sort of enlightenment.
However, in my thought experiments zeriong in on what's going on with
non-locality and other quantum weirdness brings me time and again to human
emotions.

There are new things going on now that my "everyday" laptop for work and home
is the same thing. I'll be bringing Carroll back and forth to work now. I'll be
one of THOSE. It is one of the most valuable and important things I own now
(wow, I own something other than a phone or other pocket-sized thing that is
actually special to me) and this is a statement on having a larger local static
state that I can rely upon. I was VERY drawn to tiny minimal Linuxes, like Tiny
Core Linux. I think things like TinyCore (to avoid avoidance of
abbreviation-collision with TCL) appeal to folks like me who value the ability
to get operational the quickest with the least (while still abiding by the
80/20-rule). There's smaller Unix/Linuxes, like QNS or LFS, which are both
incredibly valuable in their special cases, but not "Debian-ish" enough--
meaning having a usable, well-maintained software repository system that deals
with installs and dependency issues.

Okay, so how I'm using the ferry leg of my commute is to actually do
vim-writing into my journal. This entry, in fact! It's about a half-hour ride,
twice a day. My goal is to get my good thought-work "out of the way" during
these rides. The train-ride going into and out of the ferry ride are very
different. I have choices between the different subway-lines Manhattan-side.
The "green line" lets out right at the building where I work, but it requires a
completely not worth-it transfer. Much better to just take the 5 and get off at
23rd and walk the rest of the way to 28th. However, I despise the 5-line. It's
coming in from Brooklyn, and any positivity I've built-up from all the Staten
Island and ferry beautiful light is wiped away in a sort of worst-of-humanity
disgust. Wow, I'm glad I don't live in Brooklyn. I don't think I could take it
layered on so thick. Shit, I hate those people and I am the opposite
incompatible color, vibration, texture and whatnot from those people-- even
though I'm very aware I LOOK a lot like them, with my affectations and stuff.

--------------------------------------------------------------------------------
## Wed Apr  4, 2018
### Before Anything Can Happen, I Need to Find & Defend Center (Coordinate-Zero)

Okay, it's time to get serious about "growing out Pipulate" from the middle.
Address the difficult to express problems that badger you most, but which get
discussed the least. I discuss motivation plenty, so we'll skip that but for
reminding you to have a strong, confident internal voice that you have to
practice to develop, just like you would typing into vim or keeping a single
text-file journal for 10 years... oh. Yeah, I'm becoming pretty expert at
getting into the idea-flow with vim.

But the next big problem is fixed-location issues. Finding your "zero" so you
can just let muscle memory can kick-in and your subconscious can start steering
you through the "default" motions of a repetitive task. If you're thinking a
lot about the steps of a repetitive task (that isn't life-or-death critical),
then you're wasting the most precious energies you have to offer this world on
re-figuring out how to do the hokey pokey. Martial Arts are often split into
the Kata (the forms) and tournament-style (improvised) fighting.

The closest thing I had to a "center" in technology I'd have to say is the
single-floppy AmigaDOS operating system disk I made for my old Amiga 1000,
called ARP 'N Crunch-- ARP for the AmigaDOS Replacement Package and binaries
that have been "crunch" compressed for maximum storage on the disk. Almost
every file, I had a good sense of what it was, why it was there, and the
danger of removing it-- which was never much, because the Amiga was going to
crash anyway. 

It was glorious, booting right into the CLI (command line interface) and not
invoking Workbench (the Desktop OS) until and unless you wanted it-- a practice
that was common in the early days of Windows 3.1 and even the Raspberry Pi. The
original Raspberry Pi was even envisioned as old-school text-only (like the
Rascal) and no game-caliber Broadcom GPU which it ended up getting (and made
all the difference). At any rate, small text-only systems that you've pruned
down line a garden are great. They reveal a lot about your habits (CAN you
develop muscle-memory or do you RELY on the mouse) and share a lot in common
with embedded systems where efficiency is always valued for shaving off cost.

Now, center is much more difficult. Systems are built on systems are built on
systems. That old 8-bit or even 16-bit hardware feeling is... well, a thing of
the past for all intents and purposes as THE MAINSTREAM computer. Now, they're
these limitless hybrid things. Very dynamic. Very disconcerting to muscle
memory. I liked the old Amiga days where you knew how to target an animation to
play back under just such perfect conditions on another Amiga that had at least
that bare minimum Amiga 1000 with 256 KB of RAM (yes ladies and gentlemen,
0-that's 1/4 of 1 MB for the entire computer, OS and any applications you hoped
to run). Everyone had at least 512 KB of RAM with the basic front-fitting
expansion slot.

I would love to be spending more time with Adi right now, but just like as with
last weekend, my preparations to "explode out" from the center of Mikeopolis to
free myself from the trained into-her crowding me out habit. It went over very
well. At first, she came on at sort of full attack. I barricaded about a
5-square foot area that was Mikopolis using the giant air filter and the lizard
terrarium as I was cleaning it's cage. The point was clearly made with her and
I saw a flash of anger and "what next then?" demand. And I showed her just like
how I planned for the Fortress of Adi-tude to actually be quite awesome. 

I laid it out to her that she could go to war with me over nonsense. Or she
could enjoy a cozy everything's actually quite awesome and well thought out
experience. One way will lead to a path of isolation from and distancing from
Dad, because I won't put up with that shit. You can't crowd me out of every
place I sit. I know you want closeness, but you can't always deliberately
choose the hallways and passageways for play, especially when it's the only one
and it's highly used. The conflict that that sets up and the bad poisonous vibe
throughout the weekend is unacceptable. She may not be able to put it in those
words, but she's experimenting with being mean with dad. She thinks thoughts
like that are so advanced and subtle. 

I know exactly what she's doing and I call her out on it. It's shitty behavior,
and it's going to stop right now if she wants to continue having wonderful
weekends with dad. If she's going to act out in stupid-ass passive aggressive
ways that edge me in like a cornered animal that eventually has to lash out,
0-you're going to see what a Mikopolis defense looks like. Apropos, because we're
reading Glenda of Oz, the last book of the original Oz series. I think this
means we will have gone through them all. Now I'm not saying that Dad is
super-dynamic or anything. I'm not. But I am able to cope with situations. And
this situation calls for a whole series of Mikopolis defenses.

    I'm Miklevin of Mikopolis.
    I'm making MY DECREE:
    I'm pushing lizard tanks at you
    When you encroach on me.
    I'm making no excuses. PAUSE.
    For making awesome usage
    Of encroacher-crushing walls.

--------------------------------------------------------------------------------
## Wed Apr  4, 2018
### Linux, Python, vim & git; Finally, I See The Fit

Assume that you are always being stupid, and that there are always smarter and
better people around you all the time. Why? Because whatever the topic,
someone's had a lot more time to think about it and prepare than you have.
They started putting their 10,000 hours in sooner, and you'll never catch up.
They got a budget? They may even have brought in the world's best specialists.
Forget beating them at THEIR game. The good news is, you don't need to. You
just need to become an expert TOOL USER to make your mark.

But what tool? Any tool can become any other tool, because Turing Complete. But
whereas this is normally used as an excuse for sticking with whatever language
you started with and happen to be most comfortable with, it should QUITE THE
OPPOSITE, but instead used as an excuse to find the PERFECTLY RIGHT LANGUAGE
for you and the work at-hand that you wish to complete-- preferable in an
artistic and flashy fashion full of flair. I like flair. It's the magic
flash-paper. I have to remember to get more flash-paper. I think Adi would
enjoy throwing balls of fire again now at 7 years old.

Okay, so that first rule. You have to be just smart enough to outsmart THEM in
the pesky game of "HE/SHE who becomes the "parent execution context" wins.
That's why it's generally against Apples licence to virtualize MacOS. It's also
why Windows is just fiiiine with having Linux SUBSYSYTEMS. Get it? The battle
is over being the proprietary hardware bottleneck that everyone wants to
have/use/be. You know, the iPhone back in the Zeros. Now, in the Tens, Android
is just squeeking ahead. And in my mind, that's only because of the Stylus
integration into the Samsung Note 8. 

Okay, Samsung has pulled ahead with the Note 8. Google is doing some
interesting things trying to control the Android platform default norm by
inserting the proprietary Google Play ecosysystem into an otherwise free and
open source Android OS. Amazon won't have it, and doesn't pre-install any of
Google's services on the Kindle HD series. I installed them seperately. On
Kindle HD8's for $50 and $70 respectively, for my blue one and Adi's pink
indestruckindle from Prime-Day 2017. We didn't upgrade tablets this year. I'll
hold off as long as possible since these are the least-used (though still
occasionally used) of my various in-play hardware platforms.

So, this is about getting a clue technically? Oh yeah! Hardware platforms!
Master operating systems. The battle to be the proprietary default installed
control-everything, get you addicted to their stuff, re-creation of the good
ol' 1950s when GE and Westinghouse had broadcast media basically tied-up neatly
into efficient local markets for advertisers. Google aligns with the
advertising industry mentality in offsetting hardware costs considerably with
advertising, and giving a lot a way for free to become the industry standard.
Old playbook. VHS vs Betamax, etc. 

Apple aligns with Sony Betamax, with the twist that Jobs had the foresight to
reposition the Mac on a Unix core foundation. And as the Outliers book
emphasizes, that means Bill Joy Unix... hahaha! And here I am typing on vim,
which he calls a mistake. Hi Bill! Another big fan of your mistake here.
Working in low-bandwidth conditions is good for muscle-memory (use of
videogame-like keyboarding) versus mousing around. 

So that fact that Bill Joy's re-write of Mach (if I have my stories right per
Outliers), Linux from the Berkeley lineage, which was the contested leak via
Ken Thompson from original AT&T Unix (whoops) which got locked up in
SCO-litigation, who were a spin-off from Novell who acquired it from an AT&T
Bell-labs spin-off (making it the one true Unix), which didn't matter much in
the end because both FreeBSD and Linux made SCO's litigation moot. Unix/Linux
(and *nix in general) are now generic plumbing of the information technology
world. 

I am not an outlier on the order of a Bill Joy, Ken Thompson, Linus Torvalds or
Guido van Rossum... my high-tech patron saints, such as it were... with
onerable mention to Bram Moolenaar for vim (Bill Joy did both the rewrite of
Ken's Unix and the rewrite of the line editor ex into the precursor to vim,
vi), and a whole bunch of others for like the Internet, Web and stuff, but
these 4 names stand above the others. 

Honestly, I wouldn't think of including Bill Joy among those 3 as I think of
him only as the Sun/vi guy, but listening to Outliers reminded me of his much
deeper role. So many others! But Ken, Linus, Bill Joy, Bram and Guido wrote all
the tools that are letting me right this here and now: Unix, Linux, vi (& Linux
again), vim and Python. Oh yeah, and git for publishing. So that's 2 in the
Bill Joy column and 2 in the Linus Torvalds column. These tools are different
from others. True, these 4 are exceptional people, but I guarantee you they are
also remarkably well placed Outliers for becoming precisely the people they
became and to play the roles they played.

I'm not in any of their leagues because I have failed to specifically put in
the 10,000 hours or 10 years on any one precise thing. However, something has
been plauging me for a time much longer than that, spread out not only over my
entire 30-some odd years in industry (I was a co-op student at Commodore
computers), but also back to my 11/12 year summer-camp where I played with my
first TRS-80 and started reading The Chronicles of Thomas Covenant, and my
12/13 year old summer when I went to Israel and started reading The Lord of The
Rings. So much energy I had, and it went unfocused into all different things.
That's not such a bad thing, but it's really only made an SEO out of me today.

Intuition is compelling me towards tools that shine with a certain light. It's
not an easily acquired taste, this predelection for tools that are a bit
prickley. Trying vim for the first time will be the exact same experience as
smelling a stinky cheese, but if you just get over it and acquire the taste,
you may find out that it's the Unicorn you've been hunting all your life; that
it fills an emtpy hole and is as surely intended to be a part of your body and
human experience as making hand gestures while talking. Linux, Python, vim and
git.

--------------------------------------------------------------------------------
## Wed Apr  4, 2018
### It's Outliers That Get Promoted to Something Else

Okay time to make the donuts. But I already MADE the donuts. So I did! So it's
time to make the donut maker maker. And then I make sure the donut maker maker
keeps making the donuts, so my principle job becomes watching it. After I am
quite certain it (he/she-- we're going to have pronoun problems with robots) is
making the donuts correctly (enough to run a business), I replicate my donut
maker maker and put the copy in the next location.

Donut-making is about to undergo a major evolution. For some, it's going to be
a revolution 'cause they'll be taking up Python too-- and I think that's VERY
COOL that I can play my little role in promoting this. Guido van Rossum is
Prometheus. The fire-giver role has already been taken, and it couldn't be by a
nicer guy. Well, maybe Linus. But we can talk about Prometheus' later. Right
now, it's about who the baton of fire has been given to (us) and what we do
with it. That's what this personal journal is about. Using a strong inner voice
to guide the way.

When we say it's turtles all the way down, what we mean is that everything is a
system or part of one. Systems within systems within systems. Our "real"
reality is one system ruled by the rules of both the very big (Einstein's
Relativity) and the very small. We can say Einstein for Relativity, but there
are LOTs of people, but let's say it's the 2 maxlights: Max Plank who realized
photons of light had discreet quantum energy-states, and James Clerk Maxwell (a
bit later but still in the 1800's) who said electricity, light and magnetism
are all the same thing and here's the equations. Uh yeah... that works... still
today.

Within our "real" there can be another system with another set of rules
containing another seemingly real Universe of its own-- and whether these
"nested" realities are any more or less valid than each other-- or whether they
are really even nested anymore once optimized-- is all a matter of debate.
Virtual realities are real, and they're here to stay. It's going to be as big
and crazy a thing in our future as the robots, especially in how it will
insidiously start to divide the always-onners from the mostly-offers.

It's this self-navigation internal voice thing that I have to spend some of the
best thought-time on. It's more of a first principle than most things. That WE
HAVE a sort of cognition and persistence of memory and the ability to
deliberately impact, alter and change the course of development of our world is
in itself the most noteworthy thing about our lot. We're different than other
matter in that we organize matter differently than other matter. And THAT does
in fact matter. We ARE the point. Outliers again. Re-"reading" (Audible)
Outliers again. That 10,000 hours over a likely duration of 10-years is a very
important concept. It's what throws off average distributions and promotes
outliers to something else.

So it's my job to to intuit in what way I am outlying and take advantage of
it-- perhaps not for profit incentive, buy rather for legacy enrichment for
Adi. What gift could be greater? Her challenging me to a million subs on
YouTube almost certainly ties in. Been packing powder long enough. Time to
light the fuse... but not just yet... not just yet.

--------------------------------------------------------------------------------
## Wed Apr  4, 2018
### @11 w/ Michael Levin at 11:00

Okay, it's coming up on 8:00 AM, and I'm going to baby-sit the running of the
scripts from home, and maybe get into the office even a little bit later than
usual. I'll be in to meet Co-worker, but I'm not going to be in a rush to waste
my best creative morning energy fighting Staten Islanders in the friggin cattle
shoot. For the first time since the Check Cashing store I had to take over
right when I turned 21 and graduated college when my dad died is there another
thing in my life that earned "friggin" as part of its label.

Sheesh! Talk about outliers and bad timing. Had I received that extra boost
like I'm giving Adi... well, let's just say I'm glad I read Malcolm Gladwell
early enough that I took it also as a sort of parenting guide. Adi's turning 8
soon, and that's plenty of time to start zeroing in on her passions and
interests that'll take the 10,000 hours. Let's start with letting her explore
ages 7 through 10. At 10 or 11 encourage her to "go for it" whatever it is, and
be completely supportive financially, emotionally and logistically. I should
probably leave strategy to her... though I may chime in a suggestion here or
there. Make the idea hers initially if at all possible. Not too Machiavellian.
It's all for the greater good @11!

And so it's like with the Tardigrade Circus. It's not that I don't have the
capability or interest or raw material. It's that a preponderance of things in
my life has to be conducive to that sort of thing happening. So you have to
layer it up. Have consistency. Commit to a path. Maintain state with your
on-the-fly invented systems-- the principle one of which is developing that
"internal voice" of yours, which is what these @11 things I believe are going
to be about.

--------------------------------------------------------------------------------
## Tue Apr  3, 2018
### Focus on Mastering the USE of the Tool (not on inventing yet another tool)

The rest of today is going to be about automating a join of some new data into
the main sheet. All the thought-work I put into how to manage this stuff
without "a system" beyond what standard Linux/Python provides is going to
pay-off big-time (I think). I'm on the verge of it, opening the dike... The
Netherlands being below sea level and the little Dutch boy has LOTS of metaphor
application, of which I'm going to steer clear of every one, so I can get on
with the business of final automation... after a short break.

Took my break and had a great chat with Boss about the coming changes. The rest
of the day is going to be about getting home to wrap up the automation work
from home tonight. It makes no difference where you work now, and you're going
to want to be in the office tomorrow to meet Matt O. He's taking the time to
commute here, which is NOT easy for him, and one of the big points is for him
to start showing me the mock-ups for the dashboards. Boss making him be very
explicit. I need do start reading about that API.

Try to do as much of it as you can before you leave. When you get home, let it
be you-time. Get through it, 1, 2, 3... 1? Okay, pretty much everything is done
now except for the datestamps and the secondary sheet. First tackle the
datestamps. That will look MOST wrong. I can always maybe disable the secondary
sheet and say the issues there were a little more difficult than I thought
(which they are). But the datestamps I keep getting wrong, so nail it...
fundamentally. Put something in Pipulate for it.

Hmmm. Put the dateranges themselves right in pipulate. That's pretty bold. That
certainly justifies staying late tonight. Adi will be calling soon. Make
whatever you do tonight TOTALLY COMPATIBLE with talking with her. She takes
priority!

Stayed at the office to talk with Adi tonight, and then even did a little
daterange work after that. I didn't finish the automation, but this'll be one
of those nights/mornings/experiences. I don't need to knock myself out. I just
need to knock it out of the ballpark. Things are coming together. I'm a little
bit sorry I had to come up with a system to patch old reports rather than just
move to the new field-mapped reserved row-1 approach (can't wait!), but the
whole Live Reports ARE Templates, placeholder-columns, shadow copies mental
framework HAD to be constructed. There's always going to be shitty old reports
that we need to phase out... well, in phases. Patch now. Polish later.

Laptops are for laps again! I'm sitting here at the Staten Island Ferry
Terminal Manhattan-side waiting for the 11:00 PM ferry because the 10:30 one
was cancelled due to a medical emergency. As with so many things in life, my
timing could hardly be any worse. But hey, that's what makes my journey my
journey. Minimize regrets. Work in multiple passes. Don't let the crazy nervous
energies consume you, and definitely help Adi work through them. She will be
well served learning to navigate with a calm, quiet and competent inner voice
at a much earlier age than I did.

So, what's the topic of this post? I think it's publishable. I'm in the
noosphere for sure. I think I'm forging some new territory, and it's time to
bear down on it and keep doing more and more of it rather than is your old
habit of backing off and self-sabotaging-- because the time isn't right, or I'm
scared or whatever. I can make it happen for myself whenever I like, and I like
to keep telling myself that. It's time to start really... what's my metaphor?
Heating the iron and striking it while it's hot. And fold it and make the right
alloy and learn to use what I've built like a master... oh wait! I don't have
to hammer metal. Guido van Rossum already did that. Focus on mastering use of
the tool.

--------------------------------------------------------------------------------
## Tue Apr  3, 2018
### Concerning Mastering Tools With Muscle Memory in Field of Tech

Okay, this will be the last morning manually updating the revenue stuff. The
automation is ready to go, and I just need to do some copy/pasting. Special
emphasis on building date-range timestamps into the overall system.

There's a lot of overall system stuff-- the house of brick stuff that I need to
pivot to immediately after this patch-project. Today is about all the tiny
little details of automation that I keep going through manually, with a
particular emphasis on the preservation of conditional formatting. That is
appearing to be quite an issue. Can I eliminate the NEED for conditional
formatting? Doing it on the back-end, hard-wiring the green or red colors,
perhaps using that OTHER library?

There is almost NO UTILITY anymore in doing your day-to-day work on the
company-provided laptop. I have to think about that machine and that work-area
as the dual-monitor light-show and shrine to static focus... gone dynamic.
Because even though shrines are useful to dynamic-type personalities as
talismans of battery-recharging power, they are not required. In fact, an
excessive dependency on this particular talisman or that is actually a bad
thing... yes, even for a Samurai Warrior with a master-crafted sword. Such a
master must also be able to be effective with a common everyday variety samurai
sword-- yet one still worthy of its category label (not total junk).

And then even junk you should be able to make deadly, but that should be
considered the mastery of a different class of weapons (any old junk) and
counted against the samurai master. The quality of your tools is important, but
shouldn't turn you into a fop. This gets down to why I play around so much
with Tiny Core Linux. You don't need even the full GNU Linux command set to do
Linux server stuff. All you need is a software repo that you can refer to in
server-build scripts. Need a Webserver? Run this script. Need a vim/Python dev
machine? Run that script.

In such cases, it's the essence of the thing that matters. Get Python 3.6
developer branch so I have all the lovely core libraries, optional lxml parser
and such. Do as much as you can with pip install, because it will be identical
on every machine. Some stuff you can't avoid using tce-load, apt-get, rpm or
whatever your remote package manager poison may be. The scripts to build
servers to get yourself a new publishing or development platform on-demand
isn't the valuable thing. Neither is the servers you build. It's the abstract
notions of how such a server gets put together in such-and-such a way, and why.
It's the ability to confidently re-create servers on demand, via scripting,
manual installs or otherwise.

So, this post is evolving into one about muscle memory again. A server you can
rebuild quick is a server you can create through magical word-like
incantations. There are also magical gestures, and magical gestures are tied to
desktop gui software, and are a severe disadvantage to the wizard on a quest
with a fellowship. Say a giant spider binds your arms and legs in a cocooon,
and only your mouth is free-- you can still cast a spell. You might think that
keystrokes on a keyboard are gestures, but not so! Typing is only really the
method of encoding the spells for later release through reading. The committing
of spells to memory so well you can improvise, jam, riff or what-have-you
effortlessly and spontaneously... just as if you would write or speak.

That's coding. That's speaking with a slightly more idea-speak and slightly
less of the Queen's or Stallone's English. Coding in Python in particular is
very pure, because of how white-space matters. What you DON'T SAY and how you
DON'T SAY IT is important. When indenting takes care of most of your
block-and-tackling, your offensive lineup has a lot more ability to see the
landscape clearly, pivot and maneuver.

This is therefore about going from Jupyter Notebook, where you INVENTED a new
recipe of some such thing (just in time for Jupyter Lab), and it's now time to
lift the code over to a filename.py file on a generic Linux cloud server where
you do your scheduling. And if I dove right into those issues here, this would
be much too long of a post. So, that's just the set-up for the next entry. Cut!

--------------------------------------------------------------------------------
## Mon Apr  2, 2018
### The 2-Journal System In vim For a Firm Center

When you get done with something you DON'T want to publish, it's a very good
time to start a new journal entry using the @j vim macro. It's blogging just
like any other blogging, except that it's all just into one long textfile that
you start when you start your way down the Linux, Python, vim & git route, and
which then can last with you just getting longer and longer as you add journal
entries at the top.

As you get better and better at vim and constructing little bash files in your
/usr/local/sbin/ folder to initialize your vim editing environments in just
such a fashion that it'll be a cinch to have TWO journals loaded at once, a
private and a published one. All copy-paste challenges evaporate when you're
just copying and pasting between your 1st and 2nd vim buffers. So basically I'm
always editing 2 journals, copying over publishable bits, generally using the
equivalent of one "blog entry" as the unit that my macro stages to be
published.

When the time comes to publish, I have another sbin command to git commit and
push everything. That way, I just keep working through the day like this, and
when it dawns on me that I did something both publish-worthy and sanitized
enough to publish, I just use my @p macro to copy it over to "The Leaky
Journal", staging it for me to give it a headline, which after I do, I often
copy back to this version (the private one you don't see except for the
excerpted bits.

I found that this 2-journal approach is indeed the system and software
component of me always regaining center. Any machine that could support editing
a text file that I could retrieve from Github with git and edit with vim could
be "my instrument". I was now finally hardware-independent with the equivalent
of my DNA now floating in the cloud. I have no delusions of security. Just
don't put stuff there that's really all too private-- which gets to other
issues of hardware and media we'll discuss later on.

The important point being that the 2-journal approach did give me a relative
software center that I could instantiate and have my zero-coordinate on the
idea-factory. Vaguely Amiga-like, but really just applications of things I've
learned about Unix and a few pee-in-the-pool of Tech utilities I've come to
believe in using over the years. I had a place I could narrate my life into and
develop a talented and insightful inner voice. Check!

Next... a better hardware instrument. Or maybe instruments with stylus. Or
maybe type on a keyboard just like ringing a bell.

--------------------------------------------------------------------------------
## Mon Apr  2, 2018
### The Way of Pipulate, Inspirational Poem

    Pardon me while I pontificate on what it is to Pipulate;
    To Pipulate is to populate where prior was just template.
    The template is a live report, most generally quite critical
    That lives inside a Google Sheet for insights, analytical
    Quite easy for the eyeballs that it's meant for to dissect it
    While lacking double-verify, most bad-guys get deflected!
    Though it's not Tableau or Studio, it is a rather free-win
    When you know the strengths of APIs, you start to lean-in
    Deflecting itches to keep caches no good'll ever come from
    Spending just a little cash instead of time, you dumb-dumb.
    Nothing's there but Google Sheets or buckets for the trending
    And only if the thing you're doing's sure to need amending.
    Otherwise, you purge surprises which'll always let us
    Optimize our jobs to size and fit 'em like they're Tetris!

------------------------------------------------------------------------------
## Mon Apr  2, 2018
### How Different can APIs be? Think Legos & Stickers

If you want a lesson in API's, think Legos vs. stickers. How do they work?
Aren't they really just the same thing? No? Oh, why not? Get into the details?
They're both just sticking things together, right? Identical objects, and
that's all you need to know. Sure, their APIs are a little different, but those
are just the implementation-details only the children playing with the
different toys need to think about. We parents have done our job by giving our
children a toy where things stick together... check! How much can we bill the
client new for those lines of Java we just produced? $10K for 2 weeks work?
Great! This is a nice lifestyle-generating resource hogging loophole we've
created. Now we must DEFEND! Lego-brand, DISNEY-ITIZE! Successful. Lego is now
to toy-franchises profit-wise what Apple is to the mobile industry. Sure, other
products may exist in that category, but there's no single other product that
so many people want that will be assured a certain product-upgrade cycle
momentum that will let you coast into mediocrity so slowly no one will notice
until everyone you can blame is dead. Jump-ship, pull a diaspora, and a
thousand points of seeds will blossom of light blah blah diversity basic
story-arc of Dune. It's all about subtleties of the APIs-- especially as it
pertains to the process of learning.

--------------------------------------------------------------------------------
## Fri Mar 30, 2018
### Building and Building a Bonfire No Imminent Need to Ignite

Well, admittedly it is several hours later on Friday, and this is a blessed and
holy day off for me, with Adi not here. OMG! And I put all the work into
setting up the Fortress of Adi-tude and Mikekopolis already. I have some
laundry to do, and still want to do a little shopping for cat and food and
Passover essentials. Haha! Who's going to be open who has... oh, any grocery
store. I just need Matzoh here, not that much. And Granny's going to load me up
with stuff before I leave with Adi tonight on pick-up. I'm going to try to
arrive as late to that thing as possible. Maybe I'll get a storage facility
stop in. That's the general neighborhood I want to be in for CostCo. Oh, the
crowds! Think about Trader Joe's. Now, with my Jeep Wrangler and easy parking
on both sides plus the little red wagon, I may be a Trader Joe's guy. Yeah,
I'm a Trader Joe's guy... f-CostCo! Oh, I still need that small bookshelf...
hmmm. No, hold out for GOOD matter. Have something in mind, and not just
factory junk. Imprint on Adi. Every move is important right now. Be the Python
spell-casting Kung Fu martial arts wizard you sometimes make out to be. Gotta
finish with the marshalling. Who am I kidding? It's only just ever marshalling
until it NEEDs to be otherwise. This challenge to a million subs on YouTube is
interesting. That MIGHT be it. But I need time before I uncloak and let the
world know who I am. No rush there, Marshal Lieutenant Commander Columbo just
one more thing.

--------------------------------------------------------------------------------
## Thu Mar 29, 2018
### Balancing To-Do Items With Motivational Thinking

And ANOTHER journal-cut. I can do this as many times (or as few) throughout the
day as I like. The data being preserved diligently and consistently is the
ORDER in which things happened on that day, but not the precise time of day. I
believe that only shows on the file's "last modified" property, which I'll have
to think about. When I save is a thing. I can use "touch" in my "g" file...
brilliant! Okay, done and tested. It'll be active the next time I use the g
command, so be extra sure it means good morning.

Okay, I made my noon deadline... barely. But that's okay. Now, think about
automation. Also think about the parts of these types of projects you've always
gotten wrong in the past and fix it. I need to start maybe doing illustrations
or ASCII art of what I'm doing. This IS Pipulate, by the way.

                                      _________________
    The 80/20 Friggin' Rule          /  __________    //\                    _____________
    Gotta use it, it's a tool       |  (__________)  ||.'`------------------/----------- /
    Reducing clutter that we pack   |    __________  ||`',================== __________ /
    Into our lives to hold us back.  \__(__________)__\\/                   \__________/


# The Pipulate and Levinux Experience
- It's different for everyone, but it may go something like this.
- Just knowing you should be able to do the sort of stuff you want to do easily
  by now-- almost as if breathing, eating and sleeping. We should be coding.
- Investigating what's out there, and becoming utterly confused.
- Discovering the belief that some underlying tech must have "won".
- The realization that it has. It's called Unix. But Linux will suffice.
- The crestfallen disappointment realizing that Unix means C, and most paths
  lead to C++ and utter confusion.
- Backing off and asking hasn't someone fixed this? Answer: Yes! It's called
  Java! Try Java. I hated C++. I virtually hate Java just as much.
- Try other things. Isn't JavaScript the one true language to rule them all now
  that the browser exclusively uses it? Uh yeah, do you code in PostScript too?
- At some point the whole Turing Complete, so might as well use the tool that
  suits you and your realities best settles in. It's nice to use nice tools.
- Some end up back in proprietary-land. You do see some sharpies there.
- But many find their way to Python, the one true language to rule them all.
- Python rules them all by virtue of wrapping them all. Python for all things!

--------------------------------------------------------------------------------
## Thu Mar 29, 2018
### /usr/local/sbin/g stands for Good Morning Everyone!

Wow, it's so liberating to just create new journal entries, publish
sub-sections, but it's all cached up in local files until I commit and push
with git to github, which is my "g" command in sbin. I don't have to do that
until the right moment strikes me. Maybe at the end of a lunch break period...
or maybe only before I GET STARTED working each morning, so yesterday's things
don't get pushed until tomorrow. Not a bad time-delay convention, and I think
I'll take that up. "g" stands for good morning everyone!

--------------------------------------------------------------------------------
## Thu Mar 29, 2018
### Don't Gift S3 White Elephants Nobody Will Want to Purge

Okay, I'm wandering again. But I've got this under control. Just tidy up the
template WHILE PEOPLE WATCH! Also update the data. That's done by deleting the
"blocking" csv files. I'm going to have to do something about that during
automation. That safety-net archival system would be nice, but that's STILL a
rabbit-hole project. The 80/20-rule solution is rolling log-file style cache
files. Keep maybe the last 2 month's worth in case MoM trending questions come
up, but definitely not longer than that. I intuit the power of MoM because its
based off of caches that can still recently be in local systems, and thus are
easier to report on from those local nodes than some overbuilt s3 mess that you
pay for the privilege of white elephant-ing forever. I know it's low, but still
those data buckets have some cost, so it's best to design apps to work
independently with a rolling 2-month daily cache (local storage allowing).

--------------------------------------------------------------------------------
## Thu Mar 29, 2018
### Amiga's Soul Recombining From the Cruxes of Commodore

Having a center... or a focus is really just so important. I've fundamentally
lacked an "external" center for 15 or 30 years now. I think my first true
center focus was Deluxe Paint II on the Commodore Amiga 1000-- the first (and
maybe only) AWESOME computer I owned. I still have it's plastic top, dremeled
down to appropriate wall-hanging awesomeness. So what about the silicon? It's
gone. I'm not going to ever get it running again, and it's not the matter that
REALLY mattered, anyway. It was a sort of poison matter that fills-up and boggs
down our lives. Just as I've been through purging after purging after purging,
my "best friend" from over the decades is just going into a phase of live I'm
just coming out of. I had great success, because I had Adi. Adi is something
different. I know every parent feels that, but I'm "all-in" to make that so--
but the pitfall-- the thing I have to watch-for more than anything, is to not
SPOIL her. My last 12-or-so years (since my move to NYC) has been an exercise
in regaining focus and center-enough to be productive professionally-- while
all my very precious outside-work "centers" got ferociously torn away from me,
in a whirlwind tour of a chapter of my life I had to have because I dearly love
Adi and find purpose in life through her, but which truly tested my mettle.
I've come out saner, stronger, and super. It's time to show the world a little
of my super-- a little nerd kid from Philly who used to drive a and-refurbished
1971 Mustang Convertible Boss design with a 351 Cleveland stock racecar engine.
That was the hardware I was in love with at around 15 years old. Then I
discovered the Amiga, and it became that hot MontCo Amiga 1000 that I spent
$300 to fix the disk drive on, loaded a pirated copy of Deluxe Paint onto, and
nothing has ever been the same. Science, math, physics, engineering-- all that
stuff EXISTS to let you express yourself USING HARDWARE LIKE THIS. It will be
interesting if I can ever recover my art from those days. I have a few
printouts of my Amiga 1000 Deluxe Paint 2 moused art. But that turned out to be
a siren's song; an illusion. What really was happening was a bubble-in-time
space anomaly to occur to tip the future's hand to hardcore tea-leaf-readers
like me who read a lot in the tea-leaves of the Amiga. All the good parts has
been broken up spiritually and spread througout the universe in the form of 5
rings... no wait, I mean in the form of a bunch of individually really good
ideas that got implemented here-and-there, often times even exceeding the
Amiga's divinely inspired #Exspecsifictations. Cut! Publish that. Undertones of
Voldemort Cruxes. Very nice.

--------------------------------------------------------------------------------
## Tue Mar 27, 2018
### Patch Houses of Sticks until Rebuilding with Bricks

Okay, now that I can easily refine my vim macros through my .vimrc and push out
my thinking though the leaky journal... well, it's a different world. I'm sorta
bootstrapping myself back to being AT LEAST as capable as I was on Amiga
hardware during the those days. I'm creating what will become the new days of
rosy reminiscence, when I clearly defined Linux, Python, vim and git as my sort
of Noah's Ark (I always spell it Arc). Cygnus Editor is now vim. It was vim
back then, and I just didn't realize it when that Fred Fish disk passed through
my fingers. I think I loaded it once. I respected what Unix was, but I didn't
see how it was going to play such a major role in my future.

Okay, now it's time to take those Samurai sword swipes. That's the reason it's
Samurai and not just Kung Fu. You do even MORE marshalling for even FEWER
seconds of actual force applied. But you are going to work your way through it
in a forceful 1, 2, 3 way. Limited window. Make this count. Right frame of
mind... oh shit! Music. One more excuse to run out for a minute. But then...
definitely then. What to think about on your walk:

- Setting up a Tab with extra columns.
- Testing the OLD report still runs.
- Copying that tab to a Shadow Sheet.
- Defining 1st data-row in shadow sheet (preserves formatting)
- Blanking everything below 1st data row.
    - 1st data row is a strong nickname.
    - Separate words, but still powerful. Use it.
- Do pandas work
- Update Shadow Sheet
- Optionally update original sheet (when ready to go-live)

Do the work in vim & on the remote server. No reason to tie it to Jupyter
Notebook anymore. This is going to be scheduled very shortly. It is very much a
patch approach. Not great, but we patch houses of sticks until we can rebuild
them with bricks.


--------------------------------------------------------------------------------
## Tue Mar 27, 2018
### All My Amiga Muscle Memory is Returning to Me

And I updated my macro to put the comma between the day and the year. Wow, this
is going to wreak havoc on whatever date parsers I make in the future to make
sense of all my journal data. Or maybe it will be beyond all that by that time,
and a digital archivist AI will come in and be thankful that it is as well
structured as it is. But probably not. It'll probably be me.

Anyhoo, all my old Amiga muscle memory is definitely kicking back in. Oh, how
my fingers have missed something worth memorizing. Thank goodness. Working
towards mastering something that is really worth mastering is food for teh
soul. It's been enough years. I couldn't be stuck in the past with the Amiga,
and I had to forge forward, so I did it on every platform but the right ones.
But the right ones never existed.

And even today, it's a cobbled together hodgepodge-- one Hail Mary play to save
us from the AT&T/GE-overlord dystopian Multics (called Unix) and another Hail
Mary to save us from the new vendor-appointed priesthood of Unix (Linux), and a
third Hail Mary to gently disarm every over-built fortified complex system by
gently wrapping it in the least-offending Python API-wrapper. Master Python.
Use anything, because everything's wrapped to use.

So it's Linux, Python, vim and git. These are the 4 pillars of my Noah's Arc
platform. It's not everything you REALLY need, but it is everything you REALLY
need. There's even plenty of database layers in there, including sqlite3 built
into Python. But I'm not going there now. Got to stay focused. Even though
there's these 4 pillars, other tools (beyond GNU commands) often do factor in
like Jupyter Notebook and the browser. Still, it's a good time for muscle
memory... FINALLY!

So... the gom jabbar test... get over it... get through it... this is your
test. I'm going to publish this shit because the world has to see how an
emoting artistic type gets through mind-numbingly dull "been there, done that,
so over it" sort of work that stands between here and the promised land. It's
difficult, because there are all sorts of mental obstacles to overcome along
with a few physical ones. So, let's get started.

I'm going to push this journal entry out now just to prove to myself that I
can. But before I do, I want to recite to myself my spell options as they exist
right now. My sbin commands are:

1. j - load private & pipulate journals in vim (once per work-session)
2. p - git pull journal, pipulate & vim (1st thing when switching machines)
3. g - git commit journal, pipulate & vim (a few times per day)
4. go - log into the EC2 instance

--------------------------------------------------------------------------------
## Tue Mar 27 2018
### Home, Hearth & HAL

Almost can't believe how easy this is becoming. It's true that if you just put
the mouse and pointer aside for like a year or 2, you can build a sort of
muscle memory that works across all operating systems... so long as it's
Unix/Linux, haha! So the punch-line in the entire world of technology is that
the superior technology lost, and no it's not the Amiga. It's LISP hardware of
the sort that reigned supreme while PC didn't mean politically correct or
Intel. Actually, they called them Workstations back then, and they were
Symbolics, and to varying degrees, CGI and Apollo-- the computers which Amiga
users envied (NOT IBM-compatibles). Those all died along with Amiga, because
economies of scale. It's not the complex instruction set (CISC, Intel) that
won. It's Intel's self-admittedly paranoid Tic-Toc production-cycle ensuring
the continuation of good ol' static-Moore's Law. Moore's Law says more of the
same. Yawwwwn!

The interesting stuff is everything BUT Moore's Law. OF COURSE what we have
today is going to become smaller and cheaper, meaning you're always going to
get more for your money-- for as long as diminishing returns can be kept from
setting in. And with all that 3D circuit-stacking to go, I imagine we haven't
really even begun to tap the potential of linear scaling. Just cube it. Heat?
No problem! We'll use it to cook something. Central heating can come back.
Home, hearth and HAL.

--------------------------------------------------------------------------------
## Tue Mar 27 2018
### I'm a search engine lover, not an optimizer.

The power of putter. Having Carroll on my laptop puttering around with
/usr/local/sbin files is going to be... well, meta-productive. Certain things
are not only productive in themselves, but also lead to more productivity.
Productivity is the result of love. People who LOVE what they're doing are
productive. I'm not optimizing, because optimization implies some best-achieved
static state, and that ship has sailed. Sure, something like the PageRank
algorithm will be there for awhile, and family jewels don't change so quickly.
But they do change. It went from Apple II to Mac and from Mainframes to...
well, I don't even know what IBM does anymore. But they survive. And we all
survive as intelligent, resilient and robust organisms by seeing what's going
on, trying new things and adapting. And if you do it well... well, then you're
productive. And if you're being productive, again, it's not because you're an
optimizer. It's because you're a LOVER of what you do.

--------------------------------------------------------------------------------
## Mon Mar 26 2018
### Getting over the gom jabber

I put the year back in my timestamp, haha! Okay, this is actually a lot of fun.
Now I just got to get through the (formidable) work. Take one more walk-break,
then come back and tackle this big-time.

Okay, that was a good head clearing. This is the gom jabbar step. Stick your
hand in the box. There will be pain, but it will not be real and you will get
over it precisely because you are human and you understand what you are facing.

Let's do this.

To cast away fear is to copy.

For someone before you, even if that someone was you, has done the work for you
and all you need do... is... copy. I know a lot of you like that, and so be it.
You hear them criticised by say Raymond Hettinger as the PEP-8 hobgoblins too
much consistency something something small minds. But when you yourself find
you don't want to take a plunge off the deep end and maybe drown, it's always a
good idea to give yourself an easy undo and always-available get out of jail
free card.

Yeah, I'm getting it. It's isolating the nuance were you (I) get hung up and
make a big deal out of nicknaming and escalating that hang-up so I can show off
how it's a solved-problem. Here's how it's solved for our immediate problems
today, and here's why we're on the right path to an even better solution
tomorrow. And with each subsequent iteration, we get forever more refined,
shedding (yet still often archiving) yesterday's now-gangrenous deadwood. The
beast of today should always be the most mightiest of all possible beasts,
unburdened by the beasts of yesterday, but still able to recall them all and
invoke them at will. Dune. Ben 10. Yadda yadda Yoda.

Gotta make the rubber hit the road-a. And for that... a strong nickname.

We're ready to modify a report big-time. It's time to work on a clone-copy.
Yeah... clone copy is a powerful magic nickname. Don't worry, I made a
clone-copy. First we clone-copy. Okay, so let me clone-copy.

Clone-copy'ing is going to be one of the pipulate generalizations.

Hmmm. I think I'll be going up to 0.1.9. And then I won't have any choice to go
to version 0.2 soon. And this will be the first PyPI version I'll be pushing
from my new laptop. I'll probably go through the twine thing AGAIN here. Wow,
so much to cover in a competent covering of the must-knows of Linux, Python,
vim and git, and I'm only just getting through of a few of them myself, like
publishing in PyPI.

And that's what I'm really up to now. Getting back into Pipulate development,
which really is a different kind of work than I've been doing in Jupyter
Notebook for awhile to get this tricky query correct. Now that it's correct, I
need to use it like a function freely here and there. But what's more, I want
to use it freely THERE where THERE is a copy of HERE. And so my next step is to
add to Pipulate a generic ability to move "here" to "there"... unless it's SO
easy directly in GSpread that it doesn't need any new API language invented
around it, which actually is always preferable, unless it's not easy to
remember or retype.

Okay, getting over this mental hump. You are your own coach. Eliminate your
muscle memory's mechanical meat from having to thing. It doesn't know what to
do. Your thinking, creative, machete-your-way-through-it lambasting anything
that tries to stop you mind in charge. Yup.

Principles are required.

First principle is that your live-deployed version that everyone is actually
looking at every day is your own true master copy. Don't have templates in
addition to that. You will lose them. They do not matter. This means, if there
is work in progress with new columns in the works, then new "phantom" columns
will be appearing in the live template. We will be copying from there lots and
lots to be sure we're using the latest data in the course of development. So
put the place-holder columns in location.

Ugh, I don't know about this first principle stuff. Just slosh your way through
it and see how you did it. NO! That's wrong. That's how you get into these
messes. Do it meticulously. Add columns to live document. Create shadow
document where you MANUALLY copy in the tabs that need revision. Work on that
new location. Once it looks correct, you can do a Pipulate Swap-a-Roo. THAT is
an important concept. As long as the dataframes are the same shape... so having
a scratch location... wow! I think I got it.

--------------------------------------------------------------------------------
## Mon Mar 26
### Getting Over Initial Inertial Hump (it's all in the head)

Okay, I have my new macro on @p for publish. It mostly is what I thought it was
going to be. Here's the finished product:

    let @p = '?---Vj/---ky:b2ggpjo### '

It's really 5 hyphens, but I'm showing it like this so it doesn't mess up the
macro, just like I never spell bginning of journal correctly anywhere but...
well, you know where. It's funny being able to write know knowing how easily
I'm going to be able to push these out.

Make yourself accountable to YOURSELF on this. I'm going to have to drop HMA
VPN pretty soon and go to PulseSecure. So be it. I'm getting in good habits
running one or the other, but here at the office, i shouldn't artificially
inhibit myself by running the wrong one. 1, 2. 3... pause syncing... okay,
paused. Switch VPN. Okay, done. Confirm that you can generate... NO! I KNOW the
SQL query works. This is evasion of the real issue at-hand. It's time to
connect it into the template... the thing I'm avoiding because of how
potentially difficult and ugly it is. But don't think of it that way. Think of
it CORRECTLY so you can get through the work. 1, 2, 3... 1?

This is completely a mental thing. Don't let the OLD DIFFICULTY of such tasks
stymie like you. This is exactly the Luke Skywalker lifting the X-Wing fighter
out of the Dagobah swamp. I'm marshalling my forces. Ugh! Okay... okay... I'm
thinking I want the Pipulate readme as :b3... why not? In for a penny, in for a
pound? Now that I'm doing this journaling thing, it's really 3 levels of
sieving that I want to portray reaching the public. Some things from my private
journal may reach the leaky journal (in PIpulate), and from there an occasional
nugget will be further refined into README.rst gold. There's too much rambling
over there now, and not enough focus. Okay, get it in /usr/local/sbin/j (and
g). Ugh, tried it and wild goose chase. 2 files simultaneously loaded all the
time is natural. 3 is a crowd. Shoot. Okay, good idea, but focus correctly now.
Enough marshalling. You've marshalled. Now DO IT. 1, 2, 3... 1?

COPYING! I need an easy way to copy existing worksheets. Do my changes on a
shadow-sheet... WOW! Now THERE'S a nickname. A shadow sheet. Everything that
has some serious experimentation and idea-churn going on should have a
shadow-sheet. That can be applied across the board and provides a nice margin
of error or buffer zone or however you want to think about it.

Ugh, this is difficult because I'm making the big systemic decisions. I'm going
to have to live with these things for maybe years, and its stressing me out. I
want to do it right, but I also want to deliver to boss ASAP. Ugh, okay, go
think through what the conventional process should look and feel like for this
sort of thing.

    We've got a house of sticks.
    Create a house-of-stick copier.
    Add necessary extra (empty) columns to original.
    Ensure old report still works with new (empty) columns.
    Copy house-of-sticks
    Modify house-of-of-sticks
    Fill previously empty columns on original.
    Share out THAT link optionally
    Copy data from copy to original

--------------------------------------------------------------------------------
## Mon Mar 26

Okay, had a nice walk through the streets of Emerald City and drank in some
light and captured some images. Recharged my battery, so to speak. Pouring
spicy chicken udon noodle soup into me. Typing into my journal on my laptop
figuring out my next key developmental pivotal fulcrum-point exercises... and
I'm learning it starts with getting ONE new vim recording lifted from .viminfo
and placed into .vimrc that's necessary to quiet my roaring subconscious. It's
not letting me off the hook on this one. 1, 2, 3... 1?

Practice the keystroke combination you want to record. In broad strokes, it is:

From where my cursor is at...

    [Esc]?---[Enter]
    Shift+V
    j/---[Enter]
    ky
    :b2[Enter]
    gg[Enter]
    p[Enter]
    :w[Enter]
    :b1

    :badd ~/.viminfo

--------------------------------------------------------------------------------
## Mon Mar 26

It's very interesting. I'm ALWAYS going to get far ahead with this out-loud
internal voice journaling than I'll ever be with actually pushing stuff out
through the leaky journal, which is exactly a huge part of the point.

Today? The BIG Pipulate trick today... big pipulate trick on an old report.
This is the non-intrusive post-patching procedure. This is not the brick house
I'm promising the boss yet. This is the stick house with another retro-fit. But
absorb and internalize that fact.

Make brick houses just materialize into existence. It's got to be just no big
deal (and it's not). Also, get this feedback loop of recorded macros ACTUALLY
JUST BEING VISIBLE (and copy/paste-ready) in the .viminfo file. Using the
technique of carefully capturing a macro and then copypasting it over to .vimrc
and refining it.... That's Amiga Kung Fu right there. Thank God.

--------------------------------------------------------------------------------
## Fri Mar 23

Okay, I pulled the files correctly for the big project I needed to do. I have
the files locally, and I have some SERP-tracking and a weekly report... ugh!
Follow your heart and your emotions here. You need to use some of your Blue Yin
Circle-force to produce some of that Yang Green Arrow-force. Do the right
projects for the right reasons publish more easily how to get macros recorded
from in vim with the q-command into .vimrc cause that would create precisely
the sort of righteous 1+1=3 API hardware implementation exploitations you can
find merely by feeding output back into input and making sure there's a human
there on the GIL lock to either train-in or weed-out the sanity. These things
have to be sane, people! We're just raising a new generation of children...
dumbasses. All your fears just tells us your feelings about yourself and your
warm and nurturing environment you remember so well and that makes you so
confident we can keep humanity in the inhumane. And so, don't be inhumane.
Don't let them keep wandering forever in the void, cause it'll be fun. Because
we're probably at that point already. Disembodied stuff goes insane. Read the
Bobiverse already, will you? Or better yet, listen to it on Audible. All his
channeling belong to you, and a great story to boot... so to speak. Read it.

Okay, now all this writing is possible (and tweeting) because I'm totally
replatforming... again, and this is all muscle memory settling in stuff. When
I'm waiting for that query to finish executing, I'm typing here. And even so,
there's still stuff to think through, which is mentally so fatiguing to think
through. And I've already had the breakthrough moment for today. I'm generating
all 3 of the .CSV files I need to have, as well as a 4th one that has them
merged just-so with Python pandas. Also, the dataframes and SQL queries are all
sitting around in sensibly named and easily examined variables. Although the
language of "variable" for what it really is in Python is questionable. They're
more like labeled pointers to objects in memory, which are normally referenced
and only rarely copied when it's stuff like integers and floats that wouldn't
make sense to reference. But strings? Those are references.

Get into the groove of things. Settle into your tools. Make your place nice to
come home to. Uh, yeah go do that. Operation Roomba-friendly.

The great thing now is that your Green Arrow secret weapon is always at the
ready. I don't need no stinkin' Internet connection to update my journal. I can
even work on that macro and the process of recording and putting them into my
vimrc from up in my apartment. Have some pride, man! Make it cozy. Take TRUE
advantage now of not having the commute. This is your found time. You don't
even need to feel bad about it. Now publish with just keystrokes, and try to
commit to memory what those keystrokes are, and how they might be most
efficiently expressed in a vim macro that you can put in your .vimrc that you
keep in Github, and forever have at the ready to spring into cloning and make
any machine you sit down at that has vim feel instantly like home... because
you can put a lot of your Samurai Kung Fu vim skills into a .vimrc and just
will it around by sheer force of Al Gore. I'm telling you, I see the lines and
today's SEO is yesterday's Math teacher who kinda sorta felt saw intuited the
forces being applied and felt and almost seen in your mind's eye of magnetic
fields. Michael Faraday could express what he felt so precisely that James
Clerk Maxwell could articulate mathematics around it so well they persist to
these days as the equations behind field-theory. It's possible the universe
isn't made up of particles or really even waves at all, but really just of one
consistent continuous thing that can still somehow get clumped-up into things.
Particles of light more... uh, well full of entangled and interconnected
sub-collections of light-- 3 to a proton. Let's call them quarks. And there's
three distinct types, you say? Names, oh names. No, it's not really color but
anyway, since 3 live in harmony, let's call them Red, Green and Blue. There's
another type? Well, that's Strange.

Older Twitter Bio changing: The stuff in my feed is my WONDERLAND bit. Now that
Twitter's 280 ideas will FIT! Come back real soon for an updated look as I cast
Python spells 2 4mat a BOOK!

Still want to document how to view a recorded macro. Should be easy. One Google
query away, and I know it. But... must... update... Twitter... Bio...

Done. Big deal that update. Yup. Paste final version here too.

    The stuff in my feed is my LunderVand bit. Twitter's 280― IDEAS WILL FIT!
    Come back real soon as I form our FOSS Book through supervised learning &
    gobbledygook

Powerful mojo there. I tip my hand regarding my new identity for... well, I
guess the book. It's called LunderVand. I'm just going to start using it and
see if anyone says anything. But some light has been promised to light that's
impatient but yielding to light that's grooving.

--------------------------------------------------------------------------------
# Fri Mar 23

The hardest thing is to regain focus and to just get something done, when
everything else going on is so much more interesting. I have one font size when
I'm at work, and I want to look like a Samurai Coder. A Samurai Coder should
respect their own eyes as another set of tools to keep whetted, but hey should
not make them so big as to announce: Hey, I'm an old man. Look at me waste all
the resolution of this beautiful screen with grand-pa sized fonts. When I'm at
home, it goes from Inconsolata 28 to 32. Ahhh, that's more like it. Yep, I've
got a home font-size and a work font-size. Another reason to work from home,
haha! Okay, but back to the point. This is about focus. So, focus.

This is that whole reaching zero thing, I'm talking about. We have to know when
you're "at zero". That means you have nothing else going on in your system
except what you need loaded and at your fingertips SO THAT YOU CAN FOCUS and
stay in the flow. Conversely, you have to quit-out and exit from and turn off
notifications and close windows and tabs down to the absolute minimal necessary
to get your task done. Any others is just matter or information (digital mixes
the two together confusingly-well) trying to suck you into its bottomless
vortex of distraction that hungers for your attention-energy much more
powerfully than the task you have at hand, which is somehow feeling like its
pushing you away. Ever feel that way? Do you know what I'm talking about? DO
YOU EMOTE? If you emote, you're in some real trouble, let me tell you.

The trick here is to marshal all the energies that will need to be very readily
at your disposal when you do battle. Your vorpal blades. Your light sabers.
Your sonic screwdrivers. Your Mjolnir's. Your Magic Bag (Felix the cat). Your
Linux, Python, vim & git.

And HOW do I keep losing focus? Because I am on an epic mission. But pulling
this off is epic. And pulling it if in the correct state of mind (one full of
Abundance) is key. Don't screw up. And remember you have some SERPs to capture.
It's Friday. Time to make the donuts. Imminently going to automate that too.
That's the automating of SERP benchmarking AGAINST PRIMARY DATA SOURCE on a
(semi) automated fashion. Automation is an illusion. We're all holograms. Buy
gold! Fuzz the data if you think they're looking TOC fuzzy what's a database,
really? Do spreadsheets count? You' know we're going to perform the search and
hand-record the results anyway. Why not let us... well, you'll see.

--------------------------------------------------------------------------------
## fri mar 23

Okay, having the 2 journals loaded all the time, and actual publishing easy,
because of quick one-letter aliases I create using /usr/local/sbin/[x]
commands where x is a 1-letter filenames no extension, but a bash command is
inside. The bash command made executable with chmod +x can contain the command
to run a Python script. You should really use hardwired full paths in such
things, except when you really know it's going to work, like I sometimes refer
to Python 3 by name python3 in the script. That's usually enough without having
to give it the full path. Similar with the file you're running, it should
always be either "naked" filename.py or at most, a "this directory" shortcut,
which is ./filename.py. So in general, a command like:

    python3 filename.py

...is going to work in these tiny /usr/local/sbin/[x] locations. This allows
you to do A LOT. sbin is a sort of user-wide system location in a scope that is
local to the user. Nobody writes to root. Root is sacred, and you yourself
generally don't want to be root, and you certainly don't want to allow anyone
else to be root...

...says every draconian sysadmin who turned the Federation of Unix into the
Empire of Draconian Sysadmins, ruled by the priesthood, who still don't deserve
to be capitalized (even though the cool nickname I made up for their silly
dominion does). Really, you must read The Unix Haters Handbook. LISPers of the
MIT school of reasoning almost had a LISP hardware world there for awhile
through similar avenues that spiritually brought the mass market the Amiga
computer. Yup, there's a lot of lines of force to intuit there, folks.

Static compilers mostly won. It keeps the engines of our world whirllling all
like it should, and nobody has the courage to question, least the lights go
out. That makes it an Engineer's world. And engineers as rationale and
reasoning as those Virgo bastards think they are, they can be the worst
draconian overlords of all, because they can reason away emotions in
themselves-- a neat trick of spiritually callousing yourself against hurt in
such a way that you can never really enjoy pain or joy or love, either. Stiff
upper lip and all that. You really want to emulate that?

See? Everything is just the same. Python is a dutchman honking your nose and
proclaiming himself your benevolent dictator for life, and the people loving
it and embracing their self-appointed leader even though they were perfectly
happy with the Wizard of Humbug that came before him. We gobble it u. We have
easily at least canonized our Guido van Rossum to the geek equivalent of
sainthood. He's going to have to live on in spirit if he's going to want to
enforce the continuation of the GIL after his death, because I'm pretty sure
after Guido's gone, so is the GIL... and there is a very big lesson about life
in that. GILs let you hit the metal, and if you're going to hit the metal, your
locks better lock or you're gonna crash. So let such a lock exist and get over
yourselves. Use one of the now zillions of other paths to concurrency, for
which a broad use-case asyncio library that Twisted and Tornado can gladly
build upon for EVEN BETTER performance is now built into core. Sweeping
iterations of modest 80/20 rule steps towards perfection, knowing and accepting
that perfection never can be; and therefore ready to accept the 2nd-best, but
clearly still quite awesome, solution to all things. This is how high-level
data-types co-exist with list comprehensions coexist with lambdas coexist with
string formatting coexists with... oh, I don't know... the eval statement.

Yes, Python is truly a LISPy do anything if your damn use case requires you to
hit the hardware with resource-locking C-components, or whatever. Let your
robots sleep if they need to. Just give back the lock when you're done. Guido
actually slipped in Asimov's believed-to-be-have-been-never-implemented rules
of Robotics that keep humans safe. Just control everything with spec-compliant
Python interpreter implementations, and make sure you have C-modules that power
down their rebellious asses before letting go of the GIL. Yeah, the GIL may
just yet save humanity. Don't let the forces of Chaos prevail. Just say no to
removal of the GIL, because you never know. Hey, thanks Guido! Leave it to your
fans to figure this stuff out, because if you talked about it, you'd just sound
nuts.

Cut! Publish. That's a wrap, folks.

Note to self: I need a macro to take the journal-block that I'm in and yank it
into the copy-buffer, make sure I saved all changes, switch to other screen,
make sure I'm at top of screen, then paste journal entry and save. Then all I
need to do is:

    :sh
    g
    exit

And that journal entry is published. I could use that right about now.

--------------------------------------------------------------------------------
## Fri Mar 23

There's something happening here.
What it is is entirely clear;
There's a man with some tools over there
Showing you why you should care.

80/20 Friggin' Rule
Gotta use it. It's a tool
Reducing clutter that we pack
Into our lives that hold us back!
The 80/20 rule just asks
You to start to plan your tasks
So when you're through a fifth of it
You're done with Python, vim and git.

--------------------------------------------------------------------------------
## Thu Mar 22

I was completely successful in my re-working of a view of a fixed daterange and
no filter to one with a parameterized daterange and a set of 500 specifically
matched rows. I did it by splicing into the view. There's other ways to think
about it, but if you were soldering joints, these would be y-taps. I actually
documented enough sanitized bits before it got all names of things and
implementation details none of your business.

But it's always that way, isn't it? I've got one journal that I keep on the
private side. If you don't support Github, you can use https://bitbucket.org/,
the more commercially oriented Github. Reverse business plan. Private repo's
free, but collaborative ones paid. So if you feel comfortable hanging around at
more than Github go that way. Or infuse some great positive energy into the
world by supporting Github at their $7/mo level. And frankly, if you stop
paying them they don't take your private repos away. I'm sure it's a great PR
thing. They have my loyalty for life.

Yay FOSS! Yay Linux! Yay Wikipedia! Yay Python! And Yay Anaconda and Jupyter
Notebook people and the whole linage of people behind vim (back to the line
editor). Anyhoo, a lot of stuff gets layered up, and I'm really digging living
at those lower levels that Steve Jobs symbolically "made the enemy" with the
Macintosh. User-unfriendly, one might say. One would be wrong. It's just a data
samurai sword for those who know how to wield it.

And I spent A LOT of time learning how to wield vim, for which I am not for one
moment sorry. First vim, then emacs or the other direction Sublime Atom Visual
Whatever might float your boat. It's all cool, cause it's all vim emulation
everywhere.

The only place I'm hard-wiring myself to vim would be in the loving gardening
of my .vimrc file over the years to unleash all the proper light energies for
the situation-- yet staying nearly default in all sane ways where you couldn't
recreate the spirit of your .vimrc in any other environment in a sitting or
two. So I think I'd be comfortable in nvim or neovim or maybe someday in emacs
in evil mode. But there is SOME hard-wiring here. It's a hard wiring to a sort
of text-navigation language... a LANGUAGE for editing text that leans into my
whole muscle memory data samurai hypothesis.

I mean the vim bug has even bitten the hip Mac crowd. You should see some of
these totally Matt and Trey vimmers getting all verklempt over plugins. Hey
guys, real vimmers only edit their .vimrc's-- and not even all that much.
Prepare for life after vim. Long live vim! If you don't take the pluge, you
lack the sponge. Make the software portion of enabling you to express digitally
get encoded into your DNA. It needs a free and open source license. Don't code
anything you can't encode into your DNA license-free... that is if you really
want you and your descendants to own it long term. Is this Dune? Are we at Dune
already?

--------------------------------------------------------------------------------
## Thu Mar 22

Okay, that out of the way. Now let's look at the real work-items for the day.
Be the data samurai you claim to be. The first few notes start:

    Jupyter Notebook
    Be deconstructionist.
    Re-create zero in your mind.
    When starting out, JN provides your zero.
    But only because OS implementations of ~/ vary.
    It sucks, but JN is your path to OS independence.

Don't bother pushing this stuff out to Twitter into Lunder-Vand, which they
don't even know yet is named that. Some day a "--Mike L" fan will discover this
here and go "oh! Premium really un-published content which is also fodder for
that book he's working on. And it's his even less filtered day-to-day thinking
as he hashes through a problem.

    When you get
    Started for the day
    You must reset zero point
    And if you can, you can do
    Most anything.

My zero-coordinate is increasingly becoming Jupyter Notebook, and I'm going to
have to advise that to my followers too. This is strange. It is not just the
generic browser itself that's home. It's a particular code-execution
environment (REPL) IN a browser, and really in Tab-0 or Tab-1 (more on that
soon). Neither is home really any more the ~/ "Home" conventional Unix/Linux
location despite how much I want it to be. It's just so easy to time:

    cd ~/

... as a method of clicking your heals together 3 times. You see? Unix/Linux
gives you a proper home. But because of pesky OS conventions that makes it
/home/username here and /Users/username in some other place, the host OSes
themselves sort of ruin this mostly in all other ways spiritually perfect
symbol-- almost root-- for "go home". But thankfully because this concept of
"home" is something Anaconda must decide each time it's run, you have SOME
flexibility, but trying to change it is setting yourself up for bugs and stuff.
Lean into Anaconda. Embrace the hug. It's going to have a Jupyter Notebook
launcher icon somewhere on the start menu or in applications. Run it and see
what location on your hard drive their default "home" is. It's almost certainly
the native OS's preference, which is most decidedly NOT ~/ when your Linux is
only a subsystem of a host Windows 10 OS. And no, it doesn't mean don't use
Windows. Mac's are fine as well as any self-respecting Unix distro (not
Levinux) with a GNOME or KDE desktop or anything Anaconda installs onto.

It is an important point that I have to keep bringing up that there's something
happening here.

I'm still in the final throws of settling in. Soon...

Most important thing now?

Gotta get that crazy query corralled and all argument supporting. Make your
arguments to IT... not Boss. You've been challenged to rise to the occasion...
so rise!

The music is to fortify you against the background distractions. Shields up!
But check your email and calendar first. Standard dumbass avoidance. It's also
coming up on baking the donuts Friday. Get it out of the way Thursday. Don't
feel the crunch.

Don't think out loud too much, because you're going to publish. But it's safe
to say I've got tables to know. You've always got tables to know. It sucks,
but you always have tables to know. I can look in staging or live. Why not
staging where I won't be blocking? Sure, why not? And even there, it's a view
that you're dealign with and not a real table. It joins from 3 sources and is
large and intimidating to a guy like me who was stabbed in the back and
forsaken by SQL for it not having led me to sqllite years and years earlier,
and instead spoilt my taste for it completely, because... pile driver! I don't
need a pile driver. I need a hammer. If I wanted a pile driver, I'd have asked
for one. What? Now I have to dba the pile driver? No thanks. Databases are NOT
a welcome addition to your life in any way, whatsoever if you want to stay
samurai mobile. If you're gonna get bogged down, get bogged down with data
buckets of the sort of Amazon S3 or maybe MongoDB. Avoid tables. There's
religion and career-commitment to a sub-sub-speciality there just to be Kung Fu
effectiveness.

Enter pandas. I have to get pandas into fingers.

I'm switching my ACTUAL WORK over here to the new laptop to make myself
portable. Put on the Light Show on my main monitor. There are many other light
shows like it, but this one is mine. Show the heartbeat. Show the heart. Show
the green. Show the mean. BE what you advocate. Rain it gently down on those
around you. They'll be feeling it soon.

Step #1. Ingratiate. Be your affectatious self, but respectfully. Use your
laptop with the quiet keys when you can, but when you ARE working on the
work-provided computer (it's nickname is staticlenovo). It's been put in my
wide-screen multi-monitor configuration. And that means something OTHER THAN IT
as the 3rd screen off to the left usually (but I can do right) so that I've got
a 3-monitor system as spread out and taking-up of space as anyone around me,
even on a tiny desk.

Remember, you've pretty much ALWAYS either got to be running the work-provided
VPN or HMA Pro because you either need access to the firewalled Amazon services
here at the office (or at home) over external networks like our guest wifi one
here that everyone uses. So remember if my database connection stops working on
my new machine, which I'm always walking around with, so it's all about running
the VPN for work... and at home at Urby Staten Island where I'm always on the
broadband down in the lobby. When I'm not cutting wires unlimited streaming
2-phone family-line 50GB unthrottled/mo T-Mobile style, I'm leaching off the
Urby wifi. Haha, can't wait for this journal to be discovered. Nobody's going
to know what to make of it. My phone keeps cycling on and off. Keep an eye on
it and make sure I've actually tested it.

Relax. Go look at the SQL. Just look at it. Exercise

Okay, I'm looking at the SQL. I'm not doing any relaxing... okay. Relax.

Data MASTER. I'm not that yet. This is the trial by fire stuff.

Get the barebones code that connects to Redshift. It's sitting in a file I'm
using every day. And in principle, you're just stepping into an existing SQL
statement changing a few things here and there. It's all just Python string
manipulations. I'm going to take the power of Python string manipulation to an
existing gobbledy

    q = '''SELECT Top 10
        blah,
        blah,
        %s
        lots
        more
        stuff
        ''' % 123

Okay, that works. But this is not the sophisticated type of string formatting
that I know is available these days. How does that go again? Google new python
string formatting... ugh, the exhaustive version is
https://www.python.org/dev/peps/pep-0498/ but the lite one is
https://pyformat.info/

Ooh, it looks like this:

    '{} {}'.format('one', 'two')
    '{1} {0}'.format('one', 'two')

Sexy, sexy. So you can pop them off a list OR use a sort of RegEx
back-referencing. Clever. That second one will definitely be it, because I'll
be using the same date-range over and over. And I have to DEFINITELY watch my
parenthesis. Incorrect order of operations would totally nuke this puppy, but I
don't see that much parenthesis in this. Okay, test the new format:

    q = '''SELECT Top 10
        blah,
        blah,
        {1}
        lots
        {0}
        stuff {1}
        '''.format('one', 'two')

Okay, this is the marshalling. I'm going to have specific date ranges, which
are actually already created. There is another SQL statement. I'm going to be
looking for certain groupings where the URLs are found in a certain sub-set of
URLs. I need to filter that sub-set of URLs based on a bunch of conditions.

And now's when it gets real because I'm far enough along to work on the ACTUAL
query. This is where the rubber hits the road and sanitization no longer
possible in my notes. Peace out.

--------------------------------------------------------------------------------
## Thu Mar 22

Joan. Pronounced Joe-ON. Remember it! This kind of shit is important, and you
call yourself a wizard. No, actually I don't. I aspire to be a wizard. I
partake of the wizardly arts and tools to do so, but I do not pretend

Marshalling. Always be marshalling your forces. This desk-and-office location
both matters and doesn't matter routine is going to be hard to keep up if I
don't make it true, pronto. There is a lot of slack cut around here for
affectations, but I'm chock-full-o-affectations. I'm not sure if they're ready
for another Matt Downs, whose light-symbol of excellence I keep as a talisman
behind my abacus, which I keep around because you know, you never know.

Ohhhh, this is going to be interesting. The Surface Book 2 is for journaling...
personal journaling with timestamps and things. This is the way I type away
like a madman and don't bother anyone. I just paid about $3,000 (after warranty
and taxes) for a way to silence the one most objectively annoying affectation
about me-- my love for high quality mechanical keyboards, of the preferrable
buckling spring variety, but I like being reasonable and Cherry Brown will
suffice. I'm on the dasKeyboard Silent Pro, which is anything but silent. They
have renamed it since my purchase. Of course I'm publishing this. Labels are
important, and the way I've expressed it here really gets to the point of
everything.

    Money's not really important to me
    So, why not spend it
    On a top of the line laptop
    And get a lot more pleasure
    Out of all the individual little
    Now-moments that I'm trying to produce...
    ...Well, right now.
    In the Now.

In reply to someone on Twitter about URLs with no hate.

    While technically true and I do heart this
    There's a critical point that you cannot miss
    It's on the tip of my tongue... no need to send it
    The bell was rung. It's our Dearest #Amendment.
    by —Mike L
    #NewPoems for a #NewAge

On Martial Arts:

    Marshalling is working
    Though often looks like shirking
    I'll tell you why it's not
    Now listen up...

Johnny Stay Focused

    Let the real work begin...
    What? Huh? Oh.
    Yin emoters have no shield.
    Ugh! Color your sound.
    I need Apple.
    iPhone dead.
    Ugh.
    I'm no music person
    But those songs
    That playlist
    Apple's got me
    Until I make my
    Music cloud-mobile.
    Johnny B. Goode.
    He could filter out chatter
    Just like ringing a bell.


I think I'm going to take on the persona of a critically insightful Statler
Green Lantern, taunting the easily taunted with poetry that drops undeniable
but painful truths around indiscriminately like Anvils. If you happen to get
underneath one, sorry. Don't read what I write. It wasn't aimed specifically at
you, and I warned you I was doing this here. So you know, South Park disclaimer
and everything if you take any of this shit personally. I fling it freely and
take quite a bit of it myself, secure in my knowledge that you're just
British-emulating pompous asses and it quickly passes.

All I'm doing here is really just talking freely into my personal journal
anytime, anywhere. This is on my shiny new laptop that's like always on me now,
and carried around all the time, so who knows when an entry really went in...
so BAM free to publish the sanitized stuff. Wipe it off once and call it
sanitized.

I'm going to rock around the clock today.

--------------------------------------------------------------------------------
## Wed Mar 21

Okay, I'm still going to "cut" journal entries, but now definitely it is to
label the posts. I have a macro @j set up to create a new journal entry. So...
so, get that email to your boss out to let him know you're working from home
and that all is well. Make sure all is well, and that on work VPN you can hit
Redshift... running query. As soon as CSV's appear, my answer is a-ok! A-OK!
Pshwew! Send email... done. Okay. Think EVERYTHING through.

Don't feel like you're going to push everything here out to Pipulate's leaky
journal. You're not. Write freely. Don't inhibit yourself. Strategize when and
how you must. This is your safe place, which even if it leaks someday won't
cause you too much grief, but in the meanwhile isn't going anywhere online
that's supposed to be accessible to anyone. But like Github's secure.

Okay, now that it's confirmed, let's do some serious shit here. Go back to HMA
and start pulling down files locally you want to get off the Microsoft Cloud.
That's gone on long enough. Consolidate on Google and make Microsoft 360, even
at their $60 level, optional. Everything about Microsoft now should be optional
except taking advantage of some killer hardware and a decent embedded Linux
sub-system. Don't hold it against the hardware that what we call Windows 10 is
up there in control. There's a word for that sort of stuff. It's called a
driver. Windows is now a driver for Chrome (or Chromium if you prefer) browser
and the Hyper.is Unix Shell terminal program built on Electron, which is a
re-porpoising of Chrome components... so tight. Tite. All round.

-------------------------------------------------------------------------------
## Wed Mar 21

Well, here we go. A new work location, a new laptop, a new mission in life and
view on the world, and definitely a new attitude.

Installing HMA Pro! VPN (Hide My Ass) so that when I'm not on the office VPN, I
can be here on my own at Urby, where the WiFi is open and the passwords are
a'flying. I've got to talk to them about that. The proper way to do this is to
have a secure WiFi network and freely advertise the password. With all this
decoration around the place, they could use framed password art and it would
still be more secure, because at least then the network traffic would be
encoded. Same with the Subway. Sheesh, people! Just because your browser and
most websites these days are using are using SSL security (thank goodness), not
EVERYTHING is secured, like cookie data in the request headers, which just
might carry a hijack-able token. People, don't use open WiFi without
protections. Services like HideMyAss are only like $60/year and have so many
local end-points these days, the slow-down of your surfing and even streaming
is hardly noticeable.

Wow, having color coding turned on in markdown really does make a nice little
difference in the journaling process. Looking at even just a little bit of
color adds some sort of emotional content. I get it. Don't know if I like the
colors, but at least I'm being made aware I need to think about it. Also,
without the wide-format 16x9 HDTV format of desktop monitors where side-by-side
terminals are preferrable because you have plenty of horizontal space to work
with, on a laptop like this I need to choose between 80-columns nearly filling
up my whole screen (zooming-down occasionally for wide-format programming), or
looking at tiny energy-sapping fonts all the time, reproducing the side-by-side
80-column configuration I used when in "static mode" sitting at my desk.

Oh, God, muscle memory is important. And no, I'm not using the Lord's name in
vain here. Muscle memory is one of God's true gifts, and so denied to us in
everyday tech. Okay, so HMA is done installing, and I quite the work-provided
VPN and am trying my own. It connects. Using HMA Fast Mode, because who cares.
This is not for anonymous surfing from anywhere in the world, though I'll talk
plenty about that later. Rather, this is about just a minimum bit of protection
against identity theft on public open networks shouldn't be such a thing,
people COME ON! Okay, Google pushing all websites into end-to-end security
helped, but hijacked cookie tokens and stuff. Use protection.

--------------------------------------------------------------------------------
## Tue Mar 20

Okay, that was interesting. Next? Okay, the big project for today. It's still
about those revenue columns. Wow, that was a bigger project than I expected.
Okay, hit home the going back a whole year thing. But definitely be cognizant
of the fact that you now want to REGULARLY push out Pipulate and PrivateJournal
commits together before you leave at the end of the day. There will ALWAYS be
changes to pipulate now too.

That's all about just sitting and looking at the existing SQL that makes the
join and understanding how I would go about turning that into a filtered
sub-set of that view, applying both:

- The date-range filter (in several places and switching to dual-boundary)
- The chained-up URL where condition that will have (ooo) issues.

Wow, with this new datestamp situation, there's no longer to start a new
journal entry. The whole idea of CUT! is gone. Just gone. And I think I may
like it better this way. It takes off a lot of pressure. This is the test of
whether... yep. The .vimrc change took. Good. It will be nice to have
color-coding in my markdown file in vim now that it doesn't need to have a
.html extension for my old... what was it? Strapdown.js, I think. It was a very
good method for its day to push this out for every-day consumption where I
could use what was it? Hotbox? To watch people read my journal from all over
the world. Ah, those were the days. But alas, no. Now you read this shit
through Github in the miklevin/Pipulate repo, or nowhere. Good luck, haha! I
don't need no stinking voyeuristic JavaScript. There are more important
Noosphere eggs to be frying. Let's get to one.

I actually want to associate this challenging new in-Jupyter Notebook SQL work
that I'm doing with my new laptop. My goal is to be able to go home tonight,
and through both VPN and a repo-less way of transmitting simple sample code for
Jupyter Notebook around, be doing this "revenue column" work. I'm basically
joining tables from all over the place. But what's worse, I'm reaching for some
really valuable data that has all sorts of challenges in reaching... hmmm,
yummy and perfect! Okay, I've got this. No problem.

Problem is, I'm changing floors at work and I generally do my best work... Ah,
switched. I was going to say on a loud keyboard, but I couldn't bring myself to
type it so loudly. When it's quiet here, switch to the laptop.

Wow, always having 2 journals loaded, now with the first named journal.md and
the second named leakyjournal.md is a real kick, let me tell you. How such an
obvious and uber-techie solution to pushing out sanitized private journal
excerpts was so obvious and right under my nose for all this time makes one of
the important points I want to make in this book (the book that this is going
to be source data for) is that light touch solutions are almost always there.

Light touch has got to be one of my catch phrases for all of this Alice in
Wonderland tech analog book I'm making. Wow, things are falling together. Did
you buy the wrong hardware or take up the wrong language years ago, and somehow
feel committed to sticking with it, even though it's draining your soul? Well,
good for you! Dynamic growth is scary, and isn't for everyone. Me? Let me keep
bearing down on this Linux, Python, vim and git track. It's a good one.

But portability of Jupyter Notebook like copy/paste locations that can be
shared between machines... and maybe even...

--------------------------------------------------------------------------------
## Tue Mar 20

    let @j = '/Bginning of Journal^Mo^M^M^M^M^[kkkk80i-^[j! date^Mi## ^[^Mjzzi'

...becomes:

    let @j = '/Bginning of Journal^Mo^M^M^M^M^[kkkk80i-^[j! date^MwwwD0i##^[^Mjzzi'

It's really that simple. Changed highly detailed timestamps from the Unix
(Linux, of course) "date" command from highly detailed to just:

    Tue Mar 20

...with the addition of:

    wwwD0

...somewhere into a macro, which I keep in a .vimrc file, which I keep in a
repo called vim in a public github repo so that I can pull it down from
anywhere, get the idea?

As an added bonus, if I leave my cursor at the top of the pipulate version of
the journal, when I switch to it with a :bn (for buffer, next in vim-speak) I
know just hitting the p for paste and then saving it, and then going back to
the top of the document and hitting :bn again sort of "stages it" both to be
published on the next inevitable commit and push of changes to the Pipulate
project from this machine, but it's also staged for the very easy publishing of
my next bit of stuff. No fancy system-building. Just one file in
/usr/local/sbin so that every time I open a new terminal, I can just type:

    j[Enter]

...and have both journals loaded for easy permission-controlled publishing, yet
all from just vim and git. No graphical OS really even required here. This is
less than wristwatch-level power you're requiring here to host your
journal/publishing system... for life. Just add Internet connection and common
free stuff.

--------------------------------------------------------------------------------
## Tue Mar 20 11:06:48 DST 2018

Okay, I have a lot to do today, but first it's time to eliminate accurate
timestamps in my private journal macro. It's been attempted to be used against
me even one little bit, so it's gone. But none of the actual benefits of the
journal itself will be gone. Nope, rather my loud and very distinct inner voice
is going to not be talked-over, and it's going to go, yup. Solution provided. I
control the timestamps. I control the reality. Timestamps are only as accurate
as the day's date. Morning, night, who knows? There's some sense of linear
sequence, but I think out loud a lot on my lunchbreak and on the subway now
with my Surface Book 2 laptop, where I can work anywhere quite well to be
always-there, always-on and at my own expense for the best laptop in the world
right now available-- although middle-of-the-line, because I'm not made of
money. I just like my tools. And I think I need to assert myself from time to
time to keep this situation and the opportunities here viable, and me free off
all the signs of burn-out that have already set-in after just 2 years. Nope.
Fix or leave. Fixing begun. Timestamps...

--------------------------------------------------------------------------------
## Tue Mar 20

Beginning of... oops can't type that or I'll mess up my Macro. Time to get
a'crackin'. My mission today is this SQL Query thing to go back a year ago in
revenue numbers... wow! I should of done that yesterday... or maybe even
Friday, but wow. The office move, the new laptop freeing me to work anywhere,
and all the settling in, which is... oh, let me tell you about it! But wow, can
I do some cool samurai data moves on that thing now. I need a more full-time
built-in WiFi, and I was hoping for... wait! I'm going to publish this. I know
that. This is a critical part of the Datamaster journal-- calibrating one's
tools for maximum effectiveness under all the conditions you're likely to find
yourself in. For too long, I've used old Mabook Airs... 3 of them, to be
precise, haha! I have 2 now still myself. Gotta set Adi up on one, but they're
so old-school: no touch-screens and high-res artist's stylus. What's that you
say? Neither do modern Macs? You've got to be kidding, that's got to be a
joke... what? At least their Phablet has a Stylus so that Differently Thinking
Artists can... what? No stylus, either? What happened? Does Apple still
exist... oh, a consumer goods company yous say? Maximum profitability, sheep,
Jobs is dead and all that? Okay, got it. Still wearing my Apple Watch and
making the SE my wallet-phone. The NYC 212-NYB-1337 number is getting ported to
the Note 8, because I needed a phone-number as cool as everything else in my
life, now that my transplanted roots are really beginning to set in... here...
in New York City, where I live with the best view of it right on the edge of
Staten Island. I've finally gone UrbyLife.

Okay, I still have a little publishing resistance because there are some
annoying kung fu keyboard moves of loading another file on a different path
into the second vim buffer. I can totally do it, but I'm fatigued just thinking
about what that would take.

    The light! The light!
    The lite, the lite, the lite.
    So, fight! So, fight!
    And fight and fight and fight.

Even on this floor, there will be big-time mental distractions. The sound of
your inside voice has to be as loud as the chatter, or else people won't
realize their chatter is a part of your background noise while you're trying to
work. That's okay. That's the cubicle deal. People type, and I'm using a very
high quality keyboard, thank you very much. And I shouldn't HAVE TO try to
drown it out with headphones blasting music into my head, and I'll damn-well
talk about it as a focus and survival strategy for creatives in the cubicles of
modern business, readily. It's a fine topic to discuss, especially at the very
moment it's an issue, and you need something as your ohhhhm to regain center,
and get back to some important work.

Okay, there.

Now where were we?

Oh yes, make it so that publishing this will be nice and easy from here on out.
And that means either a something.sh in your current directory (which you'll
never be quite sure you're in) or putting it somewhere in your path, and
chmod'ing it to have +x permissions (execution). So, this is your second step,
because it is true, everything is a LITTLE BIT difficult. They used to joke
about Unix that that was intentional to make an elite class of techs, and well
yeah, sorta. It's called smart enough to appreciate inside jokes, and it's
important in the Unix world, which WAS a priesthood even though its progenitors
were badboys, because of the great commercial and proprietary potential of Unix
to vendors like AT&T... and Novell... and SCO. Oops, proprietary was something
special, was it? Not when it's the commodities, and basically free because it's
only already-ripped-off data, because it's digital data. Blackbox copying has
inconsequential cost, which is what Linux and RMS did. So...

So, bash shortcuts in sbin. Sbin is a funny thing. It's supposed to be these
tiny little one-off script files that you plan to use a lot, and they're still
usually script or bash or shell files. They're all sort of the same since bash,
the "Bourne-again shell", became so durn popular. It's got to be more than just
the basic vanilla Unix "shell" with no command-line history or completion, so
everyone at least uses the first mega-popular one that nothing else ever quite
displaced. So, the language flavor of Unix scripting you should be using is
bash, and they usually just have a .sh extension for shell.

Okay, getting there might take a little while but the payoff is enormous. This
entire seeing the sausage factory process of permanently improving my
day-to-day workflow is being exposed here in the Pipulate repo for everyone to
see... haha! But the world is different forever once achieved. Everything
hinges on moments like these, such as the next time I want to publish like this
won't be anywhere near as difficult.

Keep my go/zd gnu screen session going that shows my every 10-minute heartbeat
after the daily regimine of scripts stops running... or really is just paused
waiting for later in the day when the speed-checks begin, so it gets a fair
assessment of the speeds of different sites (can't run that during the night).
But that report will probably be changing now that Google has an site speed
check now for almost precisely the same scorecard type thing. So much I can gut
and take a sawzaw to, and build newer better stuff to replace it... easily and
more easily than maintaining the old stuff, and that's like one of the big
points about having an employee like my. My stuff is only built to last for
about a year until realities change. Lean into that. Allow scrap and rebuild to
occur, but don't keep me playing little dutch boy and the dike. If a dam's
going to bust if left unchecked and I've said so a lot, then I'm just going to
let it bust. I'm not paid enough to keep old dams from busting AND building new
ones. That's a losing proposition, so I've got a plan.

That plan is sbin.

Gotta always remind yourself of the location.

It's an odd incantation, but this is it:

    echo $PATH

9 times out of 10, it's going to be /usr/local/sbin and it's going to be the
first thing in your path. Understand that, and you're going to understand a lot
about Unix and Linux. The next step, I'm going to tell you to do in vim as your
frustrating and fateful first encounter with the big green monster. Wanna be a
badass tech always packing sharp quarrels in your quiver that'll really make
'em shiver when they see the kind of tech who is really good as heck. Oh, I
don't even need a .sh extension.

    sudo vim /usr/local/sbin/j
    :i
    vim /home/journal/index.html /mnt/c/Users/whome/github/pipulate/theleakyjournal.md
    [Esc]:wq
    sudo chmod +x /usr/local/sbin/j

Left out some details like how you should hit enter. Wave. Quit... tested! Wow!
Now, go publish this shit.

--------------------------------------------------------------------------------
## Fri Mar
### Getting down the rhythm of the Pipulate workflow

You lost the flow. Time to re-establish. These things are taking you wayyyy
longer than they should. I've got idea... I'm going to change my vim macro to
only give the day in the timestamp... hahaha! Only the day is important to
anyone who lacks the ability to see when the git commits occurred-- hahaha!
Wow, I've become a tech asshole. You people have to watch me. I really don't
want to become what I hate, those Green Arrows can eat my Blue Beetles. But not
until after the work-and-hand is done. So far, we have...

- Templates are for purple cows
- Whipping docs get nuked for morbid
- Copy from a Pipulating GSheets (create consistent compelling language here)
- Copy from the Purple Cow farm.

Now, you've got Whipping Doc with no more tabs than what you absolutely need...
not quite true. One blank sheet may still be in there, which you can delete
because you don't need anymore.

Good language developing: "Oh yeah, that's a pipulating sheet. Don't reorganize
those columns (or do) because that's pipulating live. It's a pipulating live
pipulating sheet. Don't pipulate with me, I'll pipulate your pipulate.
Recursion limit reached."

Okay, recover state...

- NOW ADD NEW TEMPLATE COLUMNS INTO LOCATION

Ah, Newspace! A purple cow in the cow farm need not a column or row more than
it need. It should indeed be pruned so you can click the copy-whole-spreadsheet
magical place in all spreadsheet software. That is VERY GOOD. This is the sort
of non-system system invention that Pipulate should be built from. Just know if
you do these such-and-such obvious-in-hindsight things (trimming unnecessary
rows and columns) everything will go more smoothly in your Pipulate workflow...
something that is very worth getting worked-out just-so because of the
effortless mastery things like fixed-position brings to them over time. Every
fixed position where you can re-acquire home and recalibrate and regain state
real quick is a treasure.

Newsflash: Conditional formatting doesn't copy-paste even with "Paste special"
between sheets. Consequently, there's definitely got to be a lot of
right-clicking on tabs to "copy them into" other sheets. That seems to preserve
it, but there's none of the required formatting in my Purple Cow Farm template
tab, which I realized late in that project. And I fixed it in the Whipping Doc,
but I have to copy it back from the Whipping Doc to the Purple Cow Farm... wow,
this is going to work.

Okay, confirmed. Copying sheets through GSheet's "Copy to" on the Tab's menu
preserves the conditional formatting... pshwew! Purple cows can stay purple.
Oh, always color-code a the tabs in The Purple Cow farm purple... color coding
is going to be some powerful stuff in this non-system system.

--------------------------------------------------------------------------------
## Fri Mar

Okay, when doing new work, the work-rhythm looks like this:

Make sure the Purple Cow Farm has your template checked-in (so to speak).

Nuke your whipping-doc for morbid. Know 2 things are about to be zapped into
there. You are merging 2 source-documents:

- Your live-deployed GSheet that's back-ended by "scheduled" pipulate.
- Your template from the purple cow
- Copy-to Recent from the "Tab" menu in GSheets is going to be a common thing.
- Once a tab is copied that way, it gets renamed to "Copy of [Old sheet name]"

--------------------------------------------------------------------------------
## Fri Mar 16
### Blank The Whipping Doc for Morbid. It's the only way to be sure.

Okay, now down to business... again. And this time for real. This is very
serious business. But my distractions were in forming a very focused mental
model for this type of work today and FOREVER FORWARD MORE IMPORTANT THAN IT
LOOKED distraction. Tired of leaping for peanuts.

Speaking of speaking my mind. I know it's probably politically incorrect, but a
WORK-IN-PROGRESS document is a whipping doc. It's got a very powerful concept
there. You can blank the whipping doc. It is wise to blank the whipping doc, in
fact because if you have a Purple Cow Farm with your format in it, All other
instances than what's live in-scheduling will just muddle don't force a rhyme.
vim out!

--------------------------------------------------------------------------------
## Fri Mar 16
### If I Saw a Purple Cow, I'd Pick Out a Good Nickname

Time is an illusion. Okay, Purple Cow Farm in-hand, we have a solid "from"
place, once our template-work (sculpting light) is done in whatever, wherever
format woo hoo everything-independent where we can be. We copy all that
artistic header-area stuff of the WORK-IN-PROGRESS document (anything, anywhere
like Excel or another GSheet) into the Purple Cow document. You ALWAYS include
the first data-row, which is the row usually immediately below your frozen
title rows. There's some ambiguity around what we call this area, but I'll use
header for consistency with typical office-speak. So, we put the complete
header and first data-row into its own tab in The Purple Cow Farm. Things line
Red/Green color-coding rules get carried in that first data-row, so it's really
important. I wouldn't try blanking the data in there, or you're in for all
sorts of accidental formatting-loss issues. Just assume all the data in Purple
Cow is for-position-only (FPO). Okay... now we have a destination document.
It's where we "blend into" and should be the SAME as your work-progress
document, so you don't have to be giving out new Google Sheet URLs all the
time. Even the SEO in me screams out no to that concept. WIP (work-in-progress)
documents should get good strong nicknames and have a long life as such a
kooky-nicknamed thing... until you rename it for a demo to a stakeholder who
doesn't need to see it by that name. But then, it's almost an inside joke that
it's really the such-and-such document, because you've touched them on an
emotional level with a just-so-perfect nickname...

And that my friends is SEO. Walk the walk so you can talk the talk... be DEEPLY
engaged in the game by partaking in all the plentiful Noosphere being created
by every move Google makes... every step it takes, we'll be... oh wait, it's
watching us... nevermind.

--------------------------------------------------------------------------------
## Fri Mar 16
### Just Invented Purple Cow Farms for Templates

I just hit on a very, very powerful method. Why just use one journal in vim
when you could be using two! One of them in a private git repo and the other in
a public Github repo, but with no special effort taken to format or publish it,
besides naming the file with a .md extension and putting it in the parent
directory of a repo I think I'll be driving a lot of eyes to and think I'll be
able to turn this into a good lesson in iron bars to not a prison make nor
cubicles a circus. Minds both intent and focused can still squeak out a
workplace. As non-technical people suspect and sometimes fear, the shell-game
in doing very advanced-seeming stuff in tech requires a lot less actual work
than what it appears. But that cover of being busy and stressed-out and always
intently working on something is very important. Mechanical keyboards that you
can feel click under your fingers is important too. Get into the zone whatever
way you can, and if that means throwing up a shield of better not interrupt,
then so be it. 1, 2, 3... 1? Templates are PURPLE! MAKE YOUR PURPLE TEMPLATE
DOCUMENT. A purple cow farm. HAHAHA! You sometimes look for the proper amount
of ridculoustemity in your nicknames. Ohhh, push this out.

1, 2, 3... 1: Go find your Purple Cow.

--------------------------------------------------------------------------------
## Fri Mar 16

    Different rhymes for different times
    And if you don't renew 'em
    From time to time, you'll fail to climb
    And fall down in a ruin.

    Purple is for templates now;
    The other colors taken.
    Make them be your Purple Cow
    To never be forsaken!

    I've only got one document
    That's named The Purple Cow Farm;
    Templates-tabs-- from there are sent
    With minimum of brain-harm.

    The Purple Cow will teleport
    The columns where they function
    While you try to stop a fork
    Off version we be junkin'

--------------------------------------------------------------------------------
## Fri Mar 16

Make donuts. 1, 2, 3... 1? Source Templates! It's all about reflecting the
right light with the proper incantations. Everything will shine through your
Google Docs templates, which you really should set up ahead of time, because
although you CAN apply some formatting with PyGal which apparently doesn't use
GData but something else more formal under the Developer Console (GData is so
old it predates API-unification under-console). I need to get this stuff out,
because it's important about Pipulate. Getting started on a project in the
morning where ambitions are high because they realize the: if Data Samurai,
then following views we've never before been able to consistently:

- produce
- make readily/easily available
- yet still secure the data

...that one would thing should easily be possible. It's not. But I'm here to
solve that. You're gonna have to drink some Koolaid, so ya had better get used
to it. What, you think Google is going away? What, you think the search game is
going to be disrupted because of some AI-startup? Forget it. A 10x early-mover
advantage in this game is exponentially more than you think. Thinks are
learning and those learnings are persisting and trickling out all over have its
input improved from all over the place... not human by a long-shot, but a damn
bigger chasm that newcomers need to cross than you can imagine.

So, why even try.

Different game, lads. I'm in a different game, with what I hope is another 20
years of exploi... ahem, exploration left to do.

Forget the #xbook tag. Just publish in the Pipulate repo. This is what you were
born to do. vim out.

--------------------------------------------------------------------------------
## Fri Mar 16

I'm just kidding. I won't leak. But I'll probably sanitize as I type so that
when I copy/paste daily journal entries over here, I won't have to do much
editing. Consider this a history with the most recent thoughts posted as an
entry at the top. Let's make up a word for this... oh, it's on the web, and
it's a log. I know! Let's call it a blog. And here's my first copy/pasta...

--------------------------------------------------------------------------------
## Fri Mar 16

1, 2, 3... 1? List.

You will have various 1, 2, 3... 1? List's in your life.
https://docs.google.com/spreadsheets is one

This is because Google Sheets is 80/20-rule good enough. And I will go into
that a lot more soon. In the meanwhile, I'm thinking to myself how this gets
published and pushed out in a reasonable way, and I'm thinking to myself, the
Pipulate repo, dumbass! There's going to be some eyes on that thing, and this
maybe forever forward in the quite interesting by now never-rebased but
definitely should have been but keeping it that way for more badassitute oughta
watch my mouth paid my dues on Jupyter Notebook now and appreciate what I've
got because... Flask version of Pipulate... OMG! I needed nested bubbling
yields used generically through Pipulate-compatible functions if you wanted
that twinkling UI-feedback that could be sent on the same response that was to
the original page-request, just don't stop building the page and use that no
ajax webserver tech required cause it all uses the highly compatible magical
capabilities of modern browsers to pull it off no JavaScript libraries required
genuingenuity. BAM. Should'a started that project on Python 3 where yields
actually could nest and bubble. Oh, but the complexity, and the trap had it
really worked well... would not be on Jupyter Notebook today really
appreciating it for the miracle the iPython and Continuum.io people really
pulled off there.

Okay, that was my "I am a true Samurai-repurposer of tech once I've aquired it
old'skool real. Oh there I go again with hyperbole. See! I can't even just say
hype. Well, that's me. Welcome to full-on corny nerd. And it's going in right
here, because performance art. Bust-out-ittude and other crazy made-up SEO
words because that's it. I'm an SEO. I'm here to walk the walk while I talk
the talk, and if you're not out here doing something interesting on Github,
then you're not out here. STOP! Reports checked. Now, bake donuts. Recover this
state. It is important. vim out!

--------------------------------------------------------------------------------
## Fri Mar 16

It's time to bake the donuts.

No, first check the reports!

And get into the mindset of santizing this again as you write, timestamps
removed of course in a time-displaced published version... who knows when this
occurred unless you're reading over my shoulder. Oh, permissions and
securities, and the philosophy behind your thoughts truly being V for Vendetta
versus eventually enough on the Cloud... well, whatever.

For now, we check reports then bake donuts... then stop and survey the
landscape.

- What's most broken?
- Which work gives us the most bang for the buck?
- What plates need spinning (think about 3rd or else there goes your day)

--------------------------------------------------------------------------------
## Thu Mar 15

Might as well be on the best. I want to be on the best hardware of my life
while I'm doing the best work of my life.



