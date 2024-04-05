<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Login Page</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <form action="process_login.php" method="post">  <h1>Login</h1>
    <label for="username">Username:</label>
    <input type="text" name="username" id="username" required><br><br>
    <label for="password">Password:</label>
    <input type="password" name="password" id="password" required><br><br>
    <button type="submit">Login</button>
  </form>
  <?php
    // Display error message if authentication failed
    if (isset($error)) {
        echo "<p style='color:red;'>$error</p>";
    }
    ?>
</body>
</html>
<?php 

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Retrieve username and password from the form
    $username = $_POST['username'];
    $password = $_POST['password'];

    //this is the hard-coded user
    $valid_username = 'admin';
    $valid_password = 'admin';

    // Check if the provided credentials are valid
    if ($username === $valid_username && $password === $valid_password) {
        // Authentication successful, set session variables
        $_SESSION['username'] = $username;

        // Redirect to the dashboard or another page after successful login
        header("Location: dashboard.php");
        exit;
    } else {
        // If credentials are invalid, show an error message
        $error = "Invalid username or password";
    }
}
?>
