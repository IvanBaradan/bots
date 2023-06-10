class Question:
    def __init__(self, text, qtype: str, options, answer):
        self.text = text
        self.qtype = qtype
        self.options = options
        self.answer = answer
        self.score = 0

    def add_answers(self, answer):
        self.answer = answer
        self._counter()

    def _counter(self):
        if self.qtype == 'closed':
            self.score = 1 if self.answer == 'Да' else 0
        if self.qtype == 'multiple_choice':
            self.score = 1 if self.options == self.answer else 0
        if self.qtype == 'number':
            pass


class Node:
    def __init__(self):
        self.data = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.cur_node = None

    def add_node(self, data):
        new_node = Node()
        new_node.data = data
        new_node.next = self.cur_node
        self.cur_node = new_node

    def head(self):
        return self.cur_node

def get_question_node(questions):
    qlist = LinkedList()
    for i in range(len(questions))[::-1]:
        qtext = questions[i].get('text')
        qtype = questions[i].get('type')
        qoptions = questions[i].get('options')
        qanswer = questions[i]['right_answer']
        question = Question(qtext, qtype, qoptions, qanswer)
        qlist.add_node(question)
    return qlist.head()

def sum_linked_list(head):
  total = 0
  current = head
  while current != None:
        total += current.data.score
        current = current.next
  return total
