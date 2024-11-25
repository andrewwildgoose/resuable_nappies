import { redirect } from '@sveltejs/kit';
/** @type {import('./$types').Actions} */

export const actions = {
    logout: async (event) => {
        // Make the POST request to the backend API for logout
        const response = await fetch('http://127.0.0.1:8000/api/logout', {
            method: 'POST',
            credentials: 'include', // Ensures cookies are sent with the request
        });

        // Clear user session cookies on the client side
        event.cookies.delete('user_id', { path: '/' });

        // Redirect to the login page
        throw redirect(302, '/login');
    }
};