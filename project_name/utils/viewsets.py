from wagtail.snippets.views.snippets import SnippetViewSet

from .models import AuthorSnippet, ArticleTopic, Statistic


class AuthorSnippetViewSet(SnippetViewSet):
    model = AuthorSnippet
    icon = "user"
    menu_label = "Authors"
    menu_name = "authors"
    list_display = ("title",)


class ArticleTopicViewSet(SnippetViewSet):
    model = ArticleTopic
    icon = "tag"
    menu_label = "Article Topics"
    menu_name = "article-topics"
    list_display = ("title", "slug")


class StatisticViewSet(SnippetViewSet):
    model = Statistic
    icon = "pick"
    menu_label = "Statistics"
    menu_name = "statistics"
    list_display = ("statistic", "description")
