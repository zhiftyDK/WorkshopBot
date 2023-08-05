from gpt4all import GPT4All
model = GPT4All(model_name="ggml-model-gpt4all-falcon-q4_0.bin", model_path="./models/", allow_download=False, n_threads=4)
def generate(prompt, system_prompt):
    with model.chat_session(system_prompt=system_prompt):
        output = model.generate(prompt, max_tokens=4096, n_batch=128, temp=0)
        return output