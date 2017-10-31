# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def get_num(a):
    hackedlist=[]
    for i in a:
        hackedlist.append(str(i))

    return int(''.join(hackedlist))

def addTwoHugeNumbers(a, b):

    a_num = get_num(a)
    b_num = get_num(b)
    #print(a_num)
    #print(b_num)
    
    sm = str(a_num + b_num)
    #print(sm)
    
    ret_list = []
    sm = sm[-1::-1]
    for i in range(0,len(sm), 4):
        num = sm[i:i+4]
        num = int(num[-1::-1])
        
        ret_list += [num]
        
    ret_list = ret_list[-1::-1]
    
    return ret_list
