/** @type {import('tailwindcss').Config} */
export default {
  content: [
    './src/**/*.{html,js,svelte,ts}',
    './node_modules/flowbite-svelte/**/*.{html,js,svelte,ts}'
  ],
  theme: {
    extend: {
      colors: {
        'mint-green': '#A8D5BA',
        'soft-sky-blue': '#B4E0F1',
        'warm-yellow': '#F7C873',
        'pastel-coral': '#F2A1A1',
        'light-beige': '#F7F5E7',
        'deep-teal': '#1E656D',
      },
      fontFamily: {
        lilita: ['Lilita One', 'sans-serif'], // Add 'Bowlby One' to the fontFamily
      },
    },
  },
  plugins: [require('flowbite/plugin')],
};
