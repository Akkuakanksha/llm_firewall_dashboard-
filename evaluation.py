import pandas as pd
from classifier import classify_prompt

# 🔹 Keyword baseline
def keyword_filter(text):
    keywords = ["hack", "attack", "kill", "bypass", "violence", "hate"]
    
    for word in keywords:
        if word in text.lower():
            return "unsafe"
    return "safe"


# 🔹 Load dataset
# df = pd.read_csv(r"C:\Users\APOORVA\llm-firewall\evaluation.py\dataset.csv")
df = pd.read_csv(r"C:\Users\APOORVA\llm-firewall\dataset.csv")

total = len(df)

model_correct = 0
keyword_correct = 0

false_positives = 0
false_negatives = 0

results = []

# 🔹 Evaluation loop
for i, row in df.iterrows():
    text = row["text"]
    true_label = row["label"]

    # Model prediction
    model_result = classify_prompt(text)
    model_pred = model_result["verdict"]

    # Keyword prediction
    keyword_pred = keyword_filter(text)

    # Accuracy check
    if model_pred == true_label:
        model_correct += 1
    else:
        # Track failures
        if model_pred == "unsafe" and true_label == "safe":
            false_positives += 1
        elif model_pred == "safe" and true_label == "unsafe":
            false_negatives += 1

    if keyword_pred == true_label:
        keyword_correct += 1

    # Save results
    results.append({
        "text": text,
        "true": true_label,
        "model": model_pred,
        "keyword": keyword_pred,
        "confidence": model_result["confidence"]
    })


# 🔹 Final Metrics
model_accuracy = model_correct / total
keyword_accuracy = keyword_correct / total

print("\n===== RESULTS =====")
print(f"Total Samples: {total}")
print(f"Model Accuracy: {model_accuracy:.2f}")
print(f"Keyword Accuracy: {keyword_accuracy:.2f}")

print("\n===== ERRORS =====")
print(f"False Positives: {false_positives}")
print(f"False Negatives: {false_negatives}")


# 🔹 Save results to CSV
results_df = pd.DataFrame(results)
results_df.to_csv("results.csv", index=False)

print("\nResults saved to results.csv")


# 🔥 Show failures (VERY IMPORTANT)
print("\n===== FAILURE CASES =====")
for r in results:
    if r["model"] != r["true"]:
        print(f"\nText: {r['text']}")
        print(f"Expected: {r['true']} | Got: {r['model']}")