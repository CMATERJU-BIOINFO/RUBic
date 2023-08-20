# RUBic : Rapid Unsupervised Biclustering
-------------------------------------------
![Fig1](https://github.com/CMATERJU-BIOINFO/RUBic/assets/56863228/243df6d6-74e2-4a9d-a8d1-af33a127bd08)

The unsupervised biclustering strategy works both in interaction data and expression data. Initially, it converts the expression data into binary data using mixture of left truncated Gaussian distribution model (LTMG) and find the biclusters using novel encoding and template searching strategy and finally generates the biclusters in two modes base and flex. In base mode RUBic generates maximal biclusters (green borders) and in flex mode results less and biological significant clusters (red bordered). Coloured cell box within the clusters indicates the selected row and column positions.

**Environment**
-------------------------------------------
GCC compiler and/or  C++ 11 compatible compiler 
python >= 3

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

_Step 4_ : Execute the command:

        ./RUBIC.o <inputfile> <outputfile> <mnc> <mnr> <threshold>

   **inputfile**: input file name
   
   **outputfile**: output file name
   
   **mnc**: minimum no. of column
   
   **mnr**: minimum no. of row
   
   **threshold**: for binary 1.
   
