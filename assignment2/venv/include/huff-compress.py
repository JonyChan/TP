import pickle
import array
import re,argparse,time

# calculate time
start = time.process_time()
# dictionary symbol is key, ferquent is value
binary_code = {}

def compress(symbol):
    file_input = []
    # use binary read file
    f = open(inputfile,'r')
    file_input = f.read()
    f.close()
    # a dictionary, symbol is key, frequent is value
    term_freq = {}
    # char
    if symbol == "char":
        for c in file_input:
            if c not in term_freq:
                term_freq[c] = 0
            else:
                term_freq[c]+=1

    # word
    if symbol == "word":
        word = ''
        pattern = re.compile(r'[a-z]',re.I)
        for term in file_input:
            result = pattern.match(term)
            if result != None:
                word += term
            else:
                if word == '':
                    if term not in term_freq:
                        term_freq[term] = 1
                    else:
                        term_freq[term] += 1
                else:
                    # save word into collection
                    if word not in term_freq:
                        term_freq[word] = 1
                    else:
                        term_freq[word] += 1
                    # save term into collection
                    if term not in term_freq:
                        term_freq[term] = 1
                    else:
                        term_freq[term] += 1
                    word = ''


    nodes = createtree(term_freq)
    top = huffmantree(nodes)
    encode(top, "")

    # encode all of the text
    binary_str = ''

    if symbol == "char":
        for char in file_input:
            if char in binary_code.keys():
                binary_str += binary_code[char]

    if symbol == "word":
        word = ''
        pattern = re.compile(r'[a-z]', re.I)
        for term in file_input:
            result = pattern.match(term)
            if result != None:
                word += term
            else:
                if word == '':
                    binary_str+= binary_code[term]
                else:
                    binary_str += (binary_code[word]+binary_code[term])
                    word = ''

    codearray = array.array('B')


    lenth = len(binary_str)

    for i in range(0,lenth,8):
        c = binary_str[i:i+8]
        codearray.append(int(c, 2))

    f = open(pkl_path, 'wb')
    pickle.dump(binary_code,f)
    f.close()

    f = open(outputfile, 'wb')
    codearray.tofile(f)
    f.close()

# # calculate the frequent of the term in the text
# import document
# use for loop save as dictionary
class Node:
    def __init__(self, freq, name=None):
        self.freq = freq
        self.name = name
        self.leftchild = None
        self.rightchild = None

    def has_children(self):
        return self.leftchild == None and self.rightchild == None

def createtree(term_dic):
    # self.value = value
    return [Node(term_dic[name], name) for name in term_dic]

def huffmantree(nodes):
    # self.nodes = nodes
    list_ = nodes

    while len(list_) > 1:
        list_.sort(key=lambda item: item.freq)
        node_min1 = list_[0]
        freq_min = list_[0].freq
        del list_[0]
        node_min2 = list_[0]
        freq_min += list_[0].freq
        del list_[0]
        node_father = Node(freq_min)
        node_father.leftchild = node_min1
        node_father.rightchild = node_min2
        node_min1.father = node_father
        node_min2.father = node_father
        list_.append(node_father)

    return list_[0]

def encode(node, symbol):

    if node.has_children():
        binary_code[node.name] = symbol
        return
    encode(node.leftchild, symbol+'0')
    encode(node.rightchild, symbol+'1')

parser = argparse.ArgumentParser()
parser.add_argument('-s', type=str, help='Symbol')
parser.add_argument('input', type=str, help="Input file")
args = parser.parse_args()

symbol = args.s if args.s else 'word'
inputfile = args.input if args.input else 'infile.txt'
outputfile = inputfile[:inputfile.find('.')] + '.bin'
pkl_path = inputfile[:inputfile.find('.')] + '-symbol-model.pkl'

compress(symbol)
used = time.process_time()-start
print("time used:",used)

