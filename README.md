Telegram Bot System: Lead Generation & Admin Panel

A robust, Dockerized system consisting of two independent Telegram bots sharing a single database. Designed for marketing funnels, lead collection, and real-time administration.
📋 Project Overview

The system architecture is split into two specialized services:

    Main Bot: Client-facing interface. Handles user onboarding, contact collection (leads), and delivers marketing content.

    System Bot: Admin-only tool. Provides instant notifications for new leads and full database access for user management.

🛠 Tech Stack

    Language: Python 3.10+

    Framework: Aiogram 3.x (Asynchronous Telegram Bot API)

    Database: SQLite (managed via SQLAlchemy 2.0 + aiosqlite)

    Infrastructure: Docker & Docker Compose

    Hosting: DigitalOcean Droplet (Ubuntu 24.04 LTS)

📦 System Architecture

    Shared Volume: Both bots are connected to the same data.db file through Docker Volumes, ensuring instant data synchronization.

    High Availability: Services are isolated; an issue in the client bot will not affect the admin panel.

    Persistence: Data is stored on the host machine, preventing data loss during container restarts.

Deployment Guide
1. Environment Configuration

Create a .env file in the root directory and fill in your credentials:
Plaintext

BOT_TOKEN=your_main_bot_token
SYSTEM_BOT_TOKEN=your_admin_bot_token
ADMIN_ID=your_telegram_id

2. Launch with Docker

The entire system can be deployed with a single command:
Bash

docker compose up -d --build

    up -d: Runs containers in the background.

    --build: Rebuilds images to include latest code changes.

3. Verification

Check service status:
Bash

docker compose ps

View real-time logs:
Bash

docker compose logs -f
