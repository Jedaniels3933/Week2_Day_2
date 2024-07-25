python_reviews = [ "This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "This was a poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it." ]

key_words = ["good", "excellent", "bad", "poor", "average"]
python_positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"] 
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
for i in key_words:
    print(f"Reviews containing the word '{i}':")
    for review in python_reviews:
        if i in review:
            print(review.upper())
    print("--------------------")
for i in negative_words:
    print(f"Reviews containing the word '{i}':")
    for review in python_reviews:
        if i in review:
            print(review.upper())
    print("--------------------")
    print("Positive Reviews:")
    for review in python_reviews:
        positive_count = 0
        for word in python_positive_words:
            if word in review:
                positive_count += 1
        print(f"Positive words: {positive_count}")
        print(f"Review: (upper.{review})")
        print("--------------------")
        print("Negative Reviews:")
        for review in python_reviews:
            negative_count = 0
            for word in negative_words:
                if word in review:
                    negative_count += 1
            print(f"Negative words: {negative_count}")
            print(f"Review: {review.upper()}")
            print("--------------------")
            print("Positive Reviews:")

            


            





 



















