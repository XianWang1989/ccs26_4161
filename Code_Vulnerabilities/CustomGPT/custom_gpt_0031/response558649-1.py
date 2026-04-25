
# Create and activate a virtual environment
# In terminal (not in Python):

python3 -m venv myenv
source myenv/bin/activate  # On Windows use: myenv\Scripts\activate

# Now install requests with security features
pip install requests[security]
