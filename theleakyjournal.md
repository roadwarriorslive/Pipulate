--------------------------------------------------------------------------------
## Wed Jan 15, 2020
### Windows 7 End of Support / Beginning of Journal.

Howdy! Today is the end-of-life day for Windows 7. Hope all you high-tech
Luddites who long for a life-long-gone are amped-up for your transition to
Windows 10, or something else equally gotcha-burdened. The world's not perfect,
and if you want to get on with your life, being on the best hardware, able to
play the most modern games, and generally fluent in the platform that you have
to be proficient in (yes, still) is Windows. And as of today, it's Windows 10.
But there's good news. Windows 10 isn't the evil-abode that lots of fear,
uncertainty and doubt (FUD) mongering partisans would have you believe. No
indeed, Windows 10 is a very fine platform. It's time to switch.

And that's so-says someone for whom the old Amiga Computer from Commodore, says
so. Microsoft-as-an-enemy goes back to Windows 3.1 for me, the first
mass-market-acceptable version of Windows, which everyone was sort of waiting
for since the Macintosh came out in 1984 and altered everybody's expectations
of what a computer could and should be. 

I was of the frustrated few who lived the future some 30 years ago in another
life and on another platform. Most of what folks are so infatuated with today
is so old-hat to me that I yawn. Yes, even augmented reality. I owned and used
an Amiga Mandela that mixed interactive computer graphics and reality
on-screen. It just wasn't on your mobile phone as part of a big, fast network.
It was however 1990, and doing such advanced things back then on a platform
nobody really acknowledged as a "real" computer was terribly frustrating. It
gave you a great underdog syndrome, and really positioned both Microsoft and
Apple as the enemy in my mind.

And here I am won-over by not only Windows 10, but Microsoft hardware in
general. And the stuff from HP, Lenovo and all the other convertible
manufacturers isn't too shabby, either. I just bought the Lenovo Yoga C740 for
her, and yes, cheap, well-integrated touch-screen makes a big difference no
matter what those who still advocate Mac laptops would have you believe. 

I've got to get to my work today, and I do that on my Microsoft Powerbook 2
that I carry around all the time, both as my work-from-home machine, and as the
machine I bring to the office to continue working on, even though I actually
have an office-provided Lenovo laptop. I just like being on awesome hardware,
and having my muscle-memory develop on the same keyboard I'm working on all the
time. I don't want to be working on different keyboards all the time, and I
especially don't want my Control and Alt-keys needlessly switched on me,
throwing off my muscle-memory, every time I switch between a Mac and PC.

Next step, comes publishing this stuff easily and daily. I've written too much
that stays here locked-up in my personal journal on a private repository that
never sees the light of day. But this one should be published right along with
my Microsoft Sun-setting Windows 7 Support video, which I'll be pushing out
momentarily. I've always been keen to have 2 text-files always loaded all the
time as a part of my personal journal-writing process. I used to like to
advocate (to myself in my own mind, primarily) that 1-and-only-1 text-file is
best for journaling with for-life, and that's because fixed locations.

However, when arises the issue of actually publishing some of this stuff,
suddenly there has to be the concepts of separate and sanitized spaces. The
place I write for eventual low-friction publishing needs to be actually
somewhere it belongs and with nothing in there that doesn't belong. And so that
means the physical fire-wall between systems that separate (2-different)
text-files can provide. And so... and so... we bring a brand-new textfile
online. Or is that bring an old one back online. Yes, yes! I have this in place
already-- a way to publish first into the Pipulate repository.

1, 2, 3... 1? Go Right! I am always on the left-most virtual desktop on my
ribbon of about 7 Windows virtual desktops. That left-most desktop ALWAYS has
my daily personal journal in vim in a full-screen Unix-like terminal. It used
to be Hyper.is, which is a Unix/Linux terminal built on Chrome Electron (like
VSCode, Slack, Atom, etc.), but today is the "standard" Microsoft Terminal
available now in the Microsoft Store. Just like on Mac when I use Unix-term, I
use the built-in Terminal program, and so shall it be on the other big
mainstream platform. Microsoft tools are not too shabby, and if they're
promoting a unified tabbed-shell for a COM prompt, Powershell or Linux
terminal, then I'm using it. 

And so I am (that's what I'm typing in right now). So when I "Go Right" what
I'm doing is going right from there, 99% of the time to a full-screen Chrome
instance on virtual desktop number two. From there, I can surf from Jupyter
Notebook's home-tab, which by default is ALWAYS in the first tab because I
launch Chrome by launching Jupyter Notebook, and find my github folder and surf
into my Pipulate development repo (pipdev) to look at what files are there. I
could have also done that from the Terminal, but that would have required
opening a new one or dropping out of vim. Here, I remind myself of the name of
the file I always used to have loaded simultaneously. It's theleakyjournal.md.
Perfect.

Getting this going again is a good first step. I think I'll be "re-basing" the
journal. Technically, I'm not rebasing the repo in a git sense or that would be
wiping out the history of the old leakyjournal.md in the pipulate repo. I'll
keep it intact in the repo, but just blank the file and start over. This is why
I go 1, 2, 3... 1? Go Right, all the time. I'm going right to get my bearings,
leaving the mostly blog-like reverse-chronological writing-file that I use for
my daily work journal, and going instead to a github folder inside my "natural"
home directory for Jupyter Notebook, which is also the natural home directory I
use for all my Linux-terminal-based coding that I do (mostly, in vim).

Okay, so now that jogs my memory. My "j" command that I use from the terminal
all the time to start my journaling is located in /usr/local/sbin/. Okay, so I
open another terminal window on virtual desktop #5 and type sbin, which is my
~/.bash_profile alias to change my directory to /usr/local/sbin/. From there, I
sudo vim j. In the file, I can see that I have several lines commented out. I
just swap a few of the lines around, and now my j-command loads 2 text-files
into vim allowing me to copy/paste easily between the two. vim is generally
copy/paste-challenged as a resident of the often-awkward text-terminal program,
but between multiple buffers in the same instance of vim, there's no problem.
So publishing is really just a matter of copying content from this, my private
journal, into that, theleakyjournal.md in my Pipulate repo on Gitub. I'll be in
that scenario the next time I quit and reload vim for journaling... which I
just did.

Okay, so from my using this system in the past, I know I have a "p" macro here
in vim to copy my current journal entry over to that file, inserting it at the
top exactly as if it's a newly typed-in blog journaling entry. However, I feel
I want to blank it first, so I go do that... It went back to March 15, 2018. If
I remember correctly, and I do because I peaked at my ~/.vimrc, all I need to
do is keep the first line of 80 hyphens in place and my macro should work. All
I need to do is press @p at any moment while not in vim editing mode, and this
journal entry will be copied over to the leaky journal in my pipulate repo, and
the first page of my new book will be published.

I'm doing this almost entirely in the vim text-editor on my Ubuntu Linux
terminal running on my Windows 10 on my Microsoft Powerbook 2, pushing up to
Github to do initial publishing. Subsequent journal entries will proceed
through further steps of me uncloaking to engage myself in the mainstream tech
blogging and vlogging communities with a lot I have to say. Exercises like this
take care of "what's most broken", which in this case has been the ability to
push out daily thoughts easily in a very blog-like way, without interfering
with my already existing daily work-flow (too-much). We can always add one more
command my bash profile or sbin directory.













