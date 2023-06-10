from dto.base import DbConnection
from poll.config import questions

db_creator = DbConnection()

for question in questions:
    db_creator.questions.insert(question)