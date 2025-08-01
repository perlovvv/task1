purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]


def total_revenue(purchases: list[dict]) -> float:
    total_price = 0
    for pur in purchases:
        total_price += pur["price"] * pur["quantity"]
    return total_price


def items_by_category(purchases: list[dict]) -> dict:
    items = {}
    for pur in purchases:
        if pur["category"] not in items:
            items[pur["category"]] = []
        items[pur["category"]].append(pur["item"])
    return items


def expensive_purchases(purchases: list[dict], min_price: float):
    exp = []
    for pur in purchases:
        if pur["price"] > min_price:
            exp.append(pur)
    return exp


def average_price_by_category(purchases: list[dict]):
    items = {}
    for pur in purchases:
        if pur["category"] not in items:
            items[pur["category"]] = []
        items[pur["category"]].append(pur["price"])
    for category, prices in items.items():
        avg_price = sum(prices) / len(prices) 
        items[category] = round(avg_price, 2)  
    return items

def most_frequent_category(purchases: list[dict]):
    items = {}
    for pur in purchases:
        if pur["category"] not in items:
            items[pur["category"]] = []
        items[pur["category"]].append(pur["quantity"])
    for category, quantity in items.items(): 
        items[category] = sum(quantity)  
    max_category = str()
    max_quantity = 0
    for category, quantity in items.items():
        if quantity > max_quantity:
            max_quantity = quantity
            max_category = category
    return max_category



print(f"Общая выручка: {total_revenue(purchases)}")
print(f"Товары по категориям: {items_by_category(purchases)}")
print(f"Покупки дороже 1.0: {expensive_purchases(purchases, 1.0)}") 
print(f"Средняя цена по категориям: {average_price_by_category(purchases)}") 
print(f"Категория с наибольшим количеством проданных товаров: {most_frequent_category(purchases)}")
