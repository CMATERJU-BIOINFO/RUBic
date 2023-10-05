# RUBic : Rapid Unsupervised Biclustering
-------------------------------------------
![Fig1](https://github.com/CMATERJU-BIOINFO/RUBic/assets/56863228/243df6d6-74e2-4a9d-a8d1-af33a127bd08)

The unsupervised biclustering strategy works both in interaction data and expression data. Initially, it converts the expression data into binary data using mixture of left truncated Gaussian distribution model (LTMG) and find the biclusters using novel encoding and template searching strategy and finally generates the biclusters in two modes base and flex. In base mode RUBic generates maximal biclusters (green borders) and in flex mode results less and biological significant clusters (red bordered). Coloured cell box within the clusters indicates the selected row and column positions.

## Repository Contents and Data Directory

The **data** directory contains the **dummy** data and four expression datasets named **ecoli_colombos**, **ecoli_dream5**, **yeast_dream5** and **yeast_gpl2529** in compressed format.
The dummy data includes two files, a) input.txt: sample input binary , b)op.txt: corresponding output file by executing RUBIC on the input.txt
│

├── data

│   ├── BicDataDic.json

│   ├── dummy.zip

│   ├── ecoli_colombos.rar

│   ├── ecoli_dream5.rar

│   ├── yeast_dream5.rar

│   └── yeast_gpl2529.rar

├── README.md

├── RUBIC

│   ├── inputdata.txt

│   ├── load_matrix_data.py

│   ├── P1-installandCompile.sh

│   ├── P2-runwargs.sh

│   ├── ParseCluster.py

│   ├── plotHeatmap.py

│   ├── RUBIC.c

│   └── RUBIC-Result-Analysis.ipynb

└── RUBIC-Result-Analysis.ipynb


**Compiler Installation, RUBic Compilation and Execution Commands**
-------------------------------------------
In any linux enviournment open a terminal and execute the following commands:

Navigate to the directory **RUBIC**
1.  *chmod +x P1-installandCompile.sh*
2.  *P1-installandCompile.sh RUBIC.c*
3.  *chmod +x P2-runwargs.sh*
4.  *P2-runwargs.sh RUBIC inputdata.txt output.txt 2 2 1*
   

# Mannual Setup

**Environment**
-------------------------------------------
1. GCC compiler and/or  C++ 11 compatible compiler 
2. Result Processing and visualisation  :

   a)  python >= 3
   
   b)  seaborn

**Input**
-------------------------------------------
The input to RUBic is in two formats: 

  1. Binary matrix [Interaction data: eg. Protein-protein interactions, Drug-Drug interaction)]
  2. non Binary matrix [Gene expression data of _m_ rows (Genes) and _n_ column (conditions)]
     
The data file should be comma delimited.
A sample data format is given in RUBIC directory. 

**Usage**
-------------------------------------------
_Step 1_ : Compile the RUBIC.c file with GCC compiler. : RUBIC.o

_Step 2_ : Convert the expression data into binary matrix if not binary matrix.

_Step 3_ : Keep the input file in the same directory  <Example: inputdata.txt>

_Step 4_ : Execute RUBIC wit the command:

        ./RUBIC.o <inputfile> <outputfile> <mnc> <mnr> <threshold>

   **inputfile**: input file name
   
   **outputfile**: output file name
   
   **mnc**: minimum no. of column
   
   **mnr**: minimum no. of row
   
   **threshold**: for binary 1.

**Visualisation and Result Processing**
-------------------------------------------
To visualise the result we have created a python notebook. You can find the details at (https://github.com/CMATERJU-BIOINFO/RUBic/blob/main/RUBIC/RUBIC-Result-Analysis.ipynb)
   
