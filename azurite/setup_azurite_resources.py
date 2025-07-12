from azure.storage.blob import BlobServiceClient
from azure.storage.queue import QueueServiceClient
from azure.data.tables import TableServiceClient
from azure.core.exceptions import ResourceExistsError

# Connection info (must match Docker Azurite config)
ACCOUNT_NAME = "devstoreaccount1" #Default Azurite account name
ACCOUNT_KEY = "Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==" #Default Azurite key

BLOB_CONN_STR = (
    "DefaultEndpointsProtocol=http;"
    f"AccountName={ACCOUNT_NAME};"
    f"AccountKey={ACCOUNT_KEY};"
    f"BlobEndpoint=http://127.0.0.1:10000/{ACCOUNT_NAME};"
)

QUEUE_CONN_STR = (
    "DefaultEndpointsProtocol=http;"
    f"AccountName={ACCOUNT_NAME};"
    f"AccountKey={ACCOUNT_KEY};"
    f"QueueEndpoint=http://127.0.0.1:10001/{ACCOUNT_NAME};"
)

TABLE_CONN_STR = (
    "DefaultEndpointsProtocol=http;"
    f"AccountName={ACCOUNT_NAME};"
    f"AccountKey={ACCOUNT_KEY};"
    f"TableEndpoint=http://127.0.0.1:10002/{ACCOUNT_NAME};"
)


# Resources to create
CONTAINER_NAME = "demo"
FOLDERS = ["folder1/", "folder2/", "folder3/", "folder4/", "folder5/"]

QUEUES = [
    "input-queue",
    "processing-queue",
]

TABLES = [
    "azurewebjobshosts"  # Required for Azure Functions runtime in Azurite
]

print("🔹 Connecting to Azurite Blob service...")

try:
    blob_service = BlobServiceClient.from_connection_string(BLOB_CONN_STR)
    container_client = blob_service.get_container_client(CONTAINER_NAME)

    try:
        container_client.create_container()
        print(f"✅ Created blob container: {CONTAINER_NAME}")
    except ResourceExistsError:
        print(f"ℹ️  Blob container '{CONTAINER_NAME}' already exists.")

    for folder in FOLDERS:
        blob_client = container_client.get_blob_client(folder)
        try:
            blob_client.upload_blob(b"", overwrite=True)
            print(f"📁 Created folder placeholder: {folder}")
        except Exception as e:
            print(f"❌ Failed to create folder '{folder}': {e}")

except Exception as e:
    print("❌ Blob setup failed:", e)


print("\n🔹 Connecting to Azurite Queue service...")

try:
    queue_service = QueueServiceClient.from_connection_string(QUEUE_CONN_STR)
    for queue_name in QUEUES:
        try:
            queue_client = queue_service.get_queue_client(queue_name)
            queue_client.create_queue()
            print(f"📬 Created queue: {queue_name}")
        except ResourceExistsError:
            print(f"ℹ️  Queue '{queue_name}' already exists.")
        except Exception as e:
            print(f"❌ Failed to create queue '{queue_name}': {e}")
except Exception as e:
    print("❌ Queue setup failed:", e)

# Create Tables
print("\n🔹 Connecting to Azurite Table service...")
try:
    table_service = TableServiceClient.from_connection_string(TABLE_CONN_STR)
    for table_name in TABLES:
        try:
            table_service.create_table_if_not_exists(table_name)
            print(f"📊 Created table: {table_name}")
        except ResourceExistsError:
            print(f"ℹ️  Table '{table_name}' already exists.")
        except Exception as e:
            print(f"❌ Failed to create table '{table_name}': {e}")
except Exception as e:
    print("❌ Table setup failed:", e)

print("\n🎉 Azurite setup complete.")
