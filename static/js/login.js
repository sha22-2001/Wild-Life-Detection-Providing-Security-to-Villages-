function validateLogin() {
            // Get the username and password input values
            var username = document.getElementById("username").value;
            var password = document.getElementById("password").value;

            // Check if the username and password are correct
            if (username === "srm" && password === "srm") {
                // Redirect to the main page
                window.location.href = '/home';
            } else {
                // Display an error message or perform other actions for an invalid login
                alert("Invalid username or password. Please try again.");
            }
        }