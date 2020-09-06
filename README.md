# kondense


Kondense is a small CLI application written in Python that allows the user to create summaries of a given piece of text using token frequency. In human terms, it's a simple application that scores each sentence in the text based on the frequency of its words in the whole article and scores them accordingly. The top-scoring sentences are used to create the summary.


```
Usage: kondense [OPTIONS] FILEPATH

  Summarize text based on word frequency.

  Leverages NLTK package to create summaries of texts based on word
  frequency distribution in the given text. To find out more on how it
  works, visit https://github.com/sinablk/kondense/

Options:
  -l, --length INTEGER  Number of sentences to return
  --help                Show this message and exit.
```


### Credits

The `demo.txt` is from the article [Greenland is Melting](https://projects.voanews.com/greenland/), written by Steve Baragona of VOA News.

