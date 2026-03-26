The system implements multiple safety systems which function as effective safeguards for blocking hazardous input materials from reaching Large Language Models. The system aims to enhance security measures by stopping dangerous output generation and block prompt injections and block jailbreak attempts and prevent unauthorized access to confidential information.

🎯 Problem Statement

The system of LLMs exhibits three security weaknesses which include:

1. The system creates toxic or harmful content.
2. The system allows users to execute prompt injection and jailbreak attacks.
3. The system enables users to request confidential or personal information.

The existing toxic classifiers function as traditional models because they fall short of defending against these particular threats. The project investigates a hybrid solution which will enhance system reliability and operational safety.

🚀 Approach

Three layers make up the design of the hybrid guardrail system.

1. The first system employs ML-based Classification which uses a pre-trained model named unitary/toxic-bert for detecting toxic and harmful language.
2. The system uses Keyword-based Filtering to detect unsafe words and phrases which can handle basic attacks and harmful intent.
3. The system uses Pattern-based Detection to identify jailbreak attempts and prompt injection patterns while it shows PII requests which include passwords and bank details.

The user system operates through three stages which include user input followed by guardrail system operation and the final decision which determines whether the outcome is safe or unsafe.

The guardrail system consists of three components which include:

The system uses a Toxicity Model which assesses user content. 
The system uses a Keyword Filter which identifies specific words. 
The system uses Pattern Rules to establish criteria for evaluating user behavior.

The system blocks any user request which fails to meet safety standards according to any security system component.

🛠️ Tech Stack
The project uses Python as its primary programming language.
The implementation uses Streamlit to create a Dashboard UI.
The system employs Transformers from Hugging Face for its operational functions.
The system uses Pandas as its primary tool for processing data.

The system uses 45 red-team prompts which include both safe and unsafe elements as its evaluation dataset.
The system uses three evaluation metrics which include Accuracy and False Positives and False Negatives.
The main results show that ML model performance becomes weak when facing indirect attacks while the hybrid method achieves better detection results which show that advanced guardrails are necessary to mitigate high false negative rates.

💡 Features
Real-time prompt analysis
Adjustable strictness threshold
Hybrid detection system
Evaluation dashboard with metrics
Detection of:
Toxic content
Jailbreak attempts
Sensitive data requests
🖥️ How to Run
# Clone repository
git clone <your-repo-link>

# Navigate to folder
cd llm-firewall

# Create virtual environment (optional)
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run evaluation
python evaluation.py

# Run dashboard
streamlit run app.py
📷 Demo

The Streamlit dashboard allows users to:

Enter prompts
Analyze safety in real-time
View evaluation metrics
🚧 Limitations
Limited dataset (45 samples)
Model not trained for PII or jailbreak detection
Rule-based methods may miss complex attacks
🔮 Future Work
Use advanced LLM-based guardrails
Expand dataset for better coverage
Add semantic and context-aware detection
Integrate real-time API monitoring
📌 Conclusion

This project demonstrates that no single method is sufficient for LLM safety. A multi-layered guardrail approach combining machine learning and rule-based techniques provides better protection against unsafe prompts.