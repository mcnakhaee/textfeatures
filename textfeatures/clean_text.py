import re
import emoji


def remove_mentions(text):
    return ' '.join(re.sub(r'[@][^\s#@]+', ' ', text).split())


def remove_hashtags(text):
    return ' '.join(re.sub(r'[#][^\s#@]+', ' ', text).split())


def remove_urls(text):
    pass


def remove_emails(text):
    return re.sub(r'([\w0-9._-]+@[\w0-9._-]+\.[\w0-9_-]+)', ' ', text)


def remove_all_caps(text):
    return re.sub(r"(\b(?:[A-Z]+[a-z]?[A-Z]*|[A-Z]*[a-z]?[A-Z]+)\b(?:\s+(?:[A-Z]+[a-z]?[A-Z]*|[A-Z]*[a-z]?[A-Z]+)\b)*)",
                  ' ', text)


def remove_emojis(text):
    # http://stackoverflow.com/a/13752628/6762004
    RE_EMOJI = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)
    return RE_EMOJI.sub(r'', text)
