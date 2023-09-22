/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}', './node_modules/flowbite/**/*.js'],
  theme: {
    extend: {
      colors: {
        '-light': '#d1ffe7',
        '-dark': '#213731',
        snytext: '#05242e',
        'snytext-lite': '#eafff6',
        hover: '#006B4B',
        'vida-loca': {
          DEFAULT: '#44A524',
          25: '#E5FFF4',
          50: '#BFEEB0',
          100: '#9FE587',
          200: '#84DD66',
          300: '#69D645',
          400: '#52C62C',
          500: '#44A524',
          600: '#31771A',
          700: '#1E4910',
          800: '#0B1B06',
          900: '#00191A'
        }
      }
    }
  },
  plugins: [require('flowbite/plugin')]
}
