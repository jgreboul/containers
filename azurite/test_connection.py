from azure.storage.blob import BlobServiceClient

# Constants
ACCOUNT_NAME = "devstoreaccount1" #Default Azurite account name
ACCOUNT_KEY = "Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==" #Default Azurite key

BLOB_CONN_STR = (
    "DefaultEndpointsProtocol=http;"
    f"AccountName={ACCOUNT_NAME};"
    f"AccountKey={ACCOUNT_KEY};"
    f"BlobEndpoint=http://127.0.0.1:10000/{ACCOUNT_NAME};"
)

print("Connecting to Azurite Docker on 127.0.0.1:10000...")

try:
    blob_service = BlobServiceClient.from_connection_string(BLOB_CONN_STR)
    containers = blob_service.list_containers()
    for container in containers:
        print("🪣 Found container:", container["name"])
    print("✅ Connection to Azurite succeeded.")
except Exception as e:
    print("❌ Connection failed:", e)
