
```markdown
# Telegram Consultation & Content Funnel Bot

A professional Telegram bot built with **aiogram 3.x**, designed for a freelancer/entrepreneur to automate client onboarding and content delivery.

## 🚀 Project Overview
This bot was created for a friend who is launching their consulting services. It serves as an automated funnel that:
1. Greets potential clients and introduces the expert's philosophy.
2. Collects contact information (Phone & Name) using Telegram's native contact request.
3. Delivers a sequential video-based educational flow using **FSM (Finite State Machine)**.
4. Provides direct links for consultations and community access.

## 🛠 Tech Stack
* **Python 3.10+**
* **aiogram 3.x** (Asynchronous Telegram Framework)
* **Pydantic / python-dotenv** (Configuration management)
* **Aiohttp** (Networking)

## 📂 Project Structure
```text
bot/
├─ app/
│  ├─ handlers/    # Business logic (Start, Form, Video flow)
│  ├─ keyboards/   # Reply and Inline keyboards
│  ├─ main.py      # Entry point
│  └─ ...
└─ .env            # Environment variables (Token, Video IDs)

```

## 🚧 Current Status

The project is currently **under active development**.

* [x] Core bot logic & Handlers
* [x] FSM-based video flow
* [x] Keyboard & Media management
* [ ] Dockerization (In progress)
* [ ] Database integration & VPS Deployment (In progress)

## 🔧 Installation (Development)

1. Clone the repository:
```bash
git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)

```


2. Set up a virtual environment and install dependencies.
3. Create a `.env` file based on `.env.example`.
4. Run the bot: `python -m app.main`

```

