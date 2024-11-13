<script>
    // Import required components from Flowbite Svelte
    import { Card, Button } from 'flowbite-svelte';

    // Define props for the component
    export let imgSrc = '';
    export let title = 'Card Title';
    export let description = 'Card description goes here.';
    export let buttonText = 'Read more';
</script>

<div class="space-y-6">
    <Card class="bg-warm-yellow md:max-w-2xl" img={imgSrc}>
        <h5 class="mb-2 text-2xl font-sans tracking-tight text-black dark:text-white">
            {title}
        </h5>
        <p class="mb-3 font-sans text-gray dark:text-gray-400 leading-tight">
            {description}
        </p>
        <Button class="bg-mint-green text-deep-teal hover:bg-pastel-coral">
            {buttonText}
        </Button>
    </Card>
</div>

