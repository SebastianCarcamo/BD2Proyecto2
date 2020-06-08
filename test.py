import json
import pandas as pd
from TweetContainer import * 
from tf_idf import *
import os

t1 =     {
        "id": 1,
        "date": "Tue Aug 07 20:15:51 +0000 2018",
        "text": "RT @Cluzcar: @DanielUrresti1 @PeruanoComunica @QuintoPoderPe @ManuelVelardeD @MuniLima \u00bfNo hay m\u00e1s???...",
        "user_id": 741654192079671296,
        "user_name": "@RTfujitrolls",
        "location": {},
        "retweeted": True,
        "RT_text": "@DanielUrresti1 @PeruanoComunica @QuintoPoderPe @ManuelVelardeD @MuniLima \u00bfNo hay m\u00e1s???...",
        "RT_user_id": 282155394,
        "RT_user_name": "@Cluzcar"
    }

t2 =     {
        "id": 2,
        "date": "Tue Aug 07 20:15:51 +0000 2018",
        "text": "RT @Cluzcar: @DanielUrresti1 @PeruanoComunica @QuintoPoderPe @ManuelVelardeD @MuniLima \u00bfNo hay m\u00e1s???...",
        "user_id": 741654192079671296,
        "user_name": "@RTfujitrolls",
        "location": {},
        "retweeted": True,
        "RT_text": "@DanielUrresti1 @PeruanoComunica @QuintoPoderPe @ManuelVelardeD @MuniLima \u00bfNo hay m\u00e1s???...",
        "RT_user_id": 282155394,
        "RT_user_name": "@Cluzcar"
    }

t3 =     {
        "id": 3,
        "date": "Tue Aug 07 20:15:51 +0000 2018",
        "text": "RT @Cluzcar: @DanielUrresti1 @PeruanoComunica @QuintoPoderPe @ManuelVelardeD @MuniLima \u00bfNo hay m\u00e1s???...",
        "user_id": 741654192079671296,
        "user_name": "@RTfujitrolls",
        "location": {},
        "retweeted": True,
        "RT_text": "@DanielUrresti1 @PeruanoComunica @QuintoPoderPe @ManuelVelardeD @MuniLima \u00bfNo hay m\u00e1s???...",
        "RT_user_id": 282155394,
        "RT_user_name": "@Cluzcar"
    }


lista = [TweetContainer(t1),TweetContainer(t2),TweetContainer(t3)]

print(generate_tf_idf(lista))
