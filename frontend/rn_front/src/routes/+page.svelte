<script>
    import CustCardandImg from '../lib/CustCardandImg.svelte';
    import Login from '../lib/Login.svelte';

    // Define variables for text and reverse state
    let vCard = false;
    let cardTitle = 'Reusable Nappies - crazy! Right...?';
    let cardDescription = 'Lets talk about how reusable nappies could save you money and the planet!';
    let buttonText = 'Read more';
    let imageSrc = '/images/product_example_1.jpg';
</script>

<div class="flex flex-col items-center justify-center">
    <div class="w-full p-5">
        <h1 class="text-4xl text-center text-pastel-coral">Reusable Nappies</h1>
    </div>
    <div class="grid grid-cols-3 gap-4 w-full p-5 border-2 border-solid border-pastel-coral">
        <CustCardandImg 
            imgSrc={imageSrc}
            title={cardTitle}
            description={cardDescription}
            buttonText={buttonText}
            reverse={vCard}
        />        
        <Login />   
        <CustCardandImg 
            imgSrc={imageSrc}
            title={cardTitle}
            description={cardDescription}
            buttonText={buttonText}
            reverse={vCard}
        />   
    </div>
</div>


