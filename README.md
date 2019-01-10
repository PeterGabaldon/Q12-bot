Q12 BOT - Answer predictor in Python
====================================

# Disclaimer
This software must be use only with educational purposes, any other use with no educational intent is at your own risk. These Python scripts are not developed with any intention of damaging [Q12 trivia](http://q12.live) just with a learning goal.

# What is Q12?
Q12 is a Spanish trivia app, similar to [HQ trivia](https://twitter.com/hqtrivia). Q12 trivia offers a daily 500€ prize in a live streaming at 21:00 UTC. Sundays a special prize of 2000€ is offered. The award is shared among each person that pass the 12 necessary questions to win. Questions are in the format of three options.

# Usage
Note: Python version is Python 2.7.
Firstly, you need necessary credentials. "*Q12 bot*" uses **Google Cloud Vision API**, **Google Custom Search** and **Google Natural Language API**. You can obtain them from [Google Cloud console](http://console.cloud.google.com). *Cloud Vison* API uses a service account so **GOOGLE_APPLICATION_CREDENTIALS** environment variable must be set with the path of your JSON key file. Eventually, the other two need an API key, this API key is held by API_KEY variable declared in *g_search.py*.

```
git clone https://github.com/PeterGabaldon/Q12-bot.git
cd Q12-bot
python bot.py [args]
```

Options:
```
usage: bot.py [-h] [-as, --autoshot] [-i, --image [Path]]

Q12 Bot

optional arguments:
  -h, --help          show this help message and exit
  -as, --autoshot     Auto screenshot.
  -i, --image [Path]  Path of image to use.

```

If you decide to use the "Auto screenshot" option the script will try to take a screenshot of an area and use it. For that, four environment variables must be set, "x1", "y1", "x2" and "y2". Each one represent the points of the rectangle area that will be used for the screenshot.

# The BOT
The bot performs two process for answer prediction separated in two threads.  
Note: all strings are in lowercase and the words that are not meangful(prepositions, example) are discarded.
* First one is a simple Google Search, using a custom engine. This search is performed with the question, previously read using Google OCR. After the search, the first ten results are used for counting up the times each option appear. Each time the option appear in the content of a result, exactly the same, is counted. If part of the whole option is found, i.e., one word of the whole string, 0.5 is added each time.
* The second one uses Google Natural Language API to obtain keywords of the question and Wikipedia URLs, if it is possible. Then, the same process is performed.
For each result that Google throws, after the previously described actions are done, results are printed in screen, red ones are those which comes from the search after using GNL API and the blue ones for results of the common Google Search.  

Both processes can be extended and improved, this is just a **simple proof** so they are not at their best, they work in a simple way. More complex techniques could be applied enhancing results fiability. One big problem is when questions need some logic reasoning. In **"Test"** folder you will find screenshots of game questions, so you can test "*Q12 bot*".

[![Youtube video](http://img.youtube.com/vi/ePopR13X8j8/0.jpg)](http://www.youtube.com/watch?v=ePopR13X8j8)