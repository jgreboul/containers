# Ollama + OpenWebUI: Local LLM Docker Setup
This project provides a simple Docker Compose configuration to run **Ollama** and **OpenWebUI** locally, enabling you to interact with large language models (LLMs) via a web interface — all offline and CPU-only if needed.

---

## What is Ollama?

**Ollama** is a runtime for large language models (LLMs) on your own machine. It allows you to:
- Download, serve, and run LLMs like `gemma`, `llama2`, `mistral`, etc.
- Operate fully offline.
- Expose an API endpoint (`http://localhost:11434`) for programmatic access.

More info: [https://ollama.com](https://ollama.com)

---

## What is OpenWebUI?

**OpenWebUI** is a sleek, browser-based user interface to interact with local LLMs via Ollama. Features include:
- Chat-style interface like ChatGPT.
- Support for multiple models.
- Runs entirely on your machine.

GitHub: [https://github.com/open-webui/open-webui](https://github.com/open-webui/open-webui)

---

## What does this Docker Compose file do?

This `docker-compose.yml` spins up **two containers**:
1. **Ollama (`ollama_openwebui`)**:
   - Starts the Ollama server.
   - Automatically pulls the `gemma3:1b` model at launch.

2. **OpenWebUI (`open-webui`)**:
   - Launches a web UI on `http://localhost:3000`.
   - Connects to the Ollama backend via `OLLAMA_BASE_URL`.

### Key Configuration:
- **Volumes** persist Ollama model files and UI data.
- **Environment Variables**:
  - `OPENAI_API_KEY=ollama`: Needed by OpenWebUI.
  - `OLLAMA_BASE_URL=http://ollama_openwebui:11434`: Tells OpenWebUI how to connect to Ollama.

---

## Prerequisites

Before you begin, install:

1. **Docker Desktop** (https://www.docker.com/products/docker-desktop/)
2. At least **8 GB of RAM** (16 GB recommended for smooth LLM performance)
3. Optional: **GPU support** if you want better performance (Ollama also supports CPU-only mode)

---

## How to Use on Your Personal Laptop

1. **Download this repository or `docker-compose.yml` file.**

2. **Open a terminal in the folder containing `docker-compose.yml`.**

3. **Run the following command to start the services:**

```bash
docker compose up -d
```

4. **Wait for a few minutes.** Ollama will pull the `gemma3:1b` model (hundreds of MBs).

5. **Visit your local OpenWebUI in a browser:**

```
http://localhost:3000
```

After creating your admin local user, you're ready to interact with a local LLM!

---

## Volumes Used

| Volume Name         | Purpose                         |
|---------------------|----------------------------------|
| `ollama_openwebui`  | Stores Ollama model/cache files |
| `open-webui`        | Stores OpenWebUI settings/data  |

---

## To Stop and Clean Up

```bash
docker compose down
```

To remove downloaded model data as well:

```bash
docker volume rm ollama_openwebui open-webui
```

---

## Troubleshooting

- **Model not downloading?** Ensure your internet is working the first time (after that, it's fully offline).
- **No response in WebUI?** Wait a bit longer after first startup – model loading can take time.
