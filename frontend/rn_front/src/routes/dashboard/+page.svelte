<script>
    import { Button } from 'flowbite-svelte';
    import  Dashboard from '../../lib/Dashboard.svelte';
	/** @type {{ data: import('./$types').PageData }} */
	let { data } = $props();
    let imageSrc2 = '/images/product_example_2.jpg';
</script>

<div class="flex flex-col items-center justify-center">
    <Dashboard 
        userEmail={data.user.user.email}
        hasActiveSubscription={data.subscriptionInfo[0].active}
        subscriptionType="Basic Package"
        subscriptionImage={imageSrc2}
        nextDeliveryWindow="December 25, 2024, between 2:00 PM and 5:00 PM"
    />

    <!-- Logout form -->
    <form method="POST" action="?/logout">
        <Button type="submit" class="w-full bg-mint-green text-deep-teal rounded-none hover:bg-pastel-coral">Sign out</Button>
    </form>
</div>