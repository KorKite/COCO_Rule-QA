class Node:
    def __init__(self, data):
        self.data = data
        self.link = None


class queue:
    def __init__(self):
        self.head = None

    def insert_first(self, data):
        new_node = Node(data)

        if self.head == None:  # head가 비어있으면 새 노드를 head로 설정
            self.head = new_node

        else:
            temp = self.head
            self.head = new_node
            self.head.link = temp


    def delete_last(self):

        if self.head == None:
            return "No COCO"

        else:
            node = self.head
            previous = None
            while True:
                if node.link == None:
                    if previous == None:
                        temp = self.head
                        self.head = None
                        return temp.data
                    else:
                        temp = node
                        previous.link = None
                        return node.data
                else:
                    previous = node
                    node = node.link

										
a = int(input())
adt = linked_list()
answer = []
for i in range(a):
    a, b =input().split(" ")
    if a == "0":
        adt.insert_first(b)
    else:
        data = adt.delete_last()
        answer.append(data)

if len(answer) == 0:
	  print(-1)
else:
		for i in answer:
				print(i)
