TITLE : (temp) Music recommendation app

This app is made for ericsson hackathon 2017

Works with 
- Google NLP api 
- python flask
- mongoDB

Target
- Everyone who write diary.
- Someone need some music recommendation.


How it works?
1. User put their sentences on this app.
2. Server takes and do 'Sentiment analysis' with Google NLP api.
3. Based on sentiment score, figure out how good the writer's today was.
4. Recommend some music video from youtube based on status.
5. Have a good time with the music.



Installation
1. Need to get google api authentication key. Follow the instructions on
   https://cloud.google.com/natural-language/docs/getting-started
2. ~/myflask$ python f5_memo.py


Current Issue
- Make better web UI 
- Show youtube clip on the same page.
- Connect MongoDB & save information.

