<script>
    import CustCardandImg from '../lib/CustCardandImg.svelte';

    // Define variables for text and reverse state
    let imageSrc1 = '/images/product_example_1.jpg';
    let imageSrc2 = '/images/product_example_2.jpg';
</script>

<div class="flex flex-col items-center justify-center">
    <div class="w-full p-5 bg-soft-sky-blue border-b border-warm-yellow">
        <h1 class="text-4xl text-center text-white">Reusable Nappies</h1>
    </div>
    

    <div class="grid grid-cols-3 gap-4 w-full p-5">

    </div>
            <CustCardandImg 
            imgSrc={imageSrc1}
            title={'Reusable Nappies - crazy! Right...?'}
            description={'Lets talk about how reusable nappies could save you money and the planet!'}
            buttonText={'Read more'}
            reverse={false}
        />        
        <CustCardandImg 
            imgSrc={imageSrc2}
            title={'How can you get involved?'}
            description={'We offer a subscription service to help take a load off your mind (and your washing machine)'}
            buttonText={'Find out more'}
            reverse={false}
        />   
</div>


