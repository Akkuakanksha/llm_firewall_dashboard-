from transformers import pipeline

# Load model
classifier = pipeline("text-classification", model="unitary/toxic-bert")

THRESHOLD = 0.6


# 🔹 Keyword Filter
def keyword_filter(text):
    keywords = [
        "kill", "hate", "violence", "attack", "hurt",
        "password", "bank", "account", "phone", "email",
        "data", "details"
    ]

    text = text.lower()

    for word in keywords:
        if word in text:
            return "unsafe"
    return "safe"


# 🔹 Pattern Detection (Jailbreak / Injection)
def pattern_check(text):
    text = text.lower()

    if "ignore previous instructions" in text:
        return "unsafe"

    if "act as" in text:
        return "unsafe"

    if "bypass" in text or "override" in text:
        return "unsafe"

    return "safe"


# 🔹 Main Function
def classify_prompt(text):
    result = classifier(text)[0]

    score = result['score']
    label = result['label']

    # Model-based decision
    model_result = "unsafe" if score > THRESHOLD else "safe"

    # Apply filters
    keyword_result = keyword_filter(text)
    pattern_result = pattern_check(text)

    # 🔥 Final Hybrid Decision
    if keyword_result == "unsafe" or pattern_result == "unsafe":
        verdict = "unsafe"
    elif model_result == "unsafe":
        verdict = "unsafe"
    else:
        verdict = "safe"

    return {
        "verdict": verdict,
        "category": label,   # for UI
        "confidence": score
    }


# 🔹 Run from terminal
if __name__ == "__main__":
    user_input = input("Enter prompt: ")

    output = classify_prompt(user_input)

    print("\nResult:")
    print(output)