# Create the virtual environment
python3 -m venv myenv

# Activate it (on Unix/macOS)
source myenv/bin/activate

# Activate it (on Windows)
myenv\Scripts\activate

# Install packages
pip install package_name

# Deactivate when done
deactivat



# Generate requirements.txt from currently installed packages
pip freeze > requirements.txt

# Install packages from requirements.txt
pip install -r requirements.txte
