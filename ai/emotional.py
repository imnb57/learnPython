# Import necessary libraries
from datasets import load_dataset
from transformers import BertTokenizer

# Load the GoEmotions dataset
dataset = load_dataset("go_emotions")

# Load the pre-trained BERT tokenizer
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

# Preview dataset structure
print(dataset)
