# 19.1.2024
# CTCI Chapter 2 Q2.3

####### QUESTION: Implement an algorithm to delete a note anywhere in the middle of a linked list, given access only to that node


                            # I don't know what is meant by 'access only to that node'. In the example given,
                            # they give values rather than indices so I'll search for values here
def deleteGivenNode(n):
    index = 0

    next_node = list[list[index].next].value

    while next_node != n:
        index = list[index].next
        next_node = list[list[index].next].value

                        # so now, next_node should be the n we are searching for

                            # Tell the node before it to point to the node after it
    list[index].next = list[index[list[index.next].next]]