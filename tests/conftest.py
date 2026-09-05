import sys
import pathlib
# Esto hace que 'core' sea importable aunque el CI no tenga PYTHONPATH=.
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.resolve()))
