from mongoengine import Document, \
                        StringField, ListField, \
                        BooleanField, DateTimeField
import datetime

class SampleData(Document):
    first_name = StringField(min_length=1, max_length=100, required=True)
    last_name = StringField(min_length=1, max_length=100, required=False)
    email = StringField(min_length=5, max_length=255, required=True, db_index=True)
    phone_numbers = ListField(required=False)
    enabled = BooleanField(default=True, db_index=True)
    created_on = DateTimeField(default=datetime.datetime.utcnow)