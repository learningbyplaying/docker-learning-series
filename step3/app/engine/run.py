print('Creating data on project')

import os

path="/projects/aws/data"
cmd = f"mkdir -p {path}"
output = os.popen(cmd).read()
print(output)
