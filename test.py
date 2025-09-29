print("=== PRUEBA DESDE LA CARPETA CORRECTA ===")

try:
    import pandas as pd
    print("✅ pandas OK")
except ImportError as e:
    print(f"❌ pandas Error: {e}")

try:
    import plotly.express as px
    print("✅ plotly.express OK")
except ImportError as e:
    print(f"❌ plotly.express Error: {e}")

print("=== FIN DE PRUEBA ===")