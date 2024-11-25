<script>
    import Register from '../../lib/Register.svelte';
    import { Button } from 'flowbite-svelte';
    import { goto } from '$app/navigation';

    /** @type {{ data: import('./$types').PageData, form: import('./$types').ActionData }} */
	let { data, form } = $props();

    // Watch for form success and trigger redirect
	$effect(() => {
		if (form?.success) {
			goto('/register/success');
		}
	})

</script>

<div class="flex flex-col items-center justify-center p-5">
	<Register />

	{#if form?.success}
		<p>Successfully registered! Please check your email to verify your account.</p>
	{/if}
</div>