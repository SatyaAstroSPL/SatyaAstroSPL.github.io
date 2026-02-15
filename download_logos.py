import os
import requests

logos = {
    "chatgpt": "https://upload.wikimedia.org/wikipedia/commons/0/04/ChatGPT_logo.svg",
    "claude": "https://upload.wikimedia.org/wikipedia/commons/2/23/Claude_AI_logo.svg",
    "gemini": "https://upload.wikimedia.org/wikipedia/commons/8/8a/Google_Gemini_logo.svg",
    "perplexity": "https://logo.clearbit.com/perplexity.ai",
    "consensus": "https://logo.clearbit.com/consensus.app",
    "elicit": "https://logo.clearbit.com/elicit.com",
    "copilot": "https://logo.clearbit.com/github.com",
    "cursor": "https://logo.clearbit.com/cursor.sh",
    "tabnine": "https://logo.clearbit.com/tabnine.com",
    "huggingface": "https://logo.clearbit.com/huggingface.co",
    "midjourney": "https://logo.clearbit.com/midjourney.com",
    "runway": "https://logo.clearbit.com/runwayml.com",
    "notion": "https://logo.clearbit.com/notion.so",
    "gamma": "https://logo.clearbit.com/gamma.app",
    "deepseek": "https://cdn.jsdelivr.net/gh/callback-io/allogo@main/public/logos/deepseek/icon.png",
    "notebooklm": "https://upload.wikimedia.org/wikipedia/commons/e/ed/NotebookLM_logo.svg"
}

output_dir = "assets/images/logos"
os.makedirs(output_dir, exist_ok=True)

for name, url in logos.items():
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            ext = url.split('.')[-1]
            if len(ext) > 4 or '/' in ext: # Handle clearbit URLs without extension
                ext = "png"
            filename = f"{name}.{ext}"
            with open(os.path.join(output_dir, filename), "wb") as f:
                f.write(response.content)
            print(f"Downloaded {name}")
        else:
            print(f"Failed to download {name}: Status {response.status_code}")
    except Exception as e:
        print(f"Error downloading {name}: {e}")
