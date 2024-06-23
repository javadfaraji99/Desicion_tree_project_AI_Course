import numpy as np
import pandas as pd
import csv

full_data = pd.read_csv('onlinefraud.csv')

type_mapping = {"PAYMENT": 1, "TRANSFER": 2, "DEBIT": 3, "CASH_IN": 4, "CASH_OUT": 5}
full_data['type'] = full_data['type'].map(type_mapping)

# Mapping Amount
full_data['categoricalAmount'] = pd.qcut(full_data['amount'],10)
print(full_data[['categoricalAmount','isFraud']].groupby('categoricalAmount').mean())

full_data.loc[ full_data['amount'] <= 0.319, 'amount'] 						        = 0
full_data.loc[(full_data['amount'] > 0.319) & (full_data['amount'] <= 3528.78), 'amount'] = 1
full_data.loc[(full_data['amount'] > 3528.78) & (full_data['amount'] <= 7574.786), 'amount']   = 2
full_data.loc[(full_data['amount'] > 7574.786) & (full_data['amount'] <= 12897.183), 'amount']   = 3
full_data.loc[(full_data['amount'] > 12897.183) & (full_data['amount'] <= 22475.506), 'amount']   = 4
full_data.loc[(full_data['amount'] > 22475.506) & (full_data['amount'] <= 52745.52), 'amount']   = 5
full_data.loc[(full_data['amount'] > 52745.52) & (full_data['amount'] <= 109141.484), 'amount']   = 6
full_data.loc[(full_data['amount'] > 109141.484) & (full_data['amount'] <= 173581.355), 'amount']   = 7
full_data.loc[(full_data['amount'] > 173581.355) & (full_data['amount'] <= 256638.936), 'amount']   = 8
full_data.loc[(full_data['amount'] > 256638.936) & (full_data['amount'] <= 397698.908), 'amount']   = 9
full_data.loc[(full_data['amount'] > 397698.908) & (full_data['amount'] <= 10000000.0), 'amount']   = 10
full_data.loc[ full_data['amount'] > 10000000.0, 'amount'] 							        = 11
full_data['amount'] = full_data['amount'].astype(int)

# Mapping oldbalanceOrg
full_data['categoricalOldbalanceOrg'] = pd.cut(full_data['oldbalanceOrg'],5)
print(full_data[['categoricalOldbalanceOrg','isFraud']].groupby('categoricalOldbalanceOrg').mean())
print(full_data['categoricalOldbalanceOrg'].value_counts())

full_data.loc[ full_data['oldbalanceOrg'] <= -33800.0, 'oldbalanceOrg'] 					       = 0
full_data.loc[(full_data['oldbalanceOrg'] > -33800.0) & (full_data['oldbalanceOrg'] <= 6760000.0), 'oldbalanceOrg'] = 1
full_data.loc[(full_data['oldbalanceOrg'] > 6760000.0) & (full_data['oldbalanceOrg'] <= 13520000.0), 'oldbalanceOrg'] = 2
full_data.loc[(full_data['oldbalanceOrg'] > 13520000.0) & (full_data['oldbalanceOrg'] <= 20280000.0), 'oldbalanceOrg'] = 3
full_data.loc[(full_data['oldbalanceOrg'] > 20280000.0) & (full_data['oldbalanceOrg'] <= 27040000.0), 'oldbalanceOrg'] = 4
full_data.loc[(full_data['oldbalanceOrg'] > 27040000.0) & (full_data['oldbalanceOrg'] <= 33800000.0), 'oldbalanceOrg'] = 5
full_data.loc[ full_data['oldbalanceOrg'] > 33800000.0, 'oldbalanceOrg']                                                = 6
full_data['oldbalanceOrg'] = full_data['oldbalanceOrg'].astype(int)

# Mapping oldbalanceDest
full_data['categoricaloldbalanceDest'] = pd.cut(full_data['oldbalanceDest'],5)
print(full_data[['categoricaloldbalanceDest','isFraud']].groupby('categoricaloldbalanceDest').mean())
print(full_data['categoricaloldbalanceDest'].value_counts())

full_data.loc[ full_data['oldbalanceDest'] <= -34000.0, 'oldbalanceDest'] 					       = 0
full_data.loc[(full_data['oldbalanceDest'] > -34000.0) & (full_data['oldbalanceDest'] <= 6800000.0), 'oldbalanceDest'] = 1
full_data.loc[(full_data['oldbalanceDest'] > 6800000.0) & (full_data['oldbalanceDest'] <= 13600000.0), 'oldbalanceDest'] = 2
full_data.loc[(full_data['oldbalanceDest'] > 13600000.0) & (full_data['oldbalanceDest'] <= 20400000.0), 'oldbalanceDest'] = 3
full_data.loc[(full_data['oldbalanceDest'] > 20400000.0) & (full_data['oldbalanceDest'] <= 27200000.0), 'oldbalanceDest'] = 4
full_data.loc[(full_data['oldbalanceDest'] > 27200000.0) & (full_data['oldbalanceDest'] <= 34000000.0), 'oldbalanceDest'] = 5
full_data.loc[ full_data['oldbalanceDest'] > 34000000.0, 'oldbalanceDest']                                                = 6
full_data['oldbalanceDest'] = full_data['oldbalanceDest'].astype(int)

# Mapping newbalanceOrig
full_data['categoricalnewbalanceOrig'] = pd.cut(full_data['newbalanceOrig'],5)
print(full_data[['categoricalnewbalanceOrig','isFraud']].groupby('categoricalnewbalanceOrig').mean())
print(full_data['categoricalnewbalanceOrig'].value_counts())

full_data.loc[ full_data['newbalanceOrig'] <= -34000.0, 'newbalanceOrig'] 					       = 0
full_data.loc[(full_data['newbalanceOrig'] > -34000.0) & (full_data['newbalanceOrig'] <= 6800000.0), 'newbalanceOrig'] = 1
full_data.loc[(full_data['newbalanceOrig'] > 6800000.0) & (full_data['newbalanceOrig'] <= 13600000.0), 'newbalanceOrig'] = 2
full_data.loc[(full_data['newbalanceOrig'] > 13600000.0) & (full_data['newbalanceOrig'] <= 20400000.0), 'newbalanceOrig'] = 3
full_data.loc[(full_data['newbalanceOrig'] > 20400000.0) & (full_data['newbalanceOrig'] <= 27200000.0), 'newbalanceOrig'] = 4
full_data.loc[(full_data['newbalanceOrig'] > 27200000.0) & (full_data['newbalanceOrig'] <= 34000000.0), 'newbalanceOrig'] = 5
full_data.loc[ full_data['newbalanceOrig'] > 34000000.0, 'newbalanceOrig']                                                = 6
full_data['newbalanceOrig'] = full_data['newbalanceOrig'].astype(int)

# Mapping newbalanceDest
full_data['categoricalnewbalanceDest'] = pd.cut(full_data['newbalanceDest'],5)
print(full_data[['categoricalnewbalanceDest','isFraud']].groupby('categoricalnewbalanceDest').mean())
print(full_data['categoricalnewbalanceDest'].value_counts())

full_data.loc[ full_data['newbalanceDest'] <= -38900.0, 'newbalanceDest'] 					       = 0
full_data.loc[(full_data['newbalanceDest'] > -38900.0) & (full_data['newbalanceDest'] <= 7780000.0), 'newbalanceDest'] = 1
full_data.loc[(full_data['newbalanceDest'] > 7780000.0) & (full_data['newbalanceDest'] <= 15560000.0), 'newbalanceDest'] = 2
full_data.loc[(full_data['newbalanceDest'] > 15560000.0) & (full_data['newbalanceDest'] <= 23340000.0), 'newbalanceDest'] = 3
full_data.loc[(full_data['newbalanceDest'] > 23340000.0) & (full_data['newbalanceDest'] <= 31120000.0), 'newbalanceDest'] = 4
full_data.loc[(full_data['newbalanceDest'] > 31120000.0) & (full_data['newbalanceDest'] <= 38900000.0), 'newbalanceDest'] = 5
full_data.loc[ full_data['newbalanceDest'] > 38900000.0, 'newbalanceDest']                                                = 6
full_data['newbalanceDest'] = full_data['newbalanceDest'].astype(int)


# clean redaundant data
full_data = full_data.drop(["categoricalAmount","categoricalOldbalanceOrg","categoricaloldbalanceDest","categoricalnewbalanceOrig","categoricalnewbalanceDest","nameDest","nameOrig"],axis=1)

# new csv file with cleaned data
with open('full_data_cleaned_static.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    writer.writerow(full_data.head(1))

    full_data_cleaned = np.array(full_data)
    for dataset in full_data_cleaned:
        writer.writerow(dataset)