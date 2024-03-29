import pickle,argparse,time

# calculate time
start = time.process_time()

parser = argparse.ArgumentParser()
parser.add_argument('bin', type=str, help="the compression file XXXX.bin")
parser.add_argument('-s', type=str, help='Symbol')
args = parser.parse_args()


symbol = args.s if args.s else 'word'
bin_file = args.bin
plk_file = bin_file[:bin_file.find('.bin')] + '.plk'

pkl_file = bin_file[:bin_file.find('.bin')] + '-symbol-model.pkl'
out_file = bin_file[:bin_file.find('.bin')] + '-decompressed.txt'

if symbol == 'char'or'word':
    huff_code= {}

    bytes = ""

    with open(pkl_file, 'rb') as f:
        huff_code = pickle.load(f)
    with open(bin_file, 'rb') as f:
        bytes = f.read()

    c = '00000000'

    huff_code = dict(zip(huff_code.values(), huff_code.keys()))

    bstr = ""
    temp = ""
    recover = ""
    for ab in bytes:
        bstr = bin(ab)[2:]
        bstr = c[0:(8-len(bstr))] + bstr
        for b in bstr:
            temp+=b
            if  temp in huff_code:
                recover+= huff_code[temp]
                temp =""


    with open(out_file,'w') as f:
        f.write(recover)

used = time.process_time()-start
print("time used:",used)