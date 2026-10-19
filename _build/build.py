"""Builds the Imperial Shih Tzu Momma site: python3 _build/build.py (writes the .html pages one folder up)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EMAIL = "imperialshihtzumomma@gmail.com"
FORM_ACTION = f"https://formsubmit.co/{EMAIL}"  # first submission sends her a one-time activation email
INSTAGRAM = "https://www.instagram.com/imperial_shihtzu_momma/"
FACEBOOK = "https://www.facebook.com/profile.php?id=100063466035252"
YELP = "https://www.yelp.com/biz/imperial-shih-tzu-momma-santa-maria"

NAV = [
    ("puppies.html", "Puppies"),
    ("our-dogs.html", "Our Dogs"),
    ("how-it-works.html", "How It Works"),
    ("reviews.html", "Reviews"),
    ("about.html", "About"),
    ("contact.html", "Contact"),
]

AVAILABLE = [
    ("pup-gold-girl", "Gold girl", "Amethyst × Beethoven",
     "Gold with a black mask. Sweet and a little shy. Vet checked, first vaccines done.", "Gold Shih Tzu puppy with a black mask"),
    ("pup-liver-girl", "Liver girl", "Chloe × Wonka · Born Jan 17, 2026 · Adult weight about 8 lbs",
     "A beautiful liver girl. Vet checked and up to date on shots.", "Light liver Shih Tzu puppy"),
    ("pup-red-girl", "Red girl", "Chloe × Wonka · Born Jan 17, 2026 · Adult weight about 8–9 lbs",
     "A darling red girl, trending small standard. Also available to a small breeding program.", "Red Shih Tzu puppy among sunflowers"),
    ("pup-rare-girl", "Rare color girl", "Amethyst × Beethoven · Born May 13",
     "Full of character and truly one of a kind. This litter will not be repeated.", "Rare colored Shih Tzu puppy on green grass"),
]

SOLD = [
    ("pup-small-boy", "Chloe × Wonka boy", "Gold Shih Tzu puppy boy"),
    ("pup-black-boy", "Black boy", "Black Shih Tzu puppy boy"),
    ("pup-obi-boy", "Chloe × Obi-Wan boy", "Shih Tzu puppy in a basket"),
    ("pup-gemma", "Gemma", "Blue Dobie marked Shih Tzu puppy"),
    ("pup-bubbles-boy", "Bubbles × Wonka boy", "Dark Shih Tzu puppy boy"),
]

MOMS = [
    ("bubbles", "Bubbles", "6 lbs · Light coat, carries solid black · The nursery's \"mommy\"", "Bubbles, a light colored Shih Tzu with a pink bow"),
    ("chloe", "Chloe", "About 7 lbs · Gold with black mask · Sweet and playful", "Chloe, a gold Shih Tzu"),
    ("trinket", "Trinket", "7 lbs · Juliette × Rory · Born and raised here", "Trinket, a red Shih Tzu"),
    ("honey", "Honey", "Very small · Juliette × Taz · Quiet and mild", "Honey, a Shih Tzu with a pink bow"),
    ("babs", "Babs", "5 lbs · Fun-loving and spunky", "Babs, a white Shih Tzu with an orange bow"),
]

DADS = [
    ("rory", "Rory", "6 lbs · Mahogany red · Very sweet", "Rory, a mahogany red Shih Tzu"),
    ("pilot", "Pilot", "5 lbs · White and red parti · Sweet and playful", "Pilot, a white and red parti Shih Tzu"),
    ("wonka", "Wonka", "About 6 lbs · Liver · Bouncy and cheerful", "Wonka, a liver Shih Tzu"),
]

REVIEWS = [
    ("review-theodore", "So helpful… took the time to answer all our questions.", "Jeff C., Theodore's family", "Theodore, a black and white Shih Tzu"),
    ("review-bowie", "Throughout the whole process she kept me up to date on the puppy and their health and personality.", "Kosta S., Bowie's family", "Bowie playing on a wood floor"),
    ("review-josie", "The time you put into your puppies shows she has been loved.", "Yvonne M., Josie's family", "Josie sitting on a sofa"),
]


def img(name, alt, extra=""):
    return f'<img src="images/{name}.jpg" alt="{alt}" loading="lazy"{extra}>'


def pup_card(p):
    name, title, meta, desc, alt = p
    return f"""<article class="pup">
        {img(name, alt)}
        <div class="body">
          <div class="row"><span class="tag ready">Available</span><span class="price">Starts at $3,500</span></div>
          <h3>{title}</h3>
          <p class="meta">{meta}</p>
          <p class="desc">{desc}</p>
          <a class="btn ghost" href="apply.html">Apply for her</a>
        </div>
      </article>"""


def dog(d):
    name, title, meta, alt = d
    return f'<figure class="dog">{img(name, alt)}<figcaption><strong>{title}</strong><span>{meta}</span></figcaption></figure>'


def review(r):
    name, quote, who, alt = r
    return f'<figure class="review">{img(name, alt)}<blockquote>"{quote}"</blockquote><figcaption>{who}</figcaption></figure>'


LITTER = f"""<div class="litter">
      <div class="pair">
        <figure>{img("pepper", "Pepper, the mom")}Pepper · mom</figure>
        <span class="plus" aria-hidden="true">+</span>
        <figure>{img("rory", "Rory, the dad")}Rory · dad</figure>
      </div>
      <div class="info">
        <h3>Pepper + Rory</h3>
        <dl>
          <dt>Due</dt><dd>October 19, 2026</dd>
          <dt>Expected colors</dt><dd>Gold to red sable with a black mask</dd>
          <dt>Parents</dt><dd>AKC registered and DNA tested</dd>
          <dt>Price</dt><dd>Starts at $3,500</dd>
        </dl>
        <div><a class="btn primary" href="apply.html">Join the waitlist</a></div>
      </div>
    </div>"""

CTA = """<section class="alt cta-band">
  <div class="wrap">
    <h2>Ready to meet your puppy?</h2>
    <p>Send an application to join the waitlist. You'll hear about new puppies before anyone else.</p>
    <a class="btn primary" href="apply.html">Start your application</a>
  </div>
</section>"""


def page_hero(eyebrow, title, intro=""):
    p = f"<p>{intro}</p>" if intro else ""
    return f"""<section class="page-hero"><div class="wrap"><span class="eyebrow">{eyebrow}</span><h1>{title}</h1>{p}</div></section>"""


def layout(file, title, description, body):
    current = ' aria-current="page"'
    links = "\n".join(
        f'        <li><a href="{href}"{current if href == file else ""}>{label}</a></li>'
        for href, label in NAV
    )
    page_title = "Imperial Shih Tzu Momma" if file == "index.html" else f"{title} | Imperial Shih Tzu Momma"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{page_title}</title>
<meta name="description" content="{description}">
<meta property="og:title" content="{page_title}">
<meta property="og:description" content="{description}">
<meta property="og:image" content="images/pup-red-girl.jpg">
<link rel="icon" href="images/logo.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Young+Serif&family=Mulish:wght@400;600;700;800&display=swap">
<link rel="stylesheet" href="css/styles.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header>
  <div class="wrap bar">
    <a class="brand" href="index.html"><img src="images/logo.jpg" alt="">Imperial Shih Tzu Momma</a>
    <button class="menu-btn" id="menuBtn" aria-expanded="false" aria-controls="mainNav">Menu</button>
    <nav id="mainNav" aria-label="Main">
      <ul>
{links}
      </ul>
    </nav>
    <a class="btn primary" href="apply.html">Apply</a>
  </div>
</header>
<main id="main">
{body}
</main>
<footer>
  <div class="wrap">
    <span>© 2026 Imperial Shih Tzu Momma · Yadkinville, NC · {EMAIL}</span>
    <nav aria-label="Footer"><ul><li><a href="puppies.html">Puppies</a></li><li><a href="how-it-works.html">How It Works</a></li><li><a href="apply.html">Apply</a></li><li><a href="contact.html">Contact</a></li></ul></nav>
  </div>
</footer>
<script src="js/main.js"></script>
</body>
</html>
"""


HOME = f"""<section class="hero">
  <div class="wrap">
    <div class="hero-copy">
      <span class="eyebrow">Yadkinville, North Carolina</span>
      <h1>Imperial and small standard <em>Shih Tzu puppies</em>, raised in our home</h1>
      <p>Babydoll faces, sweet temperaments and lots of love. Every puppy is handled every day and grows up around kids and other dogs.</p>
      <div class="ctas">
        <a class="btn primary" href="puppies.html">See available puppies</a>
        <a class="btn ghost" href="how-it-works.html">How to get a puppy</a>
      </div>
      <ul class="facts" aria-label="Highlights">
        <li>AKC registered parents</li>
        <li>Embark DNA tested</li>
        <li>1-year health guarantee</li>
        <li>Puppy starter kit</li>
      </ul>
    </div>
    <div class="hero-photos">
      <img src="images/pup-red-girl.jpg" alt="Red Shih Tzu puppy sitting among sunflowers">
      <img src="images/pup-black-boy.jpg" alt="Black Shih Tzu puppy in a flower box">
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="head">
      <span class="eyebrow">Ready now</span>
      <h2>Available puppies</h2>
      <p>All puppies are vet checked and up to date on shots. Puppies start at $3,500.</p>
    </div>
    <div class="grid">
      {"".join(pup_card(p) for p in AVAILABLE)}
    </div>
    <div class="more"><a class="btn ghost" href="puppies.html">See all puppies</a></div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="head">
      <span class="eyebrow">Coming soon</span>
      <h2>Upcoming litter</h2>
    </div>
    {LITTER}
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="head">
      <span class="eyebrow">Puppy families</span>
      <h2>What families say</h2>
    </div>
    <div class="reviews">
      {"".join(review(r) for r in REVIEWS)}
    </div>
  </div>
</section>

<section class="cta-band">
  <div class="wrap">
    <h2>Ready to meet your puppy?</h2>
    <p>Send an application to join the waitlist. You'll hear about new puppies before anyone else.</p>
    <a class="btn primary" href="apply.html">Start your application</a>
  </div>
</section>"""

PUPPIES = f"""{page_hero("Ready now", "Available puppies", "All puppies are vet checked and up to date on shots. They live with us in North Carolina. Prices are set at about 6 weeks, based on size, color and quality.")}
<section>
  <div class="wrap">
    <div class="grid">
      {"".join(pup_card(p) for p in AVAILABLE)}
    </div>
    <div class="sold-strip">
      <h3>Recently went home</h3>
      <div class="sold-grid">
        {"".join(f'<figure>{img(n, a)}<figcaption><span class="tag sold">Sold</span> {t}</figcaption></figure>' for n, t, a in SOLD)}
      </div>
    </div>
  </div>
</section>
<section class="alt" id="upcoming">
  <div class="wrap">
    <div class="head">
      <span class="eyebrow">Coming soon</span>
      <h2>Upcoming litters</h2>
      <p>People on our waitlist hear about new puppies before anyone else.</p>
    </div>
    {LITTER}
  </div>
</section>"""

DOGS = f"""{page_hero("Moms & dads", "Our dogs", "Every adult is health tested before breeding. Some of our girls are raised by guardian families nearby.")}
<section>
  <div class="wrap">
    <h2 class="subhead">Moms</h2>
    <div class="dogs">{"".join(dog(d) for d in MOMS)}</div>
    <h2 class="subhead">Dads</h2>
    <div class="dogs">{"".join(dog(d) for d in DADS)}</div>
  </div>
</section>
<section class="alt" id="retired">
  <div class="wrap">
    <div class="head">
      <span class="eyebrow">Retired adults</span>
      <h2>Looking for a forever home</h2>
      <p>Each of our girls has a small number of carefully planned litters. When she retires, we find her a home where she gets one-on-one love for her next chapter.</p>
    </div>
    <div class="adult">
      {img("pepper", "Pepper wearing an orange bow")}
      <div>
        <h3>Pepper</h3>
        <p>About 8 lbs. Pepper loves her people and wants to stay close to you. She does best as an only pet and needs a little time to bond. Pet home only, spay required once she settles in.</p>
        <p class="price">Rehoming fee $1,800</p>
        <div><a class="btn ghost" href="apply.html">Apply for Pepper</a></div>
      </div>
    </div>
  </div>
</section>
<section id="guardian">
  <div class="wrap">
    <div class="head">
      <span class="eyebrow">Guardian homes</span>
      <h2>Become a guardian family</h2>
      <p>A guardian family gives one of our breeding dogs a loving everyday home. Interested? Send us a message.</p>
    </div>
    <a class="btn primary" href="contact.html">Ask about guardian homes</a>
  </div>
</section>"""

PROCESS = f"""{page_hero("Getting your puppy", "How it works", "Before you apply, make sure a Shih Tzu fits your life and get any permission you need from a landlord or partner.")}
<section>
  <div class="wrap">
    <ol class="steps">
      <li><h3>Apply</h3><p>Fill out the application. Tell us what you'd like: color, gender and size.</p></li>
      <li><h3>Pay the deposit</h3><p>Once approved, a $200 deposit holds your spot. It goes toward the puppy's price and is non-refundable.</p></li>
      <li><h3>Join the waitlist</h3><p>You hear about new litters before the public. We keep first pick of each litter.</p></li>
      <li><h3>Choose your puppy</h3><p>Prices are set at about 6 weeks, based on size, color and quality. Puppies start at $3,500.</p></li>
      <li><h3>Go home</h3><p>Pay the balance before pickup. Puppies go home at about 10 weeks and at least 2 lbs.</p></li>
    </ol>
    <div class="two">
      <div class="panel">
        <h2 class="subhead">Every puppy comes with</h2>
        <ul>
          <li>Starter kit: toys, collar, bowls and some food</li>
          <li>Folder with vet records</li>
          <li>Contract with a 1-year health guarantee</li>
          <li>A head start on potty training</li>
          <li>Support from us for life</li>
        </ul>
      </div>
      <div class="panel">
        <h2 class="subhead">Getting your puppy home</h2>
        <ul>
          <li>Pick up in person in North Carolina</li>
          <li>Courier delivery</li>
          <li>Out of state: we can refer a flight nanny who carries your puppy on the plane</li>
        </ul>
        <p class="meta">Can't keep your dog someday? We will always take them back or help rehome them.</p>
      </div>
    </div>
  </div>
</section>
<section class="alt">
  <div class="wrap">
    <div class="head"><h2>Questions</h2></div>
    <div class="faq">
      <details><summary>What is an Imperial Shih Tzu?</summary><p>A smaller Shih Tzu than the AKC standard. The AKC does not list Imperial as a separate breed, but the Alianz Italian Kennel Club does recognize it. We breed both Imperial and small standard sizes.</p></details>
      <details><summary>How much does a puppy cost?</summary><p>Puppies start at $3,500. The final price is set at about 6 weeks, based on size, color and quality.</p></details>
      <details><summary>Is the waitlist first come, first served?</summary><p>Not always. If you want a specific color or gender, you may wait for the right puppy while others go ahead of you.</p></details>
      <details><summary>Do puppies come with breeding rights?</summary><p>Puppies are sold with a spay/neuter agreement. A few are offered to small breeding programs, and those are noted on the listing.</p></details>
      <details><summary>I sent my application. When will I hear back?</summary><p>Usually within a few days. Check your spam folder too. If you haven't heard back, email {EMAIL}.</p></details>
    </div>
  </div>
</section>
<section class="cta-band">
  <div class="wrap">
    <h2>Ready to start?</h2>
    <a class="btn primary" href="apply.html">Start your application</a>
  </div>
</section>"""

REVIEWS_PAGE = f"""{page_hero("Puppy families", "Reviews", "Our puppies live all over the country. Here's what a few of their families say.")}
<section>
  <div class="wrap">
    <div class="reviews">{"".join(review(r) for r in REVIEWS)}</div>
    <div class="more social">
      <a class="btn ghost" href="{YELP}" rel="noopener">Read more on Yelp</a>
      <a class="btn ghost" href="{FACEBOOK}" rel="noopener">See us on Facebook</a>
    </div>
  </div>
</section>
{CTA}"""

ABOUT = f"""<section class="page-hero">
  <div class="wrap about">
    {img("parti-blue-bow", "Parti colored Shih Tzu with a blue bow")}
    <div class="copy">
      <span class="eyebrow">About the breeder</span>
      <h1>Hi, I'm the Shih Tzu Momma</h1>
      <p>I'm an AKC Shih Tzu breeder. After many years on California's Central Coast, I moved with my family to Yadkinville, North Carolina, and the nursery came with me.</p>
      <p>I breed purebred Shih Tzus in small standard and Imperial sizes, in lots of colors. I love their babydoll faces and how affectionate they are.</p>
      <p>Every puppy is raised in our home with hands-on care. They're socialized with kids and other dogs, so they're ready to join your family.</p>
    </div>
  </div>
</section>
<section>
  <div class="wrap">
    <div class="two">
      <div class="panel">
        <h2 class="subhead">How we breed</h2>
        <ul>
          <li>Every adult is health tested before breeding</li>
          <li>Parents are AKC registered and Embark DNA tested</li>
          <li>Each girl has only a few carefully planned litters</li>
          <li>Retired dogs go to loving, hand-picked homes</li>
        </ul>
      </div>
      <div class="panel">
        <h2 class="subhead">Our promise to you</h2>
        <ul>
          <li>A written contract with a 1-year health guarantee</li>
          <li>Help and advice for your dog's whole life</li>
          <li>If you can ever no longer keep your dog, we will take them back or help rehome them</li>
        </ul>
      </div>
    </div>
  </div>
</section>
{CTA}"""


def radio(name, label, options, required=True):
    star = ' <span class="req">*</span>' if required else ""
    req = " required" if required else ""
    opts = "".join(
        f'<label><input type="radio" name="{name}" value="{o}"{req}> {o}</label>' for o in options
    )
    return f'<div class="q" role="radiogroup" aria-label="{label}"><span>{label}{star}</span><div class="choice">{opts}</div></div>'


def field(fid, label, kind="text", required=False, auto=""):
    star = ' <span class="req">*</span>' if required else ""
    req = " required" if required else ""
    ac = f' autocomplete="{auto}"' if auto else ""
    return f'<label for="{fid}"><span>{label}{star}</span><input id="{fid}" name="{label}" type="{kind}"{req}{ac}></label>'


def area(fid, label, rows=3):
    return f'<label for="{fid}"><span>{label}</span><textarea id="{fid}" name="{label}" rows="{rows}"></textarea></label>'


YN = ["Yes", "No"]

APPLY = f"""{page_hero("Puppy application", "Apply for a puppy", "Tell us about you and the puppy you're hoping for. It takes about 5 minutes. Applying doesn't commit you to anything. If you're approved, a $200 deposit holds your spot.")}
<section>
  <div class="wrap">
    <form class="form-wide" action="{FORM_ACTION}" method="POST">
      <input type="hidden" name="_subject" value="New puppy application">
      <input type="hidden" name="_template" value="table">
      <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">
      <fieldset>
        <legend>About you</legend>
        <div class="cols">
          {field("first", "First name", required=True, auto="given-name")}
          {field("last", "Last name", required=True, auto="family-name")}
        </div>
        <div class="cols">
          {field("email", "Email", "email", True, "email")}
          {field("phone", "Phone", "tel", True, "tel")}
        </div>
        {field("address", "City and state", required=True, auto="address-level2")}
        {field("kids", "Children in the home and their ages")}
      </fieldset>
      <fieldset>
        <legend>Your home</legend>
        {radio("Type of home", "What type of home do you live in?", ["House", "Apartment", "Other"])}
        {radio("Needs permission", "Do you need permission to have a dog (landlord, HOA)?", YN)}
        {radio("Primary caretaker", "Will you be your dog's main caretaker?", YN)}
        {field("caretaker", "If not, who will be?")}
        {radio("Current pets", "Do you have other pets right now?", YN)}
      </fieldset>
      <fieldset>
        <legend>Experience</legend>
        {radio("Owned a dog", "Have you owned a dog before?", YN)}
        {radio("Owned a Shih Tzu", "Have you owned a Shih Tzu before?", YN)}
        {radio("Researched Shih Tzus", "Have you researched the Shih Tzu breed?", YN)}
        {radio("Surrendered a pet", "Have you ever given up a pet?", YN)}
        {area("surrender", "If yes, please explain", 2)}
      </fieldset>
      <fieldset>
        <legend>Your puppy</legend>
        {radio("Gender", "Gender preference", ["Girl", "Boy", "No preference"])}
        {radio("Pigment", "Black or liver pigment?", ["Black", "Liver", "Not sure"])}
        <div class="cols">
          {field("color", "Color preference")}
          {field("size", "Size preference")}
        </div>
        {radio("Plans to breed", "Do you plan to breed this dog?", YN)}
        {radio("Pickup", "How would you like to get your puppy?", ["Pick up in person", "Courier", "Flight nanny", "Not sure"])}
      </fieldset>
      <fieldset>
        <legend>Anything else</legend>
        {area("about", "Tell us about you, your family and your lifestyle", 5)}
      </fieldset>
      <button class="btn primary" type="submit">Send application</button>
      <p class="form-note">We'll reply by email, usually within a few days. Please check your spam folder too.</p>
    </form>
  </div>
</section>"""

CONTACT = f"""{page_hero("Say hello", "Contact us", "Questions about a puppy, a litter or a retired adult? We're happy to help.")}
<section>
  <div class="wrap contact">
    <div class="info">
      <div><h2 class="subhead">Email</h2>
        <div class="copyline"><code id="email">{EMAIL}</code><button type="button" id="copyBtn">Copy</button></div>
      </div>
      <div><h2 class="subhead">Location</h2><p>Yadkinville, North Carolina. Visits by appointment.</p></div>
      <div><h2 class="subhead">Follow the puppies</h2>
        <div class="social">
          <a class="btn ghost" href="{INSTAGRAM}" rel="noopener">Instagram</a>
          <a class="btn ghost" href="{FACEBOOK}" rel="noopener">Facebook</a>
          <a class="btn ghost" href="{YELP}" rel="noopener">Yelp</a>
        </div>
      </div>
      <div><a class="btn primary" href="apply.html">Apply for a puppy</a></div>
    </div>
    <form action="{FORM_ACTION}" method="POST">
      <input type="hidden" name="_subject" value="New message from the website">
      <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">
      <h2 class="subhead">Send a message</h2>
      <label for="cName"><span>Your name <span class="req">*</span></span><input id="cName" name="Name" autocomplete="name" required></label>
      <label for="cEmail"><span>Email <span class="req">*</span></span><input id="cEmail" name="Email" type="email" autocomplete="email" required></label>
      <label for="cTopic">I'm asking about
        <select id="cTopic" name="Topic">
          <option>An available puppy</option>
          <option>An upcoming litter</option>
          <option>A retired adult</option>
          <option>Becoming a guardian home</option>
          <option>Something else</option>
        </select>
      </label>
      <label for="cMsg"><span>Message <span class="req">*</span></span><textarea id="cMsg" name="Message" rows="5" required></textarea></label>
      <button class="btn primary" type="submit">Send message</button>
    </form>
  </div>
</section>"""

PAGES = [
    ("index.html", "Home", "Imperial and small standard Shih Tzu puppies raised in our home in Yadkinville, North Carolina. AKC registered, DNA tested parents.", HOME),
    ("puppies.html", "Puppies", "Available Shih Tzu puppies and upcoming litters. Puppies start at $3,500.", PUPPIES),
    ("our-dogs.html", "Our Dogs", "Meet the moms and dads of Imperial Shih Tzu Momma, plus retired adults looking for homes.", DOGS),
    ("how-it-works.html", "How It Works", "How to get a puppy: application, $200 deposit, waitlist, pricing and going home.", PROCESS),
    ("reviews.html", "Reviews", "Reviews from Imperial Shih Tzu Momma puppy families.", REVIEWS_PAGE),
    ("about.html", "About", "About Imperial Shih Tzu Momma, an AKC Shih Tzu breeder in Yadkinville, North Carolina.", ABOUT),
    ("apply.html", "Apply", "Apply for an Imperial or small standard Shih Tzu puppy.", APPLY),
    ("contact.html", "Contact", "Contact Imperial Shih Tzu Momma in Yadkinville, North Carolina.", CONTACT),
]

for file, title, desc, body in PAGES:
    (ROOT / file).write_text(layout(file, title, desc, body), encoding="utf-8")
    print("wrote", file)
