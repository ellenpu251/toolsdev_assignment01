import newspaper
import nltk
import webbrowser
from newspaper import news_pool
from newspaper import Article
nltk.download('punkt')

summary = open('news_summary.txt', 'w')
keyword = input("Please enter any keyword (press enter to continue)")

# def dump_info (news_list):
#    for i in news_list:
#        for article in news_list[i]:
#            article.download()
#           article.parse()
#            article.nlp()
#            if keyword in article.keywords:
#                print(article.title)
#                print(article.authors)
#                print(article.summary)

npr_paper = newspaper.build('https://www.npr.org/', memoize_articles=False)
cnn_paper = newspaper.build('https://www.cnn.com/', memoize_articles=False)
tc_paper = newspaper.build('http://techcrunch.com', memoize_articles=False)

webbrowser.open_new('https://www.npr.org/')
webbrowser.open_new('https://www.cnn.com/')
webbrowser.open_new('http://techcrunch.com')

# newsList = [npr_paper, cnn_paper, tc_paper]
# dump_info(newsList)

for article in npr_paper.articles:
    article.download()
    article.parse()
    article.nlp()
    if keyword in article.keywords:
        print(article.title, file=summary)
        print(article.authors, file=summary)
        print(article.summary, file=summary)

for article in cnn_paper.articles:
    article.download()
    article.parse()
    article.nlp()
    if keyword in article.keywords:
        print(article.title, file=summary)
        print(article.authors, file=summary)
        print(article.summary, file=summary)

for article in tc_paper.articles:
    article.download()
    article.parse()
    article.nlp()
    if keyword in article.keywords:
        print(article.title, file=summary)
        print(article.authors, file=summary)
        print(article.summary, file=summary)
