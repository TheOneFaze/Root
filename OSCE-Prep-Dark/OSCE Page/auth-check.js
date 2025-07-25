// This script checks authentication status and redirects if necessary.
// It uses sessionStorage, which clears when the browser tab/PWA is closed.

document.addEventListener('DOMContentLoaded', () => { // <--- ADD THIS LINE
    // Define the path to your login page.
    // This path is relative to the root of your GitHub Pages site.
    const loginPagePath = '/OSCE-Prep-Dark/OSCE Page/login.html'; // Changed %20 to spaces for clarity

    // Check if the user is NOT authenticated for the current session.
    // If 'isAuthenticated' is not 'true' in sessionStorage, redirect.
    if (sessionStorage.getItem('isAuthenticated') !== 'true') {
        // Only redirect if we are not already on the login page to prevent a loop
        // Also compare against window.location.pathname without decoding for consistency
        const currentPath = window.location.pathname;
        if (currentPath !== loginPagePath && currentPath !== '/OSCE-Prep-Dark/OSCE%20Page/login.html') { // Check both encoded and decoded
            window.location.replace(loginPagePath); // Use replace to prevent back button going to protected page
        }
    }
}); // <--- ADD THIS LINE

// Optional: Add a logout function that can be called from any page
window.logout = function() {
    sessionStorage.removeItem('isAuthenticated');
    // Redirect to the login page after logout
    window.location.replace('/OSCE-Prep-Dark/OSCE Page/login.html'); // Changed %20 to spaces for clarity
};
