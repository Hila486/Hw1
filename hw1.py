import math





k = 2
iter = 10
path = "tests\\input_1.txt"
#with open()
with open(path, 'r') as file:
    data_points_x = [line.strip() for line in file]

def split_by_comma(input_string):
    return input_string.split(',')

def find_min(x,cluster_arr):
    #x_arr - for example x1 = [x1,x2,/// xd]
    min_clust_index = 0
    min_distance = distance(x,cluster_arr[0][0])

    #find the min index cluster
    for i in range(1, len(cluster_arr)):
        curr_distance = distance(x,cluster_arr[i][0])
        if curr_distance < min_distance:
            min_distance = curr_distance
            min_clust_index = i

    # assign x to the new cluster index - another func??
    # remove - reset the whole array instead??
    # assign to i

    #cluster_arr[min_clust_index][0].append(x)
    return min_clust_index

#init x arrays
x_array = [None]*len(data_points_x)
for i in range(len(x_array)):
    print(data_points_x[i])
    x_array[i] = split_by_comma(data_points_x[i])
#init cluster array
clusters_array = [None]*k
#cluster = [center, [x1,x2,....,xj]
for i in range(k):
    clusters_array[i] = [x_array,[None]]#["x1","x2"]]
print(clusters_array)

for i in range(iter):
    for j in range(len(clusters_array)):
        #עבור כל קלסטר: נעבור על כל נקודה "איקס" שנמצאת בו, נבדוק אם היא צריכה להשאר בו או להעביר אותה לקלסטר אחר
    



#data = "8.1402,-5.8022,-7.2376/n10.1626,-7.4824,-6.5774/n9.3153,-5.4974,-6.7025"

"""recives arrays p and q (size d each) and calc the distance according to Eucldiean Distance"""
def distance(p,q):
    if len(p) != len(q):
        raise ValueError("Vectors p and q must be of the same length")
    return math.sqrt(sum((pi - qi) ** 2 for pi, qi in zip(p, q)))





