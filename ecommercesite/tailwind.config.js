/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./templates/**/*.html', 
    './products/templates/**/*.html',
    './static/src/**/*.js',
    './cart/templates/**/*.html',

  ],
  theme: {
    extend: {
      colors: {
        'amazon-orange': '#FF9900',
        'amazon-black': '#000000',
        'amazon-squid-ink': '#232F3E',
      },
    },
  },
  plugins: [],
}

