from sonolus_fastapi.model.ServerOption import (
    ServerForm,
    ServerTextOption,
)
from sonolus_fastapi.model.text import SonolusText
# Post用の検索設定（ratingフィールドなし）
post_search = ServerForm(
    type="advanced",
    title=SonolusText.ADVANCED,
    icon="advanced",
    requireConfirmation=False,
    options=[
        ServerTextOption(
            query="keywords",
            name=SonolusText.KEYWORDS,
            required=False,
            type="text",
            def_="",  # 空文字列をデフォルトに戻す
            placeholder=SonolusText.KEYWORDS_PLACEHOLDER,
            limit=100,
            shortcuts=[],
        ),
    ],
)
