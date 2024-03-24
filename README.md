# Headless chrome detection sample

## Files
1. `index.html` main file with JS methods to detect headless chrome
2. `check.py` python script to test detection

## Installation

0. Clone repo

1. Install deps (selenium):

`pip install selenium`

2. Run script:

`python check.py`

Sample output:

```
Default headless result: headless, score=0.8333333333333334
testUserAgent       : 1
testAppVersion      : 1
testWebdriver       : 1
testOuterWidth      : 1
testChrome          : 1
testImage           : 0

Fake UA headless result: headless, score=0.5
testUserAgent       : 0
testAppVersion      : 0
testWebdriver       : 1
testOuterWidth      : 1
testChrome          : 1
testImage           : 0

Fake UA headless + JS fixup result: generic, score=0
testUserAgent       : 0
testAppVersion      : 0
testWebdriver       : 0
testOuterWidth      : 0
testChrome          : 0
testImage           : 0
```

## Used methods

1. User Agent / App Version substring detection
2. Webdriver / chrome flags detection
3. Outer width == 0 detection
4. Broken image zero size detection (looks like it does not work anymore)

## Used fixes to hide headless chrome

1. None
2. Fake User Agent
3. Fake User Agent + JS fixes to override chrome/webdriver tags, outerwidth

## Concl.

Some advanced methods are required for efficient headless browser detection