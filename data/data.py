# -*- coding: utf-8 -*-

import os
import pandas as pd
import joblib
from sentence_transformers import InputExample


base_path = os.path.dirname(__file__)
input_path = os.path.join(base_path, "input_data")
train_df = pd.read_csv(os.path.join(input_path, 'trial_1', 'train.csv'), encoding='utf-8-sig')
train_df['label'] = train_df['label'].astype(float)
val_df = pd.read_csv(os.path.join(input_path, 'trial_1', 'val.csv'), encoding='utf-8-sig')
val_df['label'] = val_df['label'].astype(float)

#---- train & val dataframes checks

# for example checking that those dataframes isn't empty

if len(train_df)>0 & len(val_df)>0:
    os.makedirs(os.path.join(base_path, "success"))
else:
    os.makedirs(os.path.join(base_path, "fail"))

#---------------------------------

input_train_examples_list = [InputExample(texts=[text_1, text_2], label=label) for text_1, text_2, label in
                             zip(train_df['title_en'], train_df['description_en'], train_df['label'])]

with open(os.path.join(base_path, 'input_train_examples_list.joblib'), 'wb') as f:
        joblib.dump(input_train_examples_list, f)
        
with open(os.path.join(base_path, 'train_df.joblib'), 'wb') as f:
        joblib.dump(train_df, f)
        
with open(os.path.join(base_path, 'val_df.joblib'), 'wb') as f:
        joblib.dump(val_df, f)
        
        