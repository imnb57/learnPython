from transformers import BertForSequenceClassification, AutoTokenizer
import torch

# Load pre-trained BERT model and tokenizer
model = BertForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=28)
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

# Freeze all layers except the final classification layer
for param in model.bert.parameters():
    param.requires_grad = False

# Only the classifier layer is trainable now
for param in model.classifier.parameters():
    param.requires_grad = True

# Check which parameters are trainable
for name, param in model.named_parameters():
    print(name, param.requires_grad)
