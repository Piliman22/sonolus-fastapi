def apply_query(items, query):
    if hasattr(query, "keywords") and query.keywords:
        items = [
            i for i in items
            if query.keywords.lower() in i.title.lower()
        ]
    return items

def paginate(items, page: int = 1, page_size: int = 20):
    start = (page - 1) * page_size
    end = start + page_size
    return items[start:end]