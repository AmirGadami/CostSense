# 💸 CostSense

**CostSense** is a fine-tuned AI system that estimates the prices of consumer items based on textual descriptions. It supports both **OpenAI’s `gpt-4o-mini`** and **Hugging Face LLaMA models fine-tuned with LoRA**, using a Hugging Face dataset and integrated experiment tracking with **Weights & Biases (wandb)**.

---

## 🚀 Features

- 🧠 Fine-tuned on a **Hugging Face dataset** for realistic item pricing  
- 🔬 Supports two fine-tuning tracks:
  - **OpenAI’s `gpt-4o-mini`** via OpenAI API
  - **LLaMA models** with **LoRA** using Hugging Face + PEFT  
- 📊 Built-in **Weights & Biases integration** for experiment tracking  
- 🗃️ Converts data to OpenAI-compatible JSONL format  
- 📦 Modular architecture with `Item` and `Tester` utilities  
- 📈 Model evaluation and comparison across approaches  

---

## 📁 Project Structure

```bash
.
├── gpt_model.ipynb              # Interactive testing of base or fine-tuned models
├── fine_tuned_gpt.ipynb         # Fine-tuning pipeline using OpenAI API
├── lora_fine_tuned.ipynb        # Fine-tuning LLaMA models using Hugging Face + LoRA
├── items.py                     # Item class for data structure and prompt formatting
├── loaders.py                   # Data loading from Hugging Face dataset
├── testing.py                   # Performance metrics and result testing
├── environment.yml              # Conda environment definition (name: llms)
├── train.pkl                    # Preprocessed training data
├── test.pkl                     # Preprocessed testing data
├── fine_tune_train.jsonl        # OpenAI-ready training data
├── fine_tune_validation.jsonl   # OpenAI-ready validation data
```

---

## ⚙️ Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/CostSense.git
cd CostSense
```

### 2. Create and Activate Environment

```bash
conda env create -f environment.yml
conda activate llms
```

### 3. Set Environment Variables

Create a `.env` file in the root directory with the following:

```env
HF_TOKEN=your_huggingface_token
OPENAI_API_KEY=your_openai_api_key
WANDB_API_KEY=your_wandb_api_key
```

---

## 📊 Dataset

CostSense uses a **Hugging Face dataset** containing item descriptions and ground truth prices. It's preprocessed and stored in `train.pkl` and `test.pkl`. You can swap it with your own dataset using the `Item` format.

---

## 🧪 Fine-Tuning & Evaluation

### 🔁 Option 1: OpenAI GPT Fine-Tuning

- Convert data to JSONL (`fine_tune_gpt.ipynb`)
- Upload and fine-tune `gpt-4o-mini`
- W&B tracking automatically integrated
- Evaluate predictions:

```python
Tester.test(gpt_fine_tuned, test)
```

### 🦙 Option 2: LLaMA + LoRA (Hugging Face)

- Use `lora_fine_tuned.ipynb` to fine-tune a LLaMA model
- Leverage `PEFT`, `bitsandbytes`, and Hugging Face's trainer
- Log metrics and results to W&B
- Predict and evaluate using the shared interface

---

## 📤 Example Prompt

```json
[
  {"role": "system", "content": "You estimate prices of items. Reply only with the price, no explanation"},
  {"role": "user", "content": "A high-resolution 27-inch 4K monitor with adjustable stand and HDMI support."}
]
```

**Expected Output**:
```
Price is $329.00
```

---

## 🧰 Tech Stack

- **OpenAI** (`gpt-4o-mini`)
- **Hugging Face Transformers** & **Datasets**
- **LLaMA + LoRA** with **PEFT**
- **Weights & Biases** for tracking and logging
- **Python**, **Jupyter**, **FAISS**, **Gradio**
- **dotenv**, **bitsandbytes**, **transformers**

---

## 🧠 Use Cases

- E-commerce product valuation  
- Retail analytics and forecasting  
- AI chatbots that estimate item prices  
- Educational demos of fine-tuning techniques  

---

## 📬 Contact

**Amir Ghadami**  
📧 [ah.ghadami75@gmail.com](mailto:ah.ghadami75@gmail.com)  
🔗 [LinkedIn](https://www.linkedin.com/in/amirhosseinghadami/) | 🐦 [Twitter/X](https://x.com/Amir_ghadamii) | 💻 [GitHub](https://github.com/amirgadami)