# def getdict(self, file_input):
#     dict = {}
#     # b = []
#     self.file_input = file_input
#     for i in range(len(file_input)):
#         term = file_input[i]
#         # b.append(file_input[i])
#         if term in a.keys():
#             dict[term] += 1
#         else:
#             dict[term] = 1
#         # print('dict')
#     return dict

# def get_key(self,dict):
#     key = []
#     for term in dict.keys():
#         key.append(term)
#     # print('key')
#     return key
# 
# def get_value(self,dict):
#     value = []
#     for term in dict.keys():
#         value.append(dict[term])
#     return value

# def createtree(self, freq):
#     self.freq = freq
#     a = []
#     for i in freq:
#         a.append(Node(i))
#     return a


# # add all the symbol in a list
# def createnode(freqs):
#     list = []
#     for i in freqs:
#         list.append(Node[i])
#     return list
# 
# #create huffman tree model
# def huffmantree(nodes):
#     list = node[:]
#     # use two samllest item to one item until just one in list
#     while len(list) > 1:
#         list.sort(key=lambda item:item.freq)  #sort the list
#         top = list[-0]
#         min_node1 = list[0]  # get the first smallest node
#         n_node = list[0].freq
#         del list[0]  #delete this node from the list
#         min_node2 = list[0]
#         n_node += list[0].freq
#         del list[0]  #delete the second node
#         # create a father node, the left is the smallest node,the right
#         #child is the second smallest child,then add this node into list
#         node_father = Node(n_code)
#         node_father.leftchild = min_node1
#         node_father.rightchild = min_node2
#         min_node1.father = node_father
#         min_node2.father = node_father
#         list.append(node_father)
#     return list[0]
# 
# # judge whether the node is the leftchild
# def isleft(self):
#     return self.father.left == left
# 
# # generate code of the huffman
# def generatecode(nodes, top, str):
#     encode = {}
#     for i in range(len(nodes)):
#         m = []
#         while nodes[i] != top:
#             if nodes[i].isleft:
#                 m.append('0')
#             else:
#                 m.append('1')
#             nodes[i] = nodes[i].father
#         encode[str[i]] = m
#     return encode

# a = Node(3)
# a.huffmantree(a)


