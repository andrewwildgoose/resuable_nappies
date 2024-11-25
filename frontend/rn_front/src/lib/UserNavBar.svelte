<script>
    import { Navbar, NavBrand, NavLi, NavUl, NavHamburger, Avatar, Dropdown, DropdownItem, DropdownHeader, DropdownDivider } from 'flowbite-svelte';
    export let data;
    import { page } from '$app/stores';
    $: activeUrl = $page.url.pathname;
    let activeClass = 'md:p-2 rounded-none text-deep-teal bg-pastel-coral md:bg-pastel-coral md:text-deep-teal md:dark:text-white dark:bg-green-600 md:dark:bg-transparent';
    let nonActiveClass = 'md:p-2 rounded-none text-deep-teal hover:bg-mint-green md:hover:bg-mint-green md:border-0 dark:text-gray-400 md:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent';
</script>

<Navbar fluid={true} class="bg-light-beige">
    <NavBrand href="/">
        <img src="/images/logo_transparent.webp" class="me-3 h-6 sm:h-9" alt="Flowbite Logo" />
    </NavBrand>
    <div class="cursor-pointer flex items-center md:order-2">
        <!-- <Avatar id="avatar-menu" src="/images/profile-picture-3.webp" /> -->
        <Avatar id="avatar-menu">
            <span style="color: #F2A1A1;">
                <i class="fa-solid fa-user"></i> 
            </span>
        </Avatar>
        
        <NavHamburger class1="w-full md:flex md:w-auto md:order-1" />
    </div>
    <Dropdown placement="bottom" triggeredBy="#avatar-menu">
        <DropdownHeader>
            <span class="block text-sm">User Name</span>
            <span class="block truncate text-sm font-medium">{data.user.user.email}</span>
        </DropdownHeader>
        <DropdownItem href="/dashboard">Dashboard</DropdownItem>
        <DropdownItem>Settings</DropdownItem>
        <DropdownDivider />
        <form method="POST" action="?/logout">
            <DropdownItem type="submit">Sign out</DropdownItem>
        </form>
        
    </Dropdown>
    <NavUl {activeUrl} {activeClass} {nonActiveClass}>
        <NavLi href="/" active={true}>Home</NavLi>
        <NavLi href="/about">About</NavLi>
        <NavLi href="/faq">FAQ</NavLi>
        <NavLi href="/contact">Contact</NavLi>
    </NavUl>
</Navbar>