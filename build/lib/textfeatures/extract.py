import re

def extract_mentions(text):
    return re.findall(r'[@][^\s#@]+', text)
def extract_hashtags(text):
    return re.findall(r'[#][^\s#@]+', text)
def extract_urls(text):
    return re.findall(r'(https?://[^\s]+)', text)
def extract_emails(text):
    return re.findall(r'([\w0-9._-]+@[\w0-9._-]+\.[\w0-9_-]+)', text)
def extract_all_caps(text):
    return re.findall(r"(\b(?:[A-Z]+[a-z]?[A-Z]*|[A-Z]*[a-z]?[A-Z]+)\b(?:\s+(?:[A-Z]+[a-z]?[A-Z]*|[A-Z]*[a-z]?[A-Z]+)\b)*)", text)
def extract_emojis(text):
    # http://stackoverflow.com/a/13752628/6762004
    RE_EMOJI = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)
    return RE_EMOJI.findall(text)