from ports.review_port import ReviewPort
from models import db, Review

class SQLAlchemyReviewAdapter(ReviewPort):

    def add_review(self, review_data):
        new_review = Review(**review_data)
        db.session.add(new_review)
        db.session.commit()
        return new_review