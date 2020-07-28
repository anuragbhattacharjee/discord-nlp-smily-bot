# discord-nlp-smily-bot

A discord bot to analyse message and react with a smily.

![Discord](https://github.com/anuragbhattacharjee/discord-nlp-smily-bot/blob/master/smily-bot.png)

This repo contains the code and detailed instruction to implement a discord bot to read messages and detect the sentiment, emotion and sarcasm of the message according to it’s 1.2B twitter trained data and reply with a suitable smily. I have deployed it in my office server to have some fun with it.

You can read the details in my [blog post](https://medium.com/@anuragbhattacharjee/i-created-a-deep-learning-powered-discord-bot-to-react-with-smily-fec831d30d1b).

Before proceeding, make sure you have installed `python3` (the repo is tested with python3.7)

## Installation

1. Clone the repo: `git clone https://github.com/anuragbhattacharjee/discord-nlp-smily-bot.git`
2. Make an environment: `python3 -m venv your-path-to-venv`
3. Activate the environemnt: `source venv/bin/activate`
4. Install requirements: `pip3 install -r requirements.txt`
5. Download the [vocabulary](https://github.com/cw75/torchMoji/blob/master/model/vocabulary.json) and save it in tochMoji/model
6. Download [weights](https://www.dropbox.com/s/q8lax9ary32c7t9/pytorch_model.bin?dl=0#) and save it in tochMoji/model

## Test

```
python3
>>> from emojize import Emojize
>>> e = Emojize()
>>> e.predict("I am doing great today!")
:smile:
```

## Test in Dscord

1. Connect to discord bot following my [blog post](https://medium.com/@anuragbhattacharjee/i-created-a-deep-learning-powered-discord-bot-to-react-with-smily-fec831d30d1b).
2. type a message in a channel and see the bot reacting
