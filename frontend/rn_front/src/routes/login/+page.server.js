/** @satisfies {import('./$types').Actions} */
export const actions = {
    default: async (event) => {
        const formData = await event.request.formData();
        const email = formData.get('email');
        const password = formData.get('password');

        const body = new URLSearchParams();
        body.append('email', email);
        body.append('password', password);

        try {
            const response = await fetch('http://127.0.0.1:8000/api/signin', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: body,
                credentials: 'include',  // To handle cookies
            });

            const result = await response.json();

            if (response.ok) {
                console.log('Login successful:', result.message);
                // Redirect using SvelteKit's helper
                return { success: true };
            } else {
                console.error('Login failed:', result.detail);
                // Return an error message as part of the action response
                return { error: true, message: result.detail };
            }
        } catch (error) {
            console.error('Error during signin:', error);
            return { error: true, message: 'An error occurred during login.' };
        }
    }
}
