<script>
    import CustCardandImg from '../lib/CustCardandImg.svelte';

    // Define variables for text and reverse state
    let logo = '/images/logo_transparent.webp';
    let imageSrc1 = '/images/product_example_1.jpg';
    let imageSrc2 = '/images/product_example_2.jpg';
</script>

<div class="flex flex-col items-center justify-center">
    
    <div class="relative h-screen w-full overflow-hidden border-2 border-solid border-pastel-coral">
        <!-- Background Image -->
        <img 
            src="{imageSrc1}"
            alt="Large product" 
            class="absolute inset-0 h-full w-full object-cover"
        />

        <!-- Gradient Overlay -->
        <div class="absolute inset-0 bg-gradient-to-l from-[rgba(0,0,0,0.7)] to-transparent"></div>
        <!-- Text and Logo -->
        <div class="relative z-10 flex flex-col items-start justify-center h-full px-8 md:px-16 text-white">
            <!-- Logo -->
            <img src="{logo}" alt="Logo" class="h-24 w-auto md:h-24" />
        
            <!-- Text -->
            <h1 class="mt-6 text-4xl font-bold md:text-6xl">
                Welcome to Our Service
            </h1>
            <p class="mt-4 text-lg md:text-2xl max-w-xl">
                Discover the best experience with our amazing platform.
            </p>
        </div>
    </div>
</div>


