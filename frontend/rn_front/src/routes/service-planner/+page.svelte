<script>
    let currentStep = 0; // Keeps track of the current step
    let nappyType = "";
    let quantity = 0;
    let pickupDay = "";
    
    // Steps for the form
    const steps = [
        { title: "Select Nappy Type", options: ["Type 1", "Type 2", "Type 3"] },
        { title: "Select Quantity", options: [1, 2, 3, 4] },
        { title: "Select Pickup Day", options: ["Monday", "Wednesday", "Friday"] },
    ];
    
    // Handles step navigation
    function nextStep() {
        if (currentStep < steps.length - 1) {
            currentStep += 1;
        }
    }
    
    function prevStep() {
        if (currentStep > 0) {
            currentStep -= 1;
        }
    }

    // Updates the selection based on the current step
    function handleSelect(option) {
        if (currentStep === 0) nappyType = option;
        if (currentStep === 1) quantity = option;
        if (currentStep === 2) pickupDay = option;
    }
    
    function isSelected(option) {
        if (currentStep === 0) {
            return option === nappyType;
        } else if (currentStep === 1) {
            return option === quantity;
        } else if (currentStep === 2) {
            return option === pickupDay;
        }
        return false;
    }
    // You can use this function to handle form submission at the end.
    function submitForm() {
        console.log('Form submitted:', { nappyType, quantity, pickupDay });
    }
</script>

<style>
    .step {
        opacity: 0;
        transition: opacity 0.5s ease-in-out;
    }

    .step.active {
        opacity: 1;
    }

    .selected-option {
      background-color: #A8D5BA; /* mint-green */
    }

    .hover-bg:hover {
      background-color: #B4E0F1; /* soft-sky-blue */
    }
</style>

<div class="max-w-lg mx-auto mt-10">
    <div class="text-center mb-8">
        <h1 class="text-2xl font-semibold">Reusable Nappy Subscription</h1>
        <p class="text-gray-500">Follow the steps to set up your subscription</p>
    </div>

    <div class="relative">
        {#each steps as step, index (step.title)}
            <div 
            class="step transition-all p-4" 
            class:active={index === currentStep}
            style="z-index: {index === currentStep ? 1 : 0};"
            >
            <h2 class="text-xl font-semibold mb-4">{step.title}</h2>
            <div class="grid grid-cols-1 gap-4">
                {#each step.options as option}
                    <button
                        class="px-4 py-2 rounded-md transition-colors duration-300"
                        class:bg-mint-green={isSelected(option)}
                        class:hover-bg={true} 
                        on:click={() => handleSelect(option)}
                        >
                        {option}
                    </button>
                {/each}
            </div>
        </div>
    {/each}
    
        <!-- Navigation Buttons -->
        <div class="flex justify-between mt-8">
            <button
            on:click={prevStep}
            class="px-4 py-2 bg-gray-300 text-gray-700 rounded-md disabled:opacity-50"
            disabled={currentStep === 0}
            >
            Back
            </button>
            <button
            on:click={currentStep === steps.length - 1 ? submitForm : nextStep}
            class="px-4 py-2 bg-deep-teal text-white rounded-md"
            >
            {currentStep === steps.length - 1 ? 'Submit' : 'Next'}
            </button>
        </div>
    </div>
</div>
