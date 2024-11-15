<script>
    import Login from '../../lib/Login.svelte';

    /** @type {{ data: import('./$types').PageData, form: import('./$types').ActionData }} */
	let { data, form } = $props();
</script>

<div class="flex flex-col items-center justify-center p-5">
	<Login />

	{#if form?.success}
		<!-- this message is ephemeral; it exists because the page was rendered in
		response to a form submission. it will vanish if the user reloads -->
		<p>Successfully logged in! Welcome back</p>
	{/if}
</div>
