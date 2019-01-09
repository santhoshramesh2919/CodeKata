class node:

    def __init__(self,data):

        self.data=data

        self.next=None

class linkedlist:

    def __init__(self):

        self.head=None

    def insert(self,data):

        curr=self.head

        while currr.next!=None:

            curr=curr.next

        curr.next=node(data)

    def display(self):

        curr=self.head

        while curr!=None:

            print(curr.data)

            current=current.next

li=linkedlist()

li.head=node(10)

for i in range(1,100,10):

     li.insert(i)

li.display()
