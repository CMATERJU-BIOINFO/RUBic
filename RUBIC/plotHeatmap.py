import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import numpy.ma as ma

def draw_heatmap(matrix,row_list, col_list, border_color,m,n,fin):

    color_map = ["white","yellow"]#, "red"]#, "orange",'blue']  # Define custom colors for values 2, 3, 4
    cmap = sns.color_palette(color_map)
    plt.figure(figsize=(5, 5), dpi=300)

    g=sns.heatmap(matrix, cmap=cmap,linewidth=0.01,annot=True, fmt="d",xticklabels=False, yticklabels=False,cbar=False)

    plt.tight_layout()
    
    print(f"----------{m}-{n}--------------")
    for i in range(m):
        for j in range(n):
            if i in row_list and j in col_list:
                g.add_patch(plt.Rectangle((j, i), 1, 1, fill=False, edgecolor=border_color, lw=3))

    ax = plt.gca()
    for t in ax.texts:
        t.set_fontsize(6)  # Set the font size

    plt.savefig(f'{fin}-1.png')
    plt.show()

def HeatmapGenX(data_matrix, Name, row_labels, vmin=None, vmax=None):
    # Transpose the data matrix to arrange the figure
    transposed_data = np.transpose(data_matrix)

    plt.figure(figsize=(4, 7), dpi=300)
    # Create heatmap with transposed data
    ax = sns.heatmap(transposed_data, cmap='coolwarm', annot=False, fmt='.2f', cbar=True, vmin=vmin, vmax=vmax)
    # Set x-axis ticks at the top
    ax.xaxis.tick_top()
    plt.xticks(np.arange(len(row_labels)) + 0.1, row_labels, rotation=90, fontsize=3)
    plt.title(Name)
    # Hide y-axis labels
    ax.set_yticklabels([])

    # Display the plot
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
#     plt.xlabel('X-axis label')
#     plt.ylabel('Y-axis label')

    # Display the plot
    plt.show()
    
    
def correlationHeatmap(dict1,dict2,xk,yk,a,b):
    #  def plotHtm(dict1,dict2,xk,yk,a,b):
    
    m = len(dict1)
    n = len(dict2)
    
    plt.figure(figsize=(a,b),dpi=300)
    # Create empty correlation matrix
    correlation_matrix = np.zeros((m, n))

    # Calculate the correlation between each key pair
    for i, key1 in enumerate(dict1.keys()):
        for j, key2 in enumerate(dict2.keys()):
            correlation = np.corrcoef(dict1[key1], dict2[key2])[0, 1]
            correlation_matrix[i, j] = correlation

            
    mask = np.triu(np.ones_like(correlation_matrix))

# Apply the mask to the correlation matrix
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

    
def plotHtmpRB(dict1,dict2,xk,yk,a,b,fin,border_color='black'):
    
    m = len(dict2)
    n = len(dict1)
    
    plt.figure(figsize=(a,b),dpi=300)
    # Create empty correlation matrix
    correlation_matrix = np.zeros((m, n))


    
    # Calculate the correlation between each key pair
    for i, key1 in enumerate(dict2.keys()):
        for j, key2 in enumerate(dict1.keys()):
            correlation = np.corrcoef(dict2[key1], dict1[key2])[0, 1]
            correlation_matrix[i, j] = correlation

    mask = np.triu(np.ones_like(correlation_matrix))

# Apply the mask to the correlation matrix
    masked_matrix = ma.masked_array(correlation_matrix, mask)
    aspect_ratio = n / m
    g=sns.heatmap(masked_matrix, annot=False, square=True,cmap="Greens",vmax=1,vmin=-0.6,\
                  linewidths=0.2, cbar=False, xticklabels=False,\
                  yticklabels=False)

    g.set_xticklabels(g.get_xticklabels(), fontsize=4)
    g.set_yticklabels(g.get_yticklabels(), fontsize=4)
    plt.xticks(rotation=90)
    plt.xlabel(xk, labelpad=8, rotation=0,fontsize=6)#,position=(1.0, 1.1))#, weight='bold')
    #Splt.gca().xaxis.set_label_coords(1.0, 1.1)  # Adjust the coordinates as needed

    plt.xlabel('KEGG (eco02020)', labelpad=1, fontsize=8 , rotation=0, va='center')#, weight='bold')
    #plt.gca().yaxis.set_label_coords(1.1, 0.5)
    plt.ylabel(yk, labelpad=1, fontsize=8)

    abs_corr = np.abs(correlation_matrix)
    LZ=[]
    for i in range(m):
        for j in range(n):
            if abs_corr[i, j] >= 0.9:
                g.add_patch(plt.Rectangle((j, i), 1, 1, fill=False, edgecolor='red', lw=1.0))
#             if abs_corr[i, j] >= 0.8:LZ.append(abs_corr[i,j])
    plt.savefig(f'{fin}-1.png')
    # Display the heatmap
    plt.show()
    
def plotHtmp(dict1,dict2,xk,yk,a,b,fin,border_color='black'):
    
    m = len(dict1)
    n = len(dict2)
    
    plt.figure(figsize=(a,b),dpi=300)
    # Create empty correlation matrix
    correlation_matrix = np.zeros((m, n))


    
    # Calculate the correlation between each key pair
    for i, key1 in enumerate(dict1.keys()):
        for j, key2 in enumerate(dict2.keys()):
            correlation = np.corrcoef(dict1[key1], dict2[key2])[0, 1]
            correlation_matrix[i, j] = correlation

    mask = np.triu(np.ones_like(correlation_matrix))

# Apply the mask to the correlation matrix
    masked_matrix = ma.masked_array(correlation_matrix, mask)
    aspect_ratio = n / m
    g=sns.heatmap(masked_matrix, annot=False, square=True,cmap="Greens",vmax=1,vmin=-0.6,\
                  linewidths=0.2, cbar=False, xticklabels=False,\
                  yticklabels=False)

    g.set_xticklabels(g.get_xticklabels(), fontsize=4)
    g.set_yticklabels(g.get_yticklabels(), fontsize=4)
    plt.xticks(rotation=90)
    plt.xlabel(xk, labelpad=8, fontsize=6)#, weight='bold')
    plt.xlabel('KEGG (eco02020)', labelpad=1, fontsize=8)#, weight='bold')
    plt.ylabel(yk, labelpad=1, fontsize=8)

    abs_corr = np.abs(correlation_matrix)
    LZ=[]
    for i in range(m):
        for j in range(n):
            if abs_corr[i, j] >= 0.9:
                g.add_patch(plt.Rectangle((j, i), 1, 1, fill=False, edgecolor='red', lw=1.2))
#             if abs_corr[i, j] >= 0.8:LZ.append(abs_corr[i,j])
    plt.savefig(f'{fin}-1.png')
    # Display the heatmap
    plt.show()
