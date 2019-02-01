def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""
    # Number of data points: n
    n = len(data)

    # x-data for the ECDF: x
    x = np.sort(data)

    # y-data for the ECDF: y
    y = np.arange(1, n+1) / n

    return x, y

def plot_ecdf(data, xname, yname)
    # Compute ECDF for versicolor data: x_vers, y_vers
    x_vers, y_vers = ecdf(data)

    # Generate plot
    plt.plot(x_vers, y_vers, marker= '.', linestyle='none')

    # Label the axes
    plt.xlabel(xname)
    plt.ylabel(yname)

    # Display the plot
    plt.show()
    
    
def pearson_r(x, y):
    """Compute Pearson correlation coefficient between two arrays."""
    # Compute correlation matrix: corr_mat
    corr_mat = np.corrcoef(x, y)

    # Return entry [0,1]
    return corr_mat[0,1]