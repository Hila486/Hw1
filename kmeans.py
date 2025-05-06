import math


ε = 0.001
k = 2
iter = 10
path = "tests/input_0EasyTest.txt"
#path = "tests/input_1.txt"
#with open()
with open(path, 'r') as file:
    data_points_x = [line.strip() for line in file]

def split_by_comma(input_string):
    return input_string.split(',')



def distance(p,q):
    sum = 0
    #print("p: ",p)
    for i in range(len(p)):
        sum += (float(p[i]) - float(q[i])) ** 2
    return math.sqrt(sum)

#finds the closest cluster to x and assigns it to the cluster
#input: x - (x1 = [a1,a2,...,an]) , clusters_array
def find_closest_cluster(x,clusters_array):
    min_clust_index = 0
    min_distance = distance(x,clusters_array[0][0])

    #find the cluster index closest to x
    for i in range(1, len(clusters_array)):
        #print("hila 123")
        #print("cluster center: ",clusters_array[i][0])
        #print("x: ",x)
        curr_distance = distance(x,clusters_array[i][0])
        if curr_distance < min_distance:
            min_distance = curr_distance
            min_clust_index = i
    #clusters_array[min_clust_index][1].append(x) #append x to the cluster

    #cluster_arr[min_clust_index][0].append(x)
    return min_clust_index


#Assign every xi to the closest cluster - step 2
def assign_clusters(cluster_arr):
    for i in range(len(cluster_arr)):
        for j in range(len(cluster_arr[i][1])):
            curr_x = cluster_arr[i][1][j]
            #print()
            #print("curr_x: ",curr_x)
            #find the closest cluster to x
            min_clust_index = find_closest_cluster(curr_x,clusters_array)
            #append x to the cluster
            if min_clust_index != i:
                #remove x from the old cluster
                clusters_array[i][1].remove(curr_x)
                #add x to the new cluster
                clusters_array[min_clust_index][1].append(curr_x)
            
def update_cluster_center(cluster, convergence_array,converged_index):
    
    prev_center = cluster[0]
    #update the cluster center
    new_center = [0]*len(cluster[0])
    for i in range(len(cluster[1])):
        for j in range(len(cluster[1][i])):
            new_center[j] += cluster[1][i][j]
    
    for i in range(len(new_center)):
        #print("new_center: ",new_center)
        if len(cluster[1]) != 0:
            new_center[i] /= len(cluster[1])

    
    convergence_array[converged_index] = distance(prev_center,new_center)
    
    return new_center


#step 3
def update_clusters_centers(clusters_array):
    
    convergence_array = [0]*len(clusters_array)
    
    #update the cluster array centers
    for i in range(len(clusters_array)):
        clusters_array[i][0] = update_cluster_center(clusters_array[i],convergence_array,i)
    return clusters_array, convergence_array

def check_convergence(convergence_array):
    for i in range(len(convergence_array)):
        if convergence_array[i] > ε:
            return False
    return True

#step 1
#init x arrays
x_array = [None]*len(data_points_x)
for i in range(len(x_array)):
    x_array[i] = split_by_comma(data_points_x[i])
#init cluster array: each cluster - [center(xi), the x's that are contained in cluster[x1,x4,....,xn] 
clusters_array = [None]*k
for i in range(k):
    clusters_array[i] = [x_array[i],[[0]*len(x_array[0])]] #["x1","x2"]]
# ",clusters_array)
convergence = False
i = 0

while not convergence and i < iter:
    assign_clusters(clusters_array)
    #update the clusters centers
    next_clusters_array, convergence_array = update_clusters_centers(clusters_array)
    
    #check if the clusters have converged
    convergence = check_convergence(convergence_array)    
    



