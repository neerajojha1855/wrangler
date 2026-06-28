/** @type {import('tailwindcss').Config} */

export default {
    content: [
        "./index.html",
        "./src/**/*.{js,ts,jsx,tsx}",
    ],
    theme: {
        extend: {
            colors: {
                'wrangler-ivory': '#FFFFF0',
                'wrangler-black': '#000000',
                'wrangler-yellow': '#FFE600',
                'wrangler-red': '#FF3366',
            },
            boxShadow: {
                'neo-sm': '3px 3px 0px 0px #000000',
                'neo-md': '5px 5px 0px 0px #000000',
            },
            fontFamily: {
                'mono': ['"JetBrains Mono"', '"Fira Code"', 'monospace'],
            }
        },
    },
    plugins: [],
}