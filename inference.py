import gradio as gr

def baseline_model(email_text):
    spam_keywords = ["win", "free", "offer", "money", "claim"]
    
    for word in spam_keywords:
        if word in email_text.lower():
            return "🚨 This looks like SPAM!"
            
    return "✅ This looks like a SAFE email."

if __name__ == "__main__":
    demo = gr.Interface(
        fn=baseline_model,
        inputs=gr.Textbox(lines=2, placeholder="Paste your email text here..."),
        outputs="text",
        title="Email Spam Classifier",
        description="Type in an email to check if it's spam or safe."
    )
    demo.launch(server_name="0.0.0.0", server_port=7860)
