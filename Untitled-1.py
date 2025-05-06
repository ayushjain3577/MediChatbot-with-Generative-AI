# %%
print("Ok")

# %%
%pwd

# %%
import os
os.chdir("../")

# %%
%pwd

# %%
import sys, os, subprocess
print(f"Python: {sys.executable}")
print(f"Env: {os.environ.get('CONDA_DEFAULT_ENV')}")

# Check actual package locations
print("\nPackage Paths:")
subprocess.run(["pip", "show", "langchain", "pypdf"])


