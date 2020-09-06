import click
import collections
from heapq import nlargest
from string import punctuation

from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.tokenize import sent_tokenize, word_tokenize

from . import __version__

try:
    word_tokenize('Lorem ipsum')
except LookupError:
    import nltk
    nltk.download('punkt')


@click.command(name='kondense')
@click.option(
    '--length', '-l',
    type=int,
    default=3,
    help='Number of sentences to return'
)
@click.argument('filepath')
@click.version_option(__version__)
def main(filepath, length):
    """ Summarize text based on word frequency.

    Leverages NLTK package to create summaries of texts based on word frequency
    distribution in the given text. To find out more on how it works, visit
    https://github.com/sinablk/kondense/
    """
    content = read_file(filepath)
    content = clean_input(content)

    # Tokenizing & Scoring
    sentence_tokens, word_tokens = tokenize_content(content)
    sentence_ranks = score_tokens(word_tokens, sentence_tokens)

    click.secho(summarize(sentence_ranks, sentence_tokens, length), fg='green')


def read_file(path):
    """ Read the file at designated path and throw exception if unable to do so """
    try:
        with open(path, 'r', encoding='utf8') as f:
            return f.read()

    except IOError:
        print(f'Fatal Error: File ({path}) could not be locaeted or is not readable.')


def clean_input(data):
    """ Removes whitespace, such as paragraph breaks and tabs."""
    replace = {
        ord('\f'): ' ',
        ord('\t'): ' ',
        ord('\n'): ' ',
        ord('\r'): None
    }

    return data.translate(replace)


def tokenize_content(content):
    """ Accept the content and produce a list of tokenized sentences,
    a list of tokenized words, and then a list of the tokenized words
    with stop words built from NLTK corpus and Python string class filtred out.
    """
    stop_words = set(stopwords.words('english') + list(punctuation))
    words = word_tokenize(content.lower())

    return [
        sent_tokenize(content),
        (word for word in words if word not in stop_words)
    ]


def score_tokens(filterd_words, sentence_tokens):
    """ Builds a frequency map based on the filtered list of words and
    uses this to produce a map of each sentence and its total score
    """
    word_freq = FreqDist(filterd_words)

    ranking = collections.defaultdict(int)

    for i, sentence in enumerate(sentence_tokens):
        for word in word_tokenize(sentence.lower()):
            if word in word_freq:
                ranking[i] += word_freq[word]   # TODO: Maybe can refactor with itertools?

    return ranking


def summarize(ranks, sentences, length):
    """ Utilizes a ranking map produced by score_tokens to extract
    the highest ranking sentences in order after converting from
    array to string.
    """
    if int(length) > len(sentences):
        raise ValueError("More sentences requested than available. Use --l (--length) flag to adjust.")

    indexes = nlargest(length, ranks, key=ranks.get)
    final_sentences = [sentences[j] for j in sorted(indexes)]
    return ' '.join(final_sentences)
