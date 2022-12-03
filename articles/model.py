class Article:
    def __init__(self, title, author, pages, description):
        self.title = title
        self.author = author
        self.pages = pages
        self.descriptions = description

    def __str__(self):
        return f"{self.title} ({self.author})"


class ArticleModel:
    def __init__(self):
        self.articles = {}

    def add_article(self, dict_article):
        article = Article(*dict_article.values())
        self.articles[article.title] = article

    def get_all_articles(self):
        return self.articles.values()

    def get_singe_article(self, user_title):
        article = self.articles[user_title]
        dict_article = {
            "название": article.title,
            "автор": article.author,
            "количество знаков": article.pages,
            "описание": article.descriptions
        }
        return dict_article

    def remove_article(self, user_title):
        return self.articles.pop(user_title)

