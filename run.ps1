# PowerShell script for Windows

Write-Host "Creating virtual environment..."
python -m venv .venv

Write-Host "Activating virtual environment..."
# For PowerShell
. .venv\Scripts\Activate.ps1

Write-Host "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

Write-Host "Launching Streamlit UI..."
streamlit run app/main.py
