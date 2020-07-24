class wiki_end:
  def get_wiki_data(url_topull):
    scraped_data = urllib.request.urlopen(url_topull)  
    article = scraped_data.read()

    parsed_article=bs.BeautifulSoup(article,'lxml')

    paragraphs = parsed_article.find_all('p')

    article_text = ""

    for p in paragraphs:  
        article_text += p.text
    article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)  
    article_text = re.sub(r'\s+', ' ', article_text)
    return article_text
