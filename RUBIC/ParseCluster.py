import pickle

def parseKegg(ffr):
    with open(ffr,'rb') as f:
        dta=pickle.load(f,encoding='latin1')
    # print(type(dta))
    HeaderL=list(dta.columns)
#     print(len(HeaderL))
    KeggCL={}
    for k in HeaderL:
        KeggCL[k]=list(dta.loc[dta[k],:].index)

    return KeggCL

def parse_QB(filename):
    with open(filename, 'r') as file:
        content = file.read()

    lines = content.split('\n')
    data = {}
    genes = []
    conds = []

    for line in lines:       
        if line.startswith('BC'):
            bcl=line.split('\t')[0]
            # print(bcl)
        line = line.strip()
        if line.startswith('Genes'):
            genes_list = line.split(':')[1].split()#[line.index('[')+1:line.index(']')].split()
        if line.startswith('Conds'):
            conds = [int(x[1:]) for x in line.split(':')[1].split()]#line[line.index('[')+1:line.index(']')].split()
            dt={'genes':[],'conds':[]}
            dt['genes']=genes_list;dt['conds']=conds
            data[bcl]=dt
    # print(len(data))
    return data

def parse_text(text):
    lines = text.split("\n")
    # print()
    data = []
    curr_dict = {}
    
    for line in lines:
        if line.startswith(" bc#"):
            # print(line)
            if curr_dict:
                data.append(curr_dict)
            curr_dict = {}
            curr_dict[line.split(":")[0].strip()] = int(line.split(":")[1].strip())
        elif line.startswith(" c:"):
            curr_dict[line.split(":")[0].strip()] = list(map(int, line.split(":")[1].strip().split()))
        elif line.startswith(" r:"):
            curr_dict[line.split(":")[0].strip()] = list(map(int, line.split(":")[1].strip().split()))
    
    if curr_dict:
        data.append(curr_dict)
    
    return data

def parse_RB(filename): #def preParse(filename):
    with open(filename,'r') as f:
        text=f.read()
    parsedDt=parse_text(text)
    return parsedDt
