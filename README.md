# Password Generator

This is a simple password generator application built with Python and Flask. The application generates a password using a formula: word + random symbol '$','&','#','@','!','*' + random number between 1-999. The word is fetched from https://random-word-api.herokuapp.com/word?number=10. Each time the user submits a request, the application generates ten passwords.

## Project Structure

```
password-generator
├── app.py
├── templates
│   └── index.html
├── static
│   └── styles.css
├── requirements.txt
└── README.md
```

## Files

- `app.py`: This is the main file that runs the application. It imports Flask and other necessary modules. It contains the route for the home page which renders the index.html template and a route for generating the passwords. It also contains the logic for generating the passwords using the specified formula.

- `templates/index.html`: This is the HTML template for the home page. It contains a form with a button for generating the passwords. When the button is clicked, it sends a request to the server to generate the passwords.

- `static/styles.css`: This is the CSS file for styling the index.html template. It defines the styles for the form and the generated passwords.

- `requirements.txt`: This file lists all the Python packages that the application depends on. It includes Flask and any other packages used in the app.py file.

## How to Run

1. Install the required packages by running `pip install -r requirements.txt`
2. Run the application by executing `python app.py`
3. Open your web browser and navigate to `http://localhost:5000` to see the application in action.

## How to Use

1. Click the "Generate" button to generate ten passwords.
2. The generated passwords will be displayed on the page.
3. Click the "Generate" button again to generate a new set of passwords.