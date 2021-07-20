# -*- coding: utf-8 -*-

import os
from datetime import datetime
import joblib
from torch.utils.data import DataLoader
from sentence_transformers import evaluation
from sentence_transformers import SentenceTransformer, losses, models


time_stamp = str(datetime.now().year) + "_" + str(datetime.now().month) + "_" + str(datetime.now().day) + "_" + \
                     str(datetime.now().hour) + "_" + str(datetime.now().minute)
base_path = os.path.dirname(__file__)
model_name = "sentence_transformers_model"
model_dir_data = model_name + "_" + time_stamp
output_path = os.path.join(base_path, "output_models")
model_path = os.path.join(output_path, model_dir_data)
if not os.path.exists(model_path):
    os.makedirs(model_path)
max_seq_length = 512
model = SentenceTransformer('distilbert-base-nli-mean-tokens')
model.max_seq_length = max_seq_length

#---- Loading data objects after data checking step
input_train_examples_list = joblib.load('input_train_examples_list.joblib')
train_df = joblib.load('train_df.joblib')
val_df = joblib.load('val_df.joblib')
#--------------------------------------------------

train_dataloader = DataLoader(input_train_examples_list, shuffle=True, batch_size=16)
train_loss = losses.CosineSimilarityLoss(model)
scores = val_df['label'].to_list()
evaluator = evaluation.EmbeddingSimilarityEvaluator(val_df['title_en'].to_list(), val_df['description_en'].to_list(), scores)
def callback(score, epoch, steps):
    pass
model.fit(train_objectives=[(train_dataloader, train_loss)], epochs=1, warmup_steps=20, steps_per_epoch=5, evaluator=evaluator,
          evaluation_steps=10, output_path=model_path, save_best_model=True,
          optimizer_params={'lr': 2e-5, 'eps': 1e-6, 'correct_bias': False}, callback=callback(scores, 1, 10))
transformer_path = os.path.join(model_path, "0_Transformer")
word_embedding_model = models.Transformer(transformer_path, max_seq_length=max_seq_length, do_lower_case=True)
pooling_model = models.Pooling(word_embedding_model.get_word_embedding_dimension())
sentence_transformer_model = SentenceTransformer(modules=[word_embedding_model, pooling_model])

with open(os.path.join(base_path, 'sentence_transformer_model.joblib'), 'wb') as f:
        joblib.dump(sentence_transformer_model, f)