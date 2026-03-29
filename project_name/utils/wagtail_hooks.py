from wagtail import hooks
from wagtail.rich_text import LinkHandler
from .viewsets import (
    AuthorSnippetViewSet,
    ArticleTopicViewSet,
    StatisticViewSet,
)

class ExternalLinkHandler(LinkHandler):
    identifier = "external"

    @classmethod
    def expand_db_attributes(cls, attrs):
        href = attrs["href"]

        return f'<a data-rich-text-external-link href="{href}">'


@hooks.register("register_rich_text_features")
def register_link_handler(features):
    features.register_link_type(ExternalLinkHandler)

@hooks.register("register_admin_viewset")
def register_author_snippet():
    return AuthorSnippetViewSet()


@hooks.register("register_admin_viewset")
def register_article_topic():
    return ArticleTopicViewSet()


@hooks.register("register_admin_viewset")
def register_statistic():
    return StatisticViewSet()
