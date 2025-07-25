// This script runs at the very start to check authentication status.
// It uses sessionStorage, which clears when the browser tab/PWA is closed.

(function() {
    // Define the path to your login page.
    // This path is relative to the root of your GitHub Pages site.
    const loginPagePath = '/OSCE-Prep-Dark/OSCE%20Page/login.html';

    // Check if the user is NOT authenticated for the current session.
    // If 'isAuthenticated' is not 'true' in sessionStorage, redirect.
    if (sessionStorage.getItem('isAuthenticated') !== 'true') {
        // Only redirect if we are not already on the login page to prevent a loop
        if (window.location.pathname !== loginPagePath && window.location.pathname !== decodeURIComponent(loginPagePath)) {
            window.location.replace(loginPagePath); // Use replace to prevent back button going to protected page
        }
    }
})();

// Optional: Add a logout function that can be called from any page
window.logout = function() {
    sessionStorage.removeItem('isAuthenticated');
    // Redirect to the login page after logout
    window.location.replace('/OSCE-Prep-Dark/OSCE%20Page/login.html');
};
