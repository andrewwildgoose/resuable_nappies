import { redirect } from '@sveltejs/kit';

/** @type {import('./$types').PageLoad} */
/** @type {import('./$types').Actions} */

export async function load({ parent, fetch, cookies }) {
	// Get user data from the parent layout
	const { user } = await parent();

	// Fetch user subscription info
	try {
		const response = await fetch('http://127.0.0.1:8000/api/user_sub_info', {
			method: 'GET',
			credentials: 'include', // Ensures cookies are sent with the request
			headers: {
				'Content-Type': 'application/json',
				'Authorization': `Bearer ${cookies.get('access_token') || ''}`, // Optional: if you use tokens
			}
		});

		const subInfo = await response.json();

		if (!response.ok) {
			console.error('Failed to fetch subscription info:', subInfo);
			return { user, subscriptionInfo: null, error: 'Failed to fetch subscription data' };
		}

		// Return both user and subscription data to the page
        console.log('subscriptionInfo:', subInfo);
        console.log('subscriptionInfo.data:', subInfo.data);
		return {
			user,
			subscriptionInfo: subInfo.data,
		};
	} catch (error) {
		console.error('Error during fetching subscription info:', error);
		return { user, subscriptionInfo: null, error: 'An error occurred while fetching subscription info' };
	}
}

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
