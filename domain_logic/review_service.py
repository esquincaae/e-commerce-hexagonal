class ReviewService:
    def __init__(self, review_adapter):
        self.review_adapter = review_adapter

    def add_review(self, review_data):
        return self.review_adapter.add_review(review_data)
