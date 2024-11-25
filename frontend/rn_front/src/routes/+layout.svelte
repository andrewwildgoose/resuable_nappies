<script>
    import { Button } from 'flowbite-svelte';
    import { goto } from '$app/navigation';
    import UserNavBar from '../lib/UserNavBar.svelte';
    import PublicNavBar from '../lib/PublicNavBar.svelte';
    import "../app.css";
    // data for user
    export let data;

    function navigateTo(route) {
        goto(route);
    }

</script>

{#if data.user}
    <UserNavBar data={data} />
{:else}
    <PublicNavBar />
{/if}

<slot />
