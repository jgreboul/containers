# Local Azure Function Development with Azurite (Docker-Based)

This guide walks through setting up a local Azure Functions environment using Python 3.11 and Azurite running in Docker.

---

## What is Azurite?

**Azurite** is the official Azure Storage emulator provided by Microsoft. It lets developers run a local simulation of Azure Storage services, including:
- **Blob Storage**
- **Queue Storage**
- **Table Storage**

### Why Use Azurite?

Azurite is perfect for local development and testing without the need for an actual Azure subscription. It provides:

- Offline development and testing
- Faster iteration and debugging
- Seamless integration with Azure Functions
- Support for CI/CD pipelines

### How It Works with Azure Functions

When using Azure Functions locally, you can point your storage bindings to Azurite instead of real Azure endpoints. This allows you to:

- Test blob triggers and outputs
- Work with queue messages
- Use local table storage for function state

Your `local.settings.json` already includes a connection string configured for Azurite. Azure Functions tooling recognizes this and automatically connects to the local emulator.

---

 
It ensures developers can test blob and queue storage interactions without relying on real Azure services.

---

## Virtual Environment Using Python 3.11
> As of June 2025, Azure Functions supports Python up to 3.11.

### Steps:
1. **Install Python 3.11** from [python.org](https://www.python.org/downloads/release)
2. **Create a virtual environment** (adjust path as needed):
   ```bash
   C:\Python311\python.exe -m venv .venv
   ```
3. **Activate**:
   - PowerShell:
     ```bash
     .\.venv\Scripts\Activate.ps1
     ```
   - CMD:
     ```cmd
     .venv\Scripts\activate.bat
     ```

---

## Azurite with Docker

### Steps:
1. Navigate to `azurite/`
2. Start container:
   ```bash
   docker-compose up -d
   ```
3. Azurite will run at:
   - Blob: `http://127.0.0.1:10000`
   - Queue: `http://127.0.0.1:10001`
   - Table: `http://127.0.0.1:10002`

---

## Verify Azurite Connection
```bash
python azurite/test_connection.py
```

Expected:
```
✅ Connection to Azurite succeeded.
```

---

## Setup Blob + Queue + Table Resources (sample)

`setup_azurite_resources.py` provides you with a simple way to configure your resources within your Azurite environment. 

More specifically, the provided sample script will create
- Container: `demo`
- Folders: `folder1/`, `folder2/`, `folder3/`, `folder4/`, `folder5/`
- Queues: `input-queue`, `processing-queue`, and host-queue to avoid 404s
- Tables: `azurewebjobshosts`

### Steps:
1. Install packages:
   ```bash
   pip install azure-core azure-storage-blob azure-storage-queue
   ```
2. Run:
   ```bash
   python azurite/setup_azurite_resources.py
   ```
---

## `local.settings.json` for Azure Functions

```json
{
  "IsEncrypted": false,
  "Values": {
    "AzureWebJobsStorage": "DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;BlobEndpoint=http://127.0.0.1:10000/devstoreaccount1;QueueEndpoint=http://127.0.0.1:10001/devstoreaccount1;",
    "STORAGE_CONNECTION_STRING": "DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;BlobEndpoint=http://127.0.0.1:10000/devstoreaccount1;QueueEndpoint=http://127.0.0.1:10001/devstoreaccount1;",
    "FUNCTIONS_EXTENSION_VERSION": "~4",
    "FUNCTIONS_WORKER_RUNTIME": "python",
    "PYTHON_VERSION": "3.11"
  },
  "Host": {
    "CORS": "*"
  }
}
```

---

## Done
Your local Azure development environment is now fully functional with Azurite and ready for development. 

---

## Optional (but recommended): Azure Storage Explorer
For a graphical interface to view and manage your Azurite storage emulator, consider installing **Azure Storage Explorer**:

- **Download**: [https://azure.microsoft.com/en-us/products/storage/storage-explorer](https://azure.microsoft.com/en-us/products/storage/storage-explorer)
- **Steps**:
  1. Install the tool for your platform (Windows/macOS/Linux).
  2. Launch the app and connect to Azurite using the following configuration:
     - **Storage Account Name**: `devstoreaccount1` (Default Account Name)
     - **Account Key**: `Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==` (Default Account Key)
     - **Blob service**: `http://127.0.0.1:10000/devstoreaccount1`
     - **Queue service**: `http://127.0.0.1:10001/devstoreaccount1`
     - **Table service**: `http://127.0.0.1:10002/devstoreaccount1`

This makes it easier to verify containers, folders, and messages in your development setup.
