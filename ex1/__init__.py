def build_roles_tree(mapping):
    """
    :param mapping: маппинг ролей в категории
    :return: дерево ролей
    """
    roles_tree = {"categories": []}
    for category_id in mapping["categoryIdsSorted"]:
        category_text = mapping["categories"][category_id]["name"]
        category_items = []
        for item_id in mapping["categories"][category_id]["roleIds"]:
            item_text = mapping["roles"][item_id]["name"]
            category_items.append({
                "id": item_id,
                "text": item_text
            })
        category = {
            "id": f'category-{category_id}',
            "text": category_text,
            "items": category_items
        }
        roles_tree["categories"].append(category)
    return roles_tree
    pass
