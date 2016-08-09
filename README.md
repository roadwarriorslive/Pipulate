See SEO Notebook in use here <a href="https://youtu.be/DVZz-Mld0M0">https://youtu.be/DVZz-Mld0M0</a>

# A Letter to SEOs

Greetings Diehards,

Now you have a machine gun ho ho ho. If you know that quote and are in this
biz, then hello old-timer. If not, then welcome millennial newb! This is where
Pipulate is moving. The Jupyter Notebook user interface is perfect for what I
was trying to do with Pipulate, and is way better than anythign I could build.
So, let's jump on the same bandwagon as all the Data Scientists who are
discovering and adopting Python for science... but our science is SEO!

It's 10 years after HitTail, and I've done a number of interesting things
working the biz, here in New York -- even though I jumped from in-house (where
all the interesting work is) to agency-side (where all the PowerPoints are). I
was the SEO for Apple, Kraft, JCPenney, and was even at the top of the Empire
State Building for awhile. And now, this is where I'm hanging my hat while the
dust settles around RankBrain, and we see how our industry has transformed
again.

As a father of a 5 year-old, I am recognizing parallels with Google "growing
up". Machine Learning techniques will get blended in with SEO Notebook if even
just for familiarity's sake, because Google sure is. Their very culture is
gradually being re-written around ML. And as they do, their own secret weapons
improve -- eventually, exponentially. Now, Google has machine learning machine
guns like TensorFlow ho ho ho. This is not yet-another-skynet-warning (YASW?)
but rather, stating the obvious.

Google's AI stuff may never evolve into SkyNet, but it will pass the Turning
Test sometime soon; you can be assured of that.  Our projects should take
baby-steps in that same direction, be lucrative, relevant and fun.
Human-to-machine languages should be no less interesting or expressive than
English, and should be no less pleasurable and beautiful than finely crafted
poetry. And that's where Python fits in. SEOs should learn Python... period!

This is a good place to begin.

## Things to do next here:

- Move this "Letter" somewhere else and do more traditional README
- Explain the implementation in more detail / write a pipulate specification?
- Add all my links to follow this project's development on YouTube and such
- Actually use this system to do various clever things - show use-cases
- "Can" the using of this system, probably an examples sub-folder

## Explanation of Implementation

SEO Notebook is the Jupyter Notebook-based implementation of the pipulation
process that uses Google Spreadsheets for I/O.

At its simplest, you put a partially filled-in spreadsheet, and get it back as
fully filled-in as it can be, as a result of an automation process that follows
conventions that feel intuitively obvious, such as processing the spreadsheet
left-to-right and top-to-bottom, plugging values from rows into functions
named by columns, and then plugging the output into the intersecting cells
until complete. You can use a system like this for such simple tasks as filling
in a set of Title Tag values belonging to URLs, or as complicated as things
that take 2 or 3 passes to create derivative indexes like spin-your-own SEO
Optimization Difficulty scores. Obvious, no? Very easy to explain. I can hardly
believe it's not already part of everybody's (in the data biz) daily process.
Maybe it's a good idea whose time has come.

Different Pipulate implementations against this specification can make
different decisions regarding behavior, to be most appropriate for the
use-case. Past versions, such as the Github repo miklevin/pipulate took full
responsibility for building the UI, with the Flask web framework and other
components. The SEO Notebook implementation does away with even this small
amount of UI development by leveraging the Jupyter Notebook to eliminate the
all user interface development. I expect some of the whiz-bang features folks
have come to expect in a UI will come back as we move this project from today's
Jupyter Notebook into tomorrow's Jupyter Lab, which has much enhanced support
for widgets both for parameterized input (sliders, etc.) and great output
(interactive JavaScript data visualizations).

Google Sheets is additionally integral to this implementation as the preferred
simple way to prepare and receive the output of pipulate job requests.

This implementation is also intended to give strong identities to the 3
sub-components of this project:

- SEO Notebook - the Jupyter Notebook-based implementation of the pipulation
  process (eventually to be base in Jupyter Lab)
- GoodSheet - the package that generically controls access-to and interaction
  with Google Sheets, including handling OAuth2 login.
- Pipulate - a library of functions that can be used within any framework
  implementing the pipulation process.
