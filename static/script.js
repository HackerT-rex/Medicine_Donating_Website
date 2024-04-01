document.getElementById('login-form').addEventListener('submit', function(event) {
    event.preventDefault();
    // Redirect to home page
    window.location.href = 'website.html';
});

function loginWithGoogle() {
  // Simulate Google login
  console.log("Login with Google");
  // Redirect to home.html after login
  window.location.href = "website.html";
}

function loginWithMicrosoft() {
  // Simulate Microsoft login
  console.log("Login with Microsoft");
  // Redirect to home.html after login
  window.location.href = "website.html";
}

