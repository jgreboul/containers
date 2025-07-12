# Containers Repository
Welcome to the **Containers** repository! This is a collection of ready-to-use, self-contained Docker environments, designed to make it easy for developers, researchers, and hobbyists to spin up useful tools with minimal configuration.

---

## Structure

Each container setup is organized in its own **subdirectory**, containing:
- A `docker-compose.yml` or `Dockerfile` file.
- A `README.md` specific to that setup
- Any configuration files or scripts needed

```
containers/
├── ollama-openwebui/
│   ├── docker-compose.yml
│   └── README.md
...
```

---

## Available Containers

| Folder              | Description                                 |
|---------------------|---------------------------------------------|
| `ollama-openwebui`  | Run Ollama + OpenWebUI for offline LLM use  |
| *(more coming soon)*| *(check back often for updates!)*           |

---

## How to Use Any Container

1. Navigate into the desired subdirectory:
   ```bash
   cd containers/ollama-openwebui
   ```

2. Follow the instructions in that folder’s `README.md`.

3. Most setups use:
   ```bash
   docker compose up -d
   ```

4. Access the application (usually via `localhost`).

---

## Prerequisites

Make sure you have:
- [Docker Desktop](https://www.docker.com/products/docker-desktop) installed
- Sufficient resources (RAM, CPU, Disk) for the container in question

---

## Contact Information
For more insights, subscribe to my Youtube Channel: https://www.youtube.com/user/jgreboul 
Thank you, 
Jean-Gael Reboul
jgreboul@gmail.com

---

## License
Unless otherwise noted, all projects in this repository are licensed under the GNU GENERAL PUBLIC LICENSE, Version 3.

---

Happy containerizing! 🐳