import numpy as np
import pandas as pd
import csv

full_data = pd.read_csv('onlinefraud.csv')

# type
type_mapping = {"PAYMENT": 1, "TRANSFER": 2, "DEBIT": 3, "CASH_IN": 4, "CASH_OUT": 5}
full_data['type'] = full_data['type'].map(type_mapping)

# Amount
num_amount_ranges = 10

full_data['categoricalAmount'], quantiles = pd.qcut(full_data['amount'], q=num_amount_ranges, labels=False, retbins=True)

code = ""
for i in range(num_amount_ranges + 2):
    if i == 0:
        condition = f"full_data['amount'] <= {quantiles[i]}"
    elif i == num_amount_ranges + 1:
        condition = f"full_data['amount'] > {quantiles[i-1]}"
    else:
        condition = f"(full_data['amount'] > {quantiles[i-1]}) & (full_data['amount'] <= {quantiles[i]})"
    code += f"full_data.loc[{condition}, 'amount'] = {i}\n"

print(code)
exec(code)

full_data['amount'] = full_data['amount'].astype(int)

print(full_data[['amount', 'isFraud']].groupby('amount').mean())

# OldbalanceOrg
num_oldbalanceOrg_ranges = 5

full_data['categoricalOldbalanceOrg'], bins = pd.cut(full_data['oldbalanceOrg'], num_oldbalanceOrg_ranges, retbins=True)

range_boundaries = list(zip(bins[:-1], bins[1:]))

code = ""
for i, (lower, upper) in enumerate(range_boundaries):
    if i == 0:
        condition = f"full_data['oldbalanceOrg'] <= {lower}"
        code += f"full_data.loc[{condition}, 'oldbalanceOrg'] = {i}\n"
        condition = f"full_data['oldbalanceOrg'] > {lower}) & (full_data['oldbalanceOrg'] <= {upper})"
        code += f"full_data.loc[({condition}, 'oldbalanceOrg'] = {i + 1}\n"
    elif i == num_oldbalanceOrg_ranges - 1:
        condition = f"full_data['oldbalanceOrg'] > {lower}) & (full_data['oldbalanceOrg'] <= {upper})"
        code += f"full_data.loc[({condition}, 'oldbalanceOrg'] = {i + 1}\n"
        condition = f"full_data['oldbalanceOrg'] > {upper}"
        code += f"full_data.loc[{condition}, 'oldbalanceOrg'] = {i + 2}\n"
    else:
        condition = f"full_data['oldbalanceOrg'] > {lower}) & (full_data['oldbalanceOrg'] <= {upper})"
        code += f"full_data.loc[({condition}, 'oldbalanceOrg'] = {i + 1}\n"

print(code)
exec(code)

full_data['oldbalanceOrg'] = full_data['oldbalanceOrg'].astype(int)

print(full_data[['oldbalanceOrg', 'isFraud']].groupby('oldbalanceOrg').mean())

print(full_data['oldbalanceOrg'].value_counts())

# NewbalanceOrig
num_newbalanceOrig_ranges = 5

full_data['categoricalnewbalanceOrig'], bins = pd.cut(full_data['newbalanceOrig'], num_newbalanceOrig_ranges, retbins=True)

range_boundaries = list(zip(bins[:-1], bins[1:]))

code = ""
for i, (lower, upper) in enumerate(range_boundaries):
    if i == 0:
        condition = f"full_data['newbalanceOrig'] <= {lower}"
        code += f"full_data.loc[{condition}, 'newbalanceOrig'] = {i}\n"
        condition = f"full_data['newbalanceOrig'] > {lower}) & (full_data['newbalanceOrig'] <= {upper})"
        code += f"full_data.loc[({condition}, 'newbalanceOrig'] = {i + 1}\n"
    elif i == num_newbalanceOrig_ranges - 1:
        condition = f"full_data['newbalanceOrig'] > {lower}) & (full_data['newbalanceOrig'] <= {upper})"
        code += f"full_data.loc[({condition}, 'newbalanceOrig'] = {i + 1}\n"
        condition = f"full_data['newbalanceOrig'] > {upper}"
        code += f"full_data.loc[{condition}, 'newbalanceOrig'] = {i + 2}\n"
    else:
        condition = f"full_data['newbalanceOrig'] > {lower}) & (full_data['newbalanceOrig'] <= {upper})"
        code += f"full_data.loc[({condition}, 'newbalanceOrig'] = {i + 1}\n"

print(code)
exec(code)

full_data['newbalanceOrig'] = full_data['newbalanceOrig'].astype(int)

print(full_data[['newbalanceOrig', 'isFraud']].groupby('newbalanceOrig').mean())

print(full_data['newbalanceOrig'].value_counts())

# OldbalanceDest
num_oldbalanceDest_ranges = 5

full_data['categoricaloldbalanceDest'], bins = pd.cut(full_data['oldbalanceDest'], num_oldbalanceDest_ranges, retbins=True)

range_boundaries = list(zip(bins[:-1], bins[1:]))

code = ""
for i, (lower, upper) in enumerate(range_boundaries):
    if i == 0:
        condition = f"full_data['oldbalanceDest'] <= {lower}"
        code += f"full_data.loc[{condition}, 'oldbalanceDest'] = {i}\n"
        condition = f"full_data['oldbalanceDest'] > {lower}) & (full_data['oldbalanceDest'] <= {upper})"
        code += f"full_data.loc[({condition}, 'oldbalanceDest'] = {i + 1}\n"
    elif i == num_oldbalanceDest_ranges - 1:
        condition = f"full_data['oldbalanceDest'] > {lower}) & (full_data['oldbalanceDest'] <= {upper})"
        code += f"full_data.loc[({condition}, 'oldbalanceDest'] = {i + 1}\n"
        condition = f"full_data['oldbalanceDest'] > {upper}"
        code += f"full_data.loc[{condition}, 'oldbalanceDest'] = {i + 2}\n"
    else:
        condition = f"full_data['oldbalanceDest'] > {lower}) & (full_data['oldbalanceDest'] <= {upper})"
        code += f"full_data.loc[({condition}, 'oldbalanceDest'] = {i + 1}\n"

print(code)
exec(code)

full_data['oldbalanceDest'] = full_data['oldbalanceDest'].astype(int)

print(full_data[['oldbalanceDest', 'isFraud']].groupby('oldbalanceDest').mean())

print(full_data['oldbalanceDest'].value_counts())

# NewbalanceDest
num_newbalanceDest_ranges = 5

full_data['categoricalnewbalanceDest'], bins = pd.cut(full_data['newbalanceDest'], num_newbalanceDest_ranges, retbins=True)

range_boundaries = list(zip(bins[:-1], bins[1:]))

code = ""
for i, (lower, upper) in enumerate(range_boundaries):
    if i == 0:
        condition = f"full_data['newbalanceDest'] <= {lower}"
        code += f"full_data.loc[{condition}, 'newbalanceDest'] = {i}\n"
        condition = f"full_data['newbalanceDest'] > {lower}) & (full_data['newbalanceDest'] <= {upper})"
        code += f"full_data.loc[({condition}, 'newbalanceDest'] = {i + 1}\n"
    elif i == num_newbalanceDest_ranges - 1:
        condition = f"full_data['newbalanceDest'] > {lower}) & (full_data['newbalanceDest'] <= {upper})"
        code += f"full_data.loc[({condition}, 'newbalanceDest'] = {i + 1}\n"
        condition = f"full_data['newbalanceDest'] > {upper}"
        code += f"full_data.loc[{condition}, 'newbalanceDest'] = {i + 2}\n"
    else:
        condition = f"full_data['newbalanceDest'] > {lower}) & (full_data['newbalanceDest'] <= {upper})"
        code += f"full_data.loc[({condition}, 'newbalanceDest'] = {i + 1}\n"

print(code)
exec(code)

full_data['newbalanceDest'] = full_data['newbalanceDest'].astype(int)

print(full_data[['newbalanceDest', 'isFraud']].groupby('newbalanceDest').mean())

print(full_data['newbalanceDest'].value_counts())

# clean redaundant data
full_data = full_data.drop(["categoricalAmount","categoricalOldbalanceOrg","categoricaloldbalanceDest","categoricalnewbalanceOrig","categoricalnewbalanceDest","nameDest","nameOrig"],axis=1)

# new csv file with cleaned data
with open('full_data_cleaned_dynamic.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    writer.writerow(full_data.head(1))

    full_data_cleaned = np.array(full_data)
    for dataset in full_data_cleaned:
        writer.writerow(dataset)