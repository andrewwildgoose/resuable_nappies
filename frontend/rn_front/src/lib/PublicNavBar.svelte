<script>
    import { Navbar, NavBrand, NavLi, NavUl, NavHamburger, Button, Input } from 'flowbite-svelte';
    import { goto } from '$app/navigation';
    import { page } from '$app/stores';
    $: activeUrl = $page.url.pathname;
    let activeClass = 'md:p-2 rounded-none text-deep-teal border-pastel-coral hover:border-2 md:border-pastel-coral md:border-2 md:text-deep-teal md:dark:text-white dark:bg-green-600 md:dark:bg-transparent';
    let nonActiveClass = 'md:p-2 rounded-none text-deep-teal hover:border-mint-green hover:border-2 md:hover:border-mint-green md:border-2 dark:text-gray-400 md:dark:hover:text-white';
    function navigateTo(route) {
        goto(route);
    }
</script>

<Navbar fluid={true} class="bg-light-beige">
    <NavBrand href="/">
        <img src="/images/logo_transparent.webp" class="me-3 h-6 sm:h-9" alt="Flowbite Logo" />
    </NavBrand>
    <div class="flex md:order-2">
        <Button on:click={() => navigateTo('/register')} size="sm" class="w-full border-2 border-pastel-coral text-deep-teal font-lilita rounded-none hover:border-mint-green">Join in</Button>
        <NavHamburger />
    </div>
    <NavUl {activeUrl} {activeClass} {nonActiveClass} class="order-1">
        <NavLi href="/">Home</NavLi>
        <NavLi href="/about">About</NavLi>
        <NavLi href="/faq">FAQ</NavLi>
        <NavLi href="/contact">Contact</NavLi>
    </NavUl>
</Navbar>
