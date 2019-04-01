import wikipediaapi

wiki_ko = wikipediaapi.Wikipedia('ko')
page_py = wiki_ko.page('파이썬')
print("Page - Exists: %s" % page_py.exists())

print("Page - Title: %s" % page_py.title)

print("Page - Summary: %s" % page_py.summary[0:100])

wiki = wikipediaapi.Wikipedia( language='ko', extract_format=wikipediaapi.ExtractFormat.WIKI)
p_wiki = wiki.page("홍익대")
print(p_wiki.text)
