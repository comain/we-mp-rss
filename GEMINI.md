# Project Context: WeRSS (we-mp-rss)

## Overview
**WeRSS** (also known as `we-mp-rss`) is a tool designed to subscribe to and manage WeChat Official Account content. It crawls articles, generates RSS feeds, and provides a web interface for management.

## Tech Stack
*   **Backend:** Python 3.13+
    *   **Framework:** FastAPI
    *   **Server:** Uvicorn
    *   **Database ORM:** SQLAlchemy
    *   **Browser Automation:** Playwright (with `playwright-stealth`)
    *   **Task Scheduling:** APScheduler / Schedule
*   **Frontend:** Vue 3, TypeScript
    *   **Build Tool:** Vite
    *   **UI Libraries:** Arco Design Vue, Ant Design Vue
*   **Database:** SQLite (default), supports MySQL/PostgreSQL via SQLAlchemy.
*   **Containerization:** Docker

## Key Directories & Files

### Root
*   `main.py`: Entry point. Starts the Uvicorn server and background jobs.
*   `web.py`: Definition of the FastAPI application (`app`).
*   `config.yaml` (from `config.example.yaml`): Main configuration file.
*   `requirements.txt`: Python dependencies.
*   `Dockerfile`: Docker build definition.
*   `docker-compose.yaml` (in `compose/`): Docker Compose configurations.

### Source Code Structure
*   `apis/`: API route definitions.
*   `core/`: Core logic and utilities.
    *   `config.py`: Configuration management.
    *   `db.py` / `database.py`: Database connection and session management.
*   `driver/`: Browser automation logic (Playwright).
    *   `playwright_driver.py`: Main driver implementation.
*   `jobs/`: Scheduled tasks (e.g., fetching articles, updating feeds).
*   `models/` (in `core/`): Database models.
*   `web_ui/`: Frontend source code.
    *   `src/`: Vue components and logic.
    *   `vite.config.ts`: Vite configuration.
    *   `package.json`: Frontend dependencies and scripts.

## Development & Usage

### Running Locally (Manual)

**Backend:**
1.  Ensure Python 3.13+ is installed.
2.  Install dependencies: `pip install -r requirements.txt`
3.  Configure: `cp config.example.yaml config.yaml`
4.  Run: `python main.py` (Use flags like `-job True -init True` as needed).

**Frontend:**
1.  Navigate to `web_ui/`.
2.  Install dependencies: `yarn install`
3.  Run dev server: `yarn dev` (Access at `http://localhost:3000`).

### Running via Docker
*   **Run:** `docker run -d --name we-mp-rss -p 8001:8001 -v ./data:/app/data ghcr.io/rachelos/we-mp-rss:latest`
*   **Compose:** Use `docker-compose up -d` with files in `compose/`.

## Conventions
*   **Configuration:** All configurable parameters are managed in `config.yaml` and loaded via `core.config`.
*   **Separation of Concerns:** Frontend (`web_ui`) is decoupled from the backend API (`apis`).
*   **Data Persistence:** Data is stored in `data/` directory (mapped in Docker), including the database (`db.db`) and cache.
