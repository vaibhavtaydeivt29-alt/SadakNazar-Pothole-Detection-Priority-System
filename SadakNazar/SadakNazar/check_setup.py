# Chalao:  python check_setup.py
import sys
print("Python:", sys.version.split()[0], "|", sys.executable)
for name in ["tensorflow", "keras", "numpy", "pandas", "matplotlib", "PIL", "scipy"]:
    try:
        m = __import__(name)
        print("OK     ", name, getattr(m, "__version__", ""))
    except Exception as e:
        print("MISSING", name, "->", type(e).__name__, e)
