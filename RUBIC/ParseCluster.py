import pickle

def parseKegg(ffr):
    
    with open(ffr,'rb') as f:
        dta=pickle.load(f,encoding='latin1')

    HeaderL=list(dta.columns)

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
        line = line.strip()
        if line.startswith('Genes'):
            genes_list = line.split(':')[1].split()#
            
        if line.startswith('Conds'):
            conds = [int(x[1:]) for x in line.split(':')[1].split()]#
            dt={'genes':[],'conds':[]}
            dt['genes']=genes_list;  
            dt['conds']=conds
            data[bcl]=dt

    return data

def parse_text(text):
    
    lines = text.split("\n")
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

def parse_RB(filename): 
    
    with open(filename,'r') as f:
        text=f.read()
    parsedDt=parse_text(text)
    
    return parsedDt