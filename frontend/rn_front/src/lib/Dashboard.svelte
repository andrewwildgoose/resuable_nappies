<script>
    import { Button } from 'flowbite-svelte';
    import CustCardandImg from './CustCardandImg.svelte';
    export let userEmail = "user@example.com"; // Replace with dynamic data
    export let hasActiveSubscription = false; // Boolean for subscription status
    export let subscriptionType = "N/A"; // Replace with dynamic subscription type
    export let subscriptionImage = "/images/product_example_2.jpg"; // Replace with dynamic image path
    export let nextDeliveryWindow = "N/A"; // Replace with dynamic delivery data
</script>

<div class="max-w-4xl mx-auto mt-8 p-6 bg-light-beige">
    <!-- Welcome Section -->
    <h1 class="p-6 text-2xl font-bold text-deep-teal">
        Welcome to your dashboard, <span class="text-pastel-coral">{userEmail}</span>.
    </h1>

    <!-- Subscription Status -->
    <div class="p-6 mt-4 flex items-center">
        <div
        class={`h-3 w-3 ${
            hasActiveSubscription ? "bg-mint-green" : "bg-pastel-coral"
        }`}
        ></div>
        <p class="ml-2 text-deep-teal">
            {hasActiveSubscription
            ? "You have an active subscription."
            : "You do not have an active subscription."}
        </p>



    </div>
    <div class="p-6">
        <CustCardandImg 
        imgSrc={subscriptionImage}
        title={subscriptionType}
        description="Your subscription inlcudes some nappies, collection, delivery & cleaning"
        buttonText="Manage Subscription"
        />
    </div>
    <!-- Next Delivery/Collection -->
    <div class="p-6">
        <h2 class="text-xl font-semibold text-deep-teal">Next Delivery/Collection</h2>
        <p class="mt-2 text-mint-green">
            {nextDeliveryWindow !== "N/A"
            ? `Your next delivery/collection is scheduled for ${nextDeliveryWindow}.`
            : "No delivery or collection scheduled at this time."}
        </p>
    </div>
</div>