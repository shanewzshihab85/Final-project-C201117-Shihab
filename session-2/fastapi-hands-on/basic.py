from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

app = FastAPI()


news = {
    1:
    {
        "id": 1,
        "title": "Most popular pogramming language",
        "content": "Python is the most popular programming the other popular",
        "author": "Mohammed"
    },
    2:
    {
        "id": 2,
        "title": "Most used database",
        "content": "Most common use database is MySql",
        "author": "Main"
    },
    3:
    {
        "id": 3,
        "title": "Best Web language to design website",
        "content": "HTML and CSS is most common used web laguage in the world",
        "author": "Uddin"
    },
    4:
    {
        "id": 4,
        "title": "Why we do web scrapping",
        "content": "Web Scraping lets you automatically extract lots of data from websites",
        "author": "C201091"
    },
}


class News(BaseModel):
    title: str
    content: str | None = None
    author: str


@app.get("/")
def hearbeat():
    return {"message": "I'm up and running!"}




@app.get("/news")
def news_by_title(title_contains: str):
    print(title_contains)
    for single_news in news.values():
        if title_contains.lower() in single_news["title"].lower():
            return single_news

    return {"data": "No news found with title containing "+title_contains}


# http://localhost:8000/news/%7Bauthor%7D?title_contains=llm
@app.get("/news/{author}")
def news_filter_by_author_title(author: str, title_contains: str = None):
    print(author, title_contains)
    filtered_news = [news for news in news.values() if news["author"].lower() == author.lower()]
    print(filtered_news)
    if title_contains:
        filtered_news = [news for news in filtered_news if title_contains.lower() in news["title"].lower()]
        if not filtered_news:
            return {"data": f"No news found from author {author} with title containing {title_contains}"}
    return filtered_news

@app.get("/news")
def all_news():
    return news


@app.get("/news/{id}")
def news_by_id(id: int):
    if id not in news:
        return {"error": f"News with id {id} not found"}
    return news[id]


@app.post("/create-news")
def create_news(response_news: News):
    print(response_news)

    id = max(news.keys()) + 1
    news[id] = {
        "id": id,
        "title": response_news.title,
        "content": response_news.content,
        "author": response_news.author
    }

    return news[id]

if __name__ == '__main__':
    uvicorn.run("basic:app", host='localhost', port=8000, reload=True)
