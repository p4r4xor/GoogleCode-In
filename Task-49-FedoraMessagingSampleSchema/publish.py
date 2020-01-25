from fedora_messaging.api import publish
from fedora_messaging.config import conf
from mailman_schema.schema import MessageV3 as Message

conf.setup_logging()
message= Message(
    topic="tutorial.topic",
    body={
        "owner": "paraxor",
        "package": {
            "name": "Sample message schema for GCI Fedora Project",
        }
    }
)
publish(message)