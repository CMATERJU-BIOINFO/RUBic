import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import numpy.ma as ma


def HeatmapGenX(data_matrix,Name,row_labels,vmin=None, vmax=None):

    plt.figure(figsize=(8,4),dpi=300)
    
    #Create heatmap
    ax = sns.heatmap(data_matrix, cmap='coolwarm', annot=False, fmt='.2f', cbar=True, vmin=vmin, vmax=vmax)
    plt.yticks(np.arange(len(row_labels)) + 0.1, row_labels, rotation='horizontal',fontsize=5)
    plt.title(Name)

    plt.show()

def HeatmapGen(data_matrix,row_labels,col_labels,vmin=None, vmax=None):
    # Generate random data matrix
    # data_matrix = matrixQ# np.random.rand(10, 10)
    plt.figure(figsize=(6,4),dpi=300)
 
    #Create heatmap
    ax = sns.heatmap(data_matrix, cmap='BuGn', annot=False, fmt='.2f', cbar=True, vmin=vmin, vmax=vmax)
    plt.xticks(np.arange(len(col_labels)) + 0.1, col_labels, rotation='vertical',fontsize=5)
    plt.yticks(np.arange(len(row_labels)) + 0.1, row_labels, rotation='horizontal',fontsize=5)
    ax.xaxis.tick_bottom()
    plt.title('Heatmap')


    # Display the plot
    plt.show()
    
    
def correlationHeatmap(dict1,dict2,xk,yk,a,b):
    
    m = len(dict1)
    n = len(dict2)
    
    plt.figure(figsize=(a,b),dpi=300)

    correlation_matrix = np.zeros((m, n))

    for i, key1 in enumerate(dict1.keys()):
        for j, key2 in enumerate(dict2.keys()):
            correlation = np.corrcoef(dict1[key1], dict2[key2])[0, 1]
            correlation_matrix[i, j] = correlation

            
    mask = np.triu(np.ones_like(correlation_matrix))

    masked_matrix = ma.masked_array(correlation_matrix, mask)
            
    # Create a heatmap
    ax=sns.heatmap(masked_matrix, annot=False, cmap="coolwarm", xticklabels=list(dict2.keys()), yticklabels=list(dict1.keys()))

    # Set the title and labels
    plt.title("Correlation ")
    ax.set_xticklabels(ax.get_xticklabels(), fontsize=4)
    ax.set_yticklabels(ax.get_yticklabels(), fontsize=4)

# Set the title and labels
    plt.xlabel(xk)
    plt.ylabel(yk)

# Display the heatmap
    plt.show()
#----------------------------------------