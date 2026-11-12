from .core import init_db
from .models import User, AuditLog, ConfigItem

if __name__ == "__main__":
    print("Initializing SQLite database...")
    init_db()
    print("Database 'shadow_core.db' initialized successfully.")
