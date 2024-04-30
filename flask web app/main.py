import os
import sys

project_path= r'C:\Users\Sreeja\PycharmProjects\flask web app'
sys.path.append(os.path.abspath(project_path))

from website import create_app
app = create_app()
if __name__ == '__main__':
    app.run(debug=True)
