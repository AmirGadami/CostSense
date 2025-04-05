# 💸 CostSense

**CostSense** is a fine-tuned GPT-based AI system that estimates the prices of consumer items based on textual descriptions. It leverages a Hugging Face dataset and OpenAI’s `gpt-4o-mini` model to deliver precise price predictions with no extra explanations—just numbers.

---

## 🚀 Features

- 🧠 Fine-tuned on a **Hugging Face dataset** for realistic item pricing  
- 🔬 Uses **OpenAI’s `gpt-4o-mini` (July 2024)** for high-quality predictions  
- 🗃️ Automatic formatting to OpenAI-compatible JSONL  
- 📦 Modular and reusable architecture with `Item` and `Tester` utilities  
- 📈 Evaluation and visualizations for model performance  
- 🧪 Weights & Biases integration for training tracking  

---

## 📁 Project Structure

```bash
.
├── gpt_model.ipynb              # Interactive testing of base or fine-tuned models
├── fine_tuned_gpt.ipynb         # End-to-end fine-tuning workflow
├── items.py                     # Item class: handles prompt formatting
├── loaders.py                   # Data loading from Hugging Face dataset
├── testing.py                   # Performance metrics and evaluation
├── environment.yml              # Conda environment definition
├── train.pkl                    # Preprocessed training data
├── test.pkl                     # Preprocessed testing data
├── fine_tune_train.jsonl        # Training data for OpenAI fine-tuning
├── fine_tune_validation.jsonl   # Validation data for OpenAI fine-tuning
```

---

## ⚙️ Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/CostSense.git
cd CostSense
```

### 2. Create the Environment

```bash
conda env create -f environment.yml
conda activate llms
```

### 3. Set Environment Variables

Create a `.env` file in the root directory:

```env
HF_TOKEN=your_huggingface_token
OPENAI_API_KEY=your_openai_api_key
```

---

## 📊 Dataset

CostSense uses a **Hugging Face dataset** containing item descriptions and ground truth prices. It is preprocessed and stored as `train.pkl` and `test.pkl`. You can easily replace it with your own dataset using the format defined in `items.py`.

---

## 🧪 Fine-Tuning & Evaluation

### Run the fine-tuning pipeline:
- Load and split your dataset  
- Convert to OpenAI's JSONL format  
- Upload data via OpenAI's API  
- Fine-tune using `gpt-4o-mini-2024-07-18`  
- Retrieve your model and evaluate it on test items  

### Evaluate model accuracy:

```python
Tester.test(gpt_fine_tuned, test)
```

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
- **Hugging Face Hub** (datasets, token management)
- **Weights & Biases** (optional integration)
- **Transformers**, **LangChain**, **Gradio**
- **Python**, **Jupyter**, **FAISS**, **dotenv**

---

## 🧠 Use Cases

- E-commerce product valuation  
- Retail market analysis  
- Intelligent chatbots that estimate costs  
- Pricing prediction for recommendation systems  

---

## 📬 Contact

**Amir Ghadami**  
📧 [ah.ghadami75@gmail.com](mailto:ah.ghadami75@gmail.com)  
🔗 [LinkedIn](https://www.linkedin.com/in/amirhosseinghadami/) | 🐦 [Twitter/X](https://x.com/Amir_ghadamii) | 💻 [GitHub](https://github.com/amirgadami)