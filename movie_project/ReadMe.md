# Movie Fan App

This project is called "Movie Fan App" and is built using the Django web framework. It allows users to browse movies, view movie details.

## Installation
1. Clone this repository to your local machine using git clone https://github.com/vlad101/movie_project_django.git
2. Navigate to the project directory using cd movie_project_django
3. Create a virtual environment using python -m venv env
4. Activate the virtual environment using source env/bin/activate on macOS/Linux or env\Scripts\activate on Windows
5. Install the project dependencies using pip install -r requirements.txt
6. Set the environment variable OMDB_API_KEY to your OMDB API key. You can do this by running export OMDB_API_KEY=<your_api_key> on macOS/Linux or set OMDB_API_KEY=<your_api_key> on Windows. 
7. Replace <your_api_key> with your actual API key.
8. Set the environment variable mysql_pswd to your MySQL database password. You can do this by running export mysql_pswd=<your_password> on macOS/Linux or set mysql_pswd=<your_password> on  
9. Windows. Replace <your_password> with your actual MySQL database password.
10. Run the project using python manage.py runserver
11. Open your web browser and navigate to http://localhost:8000/ to view the project

## Features

### This project includes the following features:

1. User authentication and authorization
2. Movie browsing and searching
3. Movie details, including synopsis, cast, crew, and ratings
4. User reviews and ratings of movies
5. Admin panel for managing movies and user accounts

## Contributing

### If you would like to contribute to this project, please follow these steps:

1. Fork this repository to your own GitHub account
2. Clone the forked repository to your local machine
3. Create a new branch for your changes using git checkout -b feature/my-new-feature
4. Make your changes to the code
5. Test your changes to ensure they work as intended
6. Commit your changes using git commit -am 'Add some feature'
7. Push your changes to your forked repository using git push origin feature/my-new-feature
8. Create a pull request on the original repository to propose your changes

Thank you for your contributions!

Make sure to replace the instructions with the appropriate commands and values for your project. Also, ensure that the directory structure and feature descriptions match the structure and features of your project. Finally, be sure to include any additional information or guidelines that would be helpful for someone who is using or contributing to your project.

Once you have created the README.md file, save it to the root directory of your project (i.e., the same directory where the manage.py file is located) and commit it to your GitHub repository.