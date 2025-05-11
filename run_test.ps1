# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Set PYTHONPATH
$env:PYTHONPATH = "F:\Coding Projects\STAR_Orig\STAR\venv\lib\site-packages"

# Run the test
python test_star_inference.py 