<script>
    import Login from '../../lib/Login.svelte';
    import { goto } from '$app/navigation';

    /** @type {{ data: import('./$types').PageData, form: import('./$types').ActionData }} */
	let { data, form } = $props();

    // Watch for form success and trigger redirect
	$effect(() => {
		if (form?.success) {
			goto('/dashboard');
		}
	})

</script>

<div class="flex flex-col items-center justify-center p-5">
	<Login />

	{#if form?.success}
		<p>Successfully logged in! Redirecting...</p>
	{/if}
</div>
