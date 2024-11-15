<script>
    import "../app.css";
    // data for user
    export let data;
</script>

{#if data.user}
    <p>Welcome back, {data.user.user.email}!</p>
    <button on:click={() => logout()}>Logout</button>
{:else}
    <p>You are not logged in.</p>
{/if}

<slot />
