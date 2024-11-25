<script>
    import { Button } from 'flowbite-svelte';
    import { goto } from '$app/navigation';

    function navigateTo(route) {
        goto(route);
    }
</script>

<p>Successfully registered! Please check your email to verify your account.</p>
<Button on:click={navigateTo('/')} size="sm" class="w-full bg-mint-green text-deep-teal rounded-none hover:bg-pastel-coral">Return to homepage</Button>
