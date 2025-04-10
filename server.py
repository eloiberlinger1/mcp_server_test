from mcp.server.fastmcp import FastMCP
import time
import signal
import sys
import logging

# Configuration du logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Gestionnaire de signal pour arrêter le serveur proprement
def signal_handler(sig, frame):
    print("\nArrêt du serveur MCP...")
    sys.exit(0)

# Configuration du gestionnaire de signal
signal.signal(signal.SIGINT, signal_handler)

# Création du serveur MCP
mcp = FastMCP(
    name="count_r",
    host="127.0.0.1",
    port=5000,
    debug=True,
    log_level="DEBUG"
)

# Définition de notre outil
@mcp.tool()
def count(word: str) -> int:
    """Compte le nombre de lettres 'r' dans un mot donné."""
    try:
        if not isinstance(word, str):
            return 0
        return word.lower().count('r')
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    print(f"Démarrage du serveur MCP count_r sur 127.0.0.1:5000")
    try:
        print("Tentative de démarrage du serveur...")
        mcp.run(transport="sse")
    except Exception as e:
        print(f"Erreur lors du démarrage du serveur: {e}")
        import traceback
        traceback.print_exc()

