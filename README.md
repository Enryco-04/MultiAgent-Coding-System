# LLM Java Evaluator

This README covers only the requirements and setup needed to run the project.

## Requirements

- Python 3.11 or newer
- Docker Desktop, or Docker Engine with Docker Compose support
- An Ollama installation if you want to use the local model configured in `main.py`
-

## Project Files You Will Use During Setup

- `requirements.txt`
- `docker-compose.yml`
- `Dockerfile`
- `.env` or `.env.example`
- `main.py`

## 1. Clone the Project

```bash
git clone <repo-url>
cd <repo-folder>
```

## 2. Create and Activate a Python Virtual Environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

macOS / Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

## 4. Configure Environment Variables

If `.env.example` exists, copy it to `.env` first.

Windows:

```bash
copy .env.example .env
```

macOS / Linux:

```bash
cp .env.example .env
```

Edit `.env` and set the values you need.

Typical variables:

```env
OPENAI_API_KEY=your_openai_key_here
SONAR_TOKEN=your_sonar_token_here
SONAR_PROJECT_KEY=llm-eval
SONAR_HOST_URL=http://localhost:9000
```

Notes:

- `SONAR_HOST_URL` defaults to `http://localhost:9000` if not set.
- `SONAR_TOKEN` and `SONAR_PROJECT_KEY` are required only if you want SonarQube analysis enabled.
- Your current `main.py` is configured to use `OllamaClient`, so `OPENAI_API_KEY` is not required unless you switch back to `CodexClient`.

## 5. Start Docker Services

Build and start the containers:

```bash
docker compose up -d --build
```

This starts:

- `java_tester`
- `sonarqube`

To check that the containers are running:

```bash
docker compose ps
```

## 6. Set Up SonarQube and Generate a Token

Open SonarQube in your browser:

`http://localhost:9000`

First-time login:

- Username: `admin`
- Password: `admin`

After logging in:

1. Change the default password if prompted.
2. Open your profile/avatar.
3. Go to `My Account`.
4. Open the `Security` tab.
5. Generate a token.
6. Copy the token into `.env` as `SONAR_TOKEN=...`

Also make sure `.env` contains a project key, for example:

```env
SONAR_PROJECT_KEY=llm-eval
```

## 7. Make Sure Ollama Is Running

Your current code uses:

```python
OllamaClient(model="qwen2.5-coder:7b-instruct")
```

So you should have Ollama running locally and the selected model available.

Example checks:

```bash
ollama list
ollama serve
```

If the model is missing, pull it:

```bash
ollama pull qwen2.5-coder:7b-instruct
```

## 8. Run the Project

Run all problems:

```bash
python main.py
```

Run a single problem by id:

```bash
python main.py infinite_sequence
```

## 9. Useful Docker Commands

Stop services:

```bash
docker compose down
```

Stop services and remove volumes:

```bash
docker compose down -v
```

Rebuild after Docker-related changes:

```bash
docker compose up -d --build
```

## 10. Common Setup Issues

- If `docker compose up` fails, make sure Docker Desktop is running.
- If SonarQube does not open on `http://localhost:9000`, wait a little longer and check `docker compose ps`.
- If Python cannot import dependencies, verify the virtual environment is activated before `pip install -r requirements.txt`.
- If Ollama requests fail, make sure the Ollama service is running and the configured model is installed.
- If Sonar analysis is skipped, check that `SONAR_TOKEN` and `SONAR_PROJECT_KEY` are both set in `.env`.
