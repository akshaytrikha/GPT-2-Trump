import gradio as gr
from transformers import GPT2LMHeadModel, AutoTokenizer, pipeline
import torch

device = 'cuda' if torch.cuda.is_available() else 'cpu'

# load pretrained + finetuned GPT2
model = GPT2LMHeadModel.from_pretrained("./model")
model = model.to(device)

# create tokenizer
tokenizer = AutoTokenizer.from_pretrained(
    "gpt2", 
    pad_token='<|endoftext|>'
)

trump = pipeline("text-generation", model=model, tokenizer=tokenizer, config={"max_length":140})

def generate(text):
    result = trump(text, num_return_sequences=1)
    return result[0]["generated_text"].replace('"', '')  # remove quotation marks

examples = [
    ["Why does the lying news media"],
    ["The democrats have"],
    ["Today I'll be"],
]

demo = gr.Interface(
    fn=generate,
    inputs=gr.inputs.Textbox(lines=5, label="Prompt"),
    outputs=gr.outputs.Textbox(label="Generated Trump Tweet"),
    examples=examples
)

demo.launch()