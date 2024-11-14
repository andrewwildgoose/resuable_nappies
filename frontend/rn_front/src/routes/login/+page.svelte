<script>
    import Login from '../../lib/Login.svelte';
    import { Card, Button, Label, Input, Checkbox } from 'flowbite-svelte';

    /** @type {{ data: import('./$types').PageData, form: import('./$types').ActionData }} */
	let { data, form } = $props();
</script>

<Login />

{#if form?.success}
	<!-- this message is ephemeral; it exists because the page was rendered in
	response to a form submission. it will vanish if the user reloads -->
	<p>Successfully logged in! Welcome back</p>
{/if}