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
                console.log('Login successful');

                const userResponse = await fetch('http://127.0.0.1:8000/api/user', {
                    method: 'GET',
                    credentials: 'include',
                });

                const userData = await userResponse.json();

                if (userResponse.ok) {
                    // Store user session data in cookies or server-side session
                    event.cookies.set('user_id', userData.id, {
                        httpOnly: true,
                        secure: true,
                        path: '/',
                        sameSite: 'lax'
                    });
                    console.log('User: ', userData)

                    return { success: true };
                } else {
                    console.error('Failed to fetch user data:', userData.detail);
                    return { error: true, message: 'Failed to retrieve user session.' };
                }
            } else {
                console.error('Login failed:', result.detail);
                return { error: true, message: result.detail };
            }
        } catch (error) {
            console.error('Error during signin:', error);
            return { error: true, message: 'An error occurred during login.' };
        }
    }
};