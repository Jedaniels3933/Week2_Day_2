
python_reviews = [ "This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "This was a poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it." ]

key_words = ["good", "excellent", "bad", "poor", "average"]

for review in python_reviews:
    for word in key_words:
        if word in review:
            x = review.replace(word, word.upper())
            print(x)
    print("--------------------")

negative_words = ["bad", "poor"]
positive_words = ["good", "excellent"]

for review in python_reviews:
    pos_count = 0
    neg_count  = 0
    for word in positive_words:
        if word in review:
            pos_count += 1
    for word in negative_words:
        if word in review:
            neg_count += 1
    print(review)
    print(f"Positive words: {pos_count}")
    print(f"Negative words: {neg_count}")
    

