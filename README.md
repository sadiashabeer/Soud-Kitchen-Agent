# 🍳 Soud — Multimodal Kitchen Agent

Soud is a multimodal AI kitchen assistant that understands
text, voice instructions, and fridge images to create
personalized recipes.

The agent can identify ingredients from a fridge image,
understand an audio cooking request, search the web for
relevant recipe information, verify the retrieved content,
and generate a final recipe.

---

## ✨ Features

- 🎤 Audio-based cooking instructions
- 📷 Fridge image understanding
- 🥕 Ingredient identification
- 🔎 Web recipe search
- 🛡️ Prompt injection protection
- 👨‍🍳 Personalized recipe generation
- 🤖 Multimodal Gemini model
- 🔗 Chained agent architecture
- 🧠 Few-shot prompting
- 📝 Prompt templating

---

## 🏗️ Architecture

```text
                 User
                  |
          -------------------
          |                 |
       🎤 Audio          📷 Image
          |                 |
          v                 v
    Request Agent      Vision Agent
          |                 |
          -----------+------
                     |
                     v
             🧠 Task Understanding
                     |
                     v
                🔎 Search Agent
                     |
                     v
              🛡️ Verifier Agent
                     |
                     v
               👨‍🍳 Recipe Agent
                     |
                     v
               🍳 Final Recipe