import numpy as np
import math
import pandas as pd
import random

full_data = pd.read_csv("full_data_cleaned_static.csv")

is_fraud = full_data["isFraud"]
full_data = full_data.drop(["isFraud"],axis=1)

num_amount_ranges = 10
num_oldbalanceOrg_ranges = 5
num_newbalanceOrig_ranges = 5
num_oldbalanceDest_ranges = 5
num_newbalanceDest_ranges = 5

feature_numbers = {
'step' : [i for i in range(1,11)],
'type' : [i for i in range(1,6)],
'amount' : [i for i in range(0,num_amount_ranges + 2)],
'oldbalanceOrg' : [i for i in range(0,num_oldbalanceOrg_ranges + 2)],
'oldbalanceDest' : [i for i in range(0,num_oldbalanceDest_ranges + 2)],
'newbalanceOrig' : [i for i in range(0,num_newbalanceOrig_ranges + 2)],
'newbalanceDest' : [i for i in range(0,num_newbalanceDest_ranges + 2)]
}

feature_names = ["step", "type", "amount", "oldbalanceOrg", "newbalanceOrig", "oldbalanceDest", "newbalanceDest"]
value_mapping = {"step" : 0 , "type" : 1 ,"amount" : 2 , "oldbalanceOrg" : 3 , "newbalanceOrig" : 4 , "oldbalanceDest" : 5 , "newbalanceDest" : 6 , }



def calculate_entropy(labels):
    total_samples = len(labels)
    unique_labels, label_counts = np.unique(labels, return_counts=True)
    entropy = 0

    for count in label_counts:
        probability = count / total_samples
        entropy += probability * math.log2(probability)

    return -entropy

def calculate_information_gain(dataset, labels, feature_index):
    total_samples = len(labels)
    unique_values, value_counts = np.unique(dataset[:, feature_index], return_counts=True)
    weighted_entropy = 0

    for value, count in zip(unique_values, value_counts):
        subset_labels = labels[dataset[:, feature_index] == value]
        entropy = calculate_entropy(subset_labels)
        weighted_entropy += (count / total_samples) * entropy

    return calculate_entropy(labels) - weighted_entropy

class DecisionTree:
    def __init__(self):
        self.tree = {}

    def build_tree(self, dataset, labels, feature_names):
        if len(np.unique(labels)) == 1:
            return np.unique(labels)[0]

        if dataset.shape[1] == 0:
            return np.bincount(labels).argmax()

        information_gains = []
        # print(labels,dataset.shape)
        for i in range(dataset.shape[1]):
            information_gains.append(calculate_information_gain(dataset, labels, i))
        # print(information_gains)
        best_feature_index = np.argmax(information_gains)
        # print(best_feature_index)
        best_feature_name = feature_names[best_feature_index]
        self.tree = {best_feature_name: {}}

        unique_values = np.unique(dataset[:, best_feature_index])

        ds = np.array([[]])
        for value in feature_numbers[best_feature_name]:
            if value not in unique_values:
                dt = DecisionTree()
                self.tree[best_feature_name][value] = dt.build_tree(ds, labels, feature_names)

        # print(unique_values)
        for value in unique_values:
            subset_indices = np.where(dataset[:, best_feature_index] == value)[0]
            subset_dataset = np.concatenate((dataset[subset_indices, :best_feature_index],dataset[subset_indices,best_feature_index + 1:]),axis=1)
            subset_labels = labels[subset_indices]
            subset_feature_names = np.delete(feature_names, best_feature_index)
            # print(subset_feature_names)
            # print(best_feature_name)
            # print(self.tree)
            dt = DecisionTree()
            self.tree[best_feature_name][value] = dt.build_tree(subset_dataset, subset_labels, subset_feature_names)


        return self.tree
    
def predict(tree, sample, value_mapping):
    feature_name = next(iter(tree))
    feature_index = value_mapping[feature_name]
    feature_value = sample[feature_index]

    if feature_value in tree[feature_name]:
        subtree = tree[feature_name][feature_value]

        if isinstance(subtree, dict):
            return predict(subtree, sample, value_mapping)
        else:
            return subtree
    else:
        return None
    
def calculate_precision(decision_tree,test_dataset,test_labels):
    correct_predictions = 0
    total_samples = len(test_labels)

    for sample, label in zip(test_dataset, test_labels):
        prediction = predict(decision_tree,sample,value_mapping)
        
        if prediction == label:
            correct_predictions += 1

    precision = correct_predictions / total_samples * 100

    return precision


dataset = np.array(full_data)

true_dataset_indices = []
false_dataset_indices = []

for i in range(100000):
    if (is_fraud[i] == 0):
        true_dataset_indices.append(i)
    else:
        false_dataset_indices.append(i)

ratio = 0.05
number_of_dataset = 2400

# stratified k fold cross validation  k = 10
random_true_dataset_indices = random.sample(range(len(true_dataset_indices)),int(number_of_dataset * (1 - ratio)))
random_false_dataset_indices = random.sample(range(len(false_dataset_indices)),int(number_of_dataset * ratio))

examin_dataset = []
examin_labels = []
x = 0
y = 0
for k in range (number_of_dataset):
    if ((k % int(number_of_dataset / 10)) > (int((number_of_dataset / 10) * (1 - ratio)) - 1)):
        examin_dataset.append(dataset[random_false_dataset_indices[x]])
        examin_labels.append(1)
        x += 1
    else:
        examin_dataset.append(dataset[random_true_dataset_indices[y]])
        examin_labels.append(0)
        y += 1

dt = DecisionTree()
decesion_trees_k = []
precisions_k = []
examin_dataset = np.array(examin_dataset)
examin_labels = np.array(examin_labels)

for k in range(10):

    train_dataset = np.concatenate((examin_dataset[0:k * int(number_of_dataset / 10)] , examin_dataset[(k + 1) * int(number_of_dataset / 10):]) , axis = 0)
    test_dataset = examin_dataset[k * int(number_of_dataset / 10):(k + 1) * int(number_of_dataset / 10)]
    train_labels = np.concatenate((examin_labels[0:k * int(number_of_dataset / 10)] , examin_labels[(k + 1) * int(number_of_dataset / 10):]) , axis=0)
    test_labels = examin_labels[k * int(number_of_dataset / 10):(k + 1) * int(number_of_dataset / 10)]


    decision_tree = dt.build_tree(train_dataset,train_labels,feature_names)

    # print(decision_tree)

    precisions_k.append(calculate_precision(decision_tree,test_dataset,test_labels))
    decesion_trees_k.append(decision_tree)

print(precisions_k)
print("\n")
print(decesion_trees_k[precisions_k.index(max(precisions_k))])
print("\n")

    
# test set 50% 50%
n = 1000
test_dataset_indices = random.sample([i for i in range(len(true_dataset_indices)) if i not in random_true_dataset_indices], n) + random.sample([i for i in range(len(false_dataset_indices)) if i not in random_false_dataset_indices], n)

test_dataset = []
test_labels = []
for i in range(len(test_dataset_indices)):
    if i < n:
        test_dataset.append(dataset[test_dataset_indices[i]])
        test_labels.append(0)
    else:
        test_dataset.append(dataset[test_dataset_indices[i]])
        test_labels.append(1)

precisions_5 = []
decesion_trees_5 = []
test_dataset = np.array(test_dataset)
test_labels = np.array(test_labels)
for k in range(10):

    train_dataset = np.concatenate((examin_dataset[0:k * int(number_of_dataset / 10)] , examin_dataset[(k + 1) * int(number_of_dataset / 10):]) , axis = 0)
    train_labels = np.concatenate((examin_labels[0:k * int(number_of_dataset / 10)] , examin_labels[(k + 1) * int(number_of_dataset / 10):]) , axis=0)

    decision_tree = dt.build_tree(train_dataset,train_labels,feature_names)

    # print(decision_tree)

    precisions_5.append(calculate_precision(decision_tree,test_dataset,test_labels))
    decesion_trees_5.append(decision_tree)

print(precisions_5)
print("\n")

print(decesion_trees_5[precisions_5.index(max(precisions_5))])


