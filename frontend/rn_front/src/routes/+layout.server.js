export async function load({ fetch }) {
    console.log("Executing +layout.server.js load function");

    try {
        const response = await fetch('http://127.0.0.1:8000/api/user', {
            method: 'GET',
            credentials: 'include',
        });

        console.log("API /api/user response status:", response.status);

        const userData = await response.json();

        if (!response.ok) {
            console.log("Failed to fetch user data");
            return { user: null, loggedIn: false };
        }
        if (!userData === null) {
            console.log("User data from routes:", userData.user.email);
        }
        return { user: userData, loggedIn: true };
    } catch (error) {
        console.error("Error during user fetch:", error);
        return { user: null, loggedIn: false };
    }
}