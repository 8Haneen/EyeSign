chrome.runtime.onInstalled.addListener(() => {
    console.log("Extension installed");
});

// OAuth2 flow setup
chrome.identity.onSignInChanged.addListener((account, signedIn) => {
    if (signedIn) {
        // Handle sign-in
        console.log("User signed in");
    }
});

// Other background tasks can be added here