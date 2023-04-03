from preClover import *

Clover_output = 'The_file_you_get_from_clover'


"""
takes clover output and parses tha data as a list of tuples where 
the left value represents a strand number that belongs to the cluster represented by the right value (key) 
"""
with open(Clover_output, 'r') as f:
    data = f.read()
# parse data as a list of tuples
data = eval(data)


"""
iterates over the clover output and counts in a dictionary for each key how many strands
belongs to it according to clover and which strands belongs to each cluster.
"""
count_dict = {}
group_dict = {}
for pair in data:
    left, right = pair
    left = int(left)
    right = int(right)
    if right in count_dict:
        count_dict[right] += 1
        group_dict[right].append(left)
    else:
        count_dict[right] = 1
        group_dict[right] = [left]





"""
sorts the keys of the group_dict and count_dict
"""
count_dict_keys = list(count_dict.keys())
count_dict_keys.sort()

group_dict_keys = list(group_dict.keys())
group_dict_keys.sort()


"""
iterates over the storalator output and for each key ( original strand) saves in dictionaries 
the size of the cluster and the strands that belongs to it.
this clustering has 100% accuracy , we use it to compare with the clover result and 
compute its accuracy
"""
storalator_dictionary = create_dict(original_strands_numbers, len(lines))
storalator_dictionary_count = {}
for strand in storalator_dictionary:
    storalator_dictionary_count[strand] = len(storalator_dictionary[strand])

dictionary1 = sorted(group_dict)
sorted_dict = {key: group_dict[key] for key in dictionary1}
group_dict = sorted_dict
temp_dict = group_dict.copy()




"""
the representitive (key) of each cluster created by clover is not necessarily the original strand
in this case, we switch the key to the original strand and the old key becomes value 
"""
rearranged_dict = switch_dict_key_value(temp_dict, original_strands_numbers)
dictionary2 = sorted(rearranged_dict)
sorted_dict2 = {key : rearranged_dict[key] for key in dictionary2}
rearranged_dict = sorted_dict2
rearranged_dict_keys = list(rearranged_dict.keys())
rearranged_dict_keys.sort()



"""
calculates the difference between the original clusters 
and the clusters outputted by clover and saves them in a list of extra or missing clusters 
"""
missing_clusters = diff_lists(rearranged_dict_keys, original_strands_numbers)
extra_clusters = diff_lists(original_strands_numbers, rearranged_dict_keys)
missing_clusters.sort()
extra_clusters.sort()







"""
for each original strand, checks if it's a key in the clover output 
calculates the difference between the strands that were belonged to it by clover 
and the storalator result 
"""
missing_strands_each_cluster = {}
extra_strands_each_cluster = {}
for strand in original_strands_numbers:
    if strand in rearranged_dict_keys:
        missing_strands = diff_lists(rearranged_dict[strand] , storalator_dictionary[strand])
        missing_strands_each_cluster[strand] = len(missing_strands)
        extra_strands = diff_lists(storalator_dictionary[strand], rearranged_dict[strand])
        extra_strands_each_cluster[strand] = len(extra_strands)





"""
creates a dictionary for the extra clusters and their strands 
"""
strands_for_extra_clusters = {}
strands_for_extra_clusters_count = {}
for cluster in extra_clusters:
    strands_for_extra_clusters[cluster] = rearranged_dict[cluster]
    strands_for_extra_clusters_count[cluster] = len(rearranged_dict[cluster])


print(f'On average Clover assigned { sum(extra_strands_each_cluster.values())/len(original_strands_numbers)} additional strands to each original cluster.')

print(f'On average Clover assigned { sum(strands_for_extra_clusters_count.values())/len(extra_clusters)} strands to each new cluster.')



"""
calculates for each original cluster how many clusters it was divided into 
"""
number_of_groups_each_orig_cluster = {}
for strand in original_strands_numbers:
    if strand in missing_clusters:
        number_of_groups_each_orig_cluster[strand] = 0
    else:
        number_of_groups_each_orig_cluster[strand] = 1

for cluster in extra_clusters:
    orig_cl = find_orig_strand(cluster, original_strands_numbers)
    number_of_groups_each_orig_cluster[orig_cl] += 1

print(f'On average each cluster was clustered into {sum(number_of_groups_each_orig_cluster.values())/len(original_strands_numbers)} new clusters.')

coverage_rate_each_cluster = {}
for strand in original_strands_numbers:
    if strand not in missing_clusters:
        coverage_rate_each_cluster[strand] = 1-missing_strands_each_cluster[strand]/storalator_dictionary_count[strand]
    if strand in missing_clusters:
        coverage_rate_each_cluster[strand] = 0

print(f'Clover produced {len(extra_clusters)} extra clusters')
print(f'Clover produced {len(missing_clusters)} missing clusters')
print(f'On average Clover assigned { sum(coverage_rate_each_cluster.values())/len(original_strands_numbers) } of the original strands to their original cluster.')
