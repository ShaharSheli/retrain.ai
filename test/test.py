# -*- coding: utf-8 -*-

import os
import pandas as pd
import joblib

base_path = os.path.dirname(__file__)
input_path = os.path.join(base_path, "input_data")
sentence_transformer_model = joblib.load('sentence_transformer_model.joblib')

test_df = pd.read_csv(os.path.join(input_path, 'trial_1', 'test.csv'), encoding='utf-8-sig')
test_list = [': '.join([text_1, text_2]) for text_1, text_2 in zip(test_df['title_en'], test_df['description_en'])]
test_sent_embed = sentence_transformer_model.encode(["hi", "hello"])