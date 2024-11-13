<script>
    import CustCardandImg from '../lib/CustCardandImg.svelte';

    // Define variables for text and reverse state
    let vCard = false;
    let cardTitle = 'Reusable Nappies - crazy! Right...?';
    let cardDescription = 'Lets talk about how reusable nappies could save you money and the planet!';
    let buttonText = 'Read more';
    let imageSrc = '/images/product_example_1.jpg';
</script>

<div class="flex flex-col items-center justify-center p-5">
    <div class="grid grid-cols-3 gap-4">
        <CustCardandImg 
            imgSrc={imageSrc}
            title={cardTitle}
            description={cardDescription}
            buttonText={buttonText}
            reverse={vCard}
        />        
        <CustCardandImg 
            imgSrc={imageSrc}
            title={cardTitle}
            description={cardDescription}
            buttonText={buttonText}
            reverse={vCard}
        />   
        <CustCardandImg 
            imgSrc={imageSrc}
            title={cardTitle}
            description={cardDescription}
            buttonText={buttonText}
            reverse={vCard}
        />   
    </div>
</div>


