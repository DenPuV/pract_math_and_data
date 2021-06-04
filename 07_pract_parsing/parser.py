from bs4 import BeautifulSoup as bs
import requests

# открываем документ
# https://habr.com/ru/post/230951/
url = input('Введите URL сайта: ')
url = requests.get(url)
url.encoding = 'utf-8'
doc = bs(url.text, 'lxml')
#doc = bs(codecs.open('article.htm', encoding='utf-8', mode='r').read(), 'html.parser')

# извлечение данных из статьи
author = doc.select('span.user-info__nickname')[0].decode_contents().strip()
title = doc.select('span.post__title-text')[0].decode_contents().strip()
date = doc.select('span.post__time')[0].decode_contents().strip()
tags = list(map(lambda x: x.decode_contents().strip(), doc.select('.post__hubs li a')))
rating = str(doc.select('.voting-wjt__counter')[0].decode_contents().strip())

# вывод на экран
print('Автор:', author)
print('Заголовок:', title)
print('Дата:', date)
print('Теги:', tags)
print('Рейтинг:', rating)

# извлечение данных о комментариях
comments = []
for node in doc.select('.comment'):
    text = node.select('.comment__message')[0].decode_contents().strip()
    rating = str(node.select('.voting-wjt__counter')[0].decode_contents().strip())
    author = node.select('.user-info__nickname')[0].decode_contents().strip()
    comments.append({'text': text, 'rating': rating, 'author': author})

# вывод информации по комментариям
print('Комментариев в статье: ', len(comments))
if len(comments) > 0:
    print('Самый маленький комментарий:', sorted(comments, key=lambda x: len(x['text']))[0]['text'])
    most_popular = sorted(comments, key=lambda x: x['rating'], reverse=True)[0]
    print('Самый популярный комментарий:', most_popular['text'], 'Рейтинг ', most_popular['rating'])

# самый активный комментатор
    commentators = {}
    for comment in comments:
        if comment['author'] in commentators:
            commentators[comment['author']] += 1
        else:
            commentators[comment['author']] = 1
    most_active = max(commentators, key=commentators.get)
    print('Самый активный:', most_active, ', комментариев:', commentators[most_active])
