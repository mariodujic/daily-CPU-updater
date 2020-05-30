class ListUtils:

    @staticmethod
    def replace_list_item(items, object_item):
        for item in items:
            if item.itemId == object_item.itemId:
                item.used = True
        return items
