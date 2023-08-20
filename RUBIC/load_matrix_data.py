import numpy as np

def load_matrix_from_file_charsExp(file_path):
    
    matrix = [];contd=[];GiD={};ico=0
    ExpMat={}
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('o') or line.startswith(' 	C'):     
                contd = [float(x[1:]) for x in line.split('\t')[1:]]
            else:
                ir=line.split('\t')
                GiD[ir[0]]=ico
                row = [float(value) for value in line.split('\t')[1:]]
                matrix.append(row)
                ExpMat[ir[0]]=row
                ico+=1
    print(f'Rows: {len(GiD)}, Col: {len(contd)}')
    ConD= {item: index for index, item in enumerate(contd)}
    return matrix,ConD,GiD,ExpMat

def load_matrix_from_file_chars(file_path):
    
    matrix = [];contd=[];GiD={};ico=0
    BinMat={}
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('o') or line.startswith(' 	C'):     
                contd = [float(x[1:]) for x in line.split('\t')[1:]]
            else:
                ir=line.split('\t')
                GiD[ir[0]]=ico
                row = [float(value) for value in line.split('\t')[1:]]
                matrix.append(row)
                BinMat[ir[0]]=row
                ico+=1
    print(f'Rows: {len(GiD)}, Col: {len(contd)}')
    ConD= {item: index for index, item in enumerate(contd)}
    return matrix,ConD,GiD,BinMat

def load_matrix_from_file(file_path):

    matrix = []
    with open(file_path, 'r') as file:
        for line in file:
            row = [int(value) for value in line.strip().split(',')]
            matrix.append(row)
    print(f'Matrix shape:{np.shape(matrix)}')    
    return matrix

##########################  submatrix loading functions  ###########################################

def load_submatrix_byRC(matrix, row_list, column_list):

    submatrix = []
    for row_index in row_list:
        row = [matrix[row_index][column_index] for column_index in column_list]
        submatrix.append(row)
    return submatrix

def load_submatrix_byGeneL(ExpMat,KeyL):  # load_submatrixK0(ExpMat,KeyL):

    MatX={}
    for k in KeyL:
        MatX[k]=ExpMat[k]
    return MatX
