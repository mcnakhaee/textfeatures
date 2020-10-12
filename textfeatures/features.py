import pandas as pd
import spacy
import re
from textblob import TextBlob
import enchant
import string
from textfeatures.extract import *
def extract_features(df,text_col = 'text',
                     use_spacy_features = True,
                     use_emoji_features = True,
                     use_misspelling_features = True):
    if use_emoji_features:

        df['n_emojis'] = df[text_col].apply(lambda x: len(extract_emojis(x)))
    if use_spacy_features:
        nlp = spacy.load('en_core_web_sm')
        df['tokens'] = df[text_col].apply(lambda x: [token.text for token in nlp(x)])
        df['n_tokens'] = df['tokens'].apply(lambda x: len(x))
        df['n_unique_tokens'] = df['tokens'].apply(lambda x: len(set(x)))
    first_person_pronouns =["i", "me", "myself", "my", "mine", "this"]
    first_personp_pronouns = ["we", "us", "our", "ours", "these"]
    second_person_pronouns = ["you", "yours", "your", "yourself"]
    third_person_pronouns = ["he", "she", "it", "its", "his", "hers"]
    third_personp_pronouns = ["they", "them", "theirs", "their", "they're", "their's", "those", "that"]
    to_be_verbs = ["am", "is", "are", "was", "were", "being",
    "been", "be", "were", "be"]
    prepositions = ["about", "below", "excepting", "off", "toward", "above", "beneath",
    "on", "under", "across", "from", "onto", "underneath", "after", "between",
    "in", "out", "until", "against", "beyond", "outside", "up", "along", "but",
    "inside", "over", "upon", "among", "by", "past", "around", "concerning",
    "regarding", "with", "at", "despite", "into", "since", "within", "down",
    "like", "through", "without", "before", "during", "near", "throughout",
    "behind", "except", "of", "to", "for"]

    df['textblob'] = df[text_col].apply(lambda x: TextBlob(x))
    df['textblobwords'] = df['textblob'].apply(lambda x: x.words)
    df['n_words'] = df['textblobwords'].apply(lambda x: len(x))
    df['n_unique_words'] = df['textblobwords'].apply(lambda x: len(set(x)))
    df['n_sentences'] = df['textblob'].apply(lambda x : len(x.sentences))
    if use_misspelling_features:
        dict = enchant.Dict("en_US")
        df['n_misspelled_words'] = df['textblobwords'].apply(lambda x : len([ word for word in x if dict.check(word) == False]))
    df['first_personp'] = df['textblobwords'].apply(lambda x : len([word for word in x if word.lower() in first_personp_pronouns]))
    df['first_personp'] = df['textblobwords'].apply(lambda x : len([word for word in x if word.lower() in first_personp_pronouns]))
    df['second_person_pronouns'] = df['textblobwords'].apply(lambda x : len([word for word in x if word.lower() in second_person_pronouns]))
    df['third_person'] = df['textblobwords'].apply(lambda x : len([word for word in x if word.lower() in third_person_pronouns]))
    df['third_personp'] = df['textblobwords'].apply(lambda x : len([word for word in x if word.lower() in third_personp_pronouns]))
    df['n_to_be'] = df['textblobwords'].apply(lambda x : len([word for word in x if word.lower() in to_be_verbs]))
    df['n_prepositions'] = df['textblobwords'].apply(lambda x : len([word for word in x if word.lower() in prepositions]))
    df['polarity'] = df['textblob'].apply(lambda x : x.sentiment.polarity)
    df['subjectivity'] = df['textblob'].apply(lambda x : x.sentiment.subjectivity)


    if n_hashtags == True:
        df['n_hashtags'] = df[text_col].apply(lambda x :len(extract_hashtags(x)))
    if n_unique_hashtags == True:
        df['n_unique_hashtags'] = df[text_col].apply(lambda x :len(set(extract_hashtags(x))))
    if   n_mentions == True:
        df['n_mentions'] = df[text_col].apply(lambda x :len(extract_mentions(x)))
    if   n_unique_mentions == True:
        df['n_unique_mentions'] = df[text_col].apply(lambda x :len(set(extract_mentions(x))))
    if n_characters:
        df['n_characters'] = df[text_col].apply(lambda x : len(x))
    if n_unique_characters:
        df['n_unique_characters'] = df[text_col].apply(lambda x : len(set([char for char in x])))
    if n_charsperword:
        df['n_charsperword'] =  df['n_characters'] + 1 / df['n_words'] + 1
    if n_unique_urls:
        df['n_unique_urls'] = df[text_col].apply(lambda x : re.findall(r'([\w0-9._-]+@[\w0-9._-]+\.[\w0-9_-]+)', x) )
    if n_upper:
        pass
    if n_lower:
        pass
    if n_puncts:
        df['n_puncts'] = df[text_col].apply(lambda x: len([c for c in x if c not in string.punctuation]))
    if n_exclaims:
        pass
    if n_all_cap:
        df['n_all_cap'] = df[text_col].apply(lambda x : re.findall(r"(\b(?:[A-Z]+[a-z]?[A-Z]*|[A-Z]*[a-z]?[A-Z]+)\b(?:\s+(?:[A-Z]+[a-z]?[A-Z]*|[A-Z]*[a-z]?[A-Z]+)\b)*)", x) )

    return df