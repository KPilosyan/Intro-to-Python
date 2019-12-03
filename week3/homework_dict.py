market = {"dairy": ["yogurt", "cheese"], "fruits": ['banana', 'apple', 'orange', 'lemon', 'apple', 'banana', 'banana']}
print("Initial:", market)
market.update({"candies": ['mars', 'kinder', 'twix'] })
market["fruits"] = set(market["fruits"]) 
market["fruits"] = list(market["fruits"])
market["fruits"].sort()
print(market["fruits"])
print("After:", market)