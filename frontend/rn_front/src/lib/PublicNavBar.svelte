<script>
    import { Navbar, NavBrand, NavLi, NavUl, NavHamburger, Button, Input } from 'flowbite-svelte';
    import { goto } from '$app/navigation';
    import { page } from '$app/stores';
    $: activeUrl = $page.url.pathname;
    let activeClass = 'md:p-2 rounded-none text-deep-teal bg-pastel-coral md:bg-pastel-coral md:text-deep-teal md:dark:text-white dark:bg-green-600 md:dark:bg-transparent';
    let nonActiveClass = 'md:p-2 rounded-none text-deep-teal hover:bg-mint-green md:hover:bg-mint-green md:border-0 dark:text-gray-400 md:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent';
    function navigateTo(route) {
        goto(route);
    }
</script>

<Navbar fluid={true} class="bg-light-beige">
    <NavBrand href="/">
        <img src="/images/logo_transparent.webp" class="me-3 h-6 sm:h-9" alt="Flowbite Logo" />
    </NavBrand>
    <div class="flex md:order-2">
        <Button on:click={() => navigateTo('/register')} size="sm" class="w-full bg-mint-green text-deep-teal rounded-none hover:bg-pastel-coral">Join in</Button>
        <NavHamburger />
    </div>
    <NavUl {activeUrl} {activeClass} {nonActiveClass} class="order-1">
        <NavLi href="/">Home</NavLi>
        <NavLi href="/about">About</NavLi>
        <NavLi href="/faq">FAQ</NavLi>
        <NavLi href="/contact">Contact</NavLi>
    </NavUl>
</Navbar>
