document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("authorize").addEventListener("click", () => {
        const meetingUrl = "https://us05web.zoom.us/j/84890093856?pwd=5FbAT2g2UPWgWyFhxbYbtdZ3Og0PCk.1";
        const redirectUri = "https://72b8-141-215-217-246.ngrok-free.app/oauth2callback";
    
        // Open the Zoom OAuth authorization URL
        chrome.identity.launchWebAuthFlow(
            {
                url: `https://zoom.us/oauth/authorize?response_type=code&client_id=L1CXvdysQgqdn2xBJfwH6w&redirect_uri=${encodeURIComponent(redirectUri)}`,
                interactive: true
            },
            (redirect_url) => {
                if (chrome.runtime.lastError || !redirect_url) {
                    document.getElementById("status").innerText = "Authorization failed";
                    return;
                }
    
                // Successfully authorized
                document.getElementById("status").innerText = "Authorization successful!";
                console.log("Redirect URL: ", redirect_url);
                
                // Extract access token from the redirect_url
                const urlParams = new URLSearchParams(new URL(redirect_url).hash.substring(1));
                const accessToken = urlParams.get('access_token');
                
                if (accessToken) {
                    console.log("Access Token: ", accessToken);
                } else {
                    console.log("Failed to get token, redirect URL:", redirect_url);
                    document.getElementsById
                }
    
                // Redirect to the Zoom meeting
                window.open(meetingUrl, "_blank");
            }
        );
    });
});